# How to Execute Prompts - Complete Guide

**Version**: 2.1.0
**Last Updated**: 2026-03-18
**Author**: System Administrator

## Overview

This guide provides step-by-step instructions for executing all 15 prompts in correct sequence, including LLM Checker System for validation. This guide has been enhanced with version control, parameterized configuration, monitoring capabilities, and security considerations.

## Prerequisites

Before starting, ensure you have:
- Access to source business documentation (PDF/Word/Excel/Email/etc.)
- LLM API access (for both Marker and Checker)
- Git repository cloned locally
- All configuration files in place
- **Configuration Management**: Review `config/prompt-config.json` for parameterized settings
- **Monitoring Setup**: Ensure monitoring and alerting systems are configured
- **Security Setup**: Verify access controls and security configurations are in place

## Generic Template Usage

The prompts in `chat-prompt-en.md` are now designed as generic templates. Before using them, you need to:

1. **Replace Placeholder**: Replace all instances of `[BUSINESS_DOCUMENT_NAME]` with your actual document name
2. **Update File Paths**: Ensure file paths in the prompts match your actual directory structure
3. **Configure Input**: Provide the actual content of your business document as input

### Example:
- If your document is named "Credit Risk Assessment Guide v2.0", replace all `[BUSINESS_DOCUMENT_NAME]` with `Credit Risk Assessment Guide v2.0`
- The output file will be created at `docs/source-files/Credit Risk Assessment Guide v2.0.md`

## Configuration Management

### Parameterized Configuration
All prompts now support parameterized configuration through `config/prompt-config.json`:

```json
{
  "prompt_config": {
    "common": {
      "language": "English",
      "output_dir": "outputs",
      "timeout": 300
    },
    "prompt1": {
      "md_template": "templates/md-template.md",
      "rule_extractor": "scripts/rule-extractor.py"
    },
    "prompt3": {
      "skill_templates": "templates/skill-templates/",
      "user_types": ["BA", "QA Lead", "Automation Tester", "Mixed"]
    }
  }
}
```

### Environment Variables
Configure environment-specific settings:
- `PROMPT_ENV`: Development/Staging/Production
- `LLM_API_KEY`: API key for LLM services
- `MONITORING_ENABLED`: Enable/disable monitoring
- `SECURITY_LEVEL`: Security compliance level

## Monitoring and Alerting

### Real-time Monitoring
All prompt executions are monitored in real-time:
- **Execution Time**: Track time for each prompt execution
- **Resource Usage**: Monitor memory and CPU usage
- **Error Tracking**: Log and track all errors
- **Dependency Monitoring**: Track dependencies between prompts

### Alerting System
Threshold-based alerts are configured for:
- **Performance**: Alert if execution time exceeds threshold
- **Errors**: Alert on critical errors
- **Resource Usage**: Alert on high resource consumption
- **Confidence Levels**: Alert if checker confidence is below threshold

## Security Considerations

### Access Control
- Role-based access control for all prompts and resources
- Least privilege principle applied to all operations
- Audit logging enabled for all operations

### Data Protection
- Input validation for all user inputs
- Data encryption for sensitive information
- Secure default configurations
- Regular security updates applied

### Best Practices
- Validate all inputs before processing
- Use secure communication channels
- Implement proper error handling
- Regular security audits

## Execution Sequence

```
Phase I: P1 → P2
Phase II: P3 → P4 → P5 → P6 → [Checker 6] → P7 → [Checker 7]
Phase III: P8/P9 (as needed)
Phase IV: P10 → P11
Phase V: P12 → P13
Phase VI: P14 → P15
```

---

## Phase I: Knowledge Base Foundation

### Prompt 1: Structured MD Knowledge Base Generation

**Purpose**: Convert source documents to structured MD files with paragraph IDs

**Input**:
- Source document: `Initial Margin Calculation Guide HKv14` (supports PDF, Word, Excel, Email, and other formats)

**Steps**:
1. Open `chat-prompt-en.md`
2. Copy Prompt 1 content
3. Replace input placeholder with actual document content
4. Execute with LLM
5. Review generated MD files
6. Verify multi-format conversion (if source is not PDF)

**Expected Output** (in `docs/source-files/`):
- `Initial Margin Calculation Guide HKv14.md` (verbatim conversion from source format)
- `Introduction-Overview.md`
- `Risk-Parameter-File-Specification.md`
- `Input-Data-Specification.md`
- `Market-Risk-Component-Calculation.md`
- `Margin-Adjustment-Process.md`
- `Other-Risk-Components.md`
- `Position-Processing-Logic.md`
- `Collateral-Management.md`
- `Corporate-Action-Processing.md`
- `Calculation-Examples.md`
- `PROMPT1-OUTPUT.md`

**Verification**:
- Check all 11 MD files exist (including verbatim conversion)
- Verify structured IDs follow format: `{DOMAIN}-{SUBDOMAIN}-{SEQUENCE}`
- Confirm cross-references are valid
- Review `PROMPT1-OUTPUT.md` for execution logs
- Verify multi-format conversion quality (if source is not PDF)
- Check match confidence score is ≥ 95%

---

### Prompt 2: Framework Structure Creation

**Purpose**: Create 7-layer framework directory structure

**Input**:
- MD files from Prompt 1

**Steps**:
1. Ensure Prompt 1 outputs are in `docs/source-files/`
2. Copy Prompt 2 from `chat-prompt-en.md`
3. Execute with LLM
4. Verify directory creation

**Expected Output**:
- Directory structure created
- Configuration files in `config/`:
  - `FRAMEWORK-CONFIG.md`
  - `RULES-VERSION.md`
  - `PROMPT2-OUTPUT.md`
- Templates in `config/skill-templates/`

**Verification**:
```bash
ls docs/ config/ copilot-skills/ tests/ governance/ scripts/
```

---

## Phase II: AI Capability & Test Assets

### Prompt 3: Copilot Skill Generation

**Purpose**: Generate modular Copilot Skills with embedded references

**Input**:
- MD files from `docs/source-files/`
- Framework configuration from `config/`

**Steps**:
1. Review `docs/source-files/` for completeness
2. Copy Prompt 3 from `chat-prompt-en.md`
3. Paste relevant MD content as input
4. Execute with LLM
5. Review generated skills

**Expected Output** (in `copilot-skills/skill-definitions/`):
- `hkex-intro-overview.md`
- `hkex-risk-parameters.md`
- `hkex-portfolio-margin.md`
- `hkex-flat-rate-margin.md`
- `hkex-lra-calculation.md`
- `hkex-structured-product-addon.md`
- `hkex-corporate-action-margin.md`
- `hkex-margin-adjustment.md`
- `hkex-collateral-management.md`
- `hkex-position-processing.md`
- `PROMPT3-OUTPUT.md`

**Verification**:
- Check all skills have structured references
- Verify `Rule_Source`, `Test_Reference`, `Verify_Reference` fields
- Review `skill-index.md`

---

### Prompt 4: BDD Framework Setup

**Purpose**: Prepare BDD framework and templates

**Input**:
- Skills from Prompt 3
- Framework configuration

**Steps**:
1. Ensure skills are generated
2. Copy Prompt 4 from `chat-prompt-en.md`
3. Execute with LLM

**Expected Output**:
- BDD directories created:
  - `tests/bdd/features/`
  - `tests/bdd/steps/`
  - `tests/bdd/templates/system/`
  - `tests/bdd/templates/user/`
- Template files for Type A/B/C/D users
- `PROMPT4-OUTPUT.md`

---

### Prompt 5: Template Learning

**Purpose**: Learn from user-provided templates

**Input**:
- User templates (if any) in `tests/bdd/templates/user/`
- System templates from Prompt 4

**Steps**:
1. Place user templates in `tests/bdd/templates/user/` (optional)
2. Copy Prompt 5 from `chat-prompt-en.md`
3. Execute with LLM

**Expected Output**:
- `tests/bdd/learned/template-profiles.json`
- `tests/bdd/learned/style-guide.md`
- `PROMPT5-OUTPUT.md`

---

### Prompt 6: Test Case Generation (MARKER) ⭐

**Purpose**: Generate structured test cases from business rules

**Input**:
- MD files with structured IDs
- Skills with references
- Templates from Prompt 5

**Steps**:
1. Select specific rule points from MD files
2. Copy Prompt 6 from `chat-prompt-en.md`
3. Paste rule content as input
4. Execute with LLM
5. Review generated test cases

**Expected Output** (in `tests/test-cases/`):
- `TC-IM-CALC-001.md`
- `TC-IM-CALC-002.md`
- `TC-COMPLIANCE-001.md`
- ... (more test cases)
- `PROMPT6-OUTPUT.md`

**Critical**: Before proceeding to Prompt 7, **MUST** run Checker 6

---

## Validation Layer: Checker System

### Checker 6: Test Case Validation

**Purpose**: Validate Prompt 6 outputs against original rules

**Input**:
- Marker output: `governance/analysis/outputs/PROMPT6-OUTPUT.md`
- Original rules: Relevant MD files from `docs/source-files/`
- Checker prompt: `governance/checker/prompts/checker-prompt.md`

**Steps**:
1. Open `governance/checker/CHECKER-HOW-TO.md`
2. Prepare input files:
   - Copy PROMPT6-OUTPUT.md content
   - Identify relevant MD rule files
3. Use `governance/checker/templates/checker-input-template.md`
4. Execute Checker LLM with Prompt 6 variant
5. Review validation report

**Expected Output**:
- Validation report using `governance/checker/outputs/output-template.md`
- Difference analysis (if issues found)
- Confidence level assessment
- Optimization suggestions

**Decision Points**:
- **Confidence >= 4**: Proceed to Prompt 7
- **Confidence 2-3**: Review suggestions, may proceed with minor fixes
- **Confidence < 2**: Return to Prompt 6 for revision

**Human Review**:
1. Initial Review: QA Lead reviews checker output
2. Peer Review: Senior QA validates findings
3. Final Approval: Project Manager authorizes

---

### Prompt 7: BDD Scenario Generation (MARKER) ⭐

**Purpose**: Generate executable BDD scenarios from test cases

**Input**:
- Validated test cases from Prompt 6
- Skills with references
- BDD templates from Prompt 4

**Steps**:
1. Ensure test cases are validated by Checker 6
2. Copy Prompt 7 from `chat-prompt-en.md`
3. Paste test case content as input
4. Execute with LLM
5. Review generated BDD scenarios

**Expected Output** (in `tests/bdd/`):
- `features/FT-IM-CALC-001.feature`
- `features/FT-IM-CALC-002.feature`
- `features/FT-COMPLIANCE-001.feature`
- ... (more feature files)
- `steps/step_definitions.py`
- `bdd-relation-manager.md`
- `PROMPT7-OUTPUT.md`

**Critical**: Before proceeding, **MUST** run Checker 7

---

### Checker 7: BDD Validation

**Purpose**: Validate Prompt 7 outputs (BDD scenarios)

**Input**:
- Marker output: `governance/analysis/outputs/PROMPT7-OUTPUT.md`
- Test cases from Prompt 6
- Original rules

**Steps**:
1. Prepare input files
2. Use `governance/checker/prompts/checker-prompt.md` (Prompt 7 variant)
3. Execute Checker LLM
4. Review validation report

**Expected Output**:
- Validation report
- Syntax validation results
- Traceability verification
- Executable check results

**Decision Points**:
- **All checks pass**: Proceed to Phase III
- **Minor issues**: Fix and re-check
- **Major issues**: Return to Prompt 7

---

## Phase III: Knowledge Base Synchronization

### Prompt 8: New Document Addition

**Purpose**: Add new business documents incrementally

**When to Use**: When new rules are added without changing existing ones

**Input**:
- New document content
- Existing knowledge base structure

**Steps**:
1. Identify new document content
2. Copy Prompt 8 from `chat-prompt-en.md`
3. Execute with LLM
4. Follow generated update process

**Output**:
- Incremental update process
- Global process node matching requirements
- Reference/Script synchronization requirements

---

### Prompt 9: Document Update

**Purpose**: Update existing business documents

**When to Use**: When existing rules are revised/modified

**Input**:
- Updated document content
- Original document content
- Existing knowledge base structure

**Steps**:
1. Identify changes between versions
2. Copy Prompt 9 from `chat-prompt-en.md`
3. Execute with LLM
4. Follow synchronization process

**Output**:
- Synchronization update process
- Rule Update Impact Scope List
- Rollback and version control requirements

---

## Phase IV: Verification

### Prompt 10: Multi-Model Verification

**Purpose**: Verify knowledge base using multiple LLM models

**Input**:
- Complete knowledge base (MD, Skills, Test Cases, BDD)

**Steps**:
1. Ensure all previous phases complete
2. Copy Prompt 10 from `chat-prompt-en.md`
3. Execute with multiple models
4. Compare results

**Output**:
- Multi-model verification report
- Inconsistency analysis
- Consensus results

---

### Prompt 11: Reference/Script Verification

**Purpose**: Verify all references and scripts

**Input**:
- All generated artifacts
- Reference specifications

**Steps**:
1. Copy Prompt 11 from `chat-prompt-en.md`
2. Execute with LLM
3. Review verification results

**Output**:
- Reference integrity report
- Script execution results
- Rollback procedures (if needed)

---

## Phase V: Optimization

### Prompt 12: Optimization Suggestions

**Purpose**: Generate optimization recommendations

**Input**:
- Complete knowledge base
- Verification results

**Steps**:
1. Copy Prompt 12 from `chat-prompt-en.md`
2. Execute with LLM
3. Review optimization suggestions

**Output**:
- Optimization report
- Improvement recommendations
- Priority rankings

---

### Prompt 13: Rectification

**Purpose**: Implement fixes and rectifications

**Input**:
- Optimization suggestions
- Issues identified

**Steps**:
1. Prioritize issues
2. Copy Prompt 13 from `chat-prompt-en.md`
3. Execute with LLM
4. Implement fixes

**Output**:
- Rectification plan
- Updated artifacts
- Verification results

---

## Phase VI: Completion

### Prompt 14: Version Archiving

**Purpose**: Archive version and create audit trail

**Steps**:
1. Ensure all changes complete
2. Copy Prompt 14 from `chat-prompt-en.md`
3. Execute with LLM

**Output**:
- Version archive
- Audit records
- Change history

---

### Prompt 15: Handover

**Purpose**: Complete knowledge base and handover

**Steps**:
1. Final review of all artifacts
2. Copy Prompt 15 from `chat-prompt-en.md`
3. Execute with LLM

**Output**:
- Completion report
- Handover documentation
- Maintenance guidelines

---

## Quick Reference

### File Locations

| Component | Location |
|-----------|----------|
| Prompt Definitions | `chat-prompt-en.md` |
| Source Documents | `docs/source-files/` |
| Generated MD Files | `docs/` |
| Copilot Skills | `copilot-skills/skill-definitions/` |
| Test Cases | `tests/test-cases/` |
| BDD Scenarios | `tests/bdd/features/` |
| Checker Prompts | `governance/checker/prompts/` |
| Checker Templates | `governance/checker/templates/` |
| Process Outputs | `governance/analysis/outputs/` |

### Checker System Quick Start

```bash
# 1. Prepare inputs
cat governance/analysis/outputs/PROMPT6-OUTPUT.md
cat docs/source-files/Initial\ Margin\ Calculation\ Guide\ HKv14.md

# 2. Use checker prompt
cat governance/checker/prompts/checker-prompt.md

# 3. Review templates
cat governance/checker/templates/checker-input-template.md
cat governance/checker/outputs/output-template.md

# 4. Check configuration
cat governance/checker/config/confidence-level-config.md
```

### Validation Checklist

- [ ] All 15 prompts defined in `chat-prompt-en.md`
- [ ] Prompt 1 outputs: 10 MD files with structured IDs
- [ ] Prompt 2 outputs: 7-layer framework created
- [ ] Prompt 3 outputs: 10+ Skills with references
- [ ] Prompt 6 outputs: Test cases with rule alignment
- [ ] Checker 6 validation: Confidence level >= threshold
- [ ] Prompt 7 outputs: BDD scenarios with traceability
- [ ] Checker 7 validation: All checks pass
- [ ] All references are bidirectional and consistent
- [ ] Documentation is updated

---

## Troubleshooting

### Common Issues

**Issue**: Checker confidence level too low
**Solution**: Review difference analysis, fix marker output, re-run checker

**Issue**: Missing references
**Solution**: Verify all Skills have complete `Rule_Source`, `Test_Reference`, `Verify_Reference`

**Issue**: BDD scenarios not executable
**Solution**: Check Gherkin syntax, verify step definitions exist

**Issue**: Test cases don't align with rules
**Solution**: Return to Prompt 6, provide clearer rule context

### Support Resources

- [Checker How-To Guide](governance/checker/CHECKER-HOW-TO.md)
- [Checker Flowchart](governance/checker/CHECKER-FLOWCHART.md)
- [Prompt Workflow Flowchart](PROMPT-WORKFLOW-FLOWCHART.md)
- [Governance Overview](governance/README.md)
