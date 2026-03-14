# Prompt 7 Input - BDD/Behave Scenario Generation

## Test Cases

### TC-IM-CALC-001: Verify VaR Platform Portfolio Margin Component for Tier P Instruments
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

### TC-IM-CALC-002: Verify VaR Platform Flat Rate Margin Component for Tier N Instruments
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

### TC-IM-CALC-003: Verify VaR Platform Corporate Action Position Margin Component
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

### TC-IM-CALC-004: Verify VaR Platform Other Margin Add-on Components
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

### TC-RISK-PARAM-001: Verify Risk Parameter File Daily Dissemination
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

### TC-RISK-PARAM-002: Verify Risk Parameter File Transparency
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

### TC-RISK-PARAM-003: Verify Risk Parameter File Usage for Margin Calculation
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

### TC-COMPLIANCE-001: Verify VaR Platform Regulatory Compliance
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

### TC-COMPLIANCE-002: Verify VaR Platform International Best Practices
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

### TC-COMPLIANCE-003: Verify VaR Platform Transparency Requirements
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

## Rule Basis

### Rule Point 1: VaR Platform Overview (IO-INTRO-001)
- **MD File Path**: `c:\Codes\hkex_risk\docs\Introduction-Overview.md`
- **Structured ID**: IO-INTRO-001
- **Rule Version**: 1.4

### Rule Point 2: Margin Components Description (IO-INTRO-002)
- **MD File Path**: `c:\Codes\hkex_risk\docs\Introduction-Overview.md`
- **Structured ID**: IO-INTRO-002
- **Rule Version**: 1.4

### Rule Point 3: Regulatory Compliance (IO-INTRO-003)
- **MD File Path**: `c:\Codes\hkex_risk\docs\Introduction-Overview.md`
- **Structured ID**: IO-INTRO-003
- **Rule Version**: 1.4

### Rule Point 4: Document Purpose (IO-INTRO-004)
- **MD File Path**: `c:\Codes\hkex_risk\docs\Introduction-Overview.md`
- **Structured ID**: IO-INTRO-004
- **Rule Version**: 1.4

### Rule Point 5: Risk Parameter Dissemination (IO-INTRO-005)
- **MD File Path**: `c:\Codes\hkex_risk\docs\Introduction-Overview.md`
- **Structured ID**: IO-INTRO-005
- **Rule Version**: 1.4

## Global Process Nodes
- VaR Platform Overview
- Regulatory Compliance Assessment
- Margin Calculation Framework Definition
- Risk Parameter Dissemination Process

## Applicable Modules
- IM-CALC: Initial Margin Calculation
- RISK-PARAM: Risk Parameter Management
- COMPLIANCE: Regulatory Compliance

## Additional Context
- Target Audience: Business Analysts (BA), QA Leads, Automation Testers
- Document Version: 1.4
- Release Date: Oct 2025
- Original Document: Initial Margin Calculation Guide HKv14
