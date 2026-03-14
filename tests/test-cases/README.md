# Test Cases Directory

This directory contains structured test cases for the HKEX Risk project, generated based on business rules and aligned with BDD scenarios.

## Directory Structure

```
test-cases/
├── README.md                    # This file
├── index.md                     # Test case index and mapping
├── TC-IM-CALC-001.md           # Initial Margin Calculation test cases
├── TC-IM-CALC-002.md
├── TC-COMPLIANCE-001.md        # Compliance test cases
└── [Future test cases...]
```

## Test Case Naming Convention

- **Format**: `TC-[MODULE]-[NUMBER].md`
- **Example**: `TC-IM-CALC-001.md`
- **Modules**:
  - `IM-CALC`: Initial Margin Calculation
  - `COMPLIANCE`: Compliance and Validation
  - `RISK-PARAM`: Risk Parameter Management

## Test Case Structure

Each test case file follows this structure:

1. **Basic Information**: ID, Title, Module, Priority, Type
2. **Rule Basis**: MD file reference, Paragraph ID, Version
3. **Global Process Node**: Associated process node
4. **Test Scenario**: Description of what is being tested
5. **Preconditions**: Required setup before execution
6. **Test Steps**: Detailed steps with actions and expected results
7. **Test Data**: Input data and expected output
8. **Relationship Mapping**: Links to requirements, skills, and BDD scenarios
9. **Boundary Conditions**: Edge cases and limits
10. **Exception Scenarios**: Error handling cases
11. **Execution History**: Record of test executions
12. **Review Status**: Quality assurance tracking

## Relationship to BDD

Test cases are designed to align with BDD scenarios:
- Each test case maps to one or more BDD scenarios
- BDD Scenario ID is referenced in the Relationship Mapping section
- Test cases provide detailed test data for BDD scenario execution

## Reference Verification

All test cases include Reference Verification Slots for:
- Skill References
- Requirement IDs
- BDD Scenario IDs
- Rule Paragraph IDs

## Status Definitions

- **Draft**: Initial creation, pending review
- **Under Review**: Being reviewed by QA team
- **Approved**: Ready for execution
- **Rejected**: Does not meet requirements, needs revision
- **Deprecated**: No longer valid, superseded by newer test case

## Automation Status

- **Ready for Automation**: Can be automated
- **Automated**: Already has automation script
- **Manual Only**: Requires manual execution
- **Not Automatable**: Cannot be automated

## Quick Links

- [Test Case Index](index.md)
- [BDD Features](../bdd/features/)
- [Test Case Review Template](../../governance/reviews/templates/test/testcase-review-template.md)
- [BDD Relation Manager](../bdd-relation-manager.md)
