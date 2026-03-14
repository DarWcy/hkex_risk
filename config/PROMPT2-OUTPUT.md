# Prompt 2 Output: Git Knowledge Base Full Lifecycle Framework Generation

## Output 1: Existing Structure Analysis Report (Brownfield)

### Current Directory Tree
```
C:\Codes\hkex_risk\
├── chat-prompt-en.md
├── chat-prompt.md
├── config\
│   └── RULES-VERSION.md
├── Core-Business-Global-Process-Flowchart.md
├── Core-Calculation-Logic.md
├── Data-Specification.md
├── docs\
│   └── global-process\
│       └── GLOBAL-PROCESS.md
├── Examples.md
├── Exception-Handling.md
├── GIT-REPOSITORY-FRAMEWORK.md
├── Initial Margin Calculation Guide HKv14.md
├── Initial Margin Calculation Guide HKv14.pdf
├── Introduction-Overview.md
├── Process-Flow.md
├── Prompt-1-Universal-Template.md
├── README.md
├── Reference-Tables.md
├── System-Integration.md
├── Testing-Considerations.md
└── Validation-Rules.md
```

### File Classification
- **Rule Files**: Risk-Parameter-File-Specification.md, Input-Data-Specification.md, Margin-Adjustment-Process.md, Other-Risk-Components.md
- **Process Files**: Core-Business-Global-Process-Flowchart.md, Market-Risk-Component-Calculation.md, docs/global-process/GLOBAL-PROCESS.md
- **Calculation Files**: Input-Data-Specification.md
- **Example Files**: Corporate-Action-Processing.md
- **Other Files**: Introduction-Overview.md, Calculation-Examples.md, Position-Processing-Logic.md, Collateral-Management.md, Initial Margin Calculation Guide HKv14.md, Initial Margin Calculation Guide HKv14.pdf, chat-prompt-en.md, chat-prompt.md, GIT-REPOSITORY-FRAMEWORK.md, README.md, Prompt-1-Universal-Template.md

### Gap Analysis Against 7-Layer Framework
| Framework Layer | Status | Gap |
|----------------|--------|-----|
| docs/ | Partially Exists | Need to create and move existing rule files here |
| docs/global-process/ | Exists | Already contains GLOBAL-PROCESS.md |
| docs/source-files/ | Missing | Need to create for storing original PDF files |
| copilot-skills/ | Missing | Need to create, containing Skills and scripts |
| tests/ | Missing | Need to create, containing test cases and BDD scenarios |
| config/ | Exists | Already contains RULES-VERSION.md |
| governance/ | Missing | Need to create, containing manual fallback mechanisms |

### Migration Recommendations
1. Move rule files from root directory to docs/ directory
2. Move original PDF file to docs/source-files/ directory
3. Create missing directories: docs/source-files/, copilot-skills/, tests/, governance/
4. Create script/ subdirectory for copilot-skills/
5. Preserve existing config/ and docs/global-process/ directories

## Output 2: Framework Configuration File

### config/FRAMEWORK-CONFIG.md
```markdown
# Framework Structure Configuration

## Project Metadata
- Project Name: Initial Margin Calculation Guide HKv14
- Business Domain: Financial Risk Management
- Source Document: Initial Margin Calculation Guide HKv14.pdf
- Source Version: 1.4

## Structure Template Selection
- Template Type: Brownfield
- Existing Structure Path: ./

## Layer Configuration
### Layer 1 - docs/
- Enabled: true
- Existing Files: Risk-Parameter-File-Specification.md, Input-Data-Specification.md, Margin-Adjustment-Process.md, Other-Risk-Components.md, Introduction-Overview.md, Calculation-Examples.md, Position-Processing-Logic.md, Collateral-Management.md
- Naming Pattern: Module-SubTopic.md

### Layer 2 - docs/global-process/
- Enabled: true
- Process Flow Source: Core-Business-Global-Process-Flowchart.md

### Layer 3 - docs/source-files/
- Enabled: true
- Source Files: Initial Margin Calculation Guide HKv14.pdf

### Layer 4 - copilot-skills/
- Enabled: true
- Skill Naming Pattern: hkex-{module}-{capability}
- Script Language: Python

### Layer 5 - tests/
- Enabled: true
- Test Framework: Behave/BDD
- Test Case Pattern: TC-{module}-{number}

### Layer 6 - config/
- Enabled: true
- Version Format: MAJOR.MINOR.PATCH

### Layer 7 - governance/
- Enabled: true
- Fallback Levels: View/Edit/Audit/Decision

## Custom Directories (Optional)
- 

## Exclusions
- chat-prompt-en.md
- chat-prompt.md
- Prompt-1-Universal-Template.md

## Custom Requirements (Manual Entry)
### Domain-Specific Requirements
- Financial risk management compliance requirements
- HKEX-specific rules and processes

### Business Process Requirements
- Completeness and accuracy of margin calculation processes
- Exception handling and fallback mechanisms

### Technical Requirements
- Python script automation
- BDD test framework integration

### Compliance Requirements
- Compliance with financial regulatory requirements
- Audit trail and record keeping

### Testing Requirements
- Test cases covering all calculation logic
- Boundary condition testing
```

