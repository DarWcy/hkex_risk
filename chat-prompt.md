# 可扩展和可重用的提示词集（兼容 M365 Copilot/GitHub Copilot）

## 核心描述
本提示词集围绕**构建可追溯/可验证/可更新的测试业务知识共同基线，实现 AI 辅助生成测试用例/BDD 场景闭环**的核心目标设计。它增加了五个核心要求：**多模型协作验证、实时 BDD 关系更新、知识库全生命周期手动回退机制、Skill 结构化 Reference 和 Skill 自动化 Script（按工具场景）**，同时保留了**业务文档添加/更新同步和标准化检查表生成**的原始功能。它按**知识构建 → AI 能力开发 → 测试资产生成 → 更新同步 → 多模型验证 → 全生命周期管理**进行逻辑分层。所有提示词严格遵循"仅基于提供的 MD 格式业务规则"的核心约束，兼容 M365 Copilot（自然语言/文档/流程生成）和 GitHub Copilot（代码/skill/BDD 开发），支持**多模型协作、手动回退、Skill 精确追溯和自动化**的全链路知识管理。

### 通用模板使用指南
**要将此提示词集应用于不同文档，请参考 `Prompt-1-Universal-Template.md`，其中提供：**
- **可配置占位符**：替换文档特定信息（名称、版本、日期、目标角色）
- **灵活的模块定义**：选择默认的 10 模块框架或自定义模块定义
- **自定义需求入口**：在指定部分添加文档特定需求
- **分步指导**：模板定制和执行的清晰说明
- **示例配置**：不同文档类型（金融、保险、银行）的样本配置
- **最佳实践**：模块粒度、角色定位和内容组织的指南

**通用模板的主要优势：**
- **文档无关**：适用于任何业务规则文档，无论领域如何
- **角色优化**：模块设计适合 BA、QA Lead 和 Automation Tester 阅读
- **可维护**：清晰的结构便于更新和修改
- **可追溯**：内置可追溯性和结构化 ID 生成
- **测试就绪**：包含每个模块的测试考虑因素

### 一般要求
- **校对要求**：所有生成的内容必须经过校对，确保语法、拼写、格式正确，与原文一致。
- **语言要求**：默认为英语；必要时可在备注中使用中文。
- **格式标准**：符合 Markdown 语法，结构清晰，易于阅读和维护。

---

## I. 基本规则转换和知识库框架构建提示词

### 适用场景
将非结构化业务规则（PDF/Word）转换为标准化 MD 文档，构建**支持全局流程定义的 Git 结构化知识库框架**，为全生命周期管理奠定基础。

### Prompt 1（规则转 MD + 业务标准化拆分）
```
### 说明
基于以下 [Initial Margin Calculation Guide HKv14] 业务规则原文（仅使用此内容），完成从非 MD 文件（如 PDF/Word）到标准化 MD 文档的转换和模块化拆分，满足以下要求：
1. **非 MD 转 MD 转换过程**：将非结构化业务规则（PDF/Word）转换为纯文本，保持原始内容的完整性，确保术语、公式、表格等信息准确。
2. **模块化拆分**：拆分为**10 个业务导向模块**，专为 BA、QA Lead 和 Automation Tester 的可读性和可追溯性设计，不遗漏规则点。每个模块针对特定业务逻辑和角色关注点：

   **模块 1: Introduction-Overview.md**
   - 目标受众：业务分析师 (BA)
   - 内容：VaR 平台介绍、IM 计算概述、监管合规背景
   - 目的：业务理解、需求分析

   **模块 2: Risk-Parameter-File-Specification.md**
   - 目标受众：QA Lead
   - 内容：IMRPF 文件布局、字段规范、FieldType 定义
   - 目的：数据验证、规范验证

   **模块 3: Input-Data-Specification.md**
   - 目标受众：自动化测试工程师
   - 内容：持仓数据要求、合约价值、市场价值、数据来源
   - 目的：测试数据准备、接口测试

   **模块 4: Market-Risk-Component-Calculation.md**
   - 目标受众：BA + QA Lead
   - 内容：投资组合保证金、HVaR、SVaR、固定费率保证金计算
   - 目的：核心计算逻辑理解、测试用例设计

   **模块 5: Margin-Adjustment-Process.md**
   - 目标受众：BA
   - 内容：保证金调整流程、四舍五入、有利 MTM、保证金信用
   - 目的：业务流程理解、需求验证

   **模块 6: Other-Risk-Components.md**
   - 目标受众：QA Lead
   - 内容：MTM 要求、持仓限额附加、信用风险附加、临时附加
   - 目的：风险组件验证、合规检查

   **模块 7: Position-Processing-Logic.md**
   - 目标受众：自动化测试工程师
   - 内容：持仓调整逻辑、跨日净额结算、跨货币净额结算
   - 目的：系统逻辑测试、边界条件验证

   **模块 8: Collateral-Management.md**
   - 目标受众：BA + QA Lead
   - 内容：特定股票/现金抵押覆盖、保证基金风险抵押
   - 目的：抵押品管理理解、风险控制验证

   **模块 9: Corporate-Action-Processing.md**
   - 目标受众：BA
   - 内容：公司行动持仓调整、股息、股票分割、供股
   - 目的：特殊业务场景理解、异常处理

   **模块 10: Calculation-Examples.md**
   - 目标受众：自动化测试工程师 + QA Lead
   - 内容：完整计算示例、分步计算过程、结果验证
   - 目的：测试用例设计、结果验证、回归测试
3. **文件命名和模板**：为每个模块创建独立的 MD 文件；文件名必须为**英文**，遵循**Module-SubTopic.md**命名约定（例如，Introduction-Overview.md、Risk-Parameter-File-Specification.md、Input-Data-Specification.md、Market-Risk-Component-Calculation.md）。所有 MD 文件使用统一的可重用模板，结构如下：
   - 标题：# [主题] - [Initial Margin Calculation Guide HKv14] 版本 [X.X]
   - 目标受众：指定主要受众（BA/QA Lead/自动化测试工程师）
   - 规则追溯：记录对应的原始文档条款/段落编号/发布版本
   - 核心内容：以清晰逻辑的项目符号/表格形式呈现规则约束，按业务相关性组织
   - 适用场景：明确定义规则适用的业务场景
   - 全局流程节点：标记当前规则所属的**核心业务全局流程节点**
   - 测试考虑因素：为 QA Lead 和自动化测试工程师提供测试指导（测试数据要求、边界条件、预期结果）
   - 结构化 ID：为每个规则段落生成唯一 ID（格式：[模块缩写]-[段落编号]），用于精确的 Skill Reference 关联
4. **可追溯性**：确保每个规则点都可追溯到原始段落，不添加或删除主观信息。
5. **语言要求**：**所有内容必须仅使用英文**。必要时，中文只能在备注/注释中使用。文件名、标题、内容、表格和所有文本必须为英文。
6. **校对要求**：校对生成的 MD 文件，确保：
   - 语法和拼写正确
   - 格式标准化，符合 Markdown 语法
   - 内容与原文一致，无信息丢失或错误
   - 表格结构完整，数据准确
   - 公式表达清晰，符号正确
   - **所有内容均为英文**
   - **角色特定清晰度**：内容对目标受众（BA/QA Lead/自动化测试工程师）清晰易懂
   - **测试指导完整性**：测试考虑因素为测试用例设计和验证提供可操作指导
   - **业务逻辑准确性**：计算和业务规则准确表示并可追溯

### 输入（替换为实际业务规则原文）
[粘贴从业务 PDF/Word 转换的纯文本规则内容]

### 输出要求
- 输出**10 个 MD 文件**的完整列表（包括文件路径/完整内容/结构化段落 ID），每个文件针对特定业务逻辑和角色关注点。
- 输出**核心业务全局流程流程图**（文本版本，包括流程节点、流程关系和规则关联），具有清晰的模块映射。
- **所有内容必须使用英文**（必要时中文只能在备注中使用），符合 Markdown 语法标准。
- 文件名必须为英文，遵循 10 个指定模块的 Module-SubTopic.md 格式。
- 提供校对结果，确保所有 MD 文件语法、拼写、格式正确，与原文一致，**且完全为英文**。
- 确保每个模块明确指示其目标受众，并提供角色特定内容和测试指导。
```

