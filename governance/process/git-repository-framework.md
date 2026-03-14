# Git Knowledge Base Full Lifecycle Framework - Initial Margin Calculation Guide HKv14

## Complete Git Repository Directory Tree

```
initial-margin-knowledge-base/
├── README.md                                    # Repository overview and navigation
├── .gitignore                                   # Git ignore rules
│
├── docs/                                        # Document Layer - Standardized MD Rules
│   ├── README.md                                # Document layer guide
│   ├── Introduction-Overview.md                 # Module 1: BA-focused introduction
│   ├── Risk-Parameter-File-Specification.md     # Module 2: QA Lead-focused IMRPF specs
│   ├── Input-Data-Specification.md              # Module 3: Automation Tester-focused data specs
│   ├── Market-Risk-Component-Calculation.md     # Module 4: Core calculation logic
│   ├── Margin-Adjustment-Process.md             # Module 5: Margin adjustment workflow
│   ├── Other-Risk-Components.md                 # Module 6: Additional risk components
│   ├── Position-Processing-Logic.md             # Module 7: Position processing rules
│   ├── Collateral-Management.md                 # Module 8: Collateral handling
│   ├── Corporate-Action-Processing.md           # Module 9: Corporate action rules
│   ├── Calculation-Examples.md                  # Module 10: Calculation examples
│   └── archived/                                # Archived historical versions
│       └── README.md                            # Archive guidelines
│
├── docs/global-process/                         # Global Process Layer - Core Business Flow
│   ├── README.md                                # Global process layer guide
│   ├── GLOBAL-PROCESS.md                        # Core business global process base document
│   ├── Core-Business-Global-Process-Flowchart.md # Visual flowchart
│   ├── process-relationships.md                 # Process node to rule mapping
│   └── process-versions/                        # Historical process versions
│       └── README.md                            # Version management
│
├── docs/source-files/                           # Original Document Layer - Source Files
│   ├── README.md                                # Source files management guide
│   ├── Initial-Margin-Calculation-Guide-HKv14.pdf  # Original PDF (if available)
│   ├── Initial-Margin-Calculation-Guide-HKv14.md   # Original converted MD
│   └── archived-versions/                       # Historical source versions
│       └── README.md                            # Archive index
│
├── copilot-skills/                              # AI Capability Layer - GitHub Copilot Skills
│   ├── README.md                                # Skills layer guide
│   ├── skill-definitions/                       # Individual skill definitions
│   │   ├── hkex-im-overview.md                  # Skill: IM overview
│   │   ├── hkex-risk-parameters.md              # Skill: Risk parameter handling
│   │   ├── hkex-portfolio-margin.md             # Skill: Portfolio margin calculation
│   │   ├── hkex-flat-rate-margin.md             # Skill: Flat rate margin calculation
│   │   ├── hkex-lra-calculation.md              # Skill: Liquidation risk add-on
│   │   ├── hkex-structured-product-addon.md     # Skill: Structured product add-on
│   │   ├── hkex-corporate-action-margin.md      # Skill: Corporate action margin
│   │   ├── hkex-margin-adjustment.md            # Skill: Margin adjustment process
│   │   ├── hkex-collateral-management.md        # Skill: Collateral management
│   │   └── hkex-position-processing.md          # Skill: Position processing
│   ├── index.md                                 # Skill index table
│   ├── skill-bdd-relation.md                    # Skill-BDD relationship management
│   ├── usage-guidelines.md                      # Skill usage guidelines
│   └── scripts/                                 # Automation Scripts
│       ├── README.md                            # Scripts documentation
│       ├── hkex-im-overview.py                  # Reference sync script
│       ├── hkex-risk-parameters.py              # Multi-model verification trigger
│       ├── hkex-portfolio-margin.py             # Git linkage script
│       └── common/                              # Shared utilities
│           └── utils.py                         # Common functions
│
├── tests/                                       # Test Asset Layer - Test Cases & BDD
│   ├── README.md                                # Test layer guide
│   ├── test-cases/                              # Structured test cases
│   │   ├── README.md                            # Test case guidelines
│   │   ├── tc-introduction-overview.md          # Test cases for Module 1
│   │   ├── tc-risk-parameter-file.md            # Test cases for Module 2
│   │   ├── tc-input-data.md                     # Test cases for Module 3
│   │   ├── tc-market-risk-component.md          # Test cases for Module 4
│   │   ├── tc-margin-adjustment.md              # Test cases for Module 5
│   │   ├── tc-other-risk-components.md          # Test cases for Module 6
│   │   ├── tc-position-processing.md            # Test cases for Module 7
│   │   ├── tc-collateral-management.md          # Test cases for Module 8
│   │   ├── tc-corporate-action.md               # Test cases for Module 9
│   │   └── tc-calculation-examples.md           # Test cases for Module 10
│   ├── bdd/                                     # BDD Scenarios
│   │   ├── README.md                            # BDD guidelines
│   │   ├── features/                            # Feature files
│   │   │   ├── im_calculation.feature           # IM calculation scenarios
│   │   │   ├── risk_parameters.feature          # Risk parameter scenarios
│   │   │   ├── portfolio_margin.feature         # Portfolio margin scenarios
│   │   │   ├── flat_rate_margin.feature         # Flat rate margin scenarios
│   │   │   ├── lra_calculation.feature          # LRA scenarios
│   │   │   ├── structured_product.feature       # Structured product scenarios
│   │   │   ├── corporate_action.feature         # Corporate action scenarios
│   │   │   ├── margin_adjustment.feature        # Margin adjustment scenarios
│   │   │   ├── collateral_management.feature    # Collateral scenarios
│   │   │   └── position_processing.feature      # Position processing scenarios
│   │   ├── steps/                               # Python step definitions
│   │   │   ├── im_calculation_steps.py          # Steps for IM calculation
│   │   │   ├── risk_parameter_steps.py          # Steps for risk parameters
│   │   │   ├── portfolio_margin_steps.py        # Steps for portfolio margin
│   │   │   ├── flat_rate_margin_steps.py        # Steps for flat rate margin
│   │   │   ├── lra_calculation_steps.py         # Steps for LRA
│   │   │   ├── structured_product_steps.py      # Steps for structured product
│   │   │   ├── corporate_action_steps.py        # Steps for corporate action
│   │   │   ├── margin_adjustment_steps.py       # Steps for margin adjustment
│   │   │   ├── collateral_management_steps.py   # Steps for collateral
│   │   │   └── position_processing_steps.py     # Steps for position processing
│   │   └── behave.ini                           # Behave configuration
│   ├── bdd-relation-manager.md                  # BDD relationship management
│   └── test-data/                               # Test data templates
│       └── README.md                            # Test data guidelines
│
├── config/                                      # Configuration Layer
│   ├── README.md                                # Configuration guide
│   ├── RULES-VERSION.md                         # Rule version overview
│   ├── UPDATE-LOG.md                            # Update history log
│   ├── NAMING-CONVENTIONS.md                    # File naming conventions
│   ├── skill-reference-spec.md                  # Reference field specifications
│   ├── skill-verify-config.md                   # Skill verification configuration
│   └── multi-model-verify-config.yaml           # Multi-model verification config
│
└── governance/                                  # Governance Layer - Manual Fallback
    ├── README.md                                # Governance overview
    ├── build/                                   # Construction phase
    │   ├── manual-audit-table.md                # Manual audit records
    │   ├── fallback-decision-record.md          # Fallback decisions
    │   └── reference-mapping-audit-table.md     # Reference mapping audit
    ├── update/                                  # Update phase
    │   ├── impact-scope-manual-verification.md  # Impact scope verification
    │   ├── relationship-reference-manual-audit.md # Relationship audit
    │   └── script-execution-exception-fallback.md # Script exception fallback
    ├── verify/                                  # Verification phase
    │   ├── multi-model-result-inconsistency.md  # Inconsistency judgment
    │   ├── reference-script-verification-failure.md # Verification failure
    │   └── verification-issue-reporting.md      # Issue reporting
    ├── optimize/                                # Optimization phase
    │   ├── optimization-suggestion-manual-audit.md # Optimization audit
    │   └── reference-script-rectification.md    # Rectification verification
    ├── archive/                                 # Archiving phase
    │   ├── version-archiving-manual-audit.md    # Version audit
    │   ├── knowledge-base-audit-record.md       # KB audit records
    │   └── reference-script-archiving-specs.md  # Archiving specifications
    └── common/                                  # Common governance
        ├── fallback-issue-rectification-tracking.md # Issue tracking
        ├── permission-assignment-table.md         # Permission management
        └── responsible-person-change-record.md    # Responsibility changes
```

