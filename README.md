# Initial Margin Calculation Knowledge Base

## Repository Overview

This Git repository serves as a **traceable, verifiable, updatable, and scalable** test business knowledge common baseline for the Initial Margin Calculation Guide HKv14. It supports full lifecycle management of business rules, AI-assisted capabilities (GitHub Copilot Skills), and test assets (BDD scenarios).

### Core Objectives

1. **Traceable**: Every rule, skill, and test case links to source documents via structured References
2. **Verifiable**: Multi-model collaborative verification ensures quality and consistency
3. **Updatable**: Incremental updates with synchronized relationship management
4. **Scalable**: Modular architecture supports knowledge base expansion

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
│   ├── script/                    # Automation scripts
│   ├── skill-definitions/         # Individual skill files
│   ├── index.md                   # Skill index table
│   ├── skill-bdd-relation.md      # Skill-BDD relationship management
│   ├── usage-guidelines.md        # Skill usage guide
│   └── PROMPT3-OUTPUT.md          # Prompt 3 process output
│
├── tests/                         # Test Asset Layer - Test Cases & BDD
│   ├── test-cases/                # Structured test cases (to be created)
│   ├── bdd/                       # BDD scenarios (to be created)
│   │   ├── features/              # Feature files
│   │   └── steps/                 # Python step definitions
│   └── bdd-relation-manager.md    # BDD relationship management (to be created)
│
├── config/                        # Configuration Layer
│   ├── FRAMEWORK-CONFIG.md        # Framework configuration
│   ├── RULES-VERSION.md           # Rule version overview
│   ├── PROMPT2-OUTPUT.md          # Prompt 2 process output
│   ├── UPDATE-LOG.md              # Update history (to be created)
│   ├── NAMING-CONVENTIONS.md      # Naming conventions (to be created)
│   ├── skill-reference-spec.md    # Reference specifications (to be created)
│   ├── skill-verify-config.md     # Skill verification config (to be created)
│   └── multi-model-verify-config.yaml  # Multi-model verification config (to be created)
│
├── governance/                    # Governance Layer - Manual Fallback
│   ├── manual-fallback.md         # Manual fallback procedures
│   ├── audit-trail.md             # Audit trail and change log
│   ├── permission-management.md   # Access control and permissions
│   └── common/                    # Common governance documents (to be created)
│
├── GIT-REPOSITORY-FRAMEWORK.md    # Framework structure documentation
├── PROMPT1-Universal-Template.md  # Prompt 1 universal template
├── chat-prompt-en.md              # English prompt configuration (source of truth)
├── chat-prompt.md                 # Chinese prompt configuration (synchronized)
└── README.md                      # This file
```

---

## Rule Version

| Attribute | Value |
|-----------|-------|
| **Document Name** | Initial Margin Calculation Guide HKv14 |
| **Version** | 1.4 |
| **Release Date** | October 2025 |
| **Source** | Hong Kong Securities Clearing Company Limited (HKSCC) |
| **Knowledge Base Version** | 1.0.3 |
| **Last Updated** | 2026-03-14 |

### Version History

| KB Version | Date | Changes | Updated By |
|------------|------|---------|------------|
| 1.0.0 | 2025-03-13 | Initial knowledge base framework creation | AI Assistant |
| 1.0.1 | 2025-03-13 | Migrated to 7-layer framework structure | AI Assistant |
| 1.0.2 | 2025-03-13 | Added process file storage rules, updated directory structure | AI Assistant |
| 1.0.3 | 2026-03-14 | Optimized Prompt 3-5 and 16 with unified standards and execution requirements | AI Assistant |
| 1.0.4 | 2026-03-14 | Renamed Prompt 16 to Prompt 5 and renumbered all subsequent prompts for consistent numbering | AI Assistant |
| 1.0.5 | 2026-03-14 | Fixed module naming and file locations, updated all affected documentation | AI Assistant |

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
   - Navigate to `copilot-skills/index.md` for skill inventory (when created)
   - Use skill trigger words in GitHub Copilot chat
   - Reference `usage-guidelines.md` for detailed instructions (when created)

2. **Reference Management**
   - When rules update, verify `Rule_Source` in skills reflects new version
   - Report Reference inconsistencies to QA Lead
   - Review `skill-bdd-relation.md` for relationship status (when created)

3. **Manual Fallback**
   - If Skill provides incorrect information, use `governance/manual-fallback.md`
   - Document issues in `governance/audit-trail.md`
   - Follow escalation path defined above

### For QA Leads

1. **Skill Verification**
   - Run multi-model verification using `config/multi-model-verify-config.yaml` (when created)
   - Check Reference integrity in `skill-bdd-relation.md` (when created)
   - Review verification results in `governance/`

2. **Relationship Management**
   - Maintain `skill-bdd-relation.md` and `tests/bdd-relation-manager.md` (when created)
   - Ensure bidirectional consistency between Skills and BDD
   - Update relationship tables after any changes

3. **Audit Responsibilities**
   - Sign off on PRs affecting Skills or References
   - Review manual fallback decisions
   - Approve version tags

### For Automation Testers

1. **Script Execution**
   - Scripts will be located in `copilot-skills/script/`
   - Run Reference sync scripts after rule updates
   - Check `governance/manual-fallback.md` on failure

2. **BDD Development**
   - Create feature files in `tests/bdd/features/` (when created)
   - Implement steps in `tests/bdd/steps/` (when created)
   - Update `tests/bdd-relation-manager.md` with new relationships (when created)

3. **Test Execution**
   - Use `behave.ini` configuration for test runs (when created)
   - Enable Reference verification switch when testing
   - Report discrepancies to QA Lead

---

## Quick Start

### For New Team Members

1. **Read Core Documents**
   - `docs/Introduction-Overview.md` - Understand the domain
   - `docs/global-process/GLOBAL-PROCESS.md` - Learn the business process
   - `GIT-REPOSITORY-FRAMEWORK.md` - Understand the structure

2. **Set Up Environment**
   - Clone this repository
   - Install Python dependencies for BDD: `pip install behave`
   - Configure GitHub Copilot with skills from `copilot-skills/` (when created)

3. **Explore Examples**
   - Review `docs/Calculation-Examples.md` for calculation samples
   - Check `docs/Input-Data-Specification.md` for core calculations
   - Examine `docs/Risk-Parameter-File-Specification.md` for data requirements

### For Rule Updates

1. **Update Documents**
   - Modify relevant files in `docs/`
   - Update version in `config/RULES-VERSION.md`
   - Log changes in `config/UPDATE-LOG.md` (when created)

2. **Sync Skills**
   - Update affected skills in `copilot-skills/skill-definitions/` (when created)
   - Run Reference sync scripts
   - Update `skill-bdd-relation.md` (when created)

3. **Update Tests**
   - Modify test cases in `tests/test-cases/` (when created)
   - Update BDD scenarios in `tests/bdd/` (when created)
   - Sync `tests/bdd-relation-manager.md` (when created)

4. **Verification**
   - Run multi-model verification
   - Complete checklist from `governance/`
   - Obtain sign-offs

---

## Migration Notes

This project was migrated to a 7-layer framework structure on 2025-03-13. The migration involved:

1. **Created New Directories:**
   - `docs/` - Moved all rule documents here
   - `docs/source-files/` - Moved source PDF here
   - `copilot-skills/` - Created for AI capabilities
   - `copilot-skills/script/` - Created for automation scripts
   - `tests/` - Created for test assets
   - `governance/` - Created for manual fallback mechanisms

2. **Moved Existing Files:**
   - Rule documents moved to `docs/`
   - Process flowchart moved to `docs/global-process/`
   - Source PDF moved to `docs/source-files/`

3. **Created New Files:**
   - `config/FRAMEWORK-CONFIG.md` - Framework configuration
   - `governance/manual-fallback.md` - Manual fallback procedures
   - `governance/audit-trail.md` - Audit trail
   - `governance/permission-management.md` - Access control

### Process File Storage Rules Update (2025-03-13)

Established standardized storage rules for all prompt process files:

1. **Process File Locations:**
   - `PROMPT1-OUTPUT.md` → `docs/source-files/`
   - `PROMPT2-OUTPUT.md` → `config/`
   - `PROMPT3-OUTPUT.md` → `copilot-skills/`
   - `PROMPT4-OUTPUT.md` → `tests/`
   - `PROMPT5+ OUTPUT.md` → `governance/`

2. **Complete Document Files:**
   - `Initial Margin Calculation Guide HKv14.md` moved to `docs/source-files/`
   - Paired with original PDF for source traceability

3. **Framework Documentation:**
   - `GIT-REPOSITORY-FRAMEWORK.md` remains in root directory
   - `PROMPT1-Universal-Template.md` remains in root directory

4. **Naming Convention:**
   - All process files follow `PROMPT{X}-{DESCRIPTION}.md` pattern
   - All filenames use UPPERCASE for PROMPT prefix
5. **Prompt Numbering Update:**
   - **Prompt 16** → **Prompt 5** (Skill Automation Script Generation)
   - **PROMPT16-OUTPUT.md** → **PROMPT5-OUTPUT.md**
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
   - Review `config/NAMING-CONVENTIONS.md` (when created)
   - Check `GIT-REPOSITORY-FRAMEWORK.md` for structure guidelines
   - Understand manual fallback procedures in `governance/`

2. **Making Changes**
   - Create feature branch: `git checkout -b feature/description`
   - Follow incremental update principles
   - Maintain Reference integrity

3. **Submitting Changes**
   - Complete relevant checklist from `governance/`
   - Run verification scripts
   - Create PR with clear description
   - Obtain required approvals

---

## License & Confidentiality

This knowledge base contains proprietary business rules from HKSCC. Access is restricted to authorized personnel only. Do not distribute outside the organization.

---

## Support

For questions or issues:
1. Check relevant README files in each directory
2. Review `GIT-REPOSITORY-FRAMEWORK.md` for structure questions
3. Consult `governance/manual-fallback.md` for fallback procedures
4. Escalate to responsible person per table above

---

**Last Updated**: 2026-03-14  
**Knowledge Base Version**: 1.0.5  
**Status**: Active Development