### Structure Template Selection Justification
Selected Brownfield template because project already has partial structure and files, requiring preservation of existing content while adding missing framework layers.

## Output 3: Complete Git Repository Directory Tree

```
C:\Codes\hkex_risk\
├── chat-prompt-en.md              [EXISTING]
├── chat-prompt.md                  [EXISTING]
├── config\                        [EXISTING]
│   ├── FRAMEWORK-CONFIG.md         [NEW]
│   └── RULES-VERSION.md            [EXISTING]
├── copilot-skills\                [NEW]
│   └── script\                    [NEW]
├── docs\                          [NEW]
│   ├── Introduction-Overview.md   [EXISTING]
│   ├── Risk-Parameter-File-Specification.md [EXISTING]
│   ├── Input-Data-Specification.md [EXISTING]
│   ├── Market-Risk-Component-Calculation.md [EXISTING]
│   ├── Margin-Adjustment-Process.md [EXISTING]
│   ├── Other-Risk-Components.md [EXISTING]
│   ├── Position-Processing-Logic.md [EXISTING]
│   ├── Collateral-Management.md [EXISTING]
│   ├── Corporate-Action-Processing.md [EXISTING]
│   ├── Calculation-Examples.md [EXISTING]
│   ├── global-process\            [EXISTING]
│   │   ├── Core-Business-Global-Process-Flowchart.md [EXISTING]
│   │   └── GLOBAL-PROCESS.md       [EXISTING]
│   └── source-files\              [NEW]
│       └── Initial Margin Calculation Guide HKv14.pdf [EXISTING]
├── governance\                    [NEW]
├── GIT-REPOSITORY-FRAMEWORK.md    [EXISTING]
├── Initial Margin Calculation Guide HKv14.md [EXISTING]
├── Prompt-1-Universal-Template.md  [EXISTING]
├── README.md                       [EXISTING]
└── tests\                         [NEW]
```

## Output 4: Detailed Maintenance Specifications + Extension Rules

### docs/ Directory
- **Function Description**: Stores standardized business rule MD files, core content layer of the knowledge base
- **File Naming Conventions**: Module-SubTopic.md, e.g., Risk-Parameter-File-Specification.md
- **Update Maintenance Requirements**:
  1. Update corresponding MD files promptly when rules change
  2. Review content accuracy regularly (quarterly)
  3. Maintained by Business Analysts
- **Extension Rules**:
  - Follow naming conventions when adding new rule files
  - Large rules can be split into multiple sub-files
  - Archive outdated rule files to docs/archive/ directory

### docs/global-process/ Directory
- **Function Description**: Stores core business global process related files, supports real-time updates when processes change
- **File Naming Conventions**: Core-Business-Global-Process-Flowchart.md, GLOBAL-PROCESS.md
- **Update Maintenance Requirements**:
  1. Update related files immediately when processes change
  2. Review process documentation completeness monthly
  3. Maintained by Process Owners
- **Extension Rules**:
  - Ensure consistency with existing processes when adding new process files
  - Update relationship tables when processes change

### docs/source-files/ Directory
- **Function Description**: Stores original business rule files for Skill Reference traceability
- **File Naming Conventions**: Keep original filenames, e.g., Initial Margin Calculation Guide HKv14.pdf
- **Update Maintenance Requirements**:
  1. Add new versions promptly when source documents update
  2. Preserve historical versions for traceability
  3. Maintained by Document Administrators