---

## Directory Maintenance Specifications & Extension Rules

### Document Layer (docs/)

**Function Description:**
- Stores standardized MD rule documents split by Prompt 1
- Each module targets specific business logic and role concerns
- Maintains traceability to original document sections

**File Naming Conventions:**
- Format: `Module-SubTopic.md`
- Examples: `Introduction-Overview.md`, `Risk-Parameter-File-Specification.md`
- Use kebab-case (hyphen-separated lowercase)

**Update Maintenance Requirements:**
1. **Version Control:** Each update must increment version number in document header
2. **Change Tracking:** All modifications must be logged in `config/UPDATE-LOG.md`
3. **Reference Synchronization:** Updates must sync to `copilot-skills/skill-definitions/` and `tests/`
4. **Traceability Preservation:** Maintain original document section references

**Extension Rules:**
- New modules: Follow Prompt 1's 10-module framework or extend with new Module-XX naming
- Archived versions: Move superseded versions to `docs/archived/`

---

### Global Process Layer (docs/global-process/)

**Function Description:**
- Stores core business global process flowcharts and documentation
- Maps process nodes to rule modules
- Supports real-time updates when processes change

**File Naming Conventions:**
- Base document: `GLOBAL-PROCESS.md`
- Flowcharts: `Core-Business-Global-Process-Flowchart.md`
- Relationships: `process-relationships.md`

