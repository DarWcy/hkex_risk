# Exception Handling - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 4. APPENDIX (4.1-4.7)

## Core Content

### 4. APPENDIX

#### 4.1 Detailed Calculation on Position Limit Add-on
- Position limit add-on assumes hypothetical conditions:
  - Apportioned liquid capital of CP = 75,000,000 (example)
  - Liquid capital multiplier = 4 (example)
  - Apportioned liquid capital cap = 280,000,000 (example)
  - Add-on% = 25% (example)
- Position limit add-on is calculated using formula:
  - Position limit add-on = If (NMV = 0, 0, Maximum {NMV – Minimum [(Apportioned liquid capital × liquid capital multiplier), Apportioned liquid capital cap], 0} / NMV × Round up(Portfolio margin + Flat rate margin + Corporate action position margin + Liquidation risk add-on + Structured product add-on, Rounding parameter) × If (Net margin after credit > 0, Add-on%, 1+ Add-on%))
- NMV = Net market value of the portfolio (absolute value in case of net short position)

#### 4.2 Guarantee Fund Risk Collateral
- Guarantee Fund Risk Collateral (default fund add-on) is the amount of Expected Uncollateralised Loss (EUL) of the CP group in excess of 50% of the Guarantee Fund threshold
- Not aggregated to total MTM and margin requirement
- Guarantee Fund risk collateral = Guarantee Fund expected uncollateralised loss – Guarantee Fund risk predefined limit
- Current Guarantee Fund risk pre-defined limit = HKD3,650,000,000

#### 4.3 Specific Stock / Cash Collateral Position Cover
- Positions covered by Specific Stock Collateral (SSC) or Specific Cash Collateral (SCC) are excluded from the MTM and margin requirement calculation
- SSC and SCC could only be arranged to cover positions prior to the settlement date (Current business date < Settlement date)
- Capped by the position quantity/position amount
- Any excess collateral is ignored

##### 4.3.1 Specific Stock Collateral for Short Position
- SSC are pledged in CCMS according to the corresponding settlement counter stock code and settlement date
- Position cover follows the same manner
- Different currency counters of a multi-counter eligible security share the same settlement counter stock code
- For half trading days, if both positions have quantity < 0, then the position with higher position average price is covered first
- If there are two positions, one with quantity > 0 while the other one with quantity < 0, only the one with quantity < 0 will undergo the position cover before cross-day position netting

##### 4.3.2 Specific Cash Collateral Position Cover
- SCC are arranged in CCMS according to the corresponding settlement counter stock code, currency and trade date
- Position cover follows the same manner
- Different currency counters of a multi-counter eligible security share the same settlement counter stock code

#### 4.4 Corporate Action Position Adjustment
- Position quantity adjustment for bonus share/stock split/stock consolidation
- Create benefit entitlement position for cash dividend
- Create benefit entitlement position for stock dividend
- Create benefit entitlement position for rights issue/open offer
- Combined effects on position adjustment for combination of corporate actions
- Position adjustment for stock conversion

#### 4.5 Cross-day Position Netting
- Process for netting positions across trading days

#### 4.6 Cross-currency Netting on MTM Requirement
- Process for netting MTM requirements across different currencies

#### 4.7 Intra-day MTM Requirement Calculation
- Intra-day MTM requirement calculation at 11:00 a.m. HKT
- Intra-day MTM requirement calculation at 2:00 p.m. HKT

## Applicable Scenarios
- Exception handling for margin calculation systems
- Edge case validation for margin calculations
- Special scenario processing (corporate actions, collateral management)
- Boundary condition testing for margin calculations
- Error handling and exception scenarios

## Global Process Nodes
- Exception Scenario Identification
- Special Case Processing
- Edge Case Handling
- Exception Resolution

## Testing Considerations
- Verify that all exception scenarios are accurately documented
- Test position limit add-on calculation with various input conditions
- Validate guarantee fund risk collateral calculation logic
- Test specific stock collateral position cover logic (including half trading days)
- Test specific cash collateral position cover logic
- Verify corporate action position adjustment logic for all action types
- Test cross-day position netting process
- Validate cross-currency netting on MTM requirement
- Test intra-day MTM requirement calculation at different times
- Ensure that all edge cases and boundary conditions are covered
- Verify that exception handling logic is correct and complete

## Structured ID
- EH-POS-001: Position Limit Add-on Calculation
- EH-POS-002: Guarantee Fund Risk Collateral
- EH-POS-003: Specific Stock Collateral Position Cover
- EH-POS-004: Specific Cash Collateral Position Cover
- EH-CORP-001: Corporate Action Position Adjustment
- EH-CROSS-001: Cross-day Position Netting
- EH-CROSS-002: Cross-currency Netting
- EH-INTRAD-001: Intra-day MTM Requirement Calculation