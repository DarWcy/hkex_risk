# Prompt 6 & 7 分析报告：用户类型 BDD 模板与差异变更跟踪

## 一、当前 Prompt 6 & 7 分析

### 1.1 Prompt 6 现状

**核心功能**：
- 生成结构化测试用例（Test Cases）
- 支持多维度关系 + Reference 验证槽
- 包含正向/负向/异常场景
- 标记全局流程节点

**现有用户类型模板**（第4-5点重复）：
- Type A (BA): 业务导向的测试用例模板
- Type B (QA Lead): 质量导向的测试用例模板
- Type C (Automation Tester): 自动化导向的测试用例模板
- Type D (Mixed/General): 通用测试用例模板

**问题**：
1. Import/Export 机制重复定义（第4点和第5点）
2. 用户类型模板只针对测试用例，未针对 BDD
3. 缺乏用户提供的模板学习机制
4. 缺乏差异分析和变更跟踪能力

### 1.2 Prompt 7 现状

**核心功能**：
- 基于测试用例生成 BDD/Behave 场景
- Gherkin 语法（Given/When/Then）
- 双向 Reference 可追溯性
- 实时更新系统

**现有模板结构**：
- Feature ID: FT-[module]-[number]
- Feature Description
- Background
- Scenario/Scenario Outline
- Examples
- Rule Basis
- Reference Verification Slot
- Relationships
- Update Marking

**问题**：
1. 没有用户类型预定义模板
2. 没有用户模板学习机制
3. 没有差异分析功能
4. 没有变更跟踪系统

---

## 二、需求分析

### 2.1 用户提供的 BDD 模板作为标准/参考

**场景**：
- 不同用户类型（BA/QA/自动化测试）可能有自己习惯的 BDD 书写风格
- 企业可能有既定的 BDD 规范模板
- 需要支持学习用户模板并应用到生成中

**需求**：
1. **模板导入**：支持导入用户提供的 BDD 模板文件
2. **模板解析**：分析模板结构、风格、关键词使用习惯
3. **模板学习**：提取模板特征，形成模板配置
4. **模板应用**：根据学习的模板生成符合用户风格的 BDD

### 2.2 差异分析与变更跟踪

**场景**：
- 需求文档频繁变更
- 需要知道新旧版本之间的差异
- 需要跟踪变更对测试用例和 BDD 的影响
- 需要记录变更历史

**需求**：
1. **差异检测**：自动检测需求文档变更
2. **影响分析**：分析变更对现有测试用例/BDD 的影响
3. **变更记录**：记录所有变更及其处理状态
4. **版本对比**：支持版本之间的对比查看

---

## 三、优化方案设计

### 3.1 用户类型 BDD 模板支持架构

```
┌─────────────────────────────────────────────────────────────┐
│                    BDD Template Manager                      │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Template   │  │   Template   │  │   Template   │      │
│  │   Importer   │  │   Analyzer   │  │   Learner    │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
├─────────────────────────────────────────────────────────────┤
│                    Template Repository                       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Type A   │ │ Type B   │ │ Type C   │ │ Type D   │       │
│  │ (User)   │ │ (User)   │ │ (User)   │ │ (User)   │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Type A   │ │ Type B   │ │ Type C   │ │ Type D   │       │
│  │ (System) │ │ (System) │ │ (System) │ │ (System) │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└─────────────────────────────────────────────────────────────┘
```

### 3.2 差异分析与变更跟踪架构

```
┌─────────────────────────────────────────────────────────────┐
│                 Change Tracking System                       │
├─────────────────────────────────────────────────────────────┤
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Change     │  │   Impact     │  │   Change     │      │
│  │   Detector   │  │   Analyzer   │  │   Logger     │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
├─────────────────────────────────────────────────────────────┤
│                    Change History DB                         │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐       │
│  │ Document │ │  Skill   │ │ TestCase │ │   BDD    │       │
│  │ Changes  │ │ Changes  │ │ Changes  │ │ Changes  │       │
│  └──────────┘ └──────────┘ └──────────┘ └──────────┘       │
└─────────────────────────────────────────────────────────────┘
```

