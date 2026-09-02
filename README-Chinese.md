# Co-Scientist Ideation

一个需要显式调用的 Codex Skill：把开放的科研方向、观察或矛盾，转化为有边界、证据可追溯的科研决策包。它把机制、证据、批评、不确定性和研究者的最终选择清楚分开。

[English documentation](README.md)

## 适合什么任务

当你已经有研究方向、观察、异常或问题，需要判断下一步最值得区分什么时，可以使用这个 Skill。它适合：

- 梳理研究问题、证据范围、矛盾、约束、隐私边界和停止条件；
- 生成少量机制上真正不同、可证伪的候选假设；
- 检查证据绑定、相近工作、替代解释、混杂因素和失败模式；
- 将一个明确的 killer objection 转化为实质性的科学修改；
- 在代码、训练、实验或数据采集前提出最低成本的判别方案；
- 为研究者整理可比较的 Decision Package。

它不是通用聊天机器人、普通文献搜索替代品、自动化实验室，也不保证新颖性、正确性或发表。

## 六阶段流程

    Goal + Evidence Map
      → Multi-strategy Generation
      → Independent Review
      → Conditional Comparison
      → Objection-driven Evolution + fresh review
      → Decision Package + Human Selection

| 阶段 | 核心工作 | 主要产物 |
|---|---|---|
| 1. Goal + Evidence Map | 冻结问题、证据边界、矛盾、资源、隐私和停止条件 | Goal–Evidence Map |
| 2. Multi-strategy Generation | 生成少量机制不同而非只换说法的候选 | Hypothesis Cards |
| 3. Independent Review | 检查证据使用、相近工作、替代解释、可证伪性、可行性和 killer objection | 独立 Review Records |
| 4. Conditional Comparison | 只有在比较能够改变修订投入或人类选择时才进行比较 | Comparison Record，或明确跳过 |
| 5. Evolution + fresh review | 将实质修订绑定到一个明确反对意见，并由非作者重新审查后代候选 | Evolution lineage 与 fresh Review |
| 6. Decision Package + Human Selection | 汇总支持、反对意见、不确定性、失败和最低成本的下一步判别，由研究者选择 | Decision Package |

流程不强制产生最终排名。没有合格 finalist、证据不足或需要人类价值判断，都是有效结论。

## 设计原则

- **证据绑定。** 事实、解释、假设、预测和设计选择保持区分。精确数值、日期、排名和具名来源比较必须绑定到真正支持该陈述的来源及位置。搜索摘要、模型记忆和角色共识只是检索线索，不是证据。
- **机制差异。** 每个候选写明一条解释主线、最近的功能性先例、关键差异、替代解释以及能够区分它们的预测。
- **独立批评。** 候选作者不审查自己的候选。Evolution 后的后代候选由非作者角色进行完整 fresh Review。这是流程角色分离，不等同于人类或统计意义上的独立。
- **反对意见驱动修订。** Evolution 必须回应一个明确 killer objection，并改变机制、关键假设、预测、反证、适用边界或判别方案等科学内容。
- **有界资源。** 候选数量、临时视角、检索和 Evolution 都保持有限。只有在能够改变科学决策时才运行可选工作。
- **人类控制。** Skill 在 Decision Package 处停止。代码、训练、实验、数据采集、外部沟通、仓库修改和论文写作需要单独授权。

## 安装

将完整的 co-scientist-ideation/ 目录复制到受支持的 Skill 根目录。不要把仓库根目录或评价方法复制到 Skill 根目录。

macOS / Linux：

```bash
git clone https://github.com/takeiteasy41/Co-Scientist-Ideation.git
mkdir -p "$HOME/.agents/skills"
cp -R Co-Scientist-Ideation/co-scientist-ideation "$HOME/.agents/skills/"
```

Windows PowerShell：

```powershell
git clone https://github.com/takeiteasy41/Co-Scientist-Ideation.git
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse ".\Co-Scientist-Ideation\co-scientist-ideation" "$HOME\.agents\skills\co-scientist-ideation"
```

