# Test Case: TC-IM-CALC-001

## Basic Information
- **Test Case ID**: TC-IM-CALC-001
- **Title**: Calculate portfolio margin for Tier P instruments
- **Module**: Initial Margin Calculation (IM-CALC)
- **Priority**: High
- **Test Type**: Positive
- **Automation Status**: Ready for Automation

## Rule Basis
- **MD File**: `docs/source-files/hkex-initial-margin-calculation-guide.md`
- **Paragraph ID**: `IO-INTRO-001`
- **Version**: v1.4
- **Rule Description**: VaR Platform calculates portfolio margin for Tier P instruments based on Risk Parameter File

## Global Process Node
- **Process Node**: VaR Platform Overview
- **Node ID**: NODE-001

## Test Scenario
Verify that VaR Platform can successfully calculate portfolio margin for Tier P instruments when valid Risk Parameter File and portfolio data are provided.

## Preconditions
1. VaR Platform is operational and accessible
2. Risk Parameter File is available and valid
3. Tier P instrument portfolio data is prepared and ready for loading
4. User has appropriate permissions to perform margin calculations

## Test Steps

| Step | Action | Expected Result | Test Data |
|------|--------|-----------------|-----------|
| 1 | Load Risk Parameter File into VaR Platform | File is successfully loaded without errors | Valid Risk Parameter File for Tier P |
| 2 | Input Tier P instrument portfolio data | Portfolio data is accepted and validated | Sample Tier P portfolio data |
| 3 | Execute portfolio margin calculation | Calculation completes successfully | N/A |
| 4 | Verify calculated margin value | Margin value is calculated and displayed correctly | Expected margin value based on input |

## Expected Results
- **Primary**: Portfolio margin is successfully calculated for Tier P instruments
- **Secondary**: Calculation result aligns with IO-INTRO-001 (v1.4) requirements
- **Tertiary**: Calculation performance meets acceptable time thresholds

## Test Data Requirements

### Input Data
```json
{
  "portfolio_type": "Tier P",
  "instruments": [
    {
      "instrument_id": "INST-001",
      "instrument_type": "Future",
      "quantity": 100,
      "price": 250.50
    }
  ],
  "risk_parameter_file": "risk_params_tier_p_20240314.xml"
}
```

### Expected Output
```json
{
  "calculation_status": "SUCCESS",
  "portfolio_margin": 12525.00,
  "currency": "HKD",
  "calculation_basis": "IO-INTRO-001",
  "rule_version": "v1.4"
}
```

## Relationship Mapping

### References
- **Requirement ID**: REQ-001
- **Skill ID**: SKILL-001 (VaR Platform Overview Skill)
- **BDD Scenario ID**: FT-IM-CALC-001
- **BDD Feature File**: `tests/bdd/features/FT-IM-CALC-001.feature`

### Reference Verification Slot
- **Skill Reference**: `hkex-intro-overview`
- **Verify**: Test_Reference matches BDD Scenario ID
- **Status**: To be verified during execution

## Boundary Conditions
- **Minimum Portfolio Size**: 1 instrument
- **Maximum Portfolio Size**: 10,000 instruments
- **Valid Currency**: HKD only
- **Valid Instrument Types**: Futures, Options (Tier P eligible)

## Exception Scenarios
1. **Invalid Risk Parameter File**: System should reject and display appropriate error
2. **Empty Portfolio**: System should handle gracefully with warning message
3. **Network Timeout**: System should retry or fail with timeout error

## Related Test Cases
- **Related To**: TC-IM-CALC-002 (Tier Q instruments)
- **Depends On**: TC-COMPLIANCE-001 (Risk Parameter validation)
- **Blocks**: TC-IM-CALC-003 (Margin reporting)

## Execution History

| Date | Executor | Environment | Result | Notes |
|------|----------|-------------|--------|-------|
| 2026-03-14 | System | DEV | Pending | Initial creation |

## Review Status
- **Review ID**: REV-TC-20260314-001
- **Reviewer**: Pending
- **Status**: Draft
- **Confidence Level**: 4/5

## Update Tracking
- **Created**: 2026-03-14
- **Last Updated**: 2026-03-14
- **Updated By**: System
- **Change Description**: Initial creation based on IO-INTRO-001

## Tags
- `@im-calc`
- `@tier-p`
- `@positive`
- `@high-priority`
- `@automatable`

## Notes
- This test case aligns with BDD scenario FT-IM-CALC-001
- Reference verification required during execution
- Ensure Risk Parameter File version matches v1.4