---

## 四、详细设计方案

### 4.1 用户类型 BDD 模板支持

#### 4.1.1 模板导入机制

**新增到 Prompt 6 & 7**：

```markdown
### 6. **User BDD Template Import Mechanism**
Support importing user-provided BDD templates as standards or references:

**Template Import Sources**:
- **File Import**: Import from `.feature`, `.md`, `.json`, `.yaml` files
- **Directory Import**: Batch import from `tests/bdd/templates/user/` directory
- **Git Import**: Import from Git repository URL
- **Paste Import**: Direct paste of template content

**Template Import Configuration**:
- **Template Name**: User-defined template name
- **User Type**: Type A/B/C/D classification
- **Template Priority**: Primary/Secondary/Fallback
- **Scope**: Global/Module-specific/Skill-specific
- **Version**: Template version for tracking
```

#### 4.1.2 模板学习机制

**新增到 Prompt 6 & 7**：

```markdown
### 7. **BDD Template Learning System**
Automatically analyze and learn from user-provided templates:

**Learning Dimensions**:
1. **Structure Analysis**:
   - Feature file organization pattern
   - Scenario grouping strategy
   - Background usage frequency
   - Tag conventions

2. **Language Style**:
   - Gherkin keyword preferences (Given/When/Then/And/But)
   - Sentence structure patterns
   - Technical vs Business language ratio
   - Parameter naming conventions

3. **Content Patterns**:
   - Assertion style (strict vs flexible)
   - Data table formats
   - Examples table structures
   - Comment styles

4. **Relationship Patterns**:
   - ID naming conventions
   - Reference linking style
   - Metadata inclusion patterns

**Learning Output**:
- **Template Profile**: JSON configuration describing template characteristics
- **Style Guide**: Generated style guide based on learned patterns
- **Validation Rules**: Rules to ensure generated BDD matches template style
```

#### 4.1.3 模板存储结构

**新增目录结构**：

```
tests/
├── bdd/
│   ├── features/              # Generated BDD features
│   ├── steps/                 # Step definitions
│   ├── templates/             # BDD Templates
│   │   ├── system/            # System predefined templates
│   │   │   ├── type-a-ba-template.feature
│   │   │   ├── type-b-qa-template.feature
│   │   │   ├── type-c-auto-template.feature
│   │   │   └── type-d-general-template.feature
│   │   └── user/              # User imported templates
│   │       ├── user-template-001/
│   │       │   ├── template.feature
│   │       │   ├── template-profile.json
│   │       │   └── style-guide.md
│   │       └── user-template-002/
│   │           ├── template.feature
│   │           ├── template-profile.json
│   │           └── style-guide.md
│   └── learned/               # Learned template configurations
│       └── template-profiles.json
```

### 4.2 差异分析与变更跟踪

#### 4.2.1 变更检测机制

**新增到 Prompt 6 & 7**：

```markdown
### 8. **Requirement Change Detection**
Automatically detect changes in requirement documents:

**Change Types**:
- **Added**: New rules, scenarios, or requirements
- **Modified**: Changed rule logic, parameters, or assertions
- **Deleted**: Removed rules or scenarios
- **Moved**: Relocated content with structural changes

**Detection Methods**:
1. **Text Diff**: Line-by-line comparison of document content
2. **Semantic Diff**: Understanding meaning changes beyond text
3. **Structure Diff**: Detecting structural changes (sections, paragraphs)
4. **Reference Diff**: Tracking reference and link changes

**Change Metadata**:
- Change ID: Unique identifier for each change
- Change Type: Added/Modified/Deleted/Moved
- Location: File path + section/paragraph ID
- Severity: Critical/Major/Minor/Cosmetic
- Impact Scope: Affected Skills/Test Cases/BDD scenarios
```

#### 4.2.2 差异分析机制

**新增到 Prompt 6 & 7**：

