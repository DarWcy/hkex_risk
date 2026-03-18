# Initial Margin Calculation Knowledge Base

**Version**: 2.2.0
**Last Updated**: 2026-03-18
**Author**: System Administrator

## Repository Overview

This Git repository serves as a **traceable, verifiable, updatable, and scalable** test business knowledge common baseline for the Initial Margin Calculation Guide HKv14. It supports full lifecycle management of business rules, AI-assisted capabilities (GitHub Copilot Skills), test assets (BDD scenarios), and comprehensive quality assurance through LLM Checker System.

### Enhanced Features (Version 2.2.0)

This version includes significant enhancements:
- **Generic Template Support**: Made prompts document-agnostic with [BUSINESS_DOCUMENT_NAME] placeholder
- **Multi-Format Support**: Added support for PDF, Word, Excel, Email, and other document formats
- **Version Control**: Structured version management for all prompts and documentation
- **Parameterized Configuration**: Flexible configuration management through JSON files
- **Real-time Monitoring**: Comprehensive monitoring and alerting system
- **Security Considerations**: Access control, input validation, and audit logging
- **Enhanced Traceability**: Improved rule-to-process mapping and bidirectional references
- **Best Practices**: Comprehensive guidelines for knowledge base management, skill development, and test automation
- **Troubleshooting Guide**: Detailed common issues and solutions

### Core Objectives

1. **Traceable**: Every rule, skill, and test case links to source documents via structured References
2. **Verifiable**: Multi-model collaborative verification ensures quality and consistency
3. **Updatable**: Incremental updates with synchronized relationship management
4. **Scalable**: Modular architecture supports knowledge base expansion
5. **Quality Assured**: LLM Checker System validates all outputs against original requirements

### Target Audience

- **Business Analysts (BA)**: Business rule understanding and requirement analysis
- **QA Leads**: Test strategy, verification, and quality assurance
- **Automation Testers**: Test case implementation and BDD scenario development

---

## Directory Navigation