如果目标位置已有同名 Skill，请先确认或备份，再复制完整目录，避免两个包被静默合并。项目级安装时，也可以将完整目录复制到 <project>/.agents/skills/。

公开评价方法是可选的，不是安装或运行 Skill 的依赖，位于 [evaluation/public-method](evaluation/public-method/README.md)。

## 使用

在新的 Codex task 中显式调用 Skill，并提供你需要作出的科研判断：

```text
$co-scientist-ideation

研究目标：<希望解释、比较或发现什么>
证据与检索范围：<已有材料、允许使用的数据库、论文或时间范围>
当前科学决策：<本次结果需要帮助你决定什么>
Web：<允许检索哪些公开来源，或要求保持离线>
隐私：<不得进入查询的未发表、专有、个人或敏感信息>
资源边界：<可用数据、测量、计算、时间、成本与专业能力>
期望输出：Decision Package
```

如果缺失的信息会影响科学有效性、隐私、授权、成本或范围，Skill 会先请求必要的人类决定。

## 返回内容

完整结果可以包括：

- Goal–Evidence Map；
- Hypothesis Cards；
- 每个候选的独立 Review Records；
- 在比较具有决策价值时生成 Comparison Record；
- Evolution 父子谱系及 fresh Review；
- 最强支持、killer objection、替代解释和相近工作状态；
- 可区分的预测、直接反证、适用边界和失败模式；
- 带有来源或设计依据的最低成本判别方案；
- 被拒绝候选、未解决证据、少数意见和流程限制；
- 合格 finalist、无排序的人类选择集，或诚实的 no-finalist 结果；
- 研究者下一步需要决定的事项。

Review 中的 continue 表示候选目前连贯且值得测试，不表示它已被证明、具有确定新颖性、得到实验验证或可以直接发表。

## 联网、隐私和执行控制

联网检索按每次运行的边界处理。只有在得到授权且结果能够改变决策时才检索，并优先使用论文、官方数据集、标准、文档或原始仓库等一手来源。搜索摘要只是发现来源的辅助；来源核验后的支持、反驳、限制、负结果和未解决主张都会保留。

未发表假设、精确私有数值、可识别信息和协作者细节默认不进入 Web 查询。除非研究者明确授权更多细节，查询使用抽象表述。未经许可，本地文件和数据不会上传到外部服务。

自动激活有意关闭。包保持 policy.allow_implicit_invocation: false，普通任务不会被触发，直到研究者输入 $co-scientist-ideation。

## Package 结构

- co-scientist-ideation/SKILL.md：入口、触发边界和总体契约；
- co-scientist-ideation/agents/openai.yaml：展示元数据和显式调用策略；
- co-scientist-ideation/references/workflow.md：路由、停止条件和合法出口；
- co-scientist-ideation/references/contracts.md：科学对象、证据准入和 Decision Package 契约；
- co-scientist-ideation/references/roles.md：临时科学视角和独立性边界；
- co-scientist-ideation/references/safety.md：来源、隐私、安全和人类控制指南；
- co-scientist-ideation/references/localization.md：激活规则和主机适配；
- co-scientist-ideation/references/paper-basis.md：科学依据和 bounded adaptation；
- co-scientist-ideation/scripts/：包校验脚本；
- co-scientist-ideation/tests/：行为和结构检查。

## 测试与评估

我们进行了一组 AI-only、固定任务的探索性配对评估，用于观察这个流程在受控证据范围内的表现。它只用于提供参考，不代表普遍有效性。

### 方法

- 4 个固定任务：2 个系统或形式化任务，2 个非系统任务；
- 每个任务向两个生成臂提供同一组 5 篇更早且已核验的论文，共 20 篇可见论文；
- 每个任务另有 1 篇后发表的隐藏参考论文，共 4 篇；它们的身份和内容不提供给生成臂或主要 reviewer；
- 隐藏参考只在评审锁定后用于非投票式的机制族比较；
- 两个生成臂为 Co-Scientist 和高质量 Generic prompt；
- 每个任务进行 3 组配对生成，共 12 对匿名输出；
- 每对有 3 个合格的 AI reviewer decisions，共 36 个嵌套 decisions；
- 任务是主要分析单位，4 个任务等权。

