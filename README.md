# Co-Scientist Ideation

> 一个面向 Codex 的、有证据约束的多角色科研构思 Skill。它把“想点子”组织成一条有边界、可审查、可停止的六阶段路径，最后把选择权交还给研究者。

发布候选（`2026-09-01`）：`1.9-rc1`  
调用方式：仅显式 `$co-scientist-ideation`  
联网策略：按每次任务的授权与隐私边界决定  
状态：本地结构、行为与有限真实使用验证通过

## 它解决什么问题

科研构思常见的失败不是“点子太少”，而是问题没有收紧、证据与推测混在一起、候选只是换皮、反对意见没有真正改变方案，或者漂亮的结论越过了证据。这个 Skill 用少量、角色分离的临时科研视角完成以下工作：

1. 把研究方向整理成可决策的 Goal–Evidence Map；
2. 生成通常 2–4 个机制上有区别、可证伪的候选；
3. 让非作者视角独立寻找最近工作、替代解释和致命反对意见；
4. 仅在比较会改变后续资源分配时做候选比较；
5. 用一个明确反对意见驱动一次实质性修订，并重新接受 fresh review；
6. 输出 Decision Package，由研究者决定继续、保留还是停止。

它适合需要“多角色提出并筛选科研假设”的任务。普通文献综述、开放式头脑风暴、实验执行、代码开发和论文写作应继续使用各自的专门工作流。

## 快速开始

安装时复制完整的 [`co-scientist-ideation/`](co-scientist-ideation/) 目录，不要只复制 `SKILL.md`。

