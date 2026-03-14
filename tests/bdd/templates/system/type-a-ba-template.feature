# Type A (BA) - Business-Focused Test Case Template

## Template Overview
This template is designed for Business Analysts (BA) who focus on business rule verification and requirement traceability.

## Test Case Structure

### Test Case ID Format
- Format: `TC-[module abbreviation]-[number]`
- Example: `TC-IM-CALC-001`, `TC-RISK-PARAM-001`
- Module Abbreviations:
  - IM-CALC: Initial Margin Calculation
  - RISK-PARAM: Risk Parameter Management
  - COMPLIANCE: Regulatory Compliance
  - COLLATERAL: Collateral Management
  - CORPORATE-ACTION: Corporate Action Processing

### Test Case Template

| Field | Description | Example |
|-------|-------------|----------|
| Test Case ID | Unique identifier | TC-IM-CALC-001 |
| Test Scenario | Clear rule verification point + global process node | Verify VaR Platform calculates portfolio margin for Tier P instruments |
| Global Process Node | Associated global process node | VaR Platform Overview |
| Preconditions | Environmental/configuration requirements | VaR Platform is operational; Risk Parameter File is available |
| Test Steps | Executable operation sequence | 1. Load Risk Parameter File; 2. Input Tier P instrument portfolio; 3. Calculate portfolio margin |
| Expected Results | Rule-based precise assertions with paragraph ID | Portfolio margin is calculated for Tier P instruments (IO-INTRO-001) |
| Rule Basis | MD file path + paragraph ID + version | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill ID + consistency check | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | Requirement ID/Skill ID/BDD scenario ID | REQ-001 / SKILL-001 / FT-IM-CALC-001 |
| Update Marking | Blank lines for updates | [RESERVED FOR UPDATES] |

## Test Case Types

### Positive Compliance Tests
- Verify that the system correctly implements business rules
- Validate that expected outcomes are achieved
- Ensure proper handling of valid inputs

### Negative Prohibition Tests
- Verify that the system rejects invalid inputs
- Validate that prohibited operations are blocked
- Ensure proper error handling

### Exception Scenario Tests
- Verify that the system handles edge cases
- Validate proper handling of boundary conditions
- Ensure graceful degradation

## Business Rule Verification Checklist
- [ ] Rule is accurately represented in test case
- [ ] Test scenario aligns with business requirement
- [ ] Expected results are measurable and verifiable
- [ ] Test steps are clear and unambiguous
- [ ] Preconditions are properly defined
- [ ] Global process node is correctly identified
- [ ] Rule basis is properly referenced with paragraph ID
- [ ] Reference verification slot is populated

## Traceability Requirements
- Each test case must reference specific rule paragraph ID
- Test case ID must be unique and follow naming convention
- Relationships to Skills and BDD scenarios must be maintained
- Update marking must be preserved for future modifications

## Quality Criteria
- Test cases are business-focused and requirement-driven
- Test scenarios are clear and unambiguous
- Expected results are precise and measurable
- Traceability to business rules is maintained
- Templates are reusable and consistent
