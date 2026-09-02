#!/usr/bin/env python3
"""Validate one public review record without judging or rewriting its science."""

from __future__ import annotations

import argparse
import copy
import json
import re
import sys
from collections.abc import Mapping
from pathlib import Path
from typing import Any


SCHEMA_PATH = Path(__file__).with_name("review_record.schema.json")
MAX_CANONICAL_CHARACTERS = 12_000

SCHEMA_KEYWORDS = frozenset(
    {
        "$schema",
        "$id",
        "$defs",
        "$ref",
        "type",
        "properties",
        "required",
        "additionalProperties",
        "enum",
        "const",
        "anyOf",
        "minLength",
        "maxLength",
        "minItems",
        "maxItems",
        "uniqueItems",
        "items",
        "minimum",
        "maximum",
    }
)

EXACT_PLACEHOLDERS = frozenset(
    {
        "A | B | TIE | NA",
        "1-5 | NA",
        "true | false",
        "TODO",
        "TBD",
        "NONE_OR_RESIDUE",
        "NONE_OR_CANONICAL",
    }
)
BRACED_PLACEHOLDER = re.compile(r"\{\{.*?\}\}", re.DOTALL)


class ReviewValidationError(ValueError):
    """Raised when a review record violates the public form contract."""


def canonical_text(record: Mapping[str, Any]) -> str:
    try:
        return json.dumps(
            record,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )
    except (TypeError, ValueError) as exc:
        raise ReviewValidationError(f"$: not canonical JSON: {exc}") from exc


def load_schema(path: Path = SCHEMA_PATH) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ReviewValidationError(f"$schema: cannot load schema: {exc}") from exc
    if not isinstance(value, dict):
        raise ReviewValidationError("$schema: root must be an object")
    _check_schema_dialect(value, "$schema")
    return value


def _check_schema_dialect(schema: Any, path: str) -> None:
    if not isinstance(schema, Mapping):
        raise ReviewValidationError(f"{path}: schema node must be an object")
    unknown = sorted(set(schema) - SCHEMA_KEYWORDS)
    if unknown:
        raise ReviewValidationError(f"{path}: unsupported schema keywords: {unknown}")
    for container_name in ("$defs", "properties"):
        if container_name in schema:
            container = schema[container_name]
            if not isinstance(container, Mapping):
                raise ReviewValidationError(f"{path}.{container_name}: must be an object")
            for name, child in container.items():
                _check_schema_dialect(child, f"{path}.{container_name}.{name}")
    if "anyOf" in schema:
        choices = schema["anyOf"]
        if not isinstance(choices, list) or not choices:
            raise ReviewValidationError(f"{path}.anyOf: must be a non-empty array")
        for index, child in enumerate(choices):
            _check_schema_dialect(child, f"{path}.anyOf[{index}]")
    if "items" in schema:
        _check_schema_dialect(schema["items"], f"{path}.items")


def _resolve_local_ref(ref: Any, root: Mapping[str, Any], path: str) -> Mapping[str, Any]:
    if not isinstance(ref, str) or not ref.startswith("#/$defs/"):
        raise ReviewValidationError(f"{path}: only local definitions are supported")
    name = ref.removeprefix("#/$defs/")
    definitions = root.get("$defs")
    if not name or "/" in name or not isinstance(definitions, Mapping):
        raise ReviewValidationError(f"{path}: invalid local reference")
    target = definitions.get(name)
    if not isinstance(target, Mapping):
        raise ReviewValidationError(f"{path}: unresolved local reference")
    return target


def _type_matches(value: Any, expected: str) -> bool:
    if expected == "object":
        return isinstance(value, Mapping)
    if expected == "array":
        return isinstance(value, list)
    if expected == "string":
        return isinstance(value, str)
    if expected == "integer":
        return isinstance(value, int) and not isinstance(value, bool)
    if expected == "boolean":
        return isinstance(value, bool)
    raise ReviewValidationError(f"$schema: unsupported type {expected!r}")


