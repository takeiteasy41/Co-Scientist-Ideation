#!/usr/bin/env python3
"""Compute an explicit-input descriptive quality and cost summary."""

from __future__ import annotations

from math import isfinite
from typing import Any


NA = "NA"
INTERPRETATION_BOUNDARY = "study-level non-causal description; no ROI inference"


class QualityCostInputError(ValueError):
    """Raised for malformed observed inputs."""


def _optional_count(value: Any, field: str) -> int | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise QualityCostInputError(f"{field} must be a non-negative integer or None")
    return value


def _optional_number(value: Any, field: str) -> float | None:
    if value is None:
        return None
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise QualityCostInputError(f"{field} must be a finite non-negative number or None")
    number = float(value)
    if not isfinite(number) or number < 0:
        raise QualityCostInputError(f"{field} must be a finite non-negative number or None")
    return number


def _missing(missing: list[str], field: str) -> None:
    if field not in missing:
        missing.append(field)


def summarize_quality_cost(
    *,
    s_task_equalized: float | None,
    co_generation_requests: int | None,
    generic_generation_requests: int | None,
    co_mean_wall_time: float | None,
    generic_mean_wall_time: float | None,
    co_mean_output_length: float | None,
    generic_mean_output_length: float | None,
    co_nested_requests: int | None,
    generic_nested_requests: int | None,
) -> dict[str, Any]:
    quality = _optional_number(s_task_equalized, "s_task_equalized")
    if quality is not None and quality > 1:
        raise QualityCostInputError("s_task_equalized must be in [0, 1]")
    co_requests = _optional_count(co_generation_requests, "co_generation_requests")
    generic_requests = _optional_count(
        generic_generation_requests, "generic_generation_requests"
    )
    co_wall = _optional_number(co_mean_wall_time, "co_mean_wall_time")
    generic_wall = _optional_number(generic_mean_wall_time, "generic_mean_wall_time")
    co_length = _optional_number(co_mean_output_length, "co_mean_output_length")
    generic_length = _optional_number(
        generic_mean_output_length, "generic_mean_output_length"
    )
    co_nested = _optional_count(co_nested_requests, "co_nested_requests")
    generic_nested = _optional_count(generic_nested_requests, "generic_nested_requests")

    values = {
        "s_task_equalized": quality,
        "co_generation_requests": co_requests,
        "generic_generation_requests": generic_requests,
        "co_mean_wall_time": co_wall,
        "generic_mean_wall_time": generic_wall,
        "co_mean_output_length": co_length,
        "generic_mean_output_length": generic_length,
        "co_nested_requests": co_nested,
        "generic_nested_requests": generic_nested,
    }
    missing: list[str] = []
    for field, value in values.items():
        if value is None:
            _missing(missing, field)
    if generic_requests == 0:
        _missing(missing, "generic_generation_requests (zero denominator)")
    if generic_wall == 0:
        _missing(missing, "generic_mean_wall_time (zero denominator)")
    if generic_length == 0:
        _missing(missing, "generic_mean_output_length (zero denominator)")

    request_ratio: float | str = NA
    if co_requests is not None and generic_requests not in (None, 0):
        request_ratio = co_requests / generic_requests
    wall_ratio: float | str = NA
    if co_wall is not None and generic_wall not in (None, 0):
        wall_ratio = co_wall / generic_wall
    length_ratio: float | str = NA
    if co_length is not None and generic_length not in (None, 0):
        length_ratio = co_length / generic_length
    extra_nested: int | str = NA
    if co_nested is not None and generic_nested is not None:
        extra_nested = co_nested - generic_nested
    quality_gain: float | str = NA
    if (
        quality is not None
        and co_requests is not None
        and generic_requests is not None
        and co_requests > generic_requests
    ):
        quality_gain = (quality - 0.5) / (co_requests - generic_requests) * 10

    pareto_label: str = NA
    if not missing:
        assert quality is not None
        assert co_requests is not None and generic_requests is not None
        assert co_wall is not None and generic_wall is not None
        assert co_length is not None and generic_length is not None
        assert co_nested is not None and generic_nested is not None
        differences = (
            co_requests - generic_requests,
            co_wall - generic_wall,
            co_length - generic_length,
            co_nested - generic_nested,
        )
        all_no_worse = all(delta <= 0 for delta in differences)
        any_lower = any(delta < 0 for delta in differences)
        no_lower = all(delta >= 0 for delta in differences)
        if quality > 0.5 and all_no_worse:
            pareto_label = "quality win"
        elif quality >= 0.5 and all_no_worse and any_lower:
            pareto_label = "cost win"
        elif quality < 0.5 and no_lower:
            pareto_label = "dominated"
        else:
            pareto_label = "trade-off"

    return {
        "generation_request_ratio": request_ratio,
        "mean_wall_time_ratio": wall_ratio,
        "mean_output_length_ratio": length_ratio,
        "extra_nested_requests": extra_nested,
        "exploratory_quality_gain_per_10_extra_generation_requests": quality_gain,
        "pareto_label": pareto_label,
        "missing_fields": missing,
        "interpretation_boundary": INTERPRETATION_BOUNDARY,
    }