```
initial-margin-knowledge-base/
├── docs/                          # Document Layer - Business Rules
│   ├── Introduction-Overview.md   # Module 1: VaR Platform introduction
│   ├── Risk-Parameter-File-Specification.md  # Module 2: IMRPF specifications
│   ├── Input-Data-Specification.md  # Module 3: Input data requirements
│   ├── Market-Risk-Component-Calculation.md  # Module 4: Market risk calculations
│   ├── Margin-Adjustment-Process.md  # Module 5: Margin adjustment rules
│   ├── Other-Risk-Components.md  # Module 6: Other risk components
│   ├── Position-Processing-Logic.md  # Module 7: Position processing
│   ├── Collateral-Management.md  # Module 8: Collateral management
│   ├── Corporate-Action-Processing.md  # Module 9: Corporate actions
│   ├── Calculation-Examples.md  # Module 10: Calculation examples
│   ├── global-process/            # Core business global process
│   │   ├── GLOBAL-PROCESS.md      # Process flow documentation
│   │   └── Core-Business-Global-Process-Flowchart.md  # Process flowchart
│   ├── rules/                     # Atomic rules
│   │   └── atomic-rules.json     # Extracted atomic rules
│   └── source-files/              # Original source documents
│       ├── [BUSINESS_DOCUMENT_NAME].pdf  # Source PDF (original)
│       ├── [BUSINESS_DOCUMENT_NAME].md   # Source MD (converted)
│       └── PROMPT1-OUTPUT.md      # Prompt 1 process output
│
├── copilot-skills/                # AI Capability Layer - Copilot Skills
│   ├── scripts/                   # Automation scripts
│   │   ├── M365-OPERATION-GUIDE.md
│   │   ├── SCRIPT-USAGE-GUIDE.md
│   │   ├── bdd-relationship-update.py
│   │   ├── dependency-integrity-validate.py
│   │   ├── execution-result-validate.py
│   │   ├── multi-model-verify.py
│   │   ├── skill-consistency-validate.py
│   │   └── skill-reference-sync.py
│   ├── skill-definitions/         # Individual skill files
│   │   ├── hkex-calculation-examples.md
│   │   ├── hkex-collateral-management.md
│   │   ├── hkex-corporate-action.md
│   │   ├── hkex-input-data.md
│   │   ├── hkex-intro-overview.md
│   │   ├── hkex-margin-adjustment.md
│   │   ├── hkex-market-risk.md
│   │   ├── hkex-other-risk.md
│   │   ├── hkex-position-processing.md
│   │   └── hkex-risk-parameters.md
│   ├── skill-index.md             # Skill index table
│   ├── PROMPT3-INPUT.md           # Prompt 3 input
│   └── PROMPT3-OUTPUT.md          # Prompt 3 process output
│
├── tests/                         # Test Asset Layer - Test Cases & BDD
│   ├── test-cases/                # Structured test cases
│   │   ├── README.md              # Test case guidelines
│   │   ├── index.md               # Test case index
│   │   ├── TC-COMPLIANCE-001.md
│   │   ├── TC-IM-CALC-001.md
│   │   └── TC-IM-CALC-002.md
│   ├── bdd/                       # BDD scenarios
│   │   ├── features/              # Feature files (.feature)
│   │   │   ├── FT-COMPLIANCE-001.feature
│   │   │   ├── FT-COMPLIANCE-002.feature
│   │   │   ├── FT-COMPLIANCE-003.feature
│   │   │   ├── FT-IM-CALC-001.feature
│   │   │   ├── FT-IM-CALC-002.feature
│   │   │   ├── FT-IM-CALC-003.feature
│   │   │   ├── FT-IM-CALC-004.feature
│   │   │   ├── FT-RISK-PARAM-001.feature
│   │   │   ├── FT-RISK-PARAM-002.feature
│   │   │   └── FT-RISK-PARAM-003.feature
│   │   ├── steps/                 # Python step definitions
│   │   │   └── step_definitions.py
│   │   ├── templates/             # BDD templates
│   │   │   └── system/            # System templates
│   │   │       ├── type-a-ba-template.feature
│   │   │       ├── type-b-qa-template.feature
│   │   │       ├── type-c-automation-template.feature
│   │   │       └── type-d-general-template.feature
│   │   ├── learned/               # Learned template configurations
│   │   │   ├── style-guide.md
│   │   │   └── template-profiles.json
│   │   ├── diff-reports/          # Difference analysis reports
│   │   │   └── diff-report.md
│   │   └── verification/          # Verification tools
│   │       ├── __init__.py
│   │       └── test-plan-change-verifier.py
│   ├── test-plans/                # Test plan templates
│   │   ├── test-plan-automation-tester-template.md
│   │   ├── test-plan-ba-template.md
│   │   ├── test-plan-mixed-template.md
│   │   └── test-plan-qa-lead-template.md
│   ├── config/                    # Test configuration
│   │   ├── skill-reference-spec.md
│   │   └── skill-verify-config.md
│   ├── bdd-relation-manager.md    # BDD relationship management
│   ├── skill-bdd-relation.md      # Skill-BDD relationship
│   ├── index.md                   # Test index
│   ├── usage-guidelines.md        # Test usage guidelines
│   ├── PROMPT4-INPUT.md           # Prompt 4 input
│   └── PROMPT4-OUTPUT.md          # Prompt 4 process output
│
├── config/                        # Configuration Layer
│   ├── rule-schema.json           # Rule schema definition
│   ├── FRAMEWORK-CONFIG.md        # Framework configuration
│   ├── RULES-VERSION.md           # Rule version overview
│   └── PROMPT2-OUTPUT.md          # Prompt 2 process output
│
├── governance/                    # Governance Layer - Quality Assurance & Process
│   ├── README.md                  # Governance overview
│   ├── DIRECTORY-STRUCTURE-PROPOSAL.md  # Directory structure proposal
│   ├── change-history.md          # Change history
│   │
│   ├── analysis/                  # Analysis and research documents
│   │   ├── prompts/               # Prompt logic analysis
│   │   │   ├── prompt-3-4-5-logic-analysis.md
│   │   │   ├── prompt-6-7-analysis.md
│   │   │   └── prompt-consistency-analysis.md
│   │   ├── outputs/               # Prompt input/output analysis
│   │   │   ├── PROMPT5-INPUT.md
│   │   │   ├── PROMPT5-OUTPUT.md
│   │   │   ├── PROMPT6-INPUT.md
│   │   │   ├── PROMPT6-OUTPUT.md
│   │   │   ├── PROMPT7-INPUT.md
│   │   │   └── PROMPT7-OUTPUT.md
│   │   └── templates/             # Template analysis
│   │       ├── prompt-template-creation-guide.md
│   │       └── template-prompt-mapping.md
│   │
│   ├── reviews/                   # Review system
│   │   ├── templates/             # Review templates by type
│   │   │   ├── skills/            # Skill review templates
│   │   │   │   ├── skill-review-template.md
│   │   │   │   └── skill-validation-review-template.md
│   │   │   ├── test/              # Test-related templates
│   │   │   │   ├── bdd-review-template.md
│   │   │   │   ├── test-execution-review-template.md
│   │   │   │   └── testcase-review-template.md
│   │   │   ├── code/              # Code review templates
│   │   │   │   └── script-review-template.md
│   │   │   ├── docs/              # Documentation templates
│   │   │   │   ├── documentation-review-template.md
│   │   │   │   ├── md-file-review-template.md
│   │   │   │   └── supporting-docs-review-template.md
│   │   │   ├── framework/         # Framework templates
│   │   │   │   ├── framework-review-template.md
│   │   │   │   └── incremental-update-review-template.md
│   │   │   └── governance/        # Governance templates
│   │   │       ├── audit-compliance-review-template.md
│   │   │       └── performance-review-template.md
│   │   ├── feedback/              # Feedback templates
│   │   │   ├── confidence-assessment.md
│   │   │   ├── failure-analysis-template.md
│   │   │   └── feedback-template.md
│   │   ├── executions/            # Review executions by prompt
│   │   │   ├── prompt1/
│   │   │   ├── prompt2/
│   │   │   ├── prompt3/
│   │   │   ├── prompt4/
│   │   │   ├── prompt5/
│   │   │   ├── prompt6/
│   │   │   ├── prompt7/
│   │   │   ├── prompt8-9/
│   │   │   ├── prompt10-11/
│   │   │   ├── prompt12-13/
│   │   │   └── prompt14-15/
│   │   ├── test-plan-confidence-template.md
│   │   ├── test-plan-failure-analysis-template.md
│   │   └── test-plan-review-template.md
│   │
│   ├── checker/                   # LLM Checker System ⭐
│   │   ├── prompts/               # Checker prompts
│   │   │   ├── checker-prompt.md
│   │   │   ├── generic-checker-prompt-generator.md
│   │   │   └── generic-checker-prompt-generator-usage.md
│   │   ├── templates/             # Checker templates
│   │   │   ├── checker-input-template.md
│   │   │   ├── checker-output-template.md
│   │   │   ├── diff-analysis-template.md
│   │   │   ├── exit-report-template.md
│   │   │   ├── feedback-template-final-approval.md
│   │   │   ├── feedback-template-general.md
│   │   │   ├── feedback-template-initial-review.md
│   │   │   └── feedback-template-peer-review.md
│   │   ├── analysis/              # Analysis templates
│   │   │   └── analysis-template.md
│   │   ├── outputs/               # Output templates
│   │   │   ├── output-template.md
│   │   │   ├── prompt6-checker-output-20260315.md
│   │   │   ├── prompt6-checker-output-20260315-002.md
│   │   │   ├── prompt6-checker-output-20260315-003.md
│   │   │   ├── prompt6-checker-output-20260315-004.md
│   │   │   ├── prompt6-checker-output-20260315-005.md
│   │   │   ├── prompt6-checker-output-20260315-006.md
│   │   │   └── prompt7-checker-output-20260315.md
│   │   ├── config/                # Configuration
│   │   │   ├── confidence-level-config.md
│   │   │   ├── review-feedback-config.md
│   │   │   └── exit-criteria-and-optimization.md
│   │   ├── CHECKER-HOW-TO.md      # How-to guide
│   │   ├── CHECKER-FLOWCHART.md   # Process flowchart
│   │   └── PRESERVATION-GUIDE.md  # Preservation guide
│   │
│   ├── templates/                 # Universal templates
│   │   └── prompts/               # Prompt templates
│   │       └── prompt1-universal-template.md
│   │
│   ├── validation/                # Validation tools
│   │   ├── prompt-update-validator.py
│   │   ├── prompt-update-validator.ps1
│   │   ├── PROMPT-UPDATE-VALIDATOR-GUIDE.md
│   │   ├── permission-management.md
│   │   └── prompt-validation-*.json
│   │
│   └── process/                   # Process documentation
│       ├── git-repository-framework.md
│       ├── EXECUTION-VERIFICATION-TABLE.md
│       ├── IMPLEMENTATION-SUMMARY.md
│       ├── audit-trail.md
│       ├── change-history.md
│       └── manual-fallback.md
│
├── scripts/                       # Root-level scripts
│   └── rule-extractor.py         # Rule extraction script
│
├── chat-prompt-en.md              # English prompt configuration (source of truth)
├── chat-prompt.md                 # Chinese prompt configuration (synchronized)
├── HOW-TO-EXECUTE-PROMPTS.md      # Prompt execution guide
├── PROMPT-WORKFLOW-FLOWCHART.md   # Complete workflow flowchart
├── behave.ini                     # Behave configuration
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

---

## LLM Checker System

The repository includes a comprehensive **LLM Checker System** for validating Marker LLM outputs (Prompt 6 and 7) against original business rules.

### Overview

The Checker System uses a second LLM (checker) to validate the outputs of the first LLM (marker), ensuring:
- Test cases align with business rules
- BDD scenarios are executable and traceable
- References are consistent and bidirectional
- Quality meets confidence thresholds

### Enhanced Features (Version 2.0.0)

The Checker System now includes:
- **Real-time Monitoring**: Track execution metrics, performance, and errors
- **Security Layer**: Access control, input validation, and audit logging
- **Parameterized Configuration**: Flexible configuration management
- **Alerting System**: Threshold-based alerts for critical events
- **Multi-model Support**: Support for multiple LLM validators

### Key Components

1. **Checker Prompts** (`governance/checker/prompts/`)
   - Dedicated prompts for validating Prompt 6 (test cases) and Prompt 7 (BDD)
   - Generic checker prompt generator for custom validation scenarios

2. **Templates** (`governance/checker/templates/`)
   - Input/output templates for structured validation
   - Feedback templates for human review (Initial/Peer/Final)
   - Difference analysis and exit report templates

3. **Configuration** (`governance/checker/config/`)
   - Confidence level assessment criteria
   - Review and feedback workflow configuration
   - Exit criteria and optimization strategies

4. **Documentation**
   - [CHECKER-HOW-TO.md](governance/checker/CHECKER-HOW-TO.md) - Complete usage guide
   - [CHECKER-FLOWCHART.md](governance/checker/CHECKER-FLOWCHART.md) - Process visualization
   - [PRESERVATION-GUIDE.md](governance/checker/PRESERVATION-GUIDE.md) - Output preservation guidelines

### Configuration Management

### Parameterized Configuration
All prompts and systems now support parameterized configuration through `config/prompt-config.json`:

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

## Best Practices and Troubleshooting

### Knowledge Base Management
- **Modularization**: Split large documents into smaller, focused modules
- **Consistent Naming**: Use consistent naming conventions for files and IDs
- **Version Control**: Implement proper Git version control for all knowledge base files
- **Regular Backups**: Schedule regular backups of the knowledge base
- **Access Control**: Implement appropriate access controls for sensitive information

### Skill Development
- **Reusability**: Design Skills to be reusable across different scenarios
- **Clear Documentation**: Document each Skill's purpose, inputs, and outputs
- **Performance Optimization**: Optimize Skill content for prompt response time
- **Testing**: Test Skills with different input variations
- **Versioning**: Maintain version history for Skills

### Test Automation
- **BDD Best Practices**: Follow Gherkin syntax best practices
- **Step Definition Reuse**: Reuse step definitions across scenarios
- **Parallel Execution**: Run tests in parallel to reduce execution time
- **Reporting**: Generate comprehensive test reports
- **CI/CD Integration**: Integrate tests into CI/CD pipelines

### Common Issues and Solutions

**Issue: Rule extraction fails**
- **Possible Causes**: Malformed Markdown, missing structured IDs, invalid rule format
- **Solution**: Validate Markdown syntax, ensure all paragraphs have structured IDs, check rule format against schema

**Issue: Skill generation errors**
- **Possible Causes**: Insufficient input information, conflicting references, invalid user type
- **Solution**: Provide complete input data, resolve reference conflicts, use valid user type

**Issue: BDD scenario execution failures**
- **Possible Causes**: Missing step definitions, incorrect Gherkin syntax, environment configuration issues
- **Solution**: Implement all required step definitions, validate Gherkin syntax, check environment setup

**Issue: Incremental update issues**
- **Possible Causes**: Change detection failures, conflicting updates, missing dependencies
- **Solution**: Verify change detection logic, resolve update conflicts, ensure all dependencies are present

**Issue: Performance issues**
- **Possible Causes**: Large knowledge base, complex Skills, inefficient scripts
- **Solution**: Optimize knowledge base structure, simplify Skill content, improve script efficiency

## Quick Start

1. **Prepare Input Files**
   - Marker output: `governance/analysis/outputs/PROMPT6-OUTPUT.md` or `PROMPT7-OUTPUT.md`
   - Original rules: Relevant MD files from `docs/source-files/`

2. **Execute Checker**
   - Use `governance/checker/prompts/checker-prompt.md`
   - Select appropriate prompt variant (Prompt 6 or 7)
   - Follow [CHECKER-HOW-TO.md](governance/checker/CHECKER-HOW-TO.md) for detailed steps

3. **Review Results**
   - Validation reports use `governance/checker/outputs/output-template.md`
   - Difference analysis uses `governance/checker/analysis/analysis-template.md`
   - Confidence level assessment follows `governance/checker/config/confidence-level-config.md`

---

## Prompt Set Overview

This repository implements a complete **15-prompt lifecycle management system**:

### Phase I: Knowledge Base Foundation (Prompts 1-2)
- **Prompt 1**: Structured MD Knowledge Base Generation with Paragraph IDs
- **Prompt 2**: Framework Structure Creation and Configuration

### Phase II: AI Capability & Test Asset Generation (Prompts 3-7)
- **Prompt 3**: Copilot Skill Modular Generation with References
- **Prompt 4**: BDD Template Preparation and Framework Setup
- **Prompt 5**: User Test Case Template Import and Learning
- **Prompt 6**: Structured Test Case Generation (Marker) ⭐
- **Prompt 7**: BDD Scenario Generation (Marker) ⭐

### Phase III: Knowledge Base Synchronization (Prompts 8-9)
- **Prompt 8**: New Document Addition - Incremental Update
- **Prompt 9**: Existing Document Update - Synchronization

### Phase IV: Verification & Validation (Prompts 10-11)
- **Prompt 10**: Multi-Model Collaborative Verification
- **Prompt 11**: Reference/Script Verification and Rollback

### Phase V: Optimization & Rectification (Prompts 12-13)
- **Prompt 12**: Knowledge Base Optimization Suggestions
- **Prompt 13**: Reference/Script Rectification

### Phase VI: Archiving & Completion (Prompts 14-15)
- **Prompt 14**: Version Archiving and Audit
- **Prompt 15**: Knowledge Base Completion and Handover

### Checker System (Validation Layer)
- **Checker Prompts**: Validate Prompt 6 and 7 outputs
- **Generic Generator**: Create custom checker prompts for any MD file

---

## Rule Version

| Attribute | Value |
|-----------|-------|
| **Document Name** | Initial Margin Calculation Guide HKv14 |
| **Version** | 1.4 |
| **Release Date** | October 2025 |
| **Source** | Hong Kong Securities Clearing Company Limited (HKSCC) |
| **Knowledge Base Version** | 1.0.6 |
| **Last Updated** | 2026-03-14 |

### Version History

| KB Version | Date | Changes | Updated By |
|------------|------|---------|------------|
| 1.0.0 | 2026-03-13 | Initial knowledge base framework creation | AI Assistant |
| 1.0.1 | 2026-03-13 | Migrated to 7-layer framework structure | AI Assistant |
| 1.0.2 | 2026-03-13 | Added process file storage rules, updated directory structure | AI Assistant |
| 1.0.3 | 2026-03-14 | Optimized Prompt 3-5 and 16 with unified standards and execution requirements | AI Assistant |
| 1.0.4 | 2026-03-14 | Renamed Prompt 16 to Prompt 5 and renumbered all subsequent prompts for consistent numbering | AI Assistant |
| 1.0.5 | 2026-03-14 | Fixed module naming and file locations, updated all affected documentation | AI Assistant |
| 1.0.6 | 2026-03-14 | Added LLM Checker System, updated README with complete documentation | AI Assistant |
| 2.0.0 | 2026-03-18 | Major enhancement: Added version control, parameterized configuration, monitoring, security, best practices, and troubleshooting guide | System Administrator |
| 2.1.0 | 2026-03-18 | Added multi-format support for PDF, Word, Excel, Email, and other document formats | System Administrator |
| 2.2.0 | 2026-03-18 | Made prompts document-agnostic with [BUSINESS_DOCUMENT_NAME] placeholder for generic template support | System Administrator |

---

## Manual Fallback Responsible Persons

### By Lifecycle Phase

| Phase | Primary Responsible | Audit Responsible | Escalation Contact |
|-------|---------------------|-------------------|-------------------|
| **Build** | BA Lead | QA Lead | Project Manager |
| **Update** | BA Lead | QA Lead | Project Manager |
| **Verify** | QA Lead | Automation Lead | QA Manager |
| **Optimize** | Automation Lead | QA Lead | Project Manager |
| **Archive** | QA Lead | BA Lead | Project Manager |

### By Module

| Module | BA Responsible | QA Responsible | Automation Responsible |
|--------|---------------|----------------|----------------------|
| Introduction-Overview | BA Lead | QA Lead | - |
| Risk-Parameter-File-Specification | BA Support | QA Lead | Automation Lead |
| Input-Data-Specification | BA Lead | QA Lead | Automation Lead |
| Market-Risk-Component-Calculation | BA Lead | QA Lead | Automation Lead |
| Margin-Adjustment-Process | BA Lead | QA Support | - |
| Other-Risk-Components | BA Support | QA Lead | Automation Support |
| Position-Processing-Logic | BA Support | QA Lead | Automation Lead |
| Collateral-Management | BA Support | QA Lead | Automation Lead |
| Corporate-Action-Processing | BA Support | QA Lead | Automation Lead |
| Calculation-Examples | BA Support | QA Lead | Automation Lead |

---

## Skill Reference / Script Usage Guidelines

### For Business Analysts (BA)

1. **Accessing Skills**
   - Navigate to `copilot-skills/skill-index.md` for skill inventory
   - Use skill trigger words in GitHub Copilot chat
   - Reference `copilot-skills/usage-guidelines.md` for detailed instructions

2. **Reference Management**
   - When rules update, verify `Rule_Source` in skills reflects new version
   - Report Reference inconsistencies to QA Lead
   - Review `copilot-skills/skill-bdd-relation.md` for relationship status

3. **Manual Fallback**
   - If Skill provides incorrect information, use `governance/process/manual-fallback.md`
   - Document issues in `governance/process/audit-trail.md`
   - Follow escalation path defined above

4. **Checker System Usage**
   - Review checker outputs for Prompt 6 and 7
   - Validate that test cases align with business rules
   - Approve or reject checker recommendations

### For QA Leads

1. **Skill Verification**
   - Run multi-model verification using `config/skill-verify-config.md`
   - Check Reference integrity in `copilot-skills/skill-bdd-relation.md`
   - Review verification results in `governance/`

2. **Relationship Management**
   - Maintain `copilot-skills/skill-bdd-relation.md` and `tests/bdd-relation-manager.md`
   - Ensure bidirectional consistency between Skills and BDD
   - Update relationship tables after any changes

3. **Audit Responsibilities**
   - Sign off on PRs affecting Skills or References
   - Review manual fallback decisions
   - Approve version tags

4. **Checker System Management**
   - Configure confidence level thresholds in `governance/checker/config/`
   - Review Initial/Peer/Final review feedback
   - Approve checker optimization suggestions

### For Automation Testers

1. **Script Execution**
   - Scripts are located in `copilot-skills/scripts/`
   - Run Reference sync scripts after rule updates
   - Check `governance/process/manual-fallback.md` on failure

2. **BDD Development**
   - Create feature files in `tests/bdd/features/`
   - Implement steps in `tests/bdd/steps/`
   - Update `tests/bdd-relation-manager.md` with new relationships

3. **Test Execution**
   - Use `behave.ini` configuration for test runs
   - Enable Reference verification switch when testing
   - Report discrepancies to QA Lead

4. **Checker System Integration**
   - Review checker validation reports for BDD scenarios
   - Implement suggested optimizations for failed checks
   - Ensure all BDD scenarios pass checker validation before submission

---

## Quick Start

### For New Team Members

1. **Read Core Documents**
   - `docs/Introduction-Overview.md` - Understand the domain
   - `docs/global-process/GLOBAL-PROCESS.md` - Learn the business process
   - `governance/process/git-repository-framework.md` - Understand the structure
   - `HOW-TO-EXECUTE-PROMPTS.md` - Learn prompt execution sequence

2. **Set Up Environment**
   - Clone this repository
   - Install Python dependencies for BDD: `pip install behave`
   - Configure GitHub Copilot with skills from `copilot-skills/`

3. **Explore Examples**
   - Review `docs/Calculation-Examples.md` for calculation samples
   - Check `docs/Input-Data-Specification.md` for core calculations
   - Examine `docs/Risk-Parameter-File-Specification.md` for data requirements
   - Review `tests/test-cases/TC-IM-CALC-001.md` for test case format

4. **Understand Quality Assurance**
   - Read `governance/checker/CHECKER-HOW-TO.md` for validation process
   - Review `PROMPT-WORKFLOW-FLOWCHART.md` for complete workflow
   - Check confidence level configuration

### For Rule Updates

1. **Update Documents**
   - Modify relevant files in `docs/`
   - Update version in `config/RULES-VERSION.md`
   - Log changes in `governance/process/change-history.md`

2. **Sync Skills**
   - Update affected skills in `copilot-skills/skill-definitions/`
   - Run Reference sync scripts
   - Update `copilot-skills/skill-bdd-relation.md`

3. **Update Tests**
   - Modify test cases in `tests/test-cases/`
   - Update BDD scenarios in `tests/bdd/`
   - Sync `tests/bdd-relation-manager.md`

4. **Verification**
   - Run multi-model verification
   - Execute Checker System for Prompt 6 and 7 outputs
   - Complete checklist from `governance/`
   - Obtain sign-offs

---

## Migration Notes

This project was migrated to a 7-layer framework structure on 2026-03-13. The migration involved:

1. **Created New Directories:**
   - `docs/` - Moved all rule documents here
   - `docs/source-files/` - Moved source PDF here
   - `copilot-skills/` - Created for AI capabilities
   - `copilot-skills/scripts/` - Created for automation scripts
   - `tests/` - Created for test assets
   - `tests/test-cases/` - Created for structured test cases
   - `tests/bdd/` - Created for BDD scenarios
   - `governance/` - Created for governance and quality assurance
   - `governance/checker/` - Created for LLM Checker System
   - `governance/analysis/` - Created for analysis documents
   - `governance/reviews/` - Created for review system
   - `governance/validation/` - Created for validation tools
   - `governance/process/` - Created for process documentation

2. **Moved Existing Files:**
   - Rule documents moved to `docs/`
   - Process flowchart moved to `docs/global-process/`
   - Source PDF moved to `docs/source-files/`
   - `GIT-REPOSITORY-FRAMEWORK.md` moved to `governance/process/`
   - `PROMPT1-Universal-Template.md` moved to `governance/templates/prompts/`

3. **Created New Files:**
   - `config/FRAMEWORK-CONFIG.md` - Framework configuration
   - `governance/process/manual-fallback.md` - Manual fallback procedures
   - `governance/process/audit-trail.md` - Audit trail
   - `governance/checker/CHECKER-HOW-TO.md` - Checker system guide
   - `governance/checker/CHECKER-FLOWCHART.md` - Checker process flowchart
   - `HOW-TO-EXECUTE-PROMPTS.md` - Complete prompt execution guide
   - `PROMPT-WORKFLOW-FLOWCHART.md` - Complete workflow visualization

### Process File Storage Rules Update (2026-03-13)

Established standardized storage rules for all prompt process files:

1. **Process File Locations:**
   - `PROMPT1-OUTPUT.md` → `docs/source-files/`
   - `PROMPT2-OUTPUT.md` → `config/`
   - `PROMPT3-OUTPUT.md` → `copilot-skills/`
   - `PROMPT4-OUTPUT.md` → `tests/`
   - `PROMPT5+ OUTPUT.md` → `governance/analysis/outputs/`

2. **Complete Document Files:**
   - `Initial Margin Calculation Guide HKv14.md` moved to `docs/source-files/`
   - Paired with original PDF for source traceability

3. **Framework Documentation:**
   - `governance/process/git-repository-framework.md` - Framework structure
   - `governance/templates/prompts/prompt1-universal-template.md` - Prompt 1 template

4. **Naming Convention:**
   - All process files follow `PROMPT{X}-{DESCRIPTION}.md` pattern
   - All filenames use UPPERCASE for PROMPT prefix

5. **Prompt Numbering Update:**
   - **Prompt 16** → **Prompt 5** (Skill Automation Script Generation)
   - **PROMPT16-OUTPUT.md** → **PROMPT5-OUTPUT.md`
   - **All subsequent Prompts** renumbered to maintain sequential order

