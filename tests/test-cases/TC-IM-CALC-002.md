# Test Case: TC-IM-CALC-002

## Basic Information
- **Test Case ID**: TC-IM-CALC-002
- **Title**: Calculate portfolio margin for Tier Q instruments
- **Module**: Initial Margin Calculation (IM-CALC)
- **Priority**: High
- **Test Type**: Positive
- **Automation Status**: Ready for Automation

## Rule Basis
- **MD File**: `docs/source-files/hkex-initial-margin-calculation-guide.md`
- **Paragraph ID**: `IO-INTRO-002`
- **Version**: v1.4
- **Rule Description**: VaR Platform calculates portfolio margin for Tier Q instruments with different risk parameters

## Global Process Node
- **Process Node**: VaR Platform Overview
- **Node ID**: NODE-001

## Test Scenario
Verify that VaR Platform can successfully calculate portfolio margin for Tier Q instruments using the appropriate risk parameter calculations.

## Preconditions
1. VaR Platform is operational and accessible
2. Risk Parameter File for Tier Q is available and valid
3. Tier Q instrument portfolio data is prepared
4. User has appropriate permissions

## Test Steps

| Step | Action | Expected Result | Test Data |
|------|--------|-----------------|-----------|
| 1 | Load Tier Q Risk Parameter File | File loaded successfully | Valid Tier Q Risk Parameter File |
| 2 | Input Tier Q instrument portfolio | Data accepted and validated | Sample Tier Q portfolio |
| 3 | Execute margin calculation | Calculation completes | N/A |
| 4 | Verify margin calculation | Correct margin value displayed | Expected Tier Q margin |

## Expected Results
- Portfolio margin calculated correctly for Tier Q instruments
- Calculation uses Tier Q specific risk parameters
- Result aligns with IO-INTRO-002 (v1.4)

## Test Data Requirements

### Input Data
```json
{
  "portfolio_type": "Tier Q",
  "instruments": [
    {
      "instrument_id": "INST-002",
      "instrument_type": "Option",
      "quantity": 50,
      "strike_price": 200.00
    }
  ],
  "risk_parameter_file": "risk_params_tier_q_20240314.xml"
}
```

## Relationship Mapping
- **Requirement ID**: REQ-002
- **Skill ID**: SKILL-001
- **BDD Scenario ID**: FT-IM-CALC-002
- **BDD Feature File**: `tests/bdd/features/FT-IM-CALC-002.feature`

## Tags
- `@im-calc`
- `@tier-q`
- `@positive`
- `@high-priority`

## Execution History
| Date | Executor | Environment | Result | Notes |
|------|----------|-------------|--------|-------|
| 2026-03-14 | System | DEV | Pending | Initial creation |

## Review Status
- **Status**: Draft
- **Confidence Level**: 4/5