### Prompt 2（Git 知识库全生命周期框架生成）
```
### 说明
生成**支持全局流程定义、全生命周期管理和 Skill Reference/Script 适配的可扩展 Git 仓库结构化框架**，核心目标是支持"可追溯/可验证/可更新/可扩展"的测试业务知识共同基线。

**关键：在生成框架之前，首先分析现有工程结构。**

#### 步骤 1：现有工程结构分析（必需）
在生成任何新结构之前，分析当前工程状态：
1. **扫描现有目录**：列出所有当前目录及其用途
2. **映射现有文件**：按内容类型（规则/流程/计算/示例）对现有 MD 文件进行分类
3. **识别差距**：将现有结构与 7 层框架（docs/、docs/global-process/、docs/source-files/、copilot-skills/、tests/、config/、governance/）进行比较
4. **保留现有文件**：不要删除或覆盖现有文件；将它们集成到框架中

#### 步骤 2：框架结构模板选择
根据分析，选择或调整适当的结构模板：

**模板选项 A：Greenfield（新项目）**
- 使用场景：从无到有开始，没有现有结构
- 使用下面定义的完整 7 层框架

**模板选项 B：Brownfield（现有项目）**
- 使用场景：工程已有现有 MD 文件和结构
- 保留现有文件，映射到适当的层
- 仅创建缺失的层
- 生成重组的迁移指南

**模板选项 C：Hybrid（部分结构）**
- 使用场景：某些框架层存在，其他层缺失
- 完善现有层，添加缺失的层
- 确保跨层一致性

#### 步骤 3：目录结构设计（7 层框架）
按**能力层、资产层、配置层和治理层**设计目录结构，具有清晰的**核心业务全局流程**专用存储位置：

**第 1 层 - 文档层：docs/**（存储标准化 MD 规则）
- 用途：Prompt 1 拆分的业务规则模块
- 现有文件映射：将现有规则 MD 映射到此层

**第 2 层 - 全局流程层：docs/global-process/**（存储核心业务全局流程）
- 用途：流程流程图、MD 文档、关系表
- 支持流程变更时的实时更新

**第 3 层 - 原始文档层：docs/source-files/**（存储原始业务规则文件）
- 用途：Skill Reference 的源文档可追溯性
- 存储原始 PDF/Word 文件和转换的 MD

**第 4 层 - AI 能力层：copilot-skills/**（存储模块化 Skills）
- 用途：带有自动化脚本的 GitHub Copilot Skills
- 子目录：script/ 用于自动化脚本

**第 5 层 - 测试资产层：tests/**（存储测试用例/BDD 场景）
- 用途：测试用例、BDD 功能、步骤定义
- 包括关系管理文件

**第 6 层 - 配置层：config/**（存储版本/配置）
- 用途：版本概览、更新日志、命名约定、验证配置

**第 7 层 - 治理层：governance/**（存储手动回退）
- 用途：手动回退机制、审计流程、权限管理

#### 步骤 4：预定义结构模板配置
为结构生成提供**可配置的模板参数**：

**模板配置文件（config/FRAMEWORK-CONFIG.md）：**
```markdown
# 框架结构配置

## 工程元数据
- 工程名称：[工程名称]
- 业务领域：[业务领域]
- 源文档：[源文档名称]
- 源版本：[版本号]

## 结构模板选择
- 模板类型：[Greenfield/Brownfield/Hybrid]
- 现有结构路径：[./]（如果是 Brownfield/Hybrid）

## 层配置
### 第 1 层 - docs/
- 启用：true
- 现有文件：[列出要映射的现有 MD 文件]
- 命名模式：[Module-SubTopic.md]

### 第 2 层 - docs/global-process/
- 启用：true
- 流程来源：[Core-Business-Global-Process-Flowchart.md]

### 第 3 层 - docs/source-files/
- 启用：true
- 源文件：[源文件列表]

### 第 4 层 - copilot-skills/
- 启用：true
- Skill 命名模式：[{business}-{module}-{capability}]
- 脚本语言：[Python/其他]

### 第 5 层 - tests/
- 启用：true
- 测试框架：[Behave/BDD/其他]
- 测试用例模式：[TC-{module}-{number}]

### 第 6 层 - config/
- 启用：true
- 版本格式：[MAJOR.MINOR.PATCH]

### 第 7 层 - governance/
- 启用：true
- 回退级别：[查看/编辑/审计/决策]

## 自定义目录（可选）
- [如需要，自定义目录路径]

## 排除项
- [要从框架中排除的文件/目录]

## 自定义要求（人工输入）
### 领域特定要求
- [在此添加领域特定要求]

### 业务流程要求
- [在此添加业务流程特定要求]

### 技术要求
- [在此添加技术要求]

### 合规要求
- [在此添加合规要求]

