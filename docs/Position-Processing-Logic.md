# Validation Rules - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.2.2.3, 3.2.7

## Core Content

### 3.2.3 Identify Margin Adjustments and Other Risk Components

#### Margin Adjustment Rules
- Position limit add-on applies to all Hong Kong market instruments
- Credit risk add-on and ad-hoc add-on are not applicable to any instruments from the Initial Margin Risk Parameter File
- Users shall refer to the add-on amounts directly from the MTM and Margin Requirement Report
- Margin adjustments are applied on a portfolio basis:
  - Rounding on aggregated market-risk-component margin
  - Consideration on favorable MTM
  - Application of margin credit

#### Margin Adjustment Validation
- Verify that position limit add-on is correctly applied to all Hong Kong market instruments
- Ensure that credit risk add-on and ad-hoc add-on are only retrieved from report, not calculated from risk parameters
- Validate that margin adjustments are applied at portfolio level, not instrument level
- Confirm that rounding is performed correctly according to rounding parameter
- Verify that favorable MTM consideration is correctly applied
- Ensure that margin credit is correctly applied (maximum with zero floor)

### 3.2.7 Summary of Market Risk Components with Margin Adjustments and Other Risk Components

#### Component Summary Validation
- Verify that all market risk components are correctly summarized:
  - Portfolio margin
  - Flat rate margin
  - Liquidation risk add-on
  - Structured product add-on
  - Corporate action position margin
  - Holiday add-on
  - Aggregated market-risk-component margin
- Ensure that all margin adjustments are correctly summarized:
  - Net margin after credit
- Verify that all other risk components are correctly summarized:
  - MTM requirement
  - Position limit add-on
  - Credit risk add-on
  - Ad-hoc add-on

#### Component Relationship Validation
- Ensure that aggregated market-risk-component margin = Sum of all market risk components
- Verify that net margin after credit is correctly calculated from aggregated margin after adjustments
- Confirm that total MTM and margin requirement = Net margin after credit + Sum of other risk components

## Applicable Scenarios
- Data validation for margin calculation systems
- Business rule verification for margin calculations
- Compliance checking for margin calculations
- Quality assurance for margin calculation outputs
- Regulatory compliance validation

## Global Process Nodes
- Margin Adjustment Validation
- Risk Component Verification
- Component Summary Validation
- Regulatory Compliance Check

## Testing Considerations
- Verify that all validation rules are accurately documented
- Test margin adjustment rules with various input conditions
- Validate component summary calculations
- Test component relationship validation logic
- Ensure that all edge cases are covered in validation rules
- Verify that validation rules are complete and comprehensive
- Test that validation rules correctly identify calculation errors
- Ensure that validation rules support regulatory compliance checking
- Validate that validation rules are testable and measurable

## Structured ID
- VR-ADJ-001: Margin Adjustment Rules
- VR-ADJ-002: Margin Adjustment Validation
- VR-SUM-001: Component Summary Validation
- VR-SUM-002: Component Relationship Validation