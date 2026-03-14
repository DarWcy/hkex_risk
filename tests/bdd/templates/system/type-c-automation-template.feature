# Type C (Automation Tester) - Automation-Focused Test Case Template

## Template Overview
This template is designed for Automation Testers who focus on BDD integration, test automation, and executable test scenarios.

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
| Automation Status | Automation status (Automated/Manual/Semi-Automated) | Automated |
| BDD Feature ID | Associated BDD feature | FT-IM-CALC-001 |
| Preconditions | Environmental/configuration requirements | VaR Platform is operational; Risk Parameter File is available |
| Test Steps (Gherkin) | Executable operation sequence in Gherkin format | Given VaR Platform is operational; When user loads Risk Parameter File; And user inputs Tier P instrument portfolio; Then portfolio margin is calculated for Tier P instruments |
| Expected Results | Rule-based precise assertions with paragraph ID | Portfolio margin is calculated for Tier P instruments (IO-INTRO-001) |
| Automation Steps | Automation implementation steps | 1. Create step definitions; 2. Implement test data setup; 3. Create assertion methods |
| Test Data | Required test data | Risk Parameter File v1.4; Tier P instrument portfolio data |
| Rule Basis | MD file path + paragraph ID + version | docs/Introduction-Overview.md + IO-INTRO-001 + v1.4 |
| Reference Verification Slot | Skill ID + consistency check | Skill: hkex-intro-overview; Verify: Test_Reference matches |
| Relationships | Requirement ID/Skill ID/BDD scenario ID | REQ-001 / SKILL-001 / FT-IM-CALC-001 |
| Automation Framework | Framework used (Behave/Cucumber/Selenium) | Behave |
| Update Marking | Blank lines for updates | [RESERVED FOR UPDATES] |

## Test Case Types

### Automated Functional Tests
- Verify that business rules are correctly implemented through automation
- Validate system behavior against requirements using automated scripts
- Ensure proper handling of valid and invalid inputs

### BDD Scenario Tests
- Verify behavior using Gherkin syntax (Given/When/Then)
- Validate scenarios are executable and maintainable
- Ensure scenarios are reusable and parameterized

### Data-Driven Tests
- Verify system behavior with multiple data sets
- Validate edge cases and boundary conditions
- Ensure test data is properly managed

### API/Integration Tests
- Verify API endpoints and integration points
- Validate data flow between modules
- Ensure proper error handling and response codes

## Automation Checklist
- [ ] Test scenario is automatable
- [ ] Gherkin steps are clear and unambiguous
- [ ] Step definitions are implementable
- [ ] Test data is manageable and parameterized
- [ ] Expected results are verifiable through automation
- [ ] Automation framework is appropriate for scenario
- [ ] Test execution time is acceptable
- [ ] Test maintenance overhead is reasonable
- [ ] Rule basis is properly referenced with paragraph ID
- [ ] Reference verification slot is populated
- [ ] Traceability to BDD scenarios is maintained

## BDD Integration Requirements
- Test cases are written in Gherkin syntax
- Step definitions are reusable and maintainable
- Scenarios are parameterized and data-driven
- Test data is externalized and manageable
- Assertions are clear and precise

## Automation Best Practices
- Use Page Object Model for UI automation
- Implement proper wait mechanisms
- Handle dynamic elements and data
- Implement proper error handling
- Use descriptive and maintainable selectors
- Implement proper test data management
- Use appropriate assertion methods
- Implement proper logging and reporting

## Automation Framework Requirements
- Support for Gherkin syntax (Given/When/Then)
- Support for data-driven testing
- Support for parallel execution
- Support for test reporting and logging
- Support for test data management
- Support for environment configuration

## Quality Criteria
- Test cases are automatable and maintainable
- Gherkin scenarios are clear and executable
- Step definitions are reusable and parameterized
- Test data is properly managed
- Automation coverage is adequate
- Test execution is efficient and reliable