### 测试要求
- [在此添加测试特定要求]
```

#### 步骤 5：详细的维护规范 + 扩展规则
为每个启用的目录提供详细规范：

**所有目录的通用要求：**
- 功能描述：在知识库生命周期中的作用
- 文件命名约定：确切的模式和示例
- 更新维护要求：分步程序、频率、负责角色
- 扩展规则：如何添加新文件、命名约定、归档程序

**copilot-skills/ 的特定要求：**
- Reference 字段维护规范：
  * 结构化格式模板
  * 同步更新触发条件
  * 更新传播链（规则变更 → Skill 更新 → 关系更新）
  * Reference 完整性验证检查清单
- Script 规范：
  * 存储路径、执行权限、异常回退规则
  * 脚本版本控制和回滚程序

**tests/ 的特定要求：**
- 带有 Reference 验证槽的测试用例维护
- BDD 关系维护程序
- 测试数据管理模板

**config/ 的特定要求：**
- 版本管理和 Git 标签同步
- 配置变更影响评估
- 多模型验证配置维护

**governance/ 的特定要求：**
- 手动回退触发矩阵
- 审计跟踪要求
- 权限管理规范
- 问题整改工作流

### 输入
1. **现有工程结构**（如果是 Brownfield/Hybrid）：
   [粘贴当前目录树和文件列表]

2. **框架配置**（模板选择）：
   [指定：Greenfield/Brownfield/Hybrid]
   [如果是 Brownfield/Hybrid：列出要保留/迁移的现有文件]

3. **Prompt 1 的 MD 文件列表**：
   [粘贴 Prompt 1 生成的 MD 文件列表]

4. **核心业务全局流程流程图**：
   [粘贴核心业务全局流程流程图描述]

5. **自定义要求**（可选）：
   [粘贴任何领域特定、业务流程、技术、合规或测试要求]

### 输出要求

#### 输出 1：现有结构分析报告（如果是 Brownfield/Hybrid）
- 当前目录树
- 文件分类（规则/流程/计算/示例/其他）
- 与 7 层框架的差距分析
- 迁移建议

#### 输出 2：框架配置文件
- `config/FRAMEWORK-CONFIG.md`，包含所有模板参数
- 结构模板选择理由
- 自定义配置和要求

#### 输出 3：完整的 Git 仓库目录树
- 包含所有文件的完整层次结构
- 每个目录的功能描述
- Skill Reference/Script 适配要求
- **标明哪些文件是 NEW vs EXISTING（如果是 Brownfield/Hybrid）**

#### 输出 4：详细的维护规范 + 扩展规则
对于 7 个目录中的每一个：
- 功能描述
- 文件命名约定
- 更新维护要求（分步）
- 扩展规则

特定深入：
- copilot-skills/：Reference 字段规范、Script 规范
- tests/：测试用例维护、BDD 关系维护
- config/：版本管理、影响评估
- governance/：回退矩阵、审计要求

#### 输出 5：迁移指南（如果是 Brownfield/Hybrid）
- 分步迁移说明
- 文件移动映射（源 → 目标）
- Reference 更新要求
- 验证检查清单

#### 输出 6：README.md 模板
- 仓库描述
- 目录导航
- 规则版本
- 手动回退负责人
- Skill Reference/Script 使用指南
- **迁移说明（如适用）**

#### 输出 7：初始配置文件
- `config/RULES-VERSION.md`（带模块版本矩阵）
- `docs/global-process/GLOBAL-PROCESS.md`（带结构化 ID）
- **现有文件的保留说明（如适用）**
```

---

## II. GitHub Copilot Skills 开发提示词（包括 BDD 关联 + Reference + Script）

### 适用场景
基于结构化 MD 知识库（包括上下游），生成**模块化、可追溯（Reference）、预嵌入 BDD 关系、支持自动化（Script）**的 GitHub Copilot Skills，确保 Skills 与主/上游/下游规则和 BDD 场景的关系可以实时更新，并具有自动同步/验证能力。

### Prompt 3（Copilot Skill 模块化生成 + BDD 关联 + 结构化 Reference + Script 预嵌入）
```
### 说明
基于以下 [Initial Margin Calculation Guide HKv14] MD 文件（仅使用此内容），为 GitHub Copilot 开发**模块化、可追溯、预嵌入 BDD 关系、支持自动化 Script**的 Skills，满足以下要求：
1. 每个 Skill 专注于单个规则场景；Skill ID 遵循**业务缩写-模块-核心能力**命名约定（例如，hkex-im-calculation、hkex-risk-parameters），以方便后续关系更新。
2. 每个 Skill 包含**固定可扩展结构 + BDD 关联预嵌入 + 结构化 Reference + Script 预嵌入**，无信息缺失。结构如下：
   - Skill ID：唯一标识符
   - 描述：Skill 的核心能力（AI 回答/规则验证/BDD 场景生成）
   - 触发词：常见用户查询（精确覆盖核心规则问题）
   - 结构化 Reference（必填）：
     + Rule_Source: {MD 文件完整路径} | {规则段落结构化 ID} | {规则版本} | {原始文档存储路径}
     + Test_Reference: {待关联的 BDD 测试用例 ID} | {待关联的 feature 文件路径}
     + Verify_Reference: {多模型验证配置 ID} | {手动审计记录路径（预留）}
     + Update_History: {创建时间} | {创建者} | {关联的 Git Commit ID（预留）}
   - BDD 关联预嵌入：预留 BDD 测试用例 ID/feature 文件路径关联槽（格式：待关联 | 关联后：TC-XXX-001, tests/xxx/xxx.feature），支持实时更新
   - Script（按场景预嵌入）：
     + Automation_Script（GitHub Copilot）：预留轻量级 Python 脚本槽（同步关系/触发验证/Git 链接），标记输入/输出规范
     + Operation_Guide（M365 Copilot）：预留自然语言操作指导槽，适配非技术人员
   - 示例响应：基于规则的精确回答（标记 Rule_Source 中的段落 ID）
3. 禁止引入 MD 文件以外的规则信息；示例响应必须 100% 符合规则约束。
4. Skill 内容预留**更新标记槽**，以方便后续规则修改和关系更新。

### 输入（替换为 MD 文件内容）
[粘贴 MD 文件完整内容（包括结构化段落 ID）]

### 输出要求
- 输出完整的 Skill MD 文件（根据 copilot-skills/skill-definitions 目录规范）。
- 输出 Skill 索引表（包括 Skill ID/描述/触发词/结构化 Reference/BDD 关联预嵌入槽/Script 预嵌入槽）。
- 所有内容用英文编写，适配 GitHub Copilot 全局语义检索。
```

