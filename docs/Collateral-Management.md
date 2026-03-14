# Testing Considerations - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
Automation Tester

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: All sections (comprehensive testing guidance)

## Core Content

### Test Data Requirements

#### Position Data Testing
- **Valid position quantities**: Test with positive (long) and negative (short) quantities
- **Contract value testing**: Test with positive (receivable) and negative (payable) contract values
- **Market value testing**: Test with various market values and price scenarios
- **Multi-currency positions**: Test with non-HKD denominated instruments and FX conversion
- **Corporate action positions**: Test with DSP, DIV, SRI instrument codes
- **Multi-counter eligible securities**: Test positions that need to be combined into settlement counters

#### Risk Parameter Testing
- **HVaR scenarios**: Test with various scenario returns and confidence levels
- **SVaR scenarios**: Test with various scenario returns and confidence levels
- **Flat rate scenarios**: Test with different flat margin rates and multipliers
- **FieldType testing**: Test each FieldType (1-7) with appropriate instruments
- **Parameter validation**: Test with various parameter values (weights, counts, confidence levels, rounding factors)

#### Calculation Testing
- **Portfolio margin**: Test with IPO and non-IPO instrument grouping
- **Margin floor testing**: Test with various portfolio margin floor rates and base calculations
- **Flat rate margin**: Test with different sub-margin groups and multipliers
- **Liquidation risk add-on**: Test with various delta-equivalent positions, thresholds, and bucket rates
- **Structured product add-on**: Test with instruments below/above price thresholds and long/short positions
- **Corporate action margin**: Test with positive/negative net market values and various scenario rates
- **Holiday add-on**: Test with various holiday factors and base calculations

### Boundary Condition Testing

#### Value Boundaries
- **Zero values**: Test with zero positions, zero market values, zero contract values
- **Maximum values**: Test with extreme position quantities and market values
- **Threshold boundaries**: Test at exact threshold values for liquidation risk add-on and structured product add-on
- **Confidence level boundaries**: Test at exact confidence level boundaries (99.4%, 98%)

#### Scenario Boundaries
- **Worst case scenarios**: Test with worst 6 scenarios for HVaR and worst 21 scenarios for SVaR
- **IPO vs non-IPO**: Test with instruments in both categories
- **Corporate action vs non-corporate action**: Test with instruments in both categories
- **Holiday add-on applicability**: Test with instruments that do/do not have FieldType 7

#### Temporal Boundaries
- **Settlement date boundaries**: Test with positions on, before, and after settlement dates
- **Business date boundaries**: Test with positions on current business date vs previous dates
- **Dissemination time boundaries**: Test data availability at various dissemination times (11:45 a.m., 5:00 p.m., 9:00 p.m.)

### Expected Results Testing

#### Calculation Accuracy
- **HVaR calculation**: Verify that average of worst 6 scenarios is correctly calculated
- **SVaR calculation**: Verify that average of worst 21 scenarios is correctly calculated
- **Portfolio margin floor**: Verify that maximum of weighted average and floor is correctly applied
- **Margin rounding**: Verify that rounding up to nearest rounding parameter is correctly applied
- **Total margin calculation**: Verify that all components are correctly aggregated

#### Data Integrity Testing
- **Position data consistency**: Verify that position data is consistent across different reports
- **FX conversion accuracy**: Verify that non-HKD instruments are correctly converted
- **Collateral exclusion**: Verify that covered positions are correctly excluded
- **Corporate action adjustment**: Verify that positions are correctly adjusted for corporate actions
- **Cross-day netting**: Verify that positions are correctly netted across trading days

### Integration Testing

#### System Integration
- **Data exchange**: Test data exchange between IMRPF, position reports, and margin calculation systems
- **Report generation**: Test generation of MTM and Margin Requirement Report
- **Real-time updates**: Test that system handles real-time data updates correctly

#### End-to-End Testing
- **Complete margin calculation**: Test entire process from position data to final margin requirement
- **Regression testing**: Test that changes to risk parameters or positions produce correct results
- **Performance testing**: Test system performance with large portfolios and complex scenarios

## Applicable Scenarios
- Test case design for margin calculation systems
- Boundary condition testing for margin calculations
- Integration testing for margin calculation systems
- Regression testing for margin calculation systems
- Performance testing for margin calculation systems

## Global Process Nodes
- Test Data Preparation
- Test Case Design
- Test Execution
- Result Verification
- Regression Testing

## Testing Considerations
- Ensure that all test data requirements are comprehensive and cover various scenarios
- Verify that boundary conditions are thoroughly tested
- Test that expected results are accurately calculated
- Validate that data integrity is maintained throughout the process
- Ensure that integration points are properly tested
- Test that system performance meets requirements
- Verify that all edge cases and special scenarios are covered
- Ensure that test cases are traceable to business rules

## Structured ID
- TC-DATA-001: Position Data Testing
- TC-DATA-002: Risk Parameter Testing
- TC-DATA-003: Calculation Testing
- TC-BOUND-001: Value Boundaries
- TC-BOUND-002: Scenario Boundaries
- TC-BOUND-003: Temporal Boundaries
- TC-RES-001: Calculation Accuracy
- TC-RES-002: Data Integrity Testing
- TC-INT-001: System Integration
- TC-INT-002: End-to-End Testing