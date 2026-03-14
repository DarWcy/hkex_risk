# Type B (QA Lead) - Quality-Focused Test Case Template

## Template Overview
This template is designed for QA Leads who focus on test case management, quality assurance, and comprehensive test coverage.

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
| Preconditions | Environmental/configuration requirements | VaR Platform is operational; Risk Parameter File is available |
| Test Steps | Executable operation sequence with expected results | 1. Load Risk Parameter File; 2. Input Tier P instrument portfolio; 3. Calculate portfolio margin; 4. Verify calculated margin |
| Expected Results | Rule-based precise assertions with paragraph ID | Portfolio margin is calculated for Tier P instruments (IO-INTRO-001) |
| Actual Results | Placeholder for test execution results | [TO BE FILLED DURING EXECUTION] |
| Status | Test execution status (Pass/Fail/Blocked/Skipped) | [TO BE FILLED DURING EXECUTION] |
| Rule Basis | MD file path + paragraph ID + version | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill ID + consistency check | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | Requirement ID/Skill ID/BDD scenario ID | REQ-001 / SKILL-001 / FT-IM-CALC-001 |
| Dependencies | Test case dependencies | Depends on TC-IM-CALC-000 (Setup) |
| Test Data | Required test data | Risk Parameter File v1.4; Tier P instrument portfolio data |
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

### Performance Tests
- Verify system performance meets requirements
- Validate response times and throughput
- Ensure system scalability

## Quality Assurance Checklist
- [ ] Test case is clear and unambiguous
- [ ] Test steps are detailed and executable
- [ ] Expected results are measurable and verifiable
- [ ] Test priority is correctly assigned
- [ ] Test type is appropriate for the scenario
- [ ] Preconditions are properly defined
- [ ] Dependencies are identified and documented
- [ ] Test data requirements are specified
- [ ] Rule basis is properly referenced with paragraph ID
- [ ] Reference verification slot is populated
- [ ] Traceability to requirements is maintained

## Test Coverage Criteria
- All business rules are covered by test cases
- Positive, negative, and exception scenarios are included
- Edge cases and boundary conditions are tested
- Performance and scalability are validated
- Integration points are tested

## Test Management Requirements
- Test cases are organized by module and priority
- Test execution status is tracked and reported
- Test results are documented and analyzed
- Test defects are logged and tracked
- Test coverage metrics are calculated and reported

## Quality Metrics
- Test case coverage percentage
- Test execution pass rate
- Defect density
- Test execution time
- Test automation coverage

## Quality Criteria
- Test cases are comprehensive and well-structured
- Test scenarios are clear and unambiguous
- Expected results are precise and measurable
- Traceability to requirements and rules is maintained
- Test coverage is adequate and balanced
- Test execution is efficient and effective
