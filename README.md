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
| **Knowledge Base Version** | 1.0.4 |
| **Last Updated** | 2026-03-14 |

### Version History

| KB Version | Date | Changes | Updated By |
|------------|------|---------|------------|
| 1.0.0 | 2025-03-13 | Initial knowledge base framework creation | AI Assistant |
| 1.0.1 | 2025-03-14 | Added LLM Checker System | AI Assistant |
| 1.0.2 | 2025-03-14 | Optimized governance directory structure | AI Assistant |
| 1.0.3 | 2025-03-14 | Added structured test cases | AI Assistant |
| 1.0.4 | 2025-03-14 | Updated README with checker system documentation | AI Assistant |

---

## Quick Links

### Documentation
- [Framework Configuration](config/FRAMEWORK-CONFIG.md)
- [Rule Version](config/RULES-VERSION.md)
- [Git Repository Framework](governance/process/git-repository-framework.md)

### AI Capabilities
- [Skill Index](copilot-skills/skill-index.md)
- [Skill Usage Guidelines](copilot-skills/usage-guidelines.md)
- [Skill-BDD Relation](copilot-skills/skill-bdd-relation.md)

### Test Assets
- [Test Case Index](tests/test-cases/index.md)
- [BDD Relation Manager](tests/bdd-relation-manager.md)
- [Test Usage Guidelines](tests/usage-guidelines.md)

### Quality Assurance
- [Checker How-To Guide](governance/checker/CHECKER-HOW-TO.md)
- [Checker Flowchart](governance/checker/CHECKER-FLOWCHART.md)
- [Governance Overview](governance/README.md)

### Prompts
- [English Prompts](chat-prompt-en.md) (Source of Truth)
- [Prompt 1 Universal Template](governance/templates/prompts/prompt1-universal-template.md)
- [Checker Prompts](governance/checker/prompts/)

---

## Getting Started

1. **Understand the Framework**: Read [GIT-REPOSITORY-FRAMEWORK.md](governance/process/git-repository-framework.md)
2. **Review Business Rules**: Explore `docs/` directory
3. **Understand AI Capabilities**: Review `copilot-skills/` directory
4. **Check Test Assets**: Review `tests/` directory
5. **Learn Quality Assurance**: Study `governance/checker/` documentation
6. **Execute Prompts**: Follow the sequence in [chat-prompt-en.md](chat-prompt-en.md)

---

## Contributing

When contributing to this repository:

1. Follow the [Naming Conventions](config/NAMING-CONVENTIONS.md) (to be created)
2. Maintain [Reference Integrity](config/skill-reference-spec.md)
3. Use the [LLM Checker System](governance/checker/CHECKER-HOW-TO.md) for validation
4. Update relevant documentation
5. Follow the [Governance Procedures](governance/README.md)

---

## License

This knowledge base is for internal use only. All business rules are derived from the Initial Margin Calculation Guide HKv14 published by HKSCC.