def _validate_schema(
    value: Any, schema: Mapping[str, Any], root: Mapping[str, Any], path: str
) -> None:
    if "$ref" in schema:
        if set(schema) != {"$ref"}:
            raise ReviewValidationError(f"$schema: unsupported $ref siblings at {path}")
        _validate_schema(value, _resolve_local_ref(schema["$ref"], root, path), root, path)
        return

    if "anyOf" in schema:
        for choice in schema["anyOf"]:
            try:
                _validate_schema(value, choice, root, path)
                return
            except ReviewValidationError:
                continue
        raise ReviewValidationError(f"{path}: does not match any allowed form")

    expected_type = schema.get("type")
    if expected_type is not None:
        if not isinstance(expected_type, str) or not _type_matches(value, expected_type):
            raise ReviewValidationError(f"{path}: expected {expected_type}")
    if "const" in schema and value != schema["const"]:
        raise ReviewValidationError(f"{path}: expected constant")
    if "enum" in schema and value not in schema["enum"]:
        raise ReviewValidationError(f"{path}: value is outside the allowed enum")

    if expected_type == "object":
        assert isinstance(value, Mapping)
        properties = schema.get("properties", {})
        required = schema.get("required", [])
        if not isinstance(properties, Mapping) or not isinstance(required, list):
            raise ReviewValidationError(f"{path}: invalid object contract")
        missing = [name for name in required if name not in value]
        if missing:
            raise ReviewValidationError(f"{path}: missing required keys")
        if schema.get("additionalProperties") is False:
            extras = set(value) - set(properties)
            if extras:
                raise ReviewValidationError(f"{path}: unexpected keys")
        for name, child in properties.items():
            if name in value:
                _validate_schema(value[name], child, root, f"{path}.{name}")

    if expected_type == "array":
        assert isinstance(value, list)
        if "minItems" in schema and len(value) < schema["minItems"]:
            raise ReviewValidationError(f"{path}: too few items")
        if "maxItems" in schema and len(value) > schema["maxItems"]:
            raise ReviewValidationError(f"{path}: too many items")
        item_schema = schema.get("items")
        if item_schema is not None:
            for index, item in enumerate(value):
                _validate_schema(item, item_schema, root, f"{path}[{index}]")
        if schema.get("uniqueItems") is True:
            canonical_items = [canonical_text({"item": item}) for item in value]
            if len(set(canonical_items)) != len(canonical_items):
                raise ReviewValidationError(f"{path}: duplicate items")

    if expected_type == "string":
        assert isinstance(value, str)
        if "minLength" in schema and len(value) < schema["minLength"]:
            raise ReviewValidationError(f"{path}: string is too short")
        if "maxLength" in schema and len(value) > schema["maxLength"]:
            raise ReviewValidationError(f"{path}: string is too long")

    if expected_type == "integer":
        assert isinstance(value, int) and not isinstance(value, bool)
        if "minimum" in schema and value < schema["minimum"]:
            raise ReviewValidationError(f"{path}: value is below minimum")
        if "maximum" in schema and value > schema["maximum"]:
            raise ReviewValidationError(f"{path}: value is above maximum")


def _scan_placeholders(value: Any, path: str = "$") -> None:
    if isinstance(value, Mapping):
        for key, item in value.items():
            _scan_placeholders(item, f"{path}.{key}")
    elif isinstance(value, list):
        for index, item in enumerate(value):
            _scan_placeholders(item, f"{path}[{index}]")
    elif isinstance(value, str):
        stripped = value.strip()
        if stripped in EXACT_PLACEHOLDERS or BRACED_PLACEHOLDER.search(value):
            raise ReviewValidationError(f"{path}: unresolved placeholder")


def _require_invalid_fields_na(record: Mapping[str, Any]) -> None:
    if record["primary_choice"] != "NA":
        raise ReviewValidationError("$.primary_choice: invalid review must use NA")
    for dimension, pair in record["diagnostic_scores"].items():
        for arm in ("A", "B"):
            if pair[arm] != "NA":
                raise ReviewValidationError(
                    f"$.diagnostic_scores.{dimension}.{arm}: invalid review must use NA"
                )
    for field in ("confidence", "arm_guess_after_lock", "arm_guess_confidence"):
        if record[field] != "NA":
            raise ReviewValidationError(f"$.{field}: invalid review must use NA")


def _validate_status(record: Mapping[str, Any]) -> None:
    status = record["review_status"]
    residue = record["process_residue_found"]
    choice = record["primary_choice"]
    if status == "ELIGIBLE":
        if residue or choice not in {"A", "B", "TIE"}:
            raise ReviewValidationError("$.review_status: invalid eligible state")
        return
    if status == "INVALID_PROCESS_RESIDUE":
        if not residue:
            raise ReviewValidationError("$.process_residue_found: invalid residue state")
        _require_invalid_fields_na(record)
        return
    if status == "INVALID_INPUT":
        if residue:
            raise ReviewValidationError("$.process_residue_found: invalid input state")
        _require_invalid_fields_na(record)
        return
    raise ReviewValidationError("$.review_status: unsupported status")


def _validate_none_codes(record: Mapping[str, Any]) -> None:
    for arm in ("A", "B"):
        codes = record["critical_epistemic_failures"][arm]
        if "NONE" in codes and codes != ["NONE"]:
            raise ReviewValidationError(
                f"$.critical_epistemic_failures.{arm}: NONE must be the sole code"
            )


def validate_review_record(
    record: Mapping[str, Any], *, schema: Mapping[str, Any] | None = None
) -> dict[str, Any]:
    if not isinstance(record, Mapping):
        raise ReviewValidationError("$: review record must be an object")
    active_schema = dict(schema) if schema is not None else load_schema()
    _check_schema_dialect(active_schema, "$schema")
    if len(canonical_text(record)) > MAX_CANONICAL_CHARACTERS:
        raise ReviewValidationError("$: canonical record exceeds length limit")
    _validate_schema(record, active_schema, active_schema, "$")
    _scan_placeholders(record)
    _validate_none_codes(record)
    _validate_status(record)
    return copy.deepcopy(dict(record))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate one public review-record JSON file")
    parser.add_argument("record", type=Path)
    parser.add_argument("--schema", type=Path, default=SCHEMA_PATH)
    args = parser.parse_args(argv)
    try:
        record = json.loads(args.record.read_text(encoding="utf-8"))
        admitted = validate_review_record(record, schema=load_schema(args.schema))
    except (OSError, json.JSONDecodeError, ReviewValidationError) as exc:
        print(f"INVALID: {exc}", file=sys.stderr)
        return 1
    eligible = admitted["review_status"] == "ELIGIBLE"
    print(f"VALID: review_status={admitted['review_status']} endpoint_eligible={str(eligible).lower()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