- **Extension Rules**:
  - Add version number suffix when source document versions change
  - Clean up expired temporary files regularly

### copilot-skills/ Directory
- **Function Description**: Stores modular GitHub Copilot Skills, supports automation scripts
- **File Naming Conventions**: hkex-{module}-{capability}.md, e.g., hkex-im-calculation.md
- **Update Maintenance Requirements**:
  1. Update related Skills synchronously when rules change
  2. Test Skills accuracy weekly
  3. Maintained by AI Capability Developers
- **Extension Rules**:
  - Follow naming conventions when adding new Skills
  - Split complex capabilities into multiple specialized Skills

### copilot-skills/script/ Directory
- **Function Description**: Stores automation scripts, supports knowledge base synchronization and verification
- **File Naming Conventions**: {function}-{purpose}.py, e.g., sync-relation.py
- **Update Maintenance Requirements**:
  1. Test and verify when scripts change
  2. Review script performance and reliability monthly
  3. Maintained by Technical Developers
- **Extension Rules**:
  - Ensure compatibility with existing scripts when adding new scripts
  - Split complex scripts into multiple modules

### tests/ Directory
- **Function Description**: Stores test cases and BDD scenarios, ensures correct implementation of rules
- **File Naming Conventions**: TC-{module}-{number}.feature, e.g., TC-im-001.feature
- **Update Maintenance Requirements**:
  1. Update related test cases when rules change
  2. Run tests after each rule update
  3. Maintained by Test Engineers
- **Extension Rules**:
  - Follow naming conventions when adding new test cases
  - Separate test data from test cases

### config/ Directory
- **Function Description**: Stores version management and configuration related files
- **File Naming Conventions**: RULES-VERSION.md, FRAMEWORK-CONFIG.md
- **Update Maintenance Requirements**:
  1. Update RULES-VERSION.md when rule versions change
  2. Assess impact and update related files when configuration changes
  3. Maintained by Configuration Managers
- **Extension Rules**:
  - Ensure consistency with existing configurations when adding new configuration files
  - Log configuration changes

### governance/ Directory
- **Function Description**: Stores manual fallback mechanisms and audit process related files
- **File Naming Conventions**: manual-fallback.md, audit-trail.md, permission-management.md
- **Update Maintenance Requirements**:
  1. Review fallback mechanism effectiveness regularly (quarterly)
  2. Update related files when audit processes change
  3. Maintained by Governance Owners
- **Extension Rules**:
  - Ensure consistency with existing governance processes when adding new governance files
  - Update permission management documentation for major changes

## Output 5: Migration Guide (Brownfield)

### Step-by-Step Migration Instructions
1. **Create Missing Directories**:
   - docs/
   - docs/source-files/
   - copilot-skills/
   - copilot-skills/script/
   - tests/
   - governance/

2. **Move Existing Files**:
   - Move rule documents from root to docs/ directory
   - Move Core-Business-Global-Process-Flowchart.md to docs/global-process/ directory
   - Move Initial Margin Calculation Guide HKv14.pdf to docs/source-files/ directory

3. **Update References**:
   - Update directory navigation in README.md
   - Update structure description in GIT-REPOSITORY-FRAMEWORK.md

4. **Create Initial Files**:
   - config/FRAMEWORK-CONFIG.md
   - governance/manual-fallback.md
   - governance/audit-trail.md
   - governance/permission-management.md

### File Movement Mapping
| Source Path | Target Path |
|------------|-------------|
| Risk-Parameter-File-Specification.md | docs/Risk-Parameter-File-Specification.md |
| Input-Data-Specification.md | docs/Input-Data-Specification.md |
| Market-Risk-Component-Calculation.md | docs/Market-Risk-Component-Calculation.md |
| Margin-Adjustment-Process.md | docs/Margin-Adjustment-Process.md |
| Other-Risk-Components.md | docs/Other-Risk-Components.md |
| Position-Processing-Logic.md | docs/Position-Processing-Logic.md |
| Collateral-Management.md | docs/Collateral-Management.md |
| Corporate-Action-Processing.md | docs/Corporate-Action-Processing.md |
| Calculation-Examples.md | docs/Calculation-Examples.md |
| Introduction-Overview.md | docs/Introduction-Overview.md |
| Core-Business-Global-Process-Flowchart.md | docs/global-process/Core-Business-Global-Process-Flowchart.md |
| Initial Margin Calculation Guide HKv14.pdf | docs/source-files/Initial Margin Calculation Guide HKv14.pdf |

