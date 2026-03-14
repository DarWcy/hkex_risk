# Initial Margin Calculation Knowledge Base

## Repository Overview

This Git repository serves as a **traceable, verifiable, updatable, and scalable** test business knowledge common baseline for the Initial Margin Calculation Guide HKv14. It supports full lifecycle management of business rules, AI-assisted capabilities (GitHub Copilot Skills), test assets (BDD scenarios), and comprehensive quality assurance through the LLM Checker System.

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
│   └── source-files/              # Original source documents
│       ├── Initial Margin Calculation Guide HKv14.pdf  # Source PDF (original)
│       ├── Initial Margin Calculation Guide HKv14.md   # Source MD (converted)
│       └── PROMPT1-OUTPUT.md      # Prompt 1 process output
│
├── copilot-skills/                # AI Capability Layer - Copilot Skills
│   ├── scripts/                   # Automation scripts
│   │   ├── skill-reference-sync.py
│   │   ├── multi-model-verify.py
│   │   ├── bdd-relationship-update.py
│   │   └── ...
│   ├── skill-definitions/         # Individual skill files
│   │   ├── hkex-intro-overview.md
│   │   ├── hkex-risk-parameters.md
│   │   └── ...
│   ├── skill-index.md             # Skill index table
│   ├── skill-bdd-relation.md      # Skill-BDD relationship management
│   ├── usage-guidelines.md        # Skill usage guide
│   ├── PROMPT3-INPUT.md           # Prompt 3 input
│   └── PROMPT3-OUTPUT.md          # Prompt 3 process output
│
├── tests/                         # Test Asset Layer - Test Cases & BDD
│   ├── test-cases/                # Structured test cases
│   │   ├── README.md              # Test case guidelines
│   │   ├── index.md               # Test case index
│   │   ├── TC-IM-CALC-001.md      # Test case examples
│   │   └── ...
│   ├── bdd/                       # BDD scenarios
│   │   ├── features/              # Feature files (.feature)
│   │   ├── steps/                 # Python step definitions
│   │   ├── templates/             # BDD templates
│   │   ├── learned/               # Learned template configurations
│   │   └── diff-reports/          # Difference analysis reports
│   ├── bdd-relation-manager.md    # BDD relationship management
│   ├── skill-bdd-relation.md      # Skill-BDD relationship
│   ├── usage-guidelines.md        # Test usage guidelines
│   ├── PROMPT4-INPUT.md           # Prompt 4 input
│   └── PROMPT4-OUTPUT.md          # Prompt 4 process output
│
├── config/                        # Configuration Layer
│   ├── FRAMEWORK-CONFIG.md        # Framework configuration
│   ├── RULES-VERSION.md           # Rule version overview
│   ├── PROMPT2-OUTPUT.md          # Prompt 2 process output
│   ├── skill-reference-spec.md    # Reference specifications
│   └── skill-verify-config.md     # Skill verification config
│
├── governance/                    # Governance Layer - Quality Assurance & Process
│   ├── README.md                  # Governance overview
│   ├── DIRECTORY-STRUCTURE-PROPOSAL.md  # Directory structure proposal
│   │
│   ├── analysis/                  # Analysis and research documents
│   │   ├── prompts/               # Prompt logic analysis
│   │   ├── outputs/               # Prompt input/output analysis
│   │   └── templates/             # Template analysis
│   │
│   ├── reviews/                   # Review system
│   │   ├── templates/             # Review templates by type
│   │   │   ├── skills/            # Skill review templates
│   │   │   ├── test/              # Test-related templates
│   │   │   ├── code/              # Code review templates
│   │   │   ├── docs/              # Documentation templates
│   │   │   ├── framework/         # Framework templates
│   │   │   └── governance/        # Governance templates
│   │   ├── feedback/              # Feedback templates
│   │   └── executions/            # Review executions by prompt
│   │
│   ├── checker/                   # LLM Checker System ⭐
│   │   ├── prompts/               # Checker prompts
│   │   │   ├── checker-prompt.md              # Main checker prompt
│   │   │   ├── generic-checker-prompt-generator.md
│   │   │   └── generic-checker-prompt-generator-usage.md
│   │   ├── templates/             # Checker templates
│   │   │   ├── checker-input-template.md
│   │   │   ├── checker-output-template.md
│   │   │   ├── diff-analysis-template.md
│   │   │   ├── exit-report-template.md
│   │   │   └── feedback-template-*.md
│   │   ├── analysis/              # Analysis templates
│   │   ├── outputs/               # Output templates
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
├── chat-prompt-en.md              # English prompt configuration (source of truth)
├── chat-prompt.md                 # Chinese prompt configuration (synchronized)
├── behave.ini                     # Behave configuration
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

### Quick Start

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

**Last Updated**: 2026-03-14  
**Knowledge Base Version**: 1.0.6  
**Status**: Active Development