```markdown
### 9. **Difference Analysis Engine**
Analyze differences between user templates and generated content:

**Analysis Dimensions**:

1. **Structure Differences**:
   ```markdown
   | Aspect | User Template | Generated | Difference | Action |
   |--------|---------------|-----------|------------|--------|
   | Feature Organization | By module | By rule | Different | Adapt |
   | Scenario Count | 3 per feature | 5 per feature | +2 | Review |
   | Background Usage | Always | Sometimes | Inconsistent | Standardize |
   ```

2. **Style Differences**:
   ```markdown
   | Aspect | User Template | Generated | Match % | Action |
   |--------|---------------|-----------|---------|--------|
   | Keyword Usage | "Given/When/Then" | Same | 100% | OK |
   | Sentence Length | 5-10 words | 8-15 words | 70% | Adjust |
   | Technical Terms | Low | High | 40% | Align |
   ```

3. **Content Differences**:
   ```markdown
   | Rule ID | Template Coverage | Generated Coverage | Gap | Priority |
   |---------|-------------------|-------------------|-----|----------|
   | RULE-001 | Full | Partial | Missing negative case | High |
   | RULE-002 | Partial | Full | Extra scenarios | Medium |
   ```

**Difference Report Format**:
- Summary: High-level difference overview
- Detailed List: Itemized differences with locations
- Recommendations: Suggested actions for alignment
- Impact Assessment: Effect on test coverage and quality
```

#### 4.2.3 变更跟踪系统

**新增到 Prompt 6 & 7**：

```markdown
### 10. **Change Tracking and History**
Comprehensive tracking of all changes across the lifecycle:

**Tracking Scope**:
- Document Changes: Source requirement document changes
- Skill Changes: Copilot Skill updates
- Test Case Changes: Test case additions/modifications/deletions
- BDD Changes: BDD scenario updates
- Template Changes: User template updates
- Relationship Changes: Cross-reference updates

**Change Record Structure**:
```json
{
  "change_id": "CHG-2026-001",
  "timestamp": "2026-03-14T10:30:00Z",
  "type": "requirement_update",
  "severity": "major",
  "source": {
    "document": "docs/hkex-margin-calculation.md",
    "version": "v2.1",
    "paragraph_id": "SEC-3.2-PARA-5"
  },
  "change_description": "Updated margin calculation formula",
  "diff": {
    "before": "Margin = Position * Price * Rate",
    "after": "Margin = Position * Price * Rate * AdjustmentFactor"
  },
  "impact": {
    "skills_affected": ["hkex-margin-calculation"],
    "test_cases_affected": ["TC-IM-CALC-001", "TC-IM-CALC-002"],
    "bdd_affected": ["FT-IM-CALC-001"]
  },
  "status": "processed",
  "actions_taken": [
    "Updated Skill definition",
    "Regenerated test cases",
    "Updated BDD scenarios"
  ],
  "verified_by": "QA-Lead",
  "verification_date": "2026-03-14T14:00:00Z"
}
```

**Change Tracking File**: `governance/change-history.md`
```

#### 4.2.4 变更跟踪存储结构

**新增文件和目录**：

```
governance/
├── change-history.md          # Master change history log
├── change-tracking/
│   ├── document-changes/      # Requirement document changes
│   │   ├── 2026-03-14-hkex-margin-update.json
│   │   └── 2026-03-15-hkex-risk-update.json
│   ├── skill-changes/         # Skill definition changes
│   ├── testcase-changes/      # Test case changes
│   ├── bdd-changes/           # BDD scenario changes
│   └── template-changes/      # Template changes
└── diff-reports/              # Generated diff reports
    ├── diff-2026-03-14.html
    └── diff-2026-03-14.md
```

### 4.3 集成到现有 Prompt 6 & 7

#### 4.3.1 Prompt 6 优化建议

**在现有第5点后添加**：

