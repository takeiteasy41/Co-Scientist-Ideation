# Co-Scientist Ideation

一个需要显式调用的 Codex Skill：把科研构思组织为有边界、证据可追溯、角色分离的六阶段过程，最终交付由研究者选择的 **Decision Package**。

## 适合什么任务

当你已有研究方向、观察、异常或问题线索，希望从“值得研究吗”推进到“下一步该判别什么”时，可以使用本 Skill。它尤其适合：

- 从证据、矛盾和未知中建立清晰的问题地图；
- 生成机制上真正不同、可证伪的候选假设；
- 让候选接受与作者分离的批评和深度核查；
- 用关键反对意见推动实质修订，而不是润色表述；
- 在投入实验、代码或数据采集前，形成可比较、可追踪的科学决策对象。

它采用显式调用：在 Codex task 中输入 `$co-scientist-ideation` 并给出科研构思目标后才开始运行。

## 六阶段流程

`Goal + Evidence Map → Multi-strategy Generation → Independent Review → conditional Comparison → Evolution + fresh review → Decision Package + Human Selection`

| 阶段 | 核心工作 | 主要产物 |
|---|---|---|
| 1. Goal + Evidence Map | 冻结研究问题、证据范围、矛盾、资源、隐私与停止条件 | Goal–Evidence Map |
| 2. Multi-strategy Generation | 从机制、反证/判别、边界/迁移等视角提出少量机制差异明确的想法 | Hypothesis Cards |
| 3. Independent Review | 核查证据绑定、最近工作碰撞、替代解释、可证伪性、可行性及 killer objection | 独立 Review Records |
| 4. conditional Comparison | 仅在比较会改变修订资源或人类选择时，识别重复、变体与不同机制 | Comparison Record 或明确跳过原因 |
| 5. Evolution + fresh review | 将一个确切反对意见绑定到实质科学修改，保留父候选，并由非作者重新审查 | Evolution lineage 与 fresh Review |
| 6. Decision Package + Human Selection | 汇总合格候选、分歧、失败和最低成本判别方案，由研究者完成最终选择 | Decision Package |

比较不强制形成总排名；没有合格 finalist、证据不足或需要人类价值判断，都是有效结论。

## 关键设计原则

- **证据绑定**：事实、解释、假设、预测和设计选择保持可区分。精确数值、日期、排名及具名来源比较必须绑定支持该具体陈述的来源与位置；搜索摘要、模型记忆和角色共识只作为检索线索。
- **机制差异**：每个候选围绕一条解释主线，写明最近功能性先例、关键差异、替代解释及能够区分二者的预测。
- **独立批评**：候选作者不审查自己的候选；Evolution 后的 descendant 由非作者执行完整 fresh Review。这里的独立性是流程中的角色分离，不替代同行评审或实验验证。
- **反对意见驱动修订**：Evolution 必须回应一个确切的 killer objection，并改变机制、关键假设、预测、反证、边界或判别设计中的科学内容。
- **有界资源**：候选、并发视角、检索和 Evolution 都保持有限；可选步骤只有在能够改变科学决策时才运行。
- **人类最终选择**：Supervisor 只整理已准入的事实和审查结果，不在最终综合中增加新的科学权威。

## 安装

克隆仓库，并复制完整的 `co-scientist-ideation/` 目录：

    git clone https://github.com/takeiteasy41/Co-Scientist-Ideation.git
    mkdir -p "$HOME/.agents/skills"
    cp -R Co-Scientist-Ideation/co-scientist-ideation "$HOME/.agents/skills/"

也可以将完整目录复制到项目级的 `<project>/.agents/skills/`。目录约定与 Skill 构建说明见 OpenAI 官方的 [Build skills](https://learn.chatgpt.com/docs/build-skills)。

## 使用

在新的 Codex task 中显式提供目标和边界：

    $co-scientist-ideation

    研究目标：<希望解释、比较或发现什么>
    证据与检索范围：<已有材料、允许使用的数据库、论文或时间范围>
    当前科学决策：<这次结果需要帮助你决定什么>
    Web：<允许检索哪些公开来源，或要求保持离线>
    隐私：<哪些未发表、专有或敏感信息不得进入查询或外部服务>
    资源边界：<可用数据、测量、计算、时间、成本与专业能力>
    期望输出：Decision Package

信息不足但会影响科学有效性、隐私、授权、成本或范围时，Skill 会先请求必要的人类决定。

## 返回内容

完整结果包括 Goal–Evidence Map、Hypothesis Cards、逐候选独立 Review、必要时的 Comparison、Evolution 父子谱系与 fresh Review，以及：

- 最强支持、killer objection、替代解释与最近工作状态；
- 可区分的预测、直接反证、适用边界和失败模式；
- 最低成本判别设计及关键阈值的证据或设计来源；
- 被拒绝候选、未解决证据、少数意见和流程限制；
- 合格 finalist、无排序的人类选择集，或诚实的 no-finalist 结论；
- 下一项需要研究者决定的事项。

Review 的 `continue` 表示候选目前连贯且值得判别，不表示其已被证明、具有确定新颖性或得到实验验证。

## 联网、隐私与执行控制

联网检索按每次运行的边界处理：只有在获得授权且结果能够改变决策时才检索，并优先打开论文、官方数据、标准、文档或原始仓库等一手来源。公开搜索中的摘要仅用于发现来源；支持、反驳、限制、负结果和未解决证据都会保留。

未发表假设、精确私有数值、可识别信息和协作者细节默认不进入 Web 查询；查询使用抽象表述，除非研究者明确授权。未经许可，本地文件和数据不会上传到外部服务。

Skill 在当前 Codex task 内运行，并止于人类 Decision Package。代码、训练、数据采集、实验、外部通信、仓库修改和论文写作需要另行明确授权。

## Package 结构

- [`co-scientist-ideation/SKILL.md`](co-scientist-ideation/SKILL.md)：入口、触发边界与总体运行契约。
- [`co-scientist-ideation/agents/openai.yaml`](co-scientist-ideation/agents/openai.yaml)：Skill 展示元数据与显式调用策略。
- [`references/workflow.md`](co-scientist-ideation/references/workflow.md)：六阶段路由、停止条件和合法出口。
- [`references/contracts.md`](co-scientist-ideation/references/contracts.md)：科学对象格式、证据准入与 Decision Package 契约。
- [`references/roles.md`](co-scientist-ideation/references/roles.md)：临时科学视角及独立性边界。
- [`references/safety.md`](co-scientist-ideation/references/safety.md)：安全、来源、隐私和人类控制。
- [`references/localization.md`](co-scientist-ideation/references/localization.md)：激活规则与本地适配。
- [`references/paper-basis.md`](co-scientist-ideation/references/paper-basis.md)：论文依据与 bounded adaptation。
- `scripts/`：package 校验脚本。
- `tests/`：行为与结构检查。

## 科学依据与官方资料

本 Skill 借鉴 Co-Scientist 论文中的科学功能，并将其适配为当前 Codex task 内可执行的 bounded workflow：

- Gottweis 等，[Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)，*Nature*，DOI `10.1038/s41586-026-10644-y`
- [Supplementary Information](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10644-y/MediaObjects/41586_2026_10644_MOESM1_ESM.pdf)
- Google Research：[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)
- OpenAI：[Build skills](https://learn.chatgpt.com/docs/build-skills) 与 [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)

## 许可证

除另有说明外，本仓库中由仓库所有者提供的原创内容采用 [Apache License 2.0](LICENSE)。第三方论文、链接资料及未包含在本 GitHub 仓库中的本地研究材料不在本许可证的授权范围内。