### Prompt 4（Copilot Skill 索引 + 关系 + Reference/Script 管理 + 使用指南）
```
### 说明
基于生成的 [Initial Margin Calculation Guide HKv14] Copilot Skill 文件，生成**支持 BDD 关系实时更新、Reference 验证和 Script 执行**的 Skill 支持文档，满足以下要求：
1. Skill 索引文件（index.md）：按**模块**分类，包括 Skill ID/描述/触发词/文件链接/规则版本/结构化 Reference/BDD 关系/Script 路径，支持关系的实时编辑和更新。
2. 关系管理文件（skill-bdd-relation.md）：生成**可编辑关系表**，添加"Reference 完整性"列。字段为"Skill ID/Rule_Source/Test_Reference/BDD 测试用例 ID/BDD feature 文件路径/Reference 完整性/更新时间/更新者"，支持实时维护。
3. 使用指南（usage-guidelines.md）：包括 Skill 集成方法、触发词使用规范、Skill 同步更新流程、**BDD 关系/Reference 更新规范**、Script 执行步骤（按 GitHub/M365 场景），以及多模型验证期间的 Skill 调用要求。
4. 多模型验证配置文件（config/skill-verify-config.md）：添加"Reference 完整性验证"和"Script 执行结果验证"维度，定义 Skill 在多模型验证中的**输入格式/验证维度/结果判断标准**。
5. Reference 维护规范（config/skill-reference-spec.md）：定义 Reference 字段的结构化格式、同步更新规则和验证方法，确保全链路追溯一致性。
6. 仅基于提供的 Skill 文件内容编写；禁止添加外部集成解决方案。

### 输入（替换为实际 Skill 文件列表）
[粘贴 Prompt 3 生成的 Skill ID + 描述 + 规则版本列表]

### 输出要求
- 输出 index.md、skill-bdd-relation.md、usage-guidelines.md、config/skill-verify-config.md 和 config/skill-reference-spec.md 的完整内容。
- 所有文档均为**可编辑格式**，支持 BDD 关系、Reference 和 Script 配置的实时更新。
```

### Prompt 16（Skill 自动化 Script 生成 + Git/验证链接）
```
### 说明
基于生成的 [Initial Margin Calculation Guide HKv14] Copilot Skill（包括结构化 Reference），生成适配 GitHub Copilot 的轻量级自动化 Scripts，同时为 M365 Copilot 生成相应的自然语言操作指导，满足以下要求：
1. Script 类型（按 Skill 生命周期）：
   - Reference 同步脚本：修改 Skill 后，自动验证并更新 `skill-bdd-relation.md` 中的"Reference 完整性"列，并同步更新关联的 MD 规则版本。
   - 多模型验证触发脚本：调用多模型验证 API，传入 Skill 的 Rule_Source 信息，生成 Reference 完整性/规则对齐验证结果。
   - Git 链接脚本：创建 Git PR，自动填写 PR 描述（包括 Skill ID/Reference 更新内容/Script 执行结果），并与手动回退审计表关联。
2. Script 开发要求：
   - 使用 Python 编写，预留配置修改槽（如 API 地址、Git 仓库地址、验证结果存储路径），适配不同环境。
   - 包含异常处理逻辑；执行失败时，自动生成手动回退触发条件 + 操作指导，写入 `governance/common/issue-tracking.md`。
   - 存储在 copilot-skills/scripts/ 目录中，文件名与 Skill IDs 一致（例如，hkex-im-calculation.py）。
3. M365 操作指导：将 Script 逻辑转换为自然语言步骤，写入 usage-guidelines.md 中的"M365 Copilot 操作区"，降低非技术人员的操作门槛。
4. 仅基于 Skill 的 Reference 和现有知识库框架编写；禁止引入复杂依赖。

### 输入
[粘贴 Skill ID + 结构化 Reference + Git 仓库地址 + 多模型验证 API 地址 + `skill-bdd-relation.md` 模板]

### 输出要求
- 输出 3 种类型的自动化 Scripts（可直接运行，包括注释/配置槽/异常处理）。
- 输出 Script 使用说明（环境依赖、配置修改、执行步骤、异常回退解决方案）。
- 输出 M365 Copilot 适配的自然语言操作指导（分步，无技术术语）。
- 输出 Script 执行结果验证表（可编辑，包括 Script ID/Skill ID/执行状态/验证结果/手动回退触发标志）。
```

---

## III. 测试用例/BDD 场景生成提示词（包括关系 + Reference 验证）

### 适用场景
基于 MD 知识库/Copilot Skill，生成**严格规则对齐、预嵌入多维关系、支持 Reference 验证**的结构化测试用例/BDD（Behave）场景，确保 BDD 与需求、知识库和 Skill References 双向可追溯。

### Prompt 5（结构化迭代测试用例生成 + 关系 + Reference 预嵌入）
```
### 说明
基于以下 [Initial Margin Calculation Guide HKv14] 规则点（仅使用此内容），生成**可验证、可追溯、迭代、预嵌入多维关系 + Reference 验证槽**的结构化测试用例，满足以下要求：
1. 测试用例严格符合规则约束，无规则外的场景设计，覆盖正向合规、负向禁止和异常场景，标记所属**全局流程节点**。
2. 测试用例使用统一的可重用模板，模板结构包含**多维关系 + Reference 验证槽**，便于实时更新。结构如下：
   - 测试用例 ID：TC-[模块缩写]-[编号]（例如，TC-IM-CALC-001、TC-RISK-PARAM-001），避免重复。
   - 测试场景：清晰的规则验证点 + 所属全局流程节点 + 规则版本。
   - 前置条件：适用于规则的环境/配置要求。
   - 测试步骤：可执行的操作序列，明确无误。
   - 预期结果：基于规则的精确断言（标记 Rule_Source 中的段落 ID）。
   - 规则依据：关联的 MD 文件完整路径 + 段落结构化 ID + 规则版本（与 Skill 的 Rule_Source 一致）。
   - Reference 验证槽：标记对应的 Skill ID + "Reference 一致性"验证要求（是否与 Skill 的 Test_Reference 匹配）。
   - 关系：预留"需求 ID/Copilot Skill ID/BDD 场景 ID"关联槽，支持实时更新。
   - 更新标记：预留空白行，用于后续规则修改和关系更新。
3. 所有参数仅使用知识库定义的有效值，不引入未定义值。

### 输入（替换为特定规则点）
规则点：[粘贴特定规则点内容（包括结构化段落 ID）]
规则依据：[粘贴关联的 MD 文件路径 + 段落结构化 ID + 规则版本]

### 输出要求
- 输出表格形式的测试用例（包括正向/负向/异常场景，带有全局流程节点和 Reference 验证槽）。
- 测试用例参数仅使用知识库定义的有效值。
- 所有内容用英文编写，可直接导入测试管理工具，**关系槽和 Reference 验证槽为可编辑格式**。
```