### 观察到的描述性终点

| 指标 | 结果 |
|---|---:|
| 倾向 Co-Scientist 的 reviewer directions | 31/36 |
| 倾向 Co-Scientist 的 pair majorities | 11/12 |
| Task-equalized score | 0.861111 |
| Co-Scientist canonical critical failures | 1 |
| Generic canonical critical failures | 0 |
| Co/Generic generation-request ratio | 约 3.83× |
| Co/Generic mean parent wall-time ratio | 约 1.99× |

在这组任务中，方向性数字倾向 Co-Scientist，但结果并不是无条件胜出：一个 Co-Scientist 输出包含实质性的来源使用错误，一个 pair 的多数判断倾向 Generic，预先规定的“不出现更多 critical failure”门槛没有通过。因此终点应解释为 heterogeneous trade-off：这组任务出现了更高的匿名评审偏好信号，同时承担了更多请求和时间成本。

Reviewer 判断嵌套在 pair 和 task 中，不是 36 个独立科学重复。终点是从冻结记录中恢复出来的，不是一次独立复现。隐藏参考论文是用于重构或对齐的历史机制，不是科学真理、唯一正确答案，也不能证明 de-novo discovery。成本比例是本地描述性记录，不是因果效率或 ROI 估计。

该评估不证明普遍优越性、人类偏好、确认性有效性、科学真实性、真正新颖性、跨领域泛化或部署 ROI。公开评价方法包记录指标分层、聚合方式、schema、确定性 validator、Generic 能力包和已知弱点，供开发者审查。

### Generic 能力包

保留的 Generic prompts 声明并限制了以下研究能力：

- research-ideation：没有确认该本地 Skill 的权威上游 GitHub 地址，因此不提供下载链接；
- [hypothesis-generation](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/hypothesis-generation)；
- [scientific-brainstorming](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/scientific-brainstorming)；
- [literature-review](https://github.com/K-Dense-AI/scientific-agent-skills/tree/main/skills/literature-review)；
- 主机提供的只读 PDF 能力，用于阅读给定论文包。

Generic 运行同时禁止联网检索、项目写入和 subagent。这些是该评估的运行控制，不是对本 Skill 获得授权后的按次联网能力的全局限制。现有 runtime receipts 没有记录每个请求实际调用的 Skill 清单，因此不能把这组结果解释为每次都使用了全部列出的 Skill。

## 科学依据和官方资料

这个 Skill 借鉴 Co-Scientist 描述的科学功能，并将它们适配为有边界、任务级的流程：

- Gottweis 等，[Accelerating scientific discovery with Co-Scientist](https://www.nature.com/articles/s41586-026-10644-y)，Nature，DOI 10.1038/s41586-026-10644-y；
- [Supplementary Information](https://media.springernature.com/original/springer-static/esm/art%3A10.1038%2Fs41586-026-10644-y/MediaObjects/41586_2026_10644_MOESM1_ESM.pdf)；
- Google Research，[Accelerating scientific breakthroughs with an AI co-scientist](https://research.google/blog/accelerating-scientific-breakthroughs-with-an-ai-co-scientist/)；
- OpenAI，[Build skills](https://learn.chatgpt.com/docs/build-skills) 与 [Subagents](https://learn.chatgpt.com/docs/agent-configuration/subagents)。

这些来源中的系统结果、架构和实验结果不会自动转移为本 Skill 的结果。

## 许可证

除另有说明外，本仓库所有者提供的原创内容采用 [Apache License 2.0](LICENSE)。第三方论文、链接资源和没有包含在本仓库中的本地研究材料仍受其各自条款约束，本仓库不对它们重新授权。