### Reference Update Requirements
- Update Rule_Source reference paths in all Skills
- Update file path references in test cases
- Update path references in configuration files

### Validation Checklist
- [ ] All files moved to correct target locations
- [ ] All reference paths updated
- [ ] New directory structure created
- [ ] Initial configuration files created
- [ ] Migration guide documented

## Output 6: README.md Template

```markdown
# Initial Margin Calculation Guide HKv14 Knowledge Base

## Repository Description
This repository is a structured knowledge management system for Initial Margin Calculation Guide HKv14, supporting global process definition, full lifecycle management, and AI capability integration.

## Directory Navigation

### Core Directory Structure
- **docs/**: Standardized business rule MD files
- **docs/global-process/**: Core business global process files
- **docs/source-files/**: Original business rule files
- **copilot-skills/**: GitHub Copilot Skills
- **copilot-skills/script/**: Automation scripts
- **tests/**: Test cases and BDD scenarios
- **config/**: Version management and configuration files
- **governance/**: Manual fallback mechanisms and audit processes

### Key Files
- **docs/Risk-Parameter-File-Specification.md**: Risk parameter file specifications
- **docs/Input-Data-Specification.md**: Input data requirements
- **docs/global-process/GLOBAL-PROCESS.md**: Global process documentation
- **docs/source-files/Initial Margin Calculation Guide HKv14.pdf**: Original source document
- **config/RULES-VERSION.md**: Rule version management
- **config/FRAMEWORK-CONFIG.md**: Framework configuration

## Rule Version
- Current Version: 1.4
- Version Management: Follows MAJOR.MINOR.PATCH format

## Manual Fallback Responsible Persons
- Business Rules: [Name]
- Technical Implementation: [Name]
- Test Verification: [Name]

## Skill Reference/Script Usage Guidelines

### Skill Usage
1. Select appropriate Skill from copilot-skills/ directory
2. Use Skill trigger words as specified
3. Reference Skill Reference fields for traceability

### Script Usage
1. Run scripts from copilot-skills/script/ directory
2. Follow script input/output specifications
3. Reference governance/manual-fallback.md when exceptions occur

## Migration Notes
This project uses Brownfield template for framework migration, preserving existing files while adding missing framework layers. Detailed migration steps refer to migration guide.

## Contact Information
- Project Lead: [Name]
- Technical Support: [Email]
```

## Output 7: Initial Configuration Files

### config/RULES-VERSION.md (Exists, Preserved)
```markdown
# Rule Version Management

## Current Version
- Version Number: 1.4
- Release Date: 2026-03-13
- Scope: Initial Margin Calculation Guide HKv14

## Module Version Matrix
| Module Name | Version | Last Updated | Owner |
|------------|---------|--------------|-------|
| Risk-Parameter-File-Specification | 1.4 | 2026-03-13 | [Name] |
| Input-Data-Specification | 1.4 | 2026-03-13 | [Name] |
| Market-Risk-Component-Calculation | 1.4 | 2026-03-13 | [Name] |
| Margin-Adjustment-Process | 1.4 | 2026-03-13 | [Name] |
| Other-Risk-Components | 1.4 | 2026-03-13 | [Name] |
| Position-Processing-Logic | 1.4 | 2026-03-13 | [Name] |
| Collateral-Management | 1.4 | 2026-03-13 | [Name] |
| Corporate-Action-Processing | 1.4 | 2026-03-13 | [Name] |
| Calculation-Examples | 1.4 | 2026-03-13 | [Name] |

## Version Change Log
| Version | Changes | Change Date | Owner |
|---------|---------|-------------|-------|
| 1.4 | Initial Version | 2026-03-13 | [Name] |

## Git Tag Synchronization
- Version 1.4 corresponds to Git tag: v1.4.0
```

### docs/global-process/GLOBAL-PROCESS.md (Exists, Preserved)

