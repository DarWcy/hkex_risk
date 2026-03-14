# Test Case: TC-COMPLIANCE-001

## Basic Information
- **Test Case ID**: TC-COMPLIANCE-001
- **Title**: Validate Risk Parameter File format and content
- **Module**: Compliance (COMPLIANCE)
- **Priority**: Critical
- **Test Type**: Positive + Negative
- **Automation Status**: Ready for Automation

## Rule Basis
- **MD File**: `docs/source-files/hkex-compliance-requirements.md`
- **Paragraph ID**: `COMP-001`
- **Version**: v1.4
- **Rule Description**: Risk Parameter File must conform to specified XML schema and contain valid risk parameters

## Global Process Node
- **Process Node**: Risk Parameter Management
- **Node ID**: NODE-002

## Test Scenario
Verify that the system correctly validates Risk Parameter File format, schema compliance, and data integrity before processing.

## Preconditions
1. Validation service is operational
2. XML schema definition is available
3. Test Risk Parameter Files are prepared (valid and invalid)

## Test Steps

### Positive Scenario

| Step | Action | Expected Result | Test Data |
|------|--------|-----------------|-----------|
| 1 | Upload valid Risk Parameter File | File accepted, validation passed | Valid XML file |
| 2 | Verify schema compliance | Schema validation successful | N/A |
| 3 | Check data integrity | All risk parameters valid | N/A |
| 4 | Confirm file processing readiness | Status: Ready for Use | N/A |

### Negative Scenario - Invalid Format

| Step | Action | Expected Result | Test Data |
|------|--------|-----------------|-----------|
| 1 | Upload malformed XML file | File rejected | Malformed XML |
| 2 | Verify error message | Clear error: "Invalid XML format" | N/A |
| 3 | Check error details | Specific line/column indicated | N/A |

### Negative Scenario - Schema Violation

| Step | Action | Expected Result | Test Data |
|------|--------|-----------------|-----------|
| 1 | Upload XML with schema violations | File rejected | Schema-invalid XML |
| 2 | Verify schema error details | Specific violations listed | N/A |
| 3 | Check rejection reason | Clear violation description | N/A |

## Expected Results
- Valid files are accepted and marked as ready
- Invalid files are rejected with clear error messages
- Schema violations are specifically identified
- Data integrity issues are reported

## Test Data Requirements

### Valid File
```xml
<?xml version="1.0"?>
<RiskParameters version="1.4">
  <Parameter type="TierP" value="0.15"/>
  <Parameter type="TierQ" value="0.20"/>
</RiskParameters>
```

### Invalid Format File
```xml
<?xml version="1.0"?>
<RiskParameters version="1.4">
  <Parameter type="TierP" value="0.15">
  <!-- Missing closing tag -->
</RiskParameters>
```

## Relationship Mapping
- **Requirement ID**: REQ-COMP-001
- **Skill ID**: SKILL-COMP-001
- **BDD Scenario ID**: FT-COMPLIANCE-001
- **BDD Feature File**: `tests/bdd/features/FT-COMPLIANCE-001.feature`

## Boundary Conditions
- **Max File Size**: 10MB
- **Supported Encoding**: UTF-8 only
- **Max Parameters**: 1000

## Exception Scenarios
1. **Empty File**: Rejected with "Empty file" error
2. **Wrong File Type**: Rejected with "Invalid file type" error
3. **Encoding Issues**: Rejected with "Encoding not supported" error

## Related Test Cases
- **Blocks**: TC-IM-CALC-001, TC-IM-CALC-002
- **Related To**: TC-COMPLIANCE-002, TC-COMPLIANCE-003

## Tags
- `@compliance`
- `@risk-parameter`
- `@validation`
- `@critical`
- `@positive`
- `@negative`

## Execution History
| Date | Executor | Environment | Result | Notes |
|------|----------|-------------|--------|-------|
| 2026-03-14 | System | DEV | Pending | Initial creation |

## Review Status
- **Status**: Draft
- **Confidence Level**: 5/5
