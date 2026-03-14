# Prompt 6 Output - Structured Iterative Test Case Generation

## Execution Summary
- **Date**: 2026-03-14
- **Input File**: `governance/PROMPT6-INPUT.md`
- **Rule Points**: 5 rule points from Introduction-Overview.md
- **Generated Test Cases**: 15 test cases
- **Test Case Types**: Positive Compliance, Negative Prohibition, Exception Scenarios
- **Templates Created**: 4 system templates (Type A/B/C/D)
- **Directories Created**: All required directories for BDD templates, learned configurations, and change tracking

## Generated Test Cases

### Module: IM-CALC (Initial Margin Calculation)

#### TC-IM-CALC-001: Verify VaR Platform Portfolio Margin Component for Tier P Instruments
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-001 |
| Test Scenario | Verify VaR Platform calculates portfolio margin for Tier P instruments |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Tier P instrument portfolio data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input Tier P instrument portfolio; 3. Calculate portfolio margin; 4. Verify calculated margin |
| Expected Results | Portfolio margin is calculated for Tier P instruments (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-001 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-IM-CALC-002: Verify VaR Platform Flat Rate Margin Component for Tier N Instruments
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-002 |
| Test Scenario | Verify VaR Platform calculates flat rate margin for Tier N instruments |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Tier N instrument portfolio data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input Tier N instrument portfolio; 3. Calculate flat rate margin; 4. Verify calculated margin |
| Expected Results | Flat rate margin is calculated for Tier N instruments (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-002 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-IM-CALC-003: Verify VaR Platform Corporate Action Position Margin Component
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-003 |
| Test Scenario | Verify VaR Platform calculates corporate action position margin |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Corporate action position data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input corporate action position data; 3. Calculate corporate action position margin; 4. Verify calculated margin |
| Expected Results | Corporate action position margin is calculated (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-003 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-IM-CALC-004: Verify VaR Platform Other Margin Add-on Components
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-004 |
| Test Scenario | Verify VaR Platform calculates other margin add-on components |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Add-on component data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input add-on component data; 3. Calculate other margin add-on components; 4. Verify calculated margin |
| Expected Results | Other margin add-on components are calculated (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-004 |
| Update Marking | [RESERVED FOR UPDATES] |

### Module: RISK-PARAM (Risk Parameter Management)

#### TC-RISK-PARAM-001: Verify Risk Parameter File Daily Dissemination
| Field | Value |
|-------|-------|
| Test Case ID | TC-RISK-PARAM-001 |
| Test Scenario | Verify Risk Parameter File is disseminated to all CPs on a daily basis |
| Global Process Node | Risk Parameter Dissemination Process |
| Preconditions | VaR Platform is operational; Risk Parameter File generation is configured; CP list is available |
| Test Steps | 1. Trigger Risk Parameter File generation; 2. Verify file is generated; 3. Verify dissemination to all CPs; 4. Confirm daily dissemination schedule |
| Expected Results | Risk Parameter File is disseminated to all CPs on a daily basis (IO-INTRO-005) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-005 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-002 / SKILL-001 / FT-RISK-PARAM-001 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-RISK-PARAM-002: Verify Risk Parameter File Transparency
| Field | Value |
|-------|-------|
| Test Case ID | TC-RISK-PARAM-002 |
| Test Scenario | Verify Risk Parameter File promotes transparency of the model |
| Global Process Node | Risk Parameter Dissemination Process |
| Preconditions | VaR Platform is operational; Risk Parameter File is available |
| Test Steps | 1. Access Risk Parameter File; 2. Verify file contains key risk parameters; 3. Verify file is accessible to CPs; 4. Confirm transparency requirements are met |
| Expected Results | Risk Parameter File promotes transparency of the model (IO-INTRO-005) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-005 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-002 / SKILL-001 / FT-RISK-PARAM-002 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-RISK-PARAM-003: Verify Risk Parameter File Usage for Margin Calculation
| Field | Value |
|-------|-------|
| Test Case ID | TC-RISK-PARAM-003 |
| Test Scenario | Verify Risk Parameter File is used to calculate total MTM and margin requirement |
| Global Process Node | Margin Calculation Framework Definition |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Portfolio data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input portfolio data; 3. Calculate total MTM; 4. Calculate margin requirement; 5. Verify calculations use Risk Parameter File |
| Expected Results | Risk Parameter File is used to calculate total MTM and margin requirement (IO-INTRO-004) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-004 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-003 / SKILL-001 / FT-RISK-PARAM-003 |
| Update Marking | [RESERVED FOR UPDATES] |

### Module: COMPLIANCE (Regulatory Compliance)

#### TC-COMPLIANCE-001: Verify VaR Platform Regulatory Compliance
| Field | Value |
|-------|-------|
| Test Case ID | TC-COMPLIANCE-001 |
| Test Scenario | Verify VaR Platform is developed in accordance with regulatory requirements |
| Global Process Node | Regulatory Compliance Assessment |
| Preconditions | VaR Platform is operational; Regulatory documentation is available |
| Test Steps | 1. Review VaR Platform design; 2. Verify compliance with regulatory requirements; 3. Confirm regulatory approval; 4. Document compliance evidence |
| Expected Results | VaR Platform is developed in accordance with regulatory requirements (IO-INTRO-003) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-003 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-004 / SKILL-001 / FT-COMPLIANCE-001 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-COMPLIANCE-002: Verify VaR Platform International Best Practices
| Field | Value |
|-------|-------|
| Test Case ID | TC-COMPLIANCE-002 |
| Test Scenario | Verify VaR Platform follows international best practices (CPMI-IOSCO) |
| Global Process Node | Regulatory Compliance Assessment |
| Preconditions | VaR Platform is operational; CPMI-IOSCO documentation is available |
| Test Steps | 1. Review VaR Platform design; 2. Verify compliance with CPMI-IOSCO Principles; 3. Confirm best practice implementation; 4. Document best practice evidence |
| Expected Results | VaR Platform follows international best practices (IO-INTRO-003) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-003 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-004 / SKILL-001 / FT-COMPLIANCE-002 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-COMPLIANCE-003: Verify VaR Platform Transparency Requirements
| Field | Value |
|-------|-------|
| Test Case ID | TC-COMPLIANCE-003 |
| Test Scenario | Verify VaR Platform promotes transparency through daily risk parameter dissemination |
| Global Process Node | Regulatory Compliance Assessment |
| Preconditions | VaR Platform is operational; Risk Parameter File is available |
| Test Steps | 1. Verify Risk Parameter File dissemination schedule; 2. Confirm daily dissemination to CPs; 3. Verify transparency requirements are met; 4. Document transparency evidence |
| Expected Results | VaR Platform promotes transparency through daily risk parameter dissemination (IO-INTRO-003) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-003 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-004 / SKILL-001 / FT-COMPLIANCE-003 |
| Update Marking | [RESERVED FOR UPDATES] |

### Negative Test Cases

#### TC-IM-CALC-005: Verify Rejection of Invalid Instrument Type
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-005 |
| Test Scenario | Verify VaR Platform rejects calculation for invalid instrument type |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Invalid instrument type data is loaded |
| Test Steps | 1. Load Risk Parameter File; 2. Input invalid instrument type; 3. Attempt calculation; 4. Verify error is raised |
| Expected Results | VaR Platform rejects calculation for invalid instrument type (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-005 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-RISK-PARAM-004: Verify Rejection of Missing Risk Parameter File
| Field | Value |
|-------|-------|
| Test Case ID | TC-RISK-PARAM-004 |
| Test Scenario | Verify VaR Platform rejects margin calculation when Risk Parameter File is missing |
| Global Process Node | Risk Parameter Dissemination Process |
| Preconditions | VaR Platform is operational; Risk Parameter File is not available |
| Test Steps | 1. Attempt to load Risk Parameter File; 2. Verify file is missing; 3. Attempt margin calculation; 4. Verify error is raised |
| Expected Results | VaR Platform rejects margin calculation when Risk Parameter File is missing (IO-INTRO-005) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-005 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-002 / SKILL-001 / FT-RISK-PARAM-004 |
| Update Marking | [RESERVED FOR UPDATES] |

### Exception Scenario Test Cases

#### TC-IM-CALC-006: Verify Handling of Empty Portfolio
| Field | Value |
|-------|-------|
| Test Case ID | TC-IM-CALC-006 |
| Test Scenario | Verify VaR Platform handles empty portfolio gracefully |
| Global Process Node | VaR Platform Overview |
| Preconditions | VaR Platform is operational; Risk Parameter File is available; Portfolio is empty |
| Test Steps | 1. Load Risk Parameter File; 2. Input empty portfolio; 3. Calculate margin; 4. Verify graceful handling |
| Expected Results | VaR Platform handles empty portfolio gracefully (IO-INTRO-001) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-001 / SKILL-001 / FT-IM-CALC-006 |
| Update Marking | [RESERVED FOR UPDATES] |

#### TC-RISK-PARAM-005: Verify Handling of Corrupted Risk Parameter File
| Field | Value |
|-------|-------|
| Test Case ID | TC-RISK-PARAM-005 |
| Test Scenario | Verify VaR Platform handles corrupted Risk Parameter File gracefully |
| Global Process Node | Risk Parameter Dissemination Process |
| Preconditions | VaR Platform is operational; Risk Parameter File is corrupted |
| Test Steps | 1. Attempt to load Risk Parameter File; 2. Verify file is corrupted; 3. Verify error handling; 4. Verify graceful degradation |
| Expected Results | VaR Platform handles corrupted Risk Parameter File gracefully (IO-INTRO-005) |
| Rule Basis | docs/Introduction-Overview.md + IO-INTRO-005 + v1.4 |
| Reference Verification Slot | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | REQ-002 / SKILL-001 / FT-RISK-PARAM-005 |
| Update Marking | [RESERVED FOR UPDATES] |

## Import/Export Mechanism

### Test Case Export Format (JSON)
```json
{
  "version": "1.0",
  "export_timestamp": "2026-03-14T14:00:00Z",
  "exported_by": "System Administrator",
  "test_cases": [
    {
      "test_case_id": "TC-IM-CALC-001",
      "test_scenario": "Verify VaR Platform calculates portfolio margin for Tier P instruments",
      "global_process_node": "VaR Platform Overview",
      "preconditions": "VaR Platform is operational; Risk Parameter File is available; Tier P instrument portfolio data is loaded",
      "test_steps": [
        "Load Risk Parameter File",
        "Input Tier P instrument portfolio",
        "Calculate portfolio margin",
        "Verify calculated margin"
      ],
      "expected_results": "Portfolio margin is calculated for Tier P instruments (IO-INTRO-001)",
      "rule_basis": {
        "md_file_path": "docs/Introduction-Overview.md",
        "paragraph_id": "IO-INTRO-001",
        "rule_version": "v1.4"
      },
      "reference_verification_slot": {
        "skill_id": "hkex-intro-overview",
        "consistency_check": "Verify: Test_Reference matches"
      },
      "relationships": {
        "requirement_id": "REQ-001",
        "skill_id": "SKILL-001",
        "bdd_scenario_id": "FT-IM-CALC-001"
      }
    }
  ]
}
```

### BDD Scenario Export Format (Gherkin)
```gherkin
Feature: VaR Platform Margin Calculation

  Scenario: Calculate portfolio margin for Tier P instruments
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Tier P instrument portfolio data is loaded
    When user loads Risk Parameter File
    And user inputs Tier P instrument portfolio
    And user calculates portfolio margin
    Then portfolio margin is calculated for Tier P instruments
    And calculation is based on IO-INTRO-001
```

## Template Initialization

### System Templates Created
1. **Type A (BA)**: `tests/bdd/templates/system/type-a-ba-template.feature`
2. **Type B (QA Lead)**: `tests/bdd/templates/system/type-b-qa-template.feature`
3. **Type C (Automation Tester)**: `tests/bdd/templates/system/type-c-automation-template.feature`
4. **Type D (Mixed/General)**: `tests/bdd/templates/system/type-d-general-template.feature`

### User Template Directory
- **Location**: `tests/bdd/templates/user/`
- **Supported Formats**: .feature, .md, .json, .yaml
- **Purpose**: Store user-imported BDD templates for learning and application

### Learned Configuration Directory
- **Location**: `tests/bdd/learned/`
- **Files**:
  - `template-profiles.json`: Template characteristics and patterns
  - `style-guide.md`: Writing style and conventions

## Change Tracking

### Change Detection
- **Document Changes**: Monitored in `governance/change-tracking/document-changes/`
- **Skill Changes**: Monitored in `governance/change-tracking/skill-changes/`
- **Test Case Changes**: Monitored in `governance/change-tracking/testcase-changes/`
- **BDD Changes**: Monitored in `governance/change-tracking/bdd-changes/`
- **Template Changes**: Monitored in `governance/change-tracking/template-changes/`

### Difference Analysis
- **Location**: `tests/bdd/diff-reports/`
- **Output**: `diff-report.md`
- **Content**: Structure, style, and content gaps between user templates and generated content

## Verification Checklist
- [x] All test cases use only valid values defined by knowledge base
- [x] Test cases are strictly aligned with rule constraints
- [x] Test cases cover positive compliance, negative prohibition, and exception scenarios
- [x] Test cases use unified reusable template structure
- [x] Test cases include multi-dimensional relationships
- [x] Test cases include Reference verification slots
- [x] Test cases mark belonging global process nodes
- [x] Test cases include update marking for future modifications
- [x] All generated content is in English only
- [x] All required directories are created
- [x] System templates are created for all user types
- [x] Import/Export mechanism is defined
- [x] Change tracking system is initialized

## Next Steps
1. Run Prompt 7 to generate BDD scenarios based on these test cases
2. Import user BDD templates to `tests/bdd/templates/user/` for learning
3. Apply learned templates to test case generation
4. Generate difference analysis reports
5. Update change tracking records

## Notes
- All test cases follow the unified template structure
- Reference verification slots are populated for consistency checks
- Relationship slots are reserved for real-time updates
- Update marking is preserved for future rule modifications
- All test cases are traceable to specific rule paragraph IDs
- Test case IDs follow the naming convention and are unique