### Prompt 6（BDD/Behave 场景生成 + 多维关系 + Reference 双向追溯）
```
### 说明
基于生成的结构化测试用例，生成**严格规则对齐、可执行、迭代、支持 Reference 双向追溯**的 BDD（Behave）场景，并构建**BDD 与需求/知识库规则/Copilot Skills 关系实时更新系统**，满足以下要求：
1. 场景使用标准 Gherkin 语法（Given/When/Then），仅包含规则约束的操作/断言，标记**测试用例 ID/全局流程节点/规则版本/Rule_Source 段落 ID**。
2. 所有参数仅使用知识库定义的有效值；禁止引入未定义值。
3. 生成**BDD 关系实时更新管理文件**（tests/bdd-relation-manager.md），添加"Reference 双向一致性"列，包含 3 个核心可编辑表格：
   - BDD-需求关系表：字段"BDD 场景 ID/feature 文件路径/需求 ID/需求描述/Reference 双向一致性/更新时间/更新者"
   - BDD-知识库关系表：字段"BDD 场景 ID/全局流程节点/MD 规则路径/段落结构化 ID/Rule_Source 匹配度/更新时间/更新者"
   - BDD-Skill 关系表：字段"BDD 场景 ID/Copilot Skill ID/Skill 触发词/Test_Reference 匹配度/更新时间/更新者"
4. 附带 Python Step Definitions 生成；步骤需要可执行（包括 API 调用/数据库断言/结果验证），添加**Reference 一致性验证埋点**，适配后续多模型验证。
5. 生成 behave.ini 配置文件，添加"Reference 验证开关"，适配测试执行和**关系/Reference 文件同步维护**。

### 输入（替换为特定测试用例）
[粘贴 Prompt 5 生成的测试用例内容（包括测试用例 ID/全局流程节点/Reference 验证槽）]

### 输出要求
- 输出 .feature 文件（Gherkin 语法，英文，标记测试用例 ID/规则版本/Rule_Source 段落 ID），存储在 tests/bdd/features 目录中。
- 输出 steps/ 目录下的 Python Step Definitions（包括注释/修改槽/Reference 验证埋点）。
- 输出 behave.ini 配置文件 + **tests/bdd-relation-manager.md**（关系实时更新管理文件，包括 Reference 双向一致性列）。
- 所有关系表均为**轻量级可编辑格式**，支持手动/自动实时更新。
```

---

## IV. 知识库同步更新提示词（包括 Reference/Script 同步）

### 适用场景
当有**新/更新的业务文档**时，生成**增量更新、关系/Reference/Script 同步**的知识库同步更新流程，确保规则、Skills 和 BDD References 及关系随着规则更新而实时维护。

### Prompt 7（新业务文档 - 知识库增量更新流程生成）
```
### 说明
基于当前 [Initial Margin Calculation Guide HKv14] Git 结构化知识库框架，生成**新业务文档**的知识库增量同步更新流程，核心要求是"增量更新而非重建，关系/Reference/Script 实时同步，全流程可追溯"，满足以下要求：
1. 业务场景：新业务文档，与原规则无冲突，仅新增规则模块。
2. 流程按**可执行、分步**方式设计，覆盖从原始文档归档到 Script 执行的全链路，包括：原始文档归档 → MD 规则转换（标记全局流程节点/结构化段落 ID）→ Copilot Skill 添加（完善 Reference）→ 测试用例/BDD 添加（标记 Reference 验证槽）→ **关系/Reference 实时更新** → Script 编写（同步/验证/Git 链接）→ 多模型验证配置同步 → Copilot 适配 → 验证落地。
3. 每步明确定义**操作要求、文件规范、存储路径、追溯要求、Reference/Script 更新标准**。
4. 流程明确**需要同步更新的关系/Reference 文件**（skill-bdd-relation.md/bdd-relation-manager.md/config/skill-reference-spec.md）及更新规范。
5. 仅基于现有知识库框架设计；禁止添加无关操作。

### 输入（替换为现有知识库框架）
[粘贴 Prompt 2 生成的 Git 仓库目录树 + 核心配置文件 + 全局流程流程图描述]

### 输出要求
- 输出分步增量更新流程（包括步骤名称/操作要求/Reference/Script 更新标准/验证标准）。
- 输出新文档的**全局流程节点匹配/Reference 映射要求**。
- 输出关系/Reference/Script 文件的**增量更新模板**，可直接填写使用。
```

### Prompt 8（更新现有业务文档 - 知识库同步更新流程生成 + Reference/Script 同步）
```
### 说明
基于当前 [Initial Margin Calculation Guide HKv14] Git 结构化知识库框架，生成**更新现有业务文档**的知识库同步更新流程，核心要求是"增量修改，关系/Reference/Script 实时同步，无关联错误修改"，满足以下要求：
1. 业务场景：更新现有业务文档，原规则修订/优化/更正，可能影响关联的 MD 规则/Copilot Skills/测试用例/BDD 及 Reference/Script。
2. 流程按**可执行、分步**方式设计，覆盖从影响范围梳理到 Script 执行的全链路，包括：**影响范围梳理（包括 Reference 映射）** → MD 规则增量修改（标记全局流程节点/结构化段落 ID）→ Copilot Skill 同步修改（更新 Reference）→ 测试用例/BDD 迭代（更新 Reference 验证槽）→ **关系/Reference 全同步更新** → Script 执行（同步/验证/Git 链接）→ 多模型验证配置更新 → Copilot 适配 → 全面验证 → Git 版本标记。
3. 每步明确定义**操作要求、修改规范、追溯标记、Reference/Script 更新要求**，强调"仅修改受影响内容，未变更部分保持不变"。
4. 流程明确**更新标记规范、Reference 验证标准、Git 回滚机制**，以及更新错误时的**关系/Reference/Script 回滚要求**。
5. 仅基于现有知识库框架设计；禁止添加无关操作。

### 输入（替换为现有知识库框架）
[粘贴 Prompt 2 生成的 Git 仓库目录树 + 核心配置文件 + Skill/BDD 关系表]

### 输出要求
- 输出分步同步更新流程（包括步骤名称/操作要求/修改规范/Reference/Script 更新要求）。
- 输出"**规则更新影响范围列表**"模板（包括文件路径/变更类型/Reference 影响/Script 影响/全局流程节点影响）。
- 输出更新标记规范、Reference/Script 回滚要求、Git 版本标记要求。
- 输出受影响的关系/Reference/Script 文件**修改列表模板**，可直接团队使用。
```