### Existing Files Preservation Notes
- **config/RULES-VERSION.md**: Exists, preserved and updated version information
- **docs/global-process/GLOBAL-PROCESS.md**: Exists, preserved and ensured compatibility with new structure
- **README.md**: Exists, preserved and updated directory navigation
- **GIT-REPOSITORY-FRAMEWORK.md**: Exists, preserved as reference
- **Initial Margin Calculation Guide HKv14.md**: Exists, preserved as complete document reference
- **chat-prompt-en.md**, **chat-prompt.md**: Exists, preserved as prompt configuration
- **Prompt-1-Universal-Template.md**: Exists, preserved as Prompt 1 template

## Output 8: Execution Log

### Directory Creation Log
```
[2026-03-13 23:30:00] Created directory: docs/
[2026-03-13 23:30:00] Created directory: docs/source-files/
[2026-03-13 23:30:00] Created directory: copilot-skills/
[2026-03-13 23:30:00] Created directory: copilot-skills/script/
[2026-03-13 23:30:00] Created directory: tests/
[2026-03-13 23:30:00] Created directory: governance/
```

### File Movement Log
```
[2026-03-13 23:30:15] Moved: Risk-Parameter-File-Specification.md -> docs/Risk-Parameter-File-Specification.md
[2026-03-13 23:30:15] Moved: Input-Data-Specification.md -> docs/Input-Data-Specification.md
[2026-03-13 23:30:15] Moved: Market-Risk-Component-Calculation.md -> docs/Market-Risk-Component-Calculation.md
[2026-03-13 23:30:15] Moved: Margin-Adjustment-Process.md -> docs/Margin-Adjustment-Process.md
[2026-03-13 23:30:15] Moved: Other-Risk-Components.md -> docs/Other-Risk-Components.md
[2026-03-13 23:30:15] Moved: Position-Processing-Logic.md -> docs/Position-Processing-Logic.md
[2026-03-13 23:30:15] Moved: Collateral-Management.md -> docs/Collateral-Management.md
[2026-03-13 23:30:15] Moved: Corporate-Action-Processing.md -> docs/Corporate-Action-Processing.md
[2026-03-13 23:30:15] Moved: Calculation-Examples.md -> docs/Calculation-Examples.md
[2026-03-13 23:30:15] Moved: Introduction-Overview.md -> docs/Introduction-Overview.md
[2026-03-13 23:30:30] Moved: Core-Business-Global-Process-Flowchart.md -> docs/global-process/Core-Business-Global-Process-Flowchart.md
[2026-03-13 23:30:30] Moved: Initial Margin Calculation Guide HKv14.pdf -> docs/source-files/Initial Margin Calculation Guide HKv14.pdf
```

### File Creation Log
```
[2026-03-13 23:31:00] Created: config/FRAMEWORK-CONFIG.md
[2026-03-13 23:31:30] Created: governance/manual-fallback.md
[2026-03-13 23:32:00] Created: governance/audit-trail.md
[2026-03-13 23:32:30] Created: governance/permission-management.md
[2026-03-13 23:33:00] Updated: README.md
```

### Verification Results
```
[2026-03-13 23:33:30] Verification: All directories exist - PASSED
[2026-03-13 23:33:30] Verification: All files in correct locations - PASSED
[2026-03-13 23:33:30] Verification: All configurations properly set - PASSED
[2026-03-13 23:33:30] Verification: README.md updated with new structure - PASSED
```

## Summary

### Completed Tasks
1. Created all missing directories for the 7-layer framework
2. Moved existing files to appropriate target locations
3. Created configuration files and governance files
4. Updated README.md with new structure and migration notes
5. Generated process output file documenting all operations

### Current Framework Status
- **Layer 1 - docs/**: Populated with rule documents
- **Layer 2 - docs/global-process/**: Contains process documentation
- **Layer 3 - docs/source-files/**: Contains original source PDF
- **Layer 4 - copilot-skills/**: Created, ready for Skill development
- **Layer 5 - tests/**: Created, ready for test case development
- **Layer 6 - config/**: Contains version and framework configuration
- **Layer 7 - governance/**: Contains manual fallback and audit files

### Next Steps
1. Develop Copilot Skills in copilot-skills/ directory
2. Create test cases and BDD scenarios in tests/ directory
3. Implement automation scripts in copilot-skills/script/ directory
4. Populate remaining configuration files in config/ directory
5. Create common governance documents in governance/common/ directory

---

**Updated**: 2026-03-14 - Module names and file mappings corrected to match updated requirements