**Update Maintenance Requirements:**
1. **Synchronization:** Must sync with `docs/` module updates
2. **Versioning:** Historical versions stored in `process-versions/`
3. **Mapping Accuracy:** Ensure process nodes correctly map to rule paragraphs

**Extension Rules:**
- Sub-processes: Create `sub-process-[name].md` for detailed subprocesses
- Cross-references: Link to related modules in `docs/`

---

### Original Document Layer (docs/source-files/)

**Function Description:**
- Stores original business rule files (PDF/Word) for traceability
- Maintains historical versions for audit purposes
- Supports Skill Reference traceability

**File Naming Conventions:**
- Original: `[Document-Name]-v[Version].[ext]`
- Converted: `[Document-Name]-v[Version].md`

**Update Maintenance Requirements:**
1. **Immutability:** Original files should not be modified; create new versions
2. **Index Maintenance:** `archived-versions/README.md` must list all versions
3. **Reference Linkage:** All `Rule_Source` references must point to files here

**Extension Rules:**
- New versions: Add to root; move old versions to `archived-versions/`
- Multiple documents: Create subdirectories by document type

---

### AI Capability Layer (copilot-skills/)

**Function Description:**
- Stores modular GitHub Copilot Skills
- Manages Skill-BDD relationships
- Contains automation scripts for lifecycle management

**File Naming Conventions:**
- Skills: `[business]-[module]-[capability].md`
  - Examples: `hkex-im-overview.md`, `hkex-portfolio-margin.md`
- Scripts: `[skill-id].py` (matching skill filename)
- Index: `index.md`

**Update Maintenance Requirements:**
1. **Reference Field Maintenance:**
   - `Rule_Source`: `{MD file full path} | {structured ID} | {version} | {original doc path}`
   - `Test_Reference`: `{test case ID} | {feature file path}`
   - `Verify_Reference`: `{config ID} | {audit record path}`
   - `Update_History`: `{timestamp} | {updater} | {commit ID}`

2. **Synchronous Update Requirements:**
   - When rules update: Update `Rule_Source` version and verify alignment
   - When BDD updates: Update `Test_Reference` associations
   - When verified: Update `Verify_Reference` with results
   - All updates: Append to `Update_History`

3. **Script Storage & Execution:**
   - **Storage Path:** `copilot-skills/scripts/`
   - **Execution Permissions:** Python scripts executable by automation service account
   - **Exception Fallback Rules:**
     - Script failure → Log to `governance/common/fallback-issue-rectification-tracking.md`
     - Trigger manual fallback with operation guidance
     - Block PR merge until manual verification complete

**Extension Rules:**
- New skills: Add to `skill-definitions/` and update `index.md`
- New scripts: Follow `[skill-id].py` naming; add to `scripts/README.md`
- Skill categories: Create subdirectories if skills exceed 20

---

### Test Asset Layer (tests/)

**Function Description:**
- Stores structured test cases and BDD scenarios
- Manages test-BDD-Skill relationships
- Contains executable step definitions

**File Naming Conventions:**
- Test cases: `tc-[module]-[description].md`
- Feature files: `[feature_name].feature`
- Step definitions: `[feature_name]_steps.py`

**Update Maintenance Requirements:**
1. **Reference Verification Slots:**
   - Each test case must include `Rule_Source` matching Skill's reference
   - Each BDD scenario must include `Test_Reference` matching test case ID
   - Verification must check consistency across all references

2. **Relationship Real-time Updates:**
   - Update `tests/bdd-relation-manager.md` when BDD scenarios change
   - Sync with `copilot-skills/skill-bdd-relation.md` for consistency
   - Log all relationship changes with timestamp and updater

**Extension Rules:**
- New test types: Create subdirectories under `tests/`
- Test data: Store templates in `tests/test-data/`

---

### Configuration Layer (config/)

**Function Description:**
- Centralizes version management, naming conventions, and verification configs
- Supports multi-model verification configuration
- Defines Reference and Script specifications

**File Naming Conventions:**
- Version: `RULES-VERSION.md`
- Update log: `UPDATE-LOG.md`
- Conventions: `NAMING-CONVENTIONS.md`
- Specs: `skill-reference-spec.md`, `skill-verify-config.md`
- Config: `multi-model-verify-config.yaml`

**Update Maintenance Requirements:**
1. **Version Management:**
   - `RULES-VERSION.md`: Master version tracking for all modules
   - Update on any rule change; sync with Git tags

2. **Update Logging:**
   - `UPDATE-LOG.md`: Chronological log of all changes
   - Include: timestamp, updater, changed files, change type, verification status

3. **Multi-model Verification Config:**
   - `multi-model-verify-config.yaml`: Model weights, thresholds, dimensions
   - Reference/Script verification weight: 30%
   - Update when verification criteria change

**Extension Rules:**
- New config types: Add to `config/` with `.md` or `.yaml` extension
- Environment configs: Create `config/environments/` for different deployments

---

### Governance Layer (governance/)

**Function Description:**
- Implements manual fallback mechanisms for full lifecycle management
- Stores audit records and permission management
- Tracks issue rectification

**File Naming Conventions:**
- By phase: `[phase]/[document-purpose].md`
- Examples: `build/manual-audit-table.md`, `verify/verification-issue-reporting.md`

**Update Maintenance Requirements:**
1. **Manual Fallback Trigger Conditions:**
   - Reference verification failure → Trigger `verify/reference-script-verification-failure.md`
   - Script execution exception → Trigger `update/script-execution-exception-fallback.md`
   - Multi-model inconsistency → Trigger `verify/multi-model-result-inconsistency.md`

2. **Audit Process:**
   - All manual operations recorded with: operation type, operator, timestamp, result
   - Sign-off required for: PR merge, version tag, production deployment

3. **Permission Management:**
   - Four-level permissions: View / Edit / Audit / Decision
   - Reference/Script audit permission: Required for `governance/verify/` and `governance/update/`

**Extension Rules:**
- New lifecycle phases: Create subdirectory with audit templates
- Cross-phase issues: Log in `governance/common/`

---

## Skill Reference/Script Adaptation Requirements

### Reference Structured Format

All Skills must include structured Reference fields:

```markdown
### Structured Reference
- **Rule_Source**: `docs/Market-Risk-Component-Calculation.md | MRC-CALC-001 | v1.4 | docs/source-files/Initial-Margin-Calculation-Guide-HKv14.pdf`
- **Test_Reference**: `TC-MRC-001 | tests/bdd/features/portfolio_margin.feature` (To be associated)
- **Verify_Reference**: `multi-model-v1 | governance/verify/audit-2025-03-13.md` (Reserved)
- **Update_History**:
  - `2025-03-13 10:00:00 | AI Assistant | abc1234` (Initial creation)
  - `2025-03-14 15:30:00 | QA Lead | def5678` (Reference update)
```

### Script Pre-embedding Specifications

Each Skill must pre-embed Script slots:

```markdown
### Automation Script (GitHub Copilot)
- **Script Path**: `copilot-skills/scripts/hkex-portfolio-margin.py`
- **Input**: Skill ID, Rule_Source, Git repository path
- **Output**: Reference sync status, verification results, PR link
- **Exception Handling**: Auto-log to `governance/common/fallback-issue-rectification-tracking.md`

### Operation Guide (M365 Copilot)
1. Open `copilot-skills/skill-bdd-relation.md`
2. Locate your Skill ID row
3. Update "Reference Integrity" column with verification result
4. Save and commit changes
5. Run "Reference Sync" from Copilot chat
```

### Synchronous Update Requirements

1. **Rule Update → Skill Update:**
   - Rule version changes → Update `Rule_Source` version in Skill
   - Rule content changes → Verify Skill example responses still align
   - New rule paragraph → Consider new Skill or extend existing

2. **Skill Update → Script Update:**
   - Reference changes → Run Reference sync script
   - New Skill → Create corresponding script
   - Script failure → Trigger manual fallback

3. **BDD Update → Relationship Update:**
   - New test case → Update `Test_Reference` in Skill
   - New BDD scenario → Update `tests/bdd-relation-manager.md`
   - Relationship change → Sync both `skill-bdd-relation.md` and `bdd-relation-manager.md`

---

## Framework Support Capabilities

### ① Unified Multi-Model Verification Configuration Management
- Central config: `config/multi-model-verify-config.yaml`
- Model weights, thresholds, dimensions defined centrally
- All verification references same configuration
- Updates propagate to all verification processes

### ② Real-Time BDD Relationship Updates
- Dual relationship files: `skill-bdd-relation.md` and `bdd-relation-manager.md`
- Editable format for manual updates
- Script automation for bulk updates
- Consistency verification across both files

### ③ Manual Fallback Mechanism Documentation
- Comprehensive governance layer with phase-specific templates
- Clear trigger conditions and audit processes
- Permission-based access control
- Full traceability with Reference/Script association

### ④ Standardized Skill Reference/Script Management
- Structured Reference format with mandatory fields
- Script pre-embedding with input/output specifications
- Exception handling with automatic fallback triggers
- Version-controlled updates with Git integration

---

## Implementation Checklist

- [ ] Create directory structure as defined above
- [ ] Move existing MD files to appropriate directories
- [ ] Create README.md files for each layer
- [ ] Initialize `config/RULES-VERSION.md` with current version
- [ ] Create `docs/global-process/GLOBAL-PROCESS.md`
- [ ] Set up `copilot-skills/` with initial skill templates
- [ ] Initialize `tests/bdd/` with behave configuration
- [ ] Create governance templates for all phases
- [ ] Configure Git hooks for Reference validation
- [ ] Test Script execution and fallback mechanisms