---

## V. 多模型协作验证提示词（包括 Reference/Script 验证）

### 适用场景
生成**多模型协作验证配置/流程/判断标准**，添加 Reference 完整性和 Script 执行结果验证维度，实现知识库（MD 规则/Skills/BDD）的自动化多模型验证，确保验证准确性和可靠性，减少手动同行评审需求。

### Prompt 9（知识库多模型协作验证整体解决方案生成）
```
### 说明
基于 [Initial Margin Calculation Guide HKv14] 知识库的核心目标（可追溯/可验证/可更新/可扩展）和现有知识库内容（MD 规则/Skills/BDD/Reference/Script），生成**知识库合规多模型协作验证整体解决方案**，核心目标是替代手动同行评审，确保验证的准确性和可靠性，满足以下要求：
1. 明确多模型协作验证的**核心验证目标、参与模型分工、验证维度和结果融合规则**，添加"Reference 完整性验证"和"Script 执行结果验证"维度。参与模型按功能分为"规则对齐验证模型/关系完整性模型/Reference 一致性模型/Script 执行模型/追溯一致性模型"，避免重复验证。
2. 设计**多模型协作验证标准化流程**，包括：验证触发条件 → 待验证内容的标准化输入（包括 Reference 结构化字段）→ 多模型并行验证 → 验证结果收集 → 结果融合和判断 → 问题报告生成 → 整改建议输出，明确每个环节的**操作要求、输入/输出格式和时间节点**。
3. 定义**待验证内容的标准化输入规范**（按 MD 规则/Skills/BDD 分类），添加 Reference/Script 专属输入字段，确保所有模型的输入格式统一，提高验证一致性。
4. 制定**多模型验证结果判断标准**，分为"通过/条件通过/失败"，明确定义不同结果的**判断阈值和问题分级标准**（高/中/低风险）。Reference/Script 验证失败直接判定为"条件通过"并触发手动回退。
5. 设计**验证结果融合机制**，基于"模型权重 + 验证维度重要性"融合多模型结果，将 Reference/Script 验证权重提升至 30%（核心追溯/自动化维度），避免单一模型偏差导致的误判。
6. 仅基于知识库核心目标和现有内容设计；适配 M365/GitHub Copilot 可调用模型系统。

### 输入（替换为知识库核心信息）
[粘贴知识库核心目标 + MD 规则/Skills/BDD 核心模块 + Reference/Script 描述 + 关系管理文件描述]

### 输出要求
- 输出多模型协作验证整体解决方案文档（包括分工/流程/输入规范/判断标准/融合机制/Reference/Script 验证权重）。
- 输出**多模型验证配置文件**（config/multi-model-verify-config.yaml），包括模型分工/权重/输入格式/判断阈值/Reference/Script 验证规则，可直接配置使用。
- 输出**验证触发条件列表**（如知识库更新/添加/版本迭代/Script 执行失败时自动触发）。
```

### Prompt 10（子模块多模型协作验证执行提示词生成）
```
### 说明
基于生成的多模型协作验证整体解决方案，为**MD 规则/Copilot Skills/BDD 场景**三个核心模块生成**标准化、可直接调用**的多模型协作验证执行提示词，添加 Reference/Script 验证维度，满足以下要求：
1. 每个模块的验证提示词包含**模型分工、输入格式、验证维度（包括 Reference/Script）、输出要求和结果判断依据**，与整体解决方案的配置要求一致。
2. 验证维度覆盖每个模块的核心合规要求，添加 Reference/Script 专属维度：
   - MD 规则：追溯性/上下游关联/全局流程节点匹配/无外部信息引入/**结构化 ID 唯一性/Reference 映射完整性**
   - Copilot Skills：规则对齐/BDD 关联预嵌入/业务域识别/示例响应准确性/**Reference 完整性/Script 执行成功率**
   - BDD 场景：规则对齐/多维关系完整性/可执行性/上下游流程匹配/**Reference 双向一致性/Skill Test_Reference 匹配度**
3. 每个提示词为**模块化可调用格式**，支持在 M365/GitHub Copilot 中直接调用多模型执行验证，输出标准化验证结果。
4. 明确**多模型结果输出格式**（统一 JSON/表格），添加 Reference/Script 验证结果字段，便于后续结果融合和问题报告生成。
5. 验证结果需要包含**问题点/风险等级/规则依据/Reference/Script 整改建议**，为后续知识库优化提供直接依据。

### 输入（替换为多模型协作验证整体解决方案核心内容）
[粘贴多模型分工/验证维度（包括 Reference/Script）/输入/输出规范/结果判断标准]

### 输出要求
- 输出**MD 规则/Copilot Skills/BDD 场景**的多模型协作验证执行提示词（各 1 个，可直接调用）。
- 输出**标准化验证结果模板**（JSON + 表格版本），包括问题点/风险等级/规则依据/Reference/Script 整改建议。
- 输出**问题报告自动生成规则**，基于验证结果快速生成知识库优化问题报告。
```

### Prompt 11（多模型验证结果融合和知识库优化建议生成）
```
### 说明
基于 [Initial Margin Calculation Guide HKv14] 多模型协作验证结果融合机制和标准化验证结果（包括 Reference/Script 维度），生成**多模型验证结果融合报告 + 优先级知识库优化建议**，满足以下要求：
1. **自动融合**多模型验证结果，根据"模型权重 + 验证维度重要性（Reference/Script 权重 30%）"，消除单一模型偏差结果，生成统一融合报告。
2. 融合报告包括：整体验证结论（通过/条件通过/失败）、按模块（按业务域/风险等级/Reference/Script 维度）的问题统计、核心问题点摘要，以及跨业务域关联问题标记。
3. 基于融合报告中的问题点，生成**优先级知识库优化建议**，按"高/中/低"优先级划分。每个建议明确定义：
   - 优化点：需要修改的具体知识库内容（MD/Skills/BDD/Reference/Script/关系文件）
   - 风险等级：高/中/低
   - 操作要求：增量修改/添加/删除，明确上下游关系/Reference/Script 同步要求
   - 验证标准：优化后需满足的合规要求/多模型验证通过标准（包括 Reference/Script 验证阈值）
   - 关系更新：是否需要同步更新关系文件及更新要求
4. 优化建议遵循"增量修改，不重建，不遗漏上下游关联"的原则，可直接指导知识库优化落地。

### 输入（替换为多模型验证结果）
[粘贴多模型验证结果（JSON/表格格式，包括 Reference/Script 维度）]

### 输出要求
- 输出多模型验证结果融合报告（包括整体结论/问题统计/核心问题摘要/跨业务域关联问题）。
- 输出**优先级知识库优化建议**（高/中/低优先级，包括操作要求/验证标准/关系更新要求）。
- 输出**优化实施检查表**（分步实施步骤，包括 Reference/Script 同步更新要求）。
```