```markdown
### 6. **User BDD Template Import and Learning**
Support importing and learning from user-provided BDD templates:

**6.1 Template Import**:
- Import from `tests/bdd/templates/user/` directory
- Support formats: .feature, .md, .json, .yaml
- Associate with user types (A/B/C/D)

**6.2 Template Learning**:
- Analyze template structure, style, and patterns
- Generate template profile (JSON)
- Create style guide documentation
- Define validation rules

**6.3 Template Application**:
- Apply learned templates to test case generation
- Generate test cases matching user style
- Validate against template standards

### 7. **Difference Analysis and Change Tracking**
Track changes and analyze differences:

**7.1 Change Detection**:
- Monitor requirement document changes
- Detect Added/Modified/Deleted/Moved content
- Calculate change severity and impact

**7.2 Difference Analysis**:
- Compare user templates vs generated content
- Identify structure, style, and content gaps
- Generate difference reports

**7.3 Change Tracking**:
- Record all changes in `governance/change-history.md`
- Track impact across Skills/Test Cases/BDD
- Maintain change history with metadata
```

#### 4.3.2 Prompt 7 优化建议

**在现有输出要求后添加**：

```markdown
### Additional Requirements

**5. User BDD Template Support**:
- Load user templates from `tests/bdd/templates/user/`
- Apply learned template styles to BDD generation
- Generate BDD scenarios matching user conventions
- Validate against template standards

**6. Difference Analysis**:
- Compare generated BDD with user template standards
- Identify and report differences
- Suggest alignment actions
- Generate difference report: `tests/bdd/diff-report.md`

**7. Change Tracking Integration**:
- Record BDD changes in `governance/change-history.md`
- Link BDD changes to requirement changes
- Track version history of each BDD scenario
- Support rollback to previous versions

**8. Template Learning Output**:
- Generate `tests/bdd/learned/template-profiles.json`
- Document learned patterns in `tests/bdd/learned/style-guide.md`
- Update template repository with new learnings
```

---

## 五、实施建议

### 5.1 文件结构更新

```
project-root/
├── tests/
│   ├── bdd/
│   │   ├── features/              # Existing
│   │   ├── steps/                 # Existing
│   │   ├── templates/             # NEW
│   │   │   ├── system/            # System templates
│   │   │   └── user/              # User imported templates
│   │   ├── learned/               # NEW - Learned configurations
│   │   │   ├── template-profiles.json
│   │   │   └── style-guide.md
│   │   └── diff-reports/          # NEW - Difference reports
│   │       └── diff-report.md
│   └── PROMPT6-OUTPUT.md          # Existing
├── governance/
│   ├── change-history.md          # NEW - Master change log
│   ├── change-tracking/           # NEW
│   │   ├── document-changes/
│   │   ├── skill-changes/
│   │   ├── testcase-changes/
│   │   ├── bdd-changes/
│   │   └── template-changes/
│   └── PROMPT7-OUTPUT.md          # Existing
```

### 5.2 关键交付物

1. **Template Import Script**: `scripts/import-bdd-templates.py`
2. **Template Learning Script**: `scripts/learn-bdd-templates.py`
3. **Difference Analysis Script**: `scripts/analyze-bdd-differences.py`
4. **Change Tracking Script**: `scripts/track-changes.py`
5. **Template Profile Schema**: `config/template-profile-schema.json`
6. **Change Record Schema**: `config/change-record-schema.json`

### 5.3 流程集成

```
Prompt 6 Flow:
1. Input: Rule points + User type
2. Load: User templates (if available)
3. Learn: Template patterns
4. Generate: Test cases with template style
5. Analyze: Differences from template
6. Track: Changes in history
7. Output: Test cases + Diff report

Prompt 7 Flow:
1. Input: Test cases + User type
2. Load: User templates + Learned profiles
3. Generate: BDD scenarios with template style
4. Validate: Against template standards
5. Analyze: Differences
6. Track: BDD changes
7. Output: BDD features + Change log
```

---

## 六、总结

### 6.1 核心价值

1. **个性化**：支持不同用户类型的 BDD 书写风格
2. **一致性**：确保生成的 BDD 符合企业/团队标准
3. **可追溯**：完整记录所有变更及其影响
4. **可学习**：系统能从用户模板中学习和进化

### 6.2 下一步行动

1. 更新 Prompt 6 和 Prompt 7 的文档
2. 创建模板导入和学习脚本
3. 实现差异分析和变更跟踪功能
4. 建立模板存储库和变更历史数据库
5. 测试和验证完整流程