For detailed migration information, see `config/PROMPT2-OUTPUT.md`.

---

## Key Contacts

| Role | Name | Responsibility |
|------|------|---------------|
| Knowledge Base Owner | TBD | Overall repository management |
| BA Lead | TBD | Business rule accuracy |
| QA Lead | TBD | Quality assurance and verification |
| Automation Lead | TBD | Test automation and scripts |
| Git Admin | TBD | Repository access and permissions |

---

## Contributing

1. **Before Making Changes**
   - Review `governance/process/git-repository-framework.md` for structure guidelines
   - Check `HOW-TO-EXECUTE-PROMPTS.md` for prompt execution sequence
   - Understand manual fallback procedures in `governance/process/manual-fallback.md`
   - Review checker system requirements in `governance/checker/CHECKER-HOW-TO.md`

2. **Making Changes**
   - Create feature branch: `git checkout -b feature/description`
   - Follow incremental update principles
   - Maintain Reference integrity
   - Run checker validation for Prompt 6 and 7 outputs

3. **Submitting Changes**
   - Complete relevant checklist from `governance/`
   - Run verification scripts
   - Execute checker system validation
   - Create PR with clear description
   - Obtain required approvals

---

## License & Confidentiality

This knowledge base contains proprietary business rules from HKSCC. Access is restricted to authorized personnel only. Do not distribute outside the organization.

---

## Support

For questions or issues:
1. Check relevant README files in each directory
2. Review `governance/process/git-repository-framework.md` for structure questions
3. Consult `governance/process/manual-fallback.md` for fallback procedures
4. Read `governance/checker/CHECKER-HOW-TO.md` for checker system questions
5. Review `HOW-TO-EXECUTE-PROMPTS.md` for prompt execution guidance
6. Escalate to responsible person per table above

---

**Last Updated**: 2026-03-18  
**Knowledge Base Version**: 2.2.0  
**Status**: Active Development
