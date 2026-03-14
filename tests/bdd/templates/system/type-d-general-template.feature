# Type D (Mixed/General) - Universal Test Case Template

## Template Overview
This template is designed for mixed/general users who need a universal template with balanced coverage across business analysis, quality assurance, and automation.

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
| Test Priority | Priority level (P0-P3) | P0 (Critical) |
| Test Type | Test classification (Functional/Integration/System/Performance) | Functional |
| Automation Status | Automation status (Automated/Manual/Semi-Automated) | Semi-Automated |
| Preconditions | Environmental/configuration requirements | VaR Platform is operational; Risk Parameter File is available |
| Test Steps | Executable operation sequence | 1. Load Risk Parameter File; 2. Input Tier P instrument portfolio; 3. Calculate portfolio margin; 4. Verify calculated margin |
| Expected Results | Rule-based precise assertions with paragraph ID | Portfolio margin is calculated for Tier P instruments (IO-INTRO-001) |
| Actual Results | Placeholder for test execution results | [TO BE FILLED DURING EXECUTION] |
| Status | Test execution status (Pass/Fail/Blocked/Skipped) | [TO BE FILLED DURING EXECUTION] |
| Rule Basis | MD file path + paragraph ID + version | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill ID + consistency check | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | Requirement ID/Skill ID/BDD scenario ID | REQ-001 / SKILL-001 / FT-IM-CALC-001 |
| Dependencies | Test case dependencies | Depends on TC-IM-CALC-000 (Setup) |
| Test Data | Required test data | Risk Parameter File v1.4; Tier P instrument portfolio data |
| BDD Feature ID | Associated BDD feature | FT-IM-CALC-001 |
| Update Marking | Blank lines for updates | [RESERVED FOR UPDATES] |

## Test Case Types

### Functional Tests
- Verify that business rules are correctly implemented
- Validate system behavior against requirements
- Ensure proper handling of valid and invalid inputs

### Integration Tests
- Verify that components work together correctly
- Validate data flow between modules
- Ensure proper integration with external systems

### System Tests
- Verify end-to-end system behavior
- Validate system performance under load
- Ensure system reliability and stability

### BDD Scenario Tests
- Verify behavior using Gherkin syntax (Given/When/Then)
- Validate scenarios are executable and maintainable
- Ensure scenarios are reusable and parameterized

## Comprehensive Checklist
- [ ] Test case is clear and unambiguous
- [ ] Test steps are detailed and executable
- [ ] Expected results are measurable and verifiable
- [ ] Test priority is correctly assigned
- [ ] Test type is appropriate for scenario
- [ ] Preconditions are properly defined
- [ ] Dependencies are identified and documented
- [ ] Test data requirements are specified
- [ ] Rule basis is properly referenced with paragraph ID
- [ ] Reference verification slot is populated
- [ ] Traceability to requirements, Skills, and BDD scenarios is maintained
- [ ] Automation feasibility is assessed
- [ ] Test execution status is tracked

## Balanced Coverage Criteria
- All business rules are covered by test cases
- Positive, negative, and exception scenarios are included
- Edge cases and boundary conditions are tested
- Performance and scalability are validated
- Integration points are tested
- BDD scenarios are defined where appropriate
- Automation opportunities are identified

## Test Management Requirements
- Test cases are organized by module and priority
- Test execution status is tracked and reported
- Test results are documented and analyzed
- Test defects are logged and tracked
- Test coverage metrics are calculated and reported
- Automation progress is monitored

## Quality Metrics
- Test case coverage percentage
- Test execution pass rate
- Defect density
- Test execution time
- Test automation coverage
- BDD scenario coverage

## Quality Criteria
- Test cases are comprehensive and well-structured
- Test scenarios are clear and unambiguous
- Expected results are precise and measurable
- Traceability to requirements, rules, Skills, and BDD scenarios is maintained
- Test coverage is adequate and balanced
- Test execution is efficient and effective
- Automation opportunities are maximized
- BDD integration is seamless