---

## VI. 知识库更新标准化检查表生成提示词（包括 Reference/Script/多模型/手动回退）

### 适用场景
生成**覆盖所有更新类型的知识库更新标准化检查表，包括 Reference/Script 验证、多模型协作验证和预嵌入手动回退审计点**，用于更新操作审计、验证和归档，确保符合全生命周期管理要求。

### Prompt 12（知识库更新标准化检查表生成，包括 Reference/Script/多模型验证 + 手动回退）
```
### 说明
基于 [Initial Margin Calculation Guide HKv14] 知识库的**新增/更新/批量更新**三种场景，生成**可直接打印填写、全链路覆盖、包括 Reference/Script/多模型协作验证、预嵌入手动回退审计点**的标准化检查表。核心检查目标是确保知识库更新符合"可追溯/可验证/可更新/可扩展"核心目标，满足以下要求：
1. 检查表包括**基本合规、Reference/Script 验证、多模型协作验证、配置文件同步、关系更新、Copilot 适配、手动回退审计和版本管理**八个模块，覆盖所有更新环节。明确区分新增/更新场景的检查项。
2. 每个检查项明确定义**检查标准、合规填写槽（√/×/N/A）和备注/问题记录槽**。Reference/Script 模块明确定义**结构化格式/执行结果/同步更新要求**。多模型验证模块明确定义**验证结果要求和融合报告审计点**。手动回退模块明确定义**审计节点、审计负责人和审计标准**。
3. 关系更新模块明确定义 **skill-bdd-relation.md/bdd-relation-manager.md/config/skill-reference-spec.md** 的更新完整性和 Reference 一致性检查要求，确保关系实时同步。
4. 检查表包括**基本信息栏、Reference/Script 验证结果栏、多模型验证结果栏、手动回退审计栏、审计结论栏、整改要求栏和附录（更新文件 + 关系 + Reference/Script 列表）**，可直接归档。
5. 检查标准与现有知识库的更新流程、多模型验证解决方案和手动回退机制一致，无冲突。

### 输入（替换为核心更新规范 + 多模型验证 + 手动回退要求）
[粘贴核心更新流程要求 + 多模型验证判断标准（包括 Reference/Script） + 手动回退审计节点/标准]

### 输出要求
- 输出完整的知识库更新标准化检查表（包括所有模块/检查项/填写槽，预嵌入手动回退审计签名槽）。
- 检查表格式清晰，按模块和场景划分，可直接打印填写/电子编辑。
- 包含附录 1"更新文件列表"（模块/文件名/路径/变更类型/追溯性/Reference ID）和附录 2"关系/Reference/Script 更新列表"（文件名/更新项/更新者/更新时间/验证结果）。
- 输出检查表使用说明（填写规范/审计流程/Reference/Script 验证结果录入要求/手动回退审计流程/归档要求）。
```

---

## VII. 知识库全生命周期管理 - 手动回退机制设置提示词（包括 Reference/Script 回退）

### 适用场景
生成**知识库全生命周期（构建/更新/验证/优化/归档）的手动回退机制设置解决方案**，添加 Reference/Script 异常回退节点，明确回退节点、审计流程、权限管理和问题整改，确保 AI 自动化流程失败时知识库的可靠性。

### Prompt 13（知识库全生命周期手动回退机制整体设置解决方案）
```
### 说明
基于 [Initial Margin Calculation Guide HKv14] 知识库的 Git 框架、多模型协作验证解决方案（包括 Reference/Script）和更新流程，生成**知识库全生命周期（构建 → 更新 → 验证 → 优化 → 归档）手动回退机制整体设置解决方案**，核心目标是"当 AI 自动化流程失败/异常时，通过手动回退确保知识库的准确性、一致性和可追溯性"，满足以下要求：
1. 明确手动回退的**核心原则、回退范围和责任体系**。原则是"**AI 为主，手动回退，节点控制，全流程追溯**"。回退范围添加"Reference 验证失败/Script 执行异常"场景，覆盖知识库全生命周期的所有 AI 自动化环节。责任体系明确定义**各环节的负责人/审计员/整改员**（按模块划分）。
2. 为知识库**构建/更新/多模型验证/优化/归档**每个生命周期阶段设计**专属手动回退节点、审计流程和触发条件**，添加 Reference/Script 专属回退触发条件（如 Reference 完整性验证失败、Script 执行失败且无自动回退逻辑）。
3. 每个回退节点明确定义**手动审计标准、操作流程、决策权限和整改要求**。Reference/Script 回退审计标准需与 `config/skill-reference-spec.md` 和 Script 执行规范匹配。
4. 设计**手动回退权限管理解决方案**（基于 Git 仓库 + 知识库治理层），按"**查看/编辑/审计/决策**"四级权限划分，添加"Reference/Script 审计权限"，匹配不同回退角色，确保最小权限。
5. 建立**手动回退问题整改和跟踪机制**，包括问题上报/分级/整改/验证/关闭全流程，添加 Reference/Script 问题分级标准（高风险：Reference 映射错误；中风险：Script 执行异常；低风险：Reference 格式不规范），确保回退发现的问题 100% 关闭。
6. 设计**手动回退文档和归档机制**；所有手动回退操作（审计/决策/整改）需记录在知识库治理层（governance/）并与对应的 Reference/Script ID 关联，以便追溯和审计。

### 输入（替换为知识库框架 + 多模型验证 + 更新流程核心内容）
[粘贴 Git 仓库目录树（包括治理层） + 多模型验证结果判断标准（包括 Reference/Script） + 知识库更新流程 + 核心目标]

### 输出要求
- 输出知识库全生命周期手动回退机制整体解决方案文档（包括原则/范围/责任体系/各阶段回退节点（包括 Reference/Script）/审计流程/权限管理）。
- 输出**各阶段手动回退审计表**（可编辑，包括 Reference/Script 验证结果/审计标准/结果/签名/时间）。
- 输出**回退问题整改跟踪机制** + 整改跟踪表（可编辑，包括问题点/分级（包括 Reference/Script）/负责人/整改时间/验证结果）。
- 输出治理层（governance/）**手动回退文档存储规范**（包括文件命名/路径/归档要求/Reference/Script 关联规则）。
```

