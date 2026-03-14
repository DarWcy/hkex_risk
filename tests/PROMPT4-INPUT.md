# Prompt 4 Input File
## Skill Index + Relationship + Reference/Script Management + Usage Guidelines

### Input Skill Files List

Based on the generated Copilot Skill files from Prompt 3, here is the complete list of Skills:

1. **hkex-intro-overview**
   - Description: Introduction Overview Skill providing information about the Initial Margin Calculation Guide
   - Rule Version: 1.4
   - User Type: Type A (BA)
   - Rule Source: docs/Introduction-Overview.md | INTRO-001 to INTRO-015

2. **hkex-risk-parameters**
   - Description: Risk Parameter File Specification Skill
   - Rule Version: 1.4
   - User Type: Type B (QA Lead)
   - Rule Source: docs/Risk-Parameter-File-Specification.md | DATA-001 to DATA-028

3. **hkex-input-data**
   - Description: Input Data Specification Skill
   - Rule Version: 1.4
   - User Type: Type C (Automation Tester)
   - Rule Source: docs/Input-Data-Specification.md | CALC-001 to CALC-045

4. **hkex-market-risk**
   - Description: Market Risk Component Calculation Skill
   - Rule Version: 1.4
   - User Type: Type A + Type B (BA + QA Lead)
   - Rule Source: docs/Market-Risk-Component-Calculation.md | PROC-001 to PROC-022

5. **hkex-margin-adjustment**
   - Description: Margin Adjustment Process Skill
   - Rule Version: 1.4
   - User Type: Type A (BA)
   - Rule Source: docs/Margin-Adjustment-Process.md | ADJ-001 to ADJ-018

6. **hkex-other-risk**
   - Description: Other Risk Components Skill
   - Rule Version: 1.4
   - User Type: Type B (QA Lead)
   - Rule Source: docs/Other-Risk-Components.md | OTHER-001 to OTHER-015

7. **hkex-position-processing**
   - Description: Position Processing Logic Skill
   - Rule Version: 1.4
   - User Type: Type C (Automation Tester)
   - Rule Source: docs/Position-Processing-Logic.md | POS-001 to POS-030

8. **hkex-collateral-management**
   - Description: Collateral Management Skill
   - Rule Version: 1.4
   - User Type: Type A + Type B (BA + QA Lead)
   - Rule Source: docs/Collateral-Management.md | COLL-001 to COLL-012

9. **hkex-corporate-action**
   - Description: Corporate Action Processing Skill
   - Rule Version: 1.4
   - User Type: Type A (BA)
   - Rule Source: docs/Corporate-Action-Processing.md | CORP-001 to CORP-010

10. **hkex-calculation-examples**
    - Description: Calculation Examples Skill
    - Rule Version: 1.4
    - User Type: Type C (Automation Tester)
    - Rule Source: docs/Calculation-Examples.md | EX-001 to EX-020

### Skill Dependencies

Based on business logic and rule dependencies:

- **hkex-intro-overview** → All other Skills (foundation)
- **hkex-risk-parameters** → hkex-market-risk, hkex-other-risk
- **hkex-input-data** → hkex-market-risk, hkex-position-processing
- **hkex-market-risk** → hkex-margin-adjustment
- **hkex-position-processing** → hkex-market-risk, hkex-collateral-management
- **hkex-collateral-management** → hkex-margin-adjustment
- **hkex-corporate-action** → hkex-position-processing
- **hkex-calculation-examples** → hkex-market-risk, hkex-other-risk

### User Type Distribution

- **Type A (BA)**: 4 Skills (hkex-intro-overview, hkex-margin-adjustment, hkex-corporate-action)
- **Type B (QA Lead)**: 2 Skills (hkex-risk-parameters, hkex-other-risk)
- **Type C (Automation Tester)**: 3 Skills (hkex-input-data, hkex-position-processing, hkex-calculation-examples)
- **Type A + B**: 2 Skills (hkex-market-risk, hkex-collateral-management)

### Module Classification

1. **Introduction**: hkex-intro-overview
2. **Risk Parameters**: hkex-risk-parameters
3. **Input Data**: hkex-input-data
4. **Market Risk**: hkex-market-risk
5. **Margin Adjustment**: hkex-margin-adjustment
6. **Other Risk**: hkex-other-risk
7. **Position Processing**: hkex-position-processing
8. **Collateral**: hkex-collateral-management
9. **Corporate Action**: hkex-corporate-action
10. **Examples**: hkex-calculation-examples

### Execution Parameters

- **Language**: English ONLY
- **Incremental Update**: Enabled
- **Parallel Execution**: Enabled
- **Error Recovery**: Enabled
- **Performance Metrics**: Enabled

### Expected Outputs

1. **index.md** - Skill index with dependency graph
2. **skill-bdd-relation.md** - Relationship management table
3. **usage-guidelines.md** - Usage guidelines for all user types
4. **config/skill-verify-config.md** - Multi-model verification configuration
5. **config/skill-reference-spec.md** - Reference maintenance specifications
6. **PROMPT4-OUTPUT.md** - Process output file

---
Generated: 2026-03-14
Responsible: System