OpenAI 的 [Build skills 文档](https://learn.chatgpt.com/docs/build-skills)将 `$HOME/.agents/skills` 作为可移植的用户级位置，并支持项目内 `.agents/skills`。`2026-09-01` 验证所用的 Codex 主机从 `~/.codex/skills` 发现个人 Skills；这是主机特定位置，不应当被当作所有 Codex 环境的通用约定。

常见安装目标如下：

| 范围 | 目标目录 | 适用情形 |
|---|---|---|
| 可移植的用户级位置 | `$HOME/.agents/skills/co-scientist-ideation` | 希望多个项目都能发现；以官方文档为准 |
| `2026-09-01` 验证主机的个人位置 | `~/.codex/skills/co-scientist-ideation` | 使用与本项目相同的本地主机配置 |
| 单个项目 | `<project>/.agents/skills/co-scientist-ideation` | 只希望该项目发现 |

安装后用显式名称调用：

```text
$co-scientist-ideation

研究目标：……
可用证据：……
当前需要做的科学决策：……
允许联网检索公开资料；查询中不要暴露未公开实验细节。
```

`allow_implicit_invocation: false` 只关闭自动触发，不影响显式调用。这样，普通编码、调试或一般研究讨论不会意外启动较重的多角色流程。

## 六阶段工作流

| 阶段 | 主要产物 | 关键控制 |
|---|---|---|
| 1. Goal + Evidence Map | 问题、证据、矛盾、边界 | 先冻结决策空间与检索权限 |
| 2. Multi-strategy Generation | 2–4 张 Hypothesis Card | 候选必须机制上有区别 |
| 3. Reflection + Deep Verification | 独立 Review Record | 作者不能审核自己的候选 |
| 4. Proximity + Ranking | 必要时的比较记录 | 比较必须能改变下一步决策 |
| 5. Evolution + Fresh Reflection | 修订后代与 fresh review | 一次修订绑定一个明确反对意见 |
| 6. Meta-review + Human Selection | Decision Package | 综合不新增事实，最终选择由人完成 |

完整规范见 [`SKILL.md`](co-scientist-ideation/SKILL.md)、[`workflow.md`](co-scientist-ideation/references/workflow.md) 和 [`contracts.md`](co-scientist-ideation/references/contracts.md)。

## 联网、证据与隐私

这一版没有全局“禁止联网”。每次运行先确定 offline/Web 边界；当联网被授权且会影响决策时，可以检索并打开一手论文、标准、官方数据库或其他权威来源。

- 搜索摘要只用于发现线索，不能直接成为结论证据；
- 被采用的事实要绑定来源身份、具体位置、适用范围、与当前主张的关系及限制；
- 未公开研究细节进入查询前先做隐私判断，默认使用抽象化关键词；
- 证据不足时保留“不确定”或“无 finalist”，而不是从记忆补齐；
- Skill 的输出只授权构思与决策，不自动授权代码、训练、实验、数据采集或对外沟通。

这些规则是领域中立的。生物、物理、计算、数据科学或 Agent 研究只加载与当前问题有关的单位、边界条件、泄漏、对照、形式化或可证伪性检查，不把某个领域的答案硬编码成默认结论。

## 验证状态

`1.9-rc1` 的公开包保留了经验证的 12 个运行时/科学有效载荷文件，并只替换了包含本地会话信息的 release manifest。

| 检查 | 结果 |
|---|---|
| 行为与回归测试 | `16/16 PASS` |
| 结构验证器 | `13 files / 0 errors / 0 warnings` |
| 官方 quick validator | `PASS` |
| 有限真实 forward usage | `PASS_ACCEPTED_NO_FINALIST` |
| 隐式触发策略 | `false` |

本地复核命令：

```powershell
python -m unittest discover -s .\co-scientist-ideation\tests -p test_scripts.py -q
python .\co-scientist-ideation\scripts\validate_skill.py
python -X utf8 "<path-to-skill-creator>\scripts\quick_validate.py" .\co-scientist-ideation
```

有限真实验证使用了一个允许 Web 检索的非计算生物学构思任务。Skill 完成了证据检索、独立审查和诚实停止，并返回“无 finalist”；这说明流程能在证据不足时停止，不代表该 Skill 在所有领域更优。

## 探索性评估

最终保留的评估端点来自 4 个固定任务、12 个匿名成对比较和每对 3 个 AI reviewer 决策。恢复后的描述性结果为：

- 31/36 个有效 reviewer 方向选择 Co-Scientist；
- task-equalized score 为 `0.861111`；
- 11/12 个 pair majority 选择 Co-Scientist。

终端类别仍是 `AI_ONLY_EXPLORATORY_HETEROGENEOUS`：Co-Scientist 一侧出现过 1 个实质性的来源误用，且有 1 个 pair majority 选择 Generic。该结果只是一组固定材料与模型条件下的本地探索性偏好信号，不是通用优越性、人类偏好、科学真理、确认性功效或部署收益证明。

公开仓库只保留方法与聚合摘要。完整的本地 endpoint-recomputation closure 为 `431 files / 44,396,408 bytes`，其中 paper corpus 为 `36 files / 42,400,715 bytes`；二者均被 `.gitignore` 排除。发布论文或原始评估材料前需要单独完成来源许可与隐私审核。详见 [`docs/EVALUATION_BASELINE.md`](docs/EVALUATION_BASELINE.md) 和 [`evaluation/README.md`](evaluation/README.md)。

## 项目结构

```text
co-scientist-ideation/   # 可安装的最终 Skill
docs/                    # 当前状态、历史、踩坑记录与维护流程
evaluation/              # 公开方法摘要；本地复算材料默认忽略
internal/                # 本地最终化与部署凭据，默认忽略
```

维护入口：

- [`docs/CURRENT_STATE.md`](docs/CURRENT_STATE.md)
- [`docs/DEVELOPMENT_HISTORY.md`](docs/DEVELOPMENT_HISTORY.md)
- [`docs/KNOWN_PITFALLS.md`](docs/KNOWN_PITFALLS.md)
- [`docs/MAINTENANCE_RUNBOOK.md`](docs/MAINTENANCE_RUNBOOK.md)

## 依据与致谢

该 Skill 是对 Gottweis 等人在 *Nature* 发表的 Co-Scientist 科学功能的有界 Codex 适配，而不是对其专有基础设施的复现。论文与官方资料见 [`paper-basis.md`](co-scientist-ideation/references/paper-basis.md)。

## 许可证

截至 `2026-09-01`，仓库尚未选择开源许可证。准备公开并邀请他人复用前，请先完成代码、文本和评估材料的权利核对，再添加明确的 `LICENSE`；不要从仓库公开可见这一事实推定复制、修改或分发许可。