### Prompt 14（手动回退机制落地和执行规范生成）
```
### 说明
基于生成的知识库全生命周期手动回退机制整体解决方案，生成**可直接落地执行**的手动回退机制执行规范，附带生成治理层所需的**所有文档模板/记录表**，添加 Reference/Script 专属回退文档，满足以下要求：
1. 执行规范包括**回退角色职责（包括 Reference/Script 审计角色）、触发条件执行细节（包括 Reference/Script 异常）、审计流程操作步骤、权限管理执行要求、问题整改闭环要求和文档归档规范**。所有内容可直接指导团队执行，无模糊表述。
2. 为治理层（governance/）生成**全套可编辑文档模板/记录表**，按生命周期阶段分类，添加 Reference/Script 专属模板：
   - 构建阶段：governance/build/manual audit table.md、fallback decision record.md、Reference mapping audit table.md
   - 更新阶段：governance/update/impact scope manual verification table.md、relationship/Reference manual audit table.md、Script execution exception fallback table.md
   - 验证阶段：governance/verify/multi-model result inconsistency manual judgment table.md、Reference/Script verification failure fallback table.md、verification issue reporting table.md
   - 优化阶段：governance/optimize/optimization suggestion manual audit table.md、Reference/Script rectification result verification table.md
   - 归档阶段：governance/archive/version archiving manual audit table.md、knowledge base audit record table.md、Reference/Script archiving specifications.md
   - 通用：governance/common/fallback issue rectification tracking table.md（包括 Reference/Script 列）、permission assignment table.md（包括 Reference/Script 审计权限）、responsible person change record.md
3. 明确**手动回退操作与 Git 仓库操作的联动要求**（如 PR 合并前需 Reference/Script 审计通过、版本标记），确保手动回退机制与 Git 版本控制深度集成。
4. 制定**手动回退机制的迭代优化规则**，定期（如季度）审查和优化回退节点（包括 Reference/Script）、审计标准和责任体系，以适应知识库扩展和业务规则迭代。

### 输入（替换为手动回退机制整体解决方案核心内容）
[粘贴手动回退责任体系/各阶段回退节点（包括 Reference/Script）/审计标准/权限管理解决方案]

### 输出要求
- 输出知识库手动回退机制执行规范（可直接落地，包括 Reference/Script 专属条款）。
- 输出治理层（governance/）**全套文档模板/记录表**（可编辑，MD 格式，包括 Reference/Script 字段）。
- 输出**手动回退与 Git 操作联动流程**（包括 PR 审计/版本标记/回退 Reference/Script 审计要求）。
- 输出**手动回退机制迭代优化检查表**（用于季度审查，可直接填写，包括 Reference/Script 回退节点审查项）。
```

---

## VIII. 验证和优化提示词（多模型 + 手动双重验证 + Reference/Script）

### 适用场景
知识库更新完成后，执行**多模型协作验证 + 手动抽查双重验证**，生成验证报告和优化建议，持续提升知识库质量。

### Prompt 15（知识库更新验证 + 优化建议生成）
```
### 说明
基于 [Initial Margin Calculation Guide HKv14] 知识库更新内容（MD 规则/Skills/BDD/Reference/Script）和多模型协作验证结果（包括 Reference/Script 维度），执行**多模型协作验证 + 手动抽查双重验证**，生成验证报告和优化建议，满足以下要求：
1. 对更新后的知识库内容执行**自动化多模型协作验证**，覆盖所有模块（MD 规则/Skills/BDD），验证维度包括规则对齐、关系完整性、Reference 一致性、Script 执行成功率等。
2. 对高风险点（如 Reference 映射、Script 执行结果）执行**手动抽查**，抽查比例不低于 30%。
3. 生成**验证报告**，包括：整体验证结论（通过/条件通过/失败）、按模块（按业务域/风险等级/Reference/Script 维度）的问题统计、核心问题点摘要，以及跨业务域关联问题标记。
4. 基于验证结果，生成**优化建议**，按"高/中/低"优先级划分。每个建议明确定义：
   - 优化点：需要修改的具体知识库内容
   - 风险等级：高/中/低
   - 操作要求：增量修改/添加/删除
   - 验证标准：优化后需满足的合规要求
5. 优化建议遵循"增量修改，不重建"的原则，可直接指导知识库优化落地。

### 输入（替换为知识库更新内容 + 多模型验证结果）
[粘贴更新后的 MD 规则/Skills/BDD 内容 + 多模型标准化验证结果（包括 Reference/Script 字段）]

### 输出要求
- 输出验证报告（包括整体结论/问题统计/核心问题摘要）。
- 输出优先级优化建议（按高/中/低划分）。
- 输出问题整改跟踪表（可编辑）。
```

---

## 附录：提示词使用指南

### 面向业务分析师（BA）
- **Prompt 1-2**：用于转换业务规则和构建知识库框架
- **Prompt 7-8**：用于处理业务文档更新
- **Prompt 13-14**：用于设计手动回退机制

### 面向 QA Lead
- **Prompt 3-4**：用于开发 Copilot Skills
- **Prompt 5-6**：用于生成测试用例和 BDD 场景
- **Prompt 9-12**：用于设计验证流程和检查表
- **Prompt 15**：用于验证和优化

### 面向自动化测试工程师
- **Prompt 5-6**：用于生成和维护自动化测试用例
- **Prompt 9-11**：用于执行多模型验证
- **Prompt 16**：用于开发自动化 Scripts

### 协作流程
1. BA 使用 Prompt 1-2 构建知识库框架
2. QA Lead 使用 Prompt 3-4 开发 Skills
3. 自动化测试工程师使用 Prompt 5-6 生成测试用例
4. 所有角色协作使用 Prompt 7-8 进行更新
5. 使用 Prompt 9-12 进行验证和审计
6. 使用 Prompt 13-15 进行回退和优化

---

## 版本历史

| 版本 | 日期 | 作者 | 变更 |
| --- | --- | --- | --- |
| 1.0 | 2025-03-13 | AI 助手 | 初始版本，包含 16 个核心提示词 |
| 1.1 | 2025-03-13 | AI 助手 | 翻译为中文，面向 BA、QA Lead 和自动化测试工程师 |

---

**注意**：本提示词集为 [Initial Margin Calculation Guide HKv14] 业务场景设计，可根据需要适配其他业务场景。