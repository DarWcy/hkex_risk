# Core Calculation Logic - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
BA + QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.2.4 Calculate Market Risk Components, 3.2.5 Aggregate Market Risk Components and Perform Margin Adjustments

## Core Content

### 3.2.4 Calculate Market Risk Components

#### 3.2.4.1 Portfolio Margin
- Portfolio margin is the weighted average of HVaR and SVaR components, subject to portfolio margin floor
- For calculation, treat each IPO stock and its relevant structured product(s) as an individual portfolio
- Group other non-IPO related instruments together as another separate portfolio

##### 3.2.4.1.1 Historical Value-at-Risk Component (HVaR)
- HVaR is calculated using scenario returns under FieldType 1
- HVaR component is the average of the worst 6 scenarios (99.4% confidence level)
- HVaR_Measure parameter indicates ES (Discrete) risk measure
- HVaR_CL parameter indicates 99.4% confidence level
- HVaR_WGT parameter indicates weighting (0.75 in example)

##### 3.2.4.1.2 Stress Value-at-Risk Component (SVaR)
- SVaR is calculated using scenario returns under FieldType 2
- SVaR component is the average of the worst 21 scenarios (98% confidence level)
- SVaR_Measure parameter indicates ES (Discrete) risk measure
- SVaR_CL parameter indicates 98% confidence level
- SVaR_WGT parameter indicates weighting (0.25 in example)

##### 3.2.4.1.3 Portfolio Margin Floor
- Portfolio margin floor is the product of portfolio margin floor base and portfolio margin floor rate
- Portfolio margin floor base is the higher of gross long and short market value of positions
- Portfolio margin floor rate is available at HKEX website (2.5% in example)
- Portfolio margin = Maximum [Sum of (HVaR × HVaR_WGT + SVaR × SVaR_WGT), Portfolio margin floor]

#### 3.2.4.2 Flat Rate Margin
- Flat rate margin is calculated for instruments identified under FieldType 3
- Aggregate absolute market value of long positions and short positions separately
- Compare total absolute market value of long positions and short positions separately for each sub-margin group
- Take higher of long and short absolute market value for each sub-margin group
- Sum the product of absolute position market value and the flat margin rate under FieldType 3
- Apply flat rate margin multiplier by referring to "Daily Participant Margin Multiplier Report" (DWH0081C)

#### 3.2.4.3 Liquidation Risk Add-on (LRA)
- LRA consists of two components: Instrument-level LRA and Portfolio-level LRA

##### 3.2.4.3.1 Instrument-level LRA
- Calculate delta-equivalent position market values for each underlying group
- Find underlying group by referring to the first column on the right of FieldType 5
- If only holding stock without corresponding structured product, calculate market value using FieldType 4
- Calculate instrument-level LRA based on bucket rates and portion of delta-equivalent position market value exceeding thresholds

##### 3.2.4.3.2 Portfolio-level LRA
- Calculate market values of beta hedge positions for each underlying group
- Calculate portfolio-level LRA with portfolio hedging instrument (Tracker Fund of Hong Kong 2800.HK)
- Portfolio-level LRA = Maximum [0, Absolute value of (Total market value of beta hedge position) – Hedging market value threshold] × Hedging instrument bucket rate

#### 3.2.4.4 Structured Product Add-on
- Includes structured products with instrument market prices smaller than price thresholds (FieldType 6)
- Only applies to instruments under long positions
- Calculate using: Quantity × Tick size multiplier × Minimum tick size
- Tick size multiplier = 10 × value under Column 2 of FieldType 6
- Minimum tick size is currently set as 0.001

#### 3.2.4.5 Corporate Action Position Margin
- Calculate net market value of positions for each scenario under FieldType 7
- Apply positive net market value positions to scenario 4 under FieldType 7
- Apply negative net market value positions to scenario 3 under FieldType 7
- Add the results obtained from scenarios 3 and 4
- Corporate Action Position Margin = Absolute value of (net market value × scenario)

#### 3.2.4.6 Holiday Add-on
- Only includes positions subject to portfolio margin or flat rate margin
- Calculate base by adding portfolio margin to flat rate margin
- Calculate holiday add-on by multiplying base by Holiday_Factor parameter
- Holiday_Factor = square root(H) – 1, where H is the number of consecutive Hong Kong holidays excluding Saturdays and Sundays

### 3.2.5 Aggregate Market Risk Components and Perform Margin Adjustments

#### 3.2.5.1 Rounding on Aggregated Market-risk-component Margin
- Calculate aggregated margin = Portfolio margin + Flat rate margin + Liquidation risk add-on + Structured product add-on + Corporate action position margin + Holiday add-on
- Round up the aggregated margin with reference to the rounding parameter (e.g., 10,000)

#### 3.2.5.2 Consideration on Favorable MTM
- Calculate favorable MTM (or MTM requirement) = Market valuePortfolio – Contract valuePortfolio
- If result is negative, it refers to MTM requirement (absolute value will be added after applying margin credit)
- If result is positive, it refers to favorable MTM
- Net margin = Maximum(0, Rounded aggregated market-risk-component margin – Favorable MTM)

#### 3.2.5.3 Application of Margin Credit
- Margin credit (normally 5,000,000) is granted to each CP
- Net margin after credit = Maximum [0,(Net margin – Margin credit)]
- Margin credit may be reduced for risk management purpose

## Applicable Scenarios
- Core margin calculation logic understanding
- Portfolio margin calculation implementation
- Risk component calculation verification
- Margin adjustment process validation
- Business rule verification for margin calculations

## Global Process Nodes
- Market Risk Component Calculation
- Margin Adjustment Processing
- Portfolio Margin Calculation
- Risk Component Aggregation

## Testing Considerations
- Verify that all calculation formulas are accurately represented
- Test portfolio margin calculation with IPO and non-IPO instrument grouping
- Validate HVaR and SVaR calculation logic (worst scenarios averaging)
- Test portfolio margin floor calculation (base × rate)
- Verify flat rate margin calculation for each sub-margin group
- Validate liquidation risk add-on calculation (instrument-level and portfolio-level)
- Test structured product add-on calculation logic
- Verify corporate action position margin calculation
- Validate holiday add-on calculation
- Test margin adjustment logic (rounding, favorable MTM, margin credit)
- Ensure all parameter references are correct and traceable

## Structured ID
- CL-PORT-001: Portfolio Margin Overview
- CL-PORT-002: HVaR Calculation
- CL-PORT-003: SVaR Calculation
- CL-PORT-004: Portfolio Margin Floor
- CL-FLAT-001: Flat Rate Margin Calculation
- CL-LRA-001: Liquidation Risk Add-on Overview
- CL-LRA-002: Instrument-level LRA
- CL-LRA-003: Portfolio-level LRA
- CL-STR-001: Structured Product Add-on
- CL-CORP-001: Corporate Action Position Margin
- CL-HOLI-001: Holiday Add-on
- CL-ADJ-001: Margin Rounding
- CL-ADJ-002: Favorable MTM Consideration
- CL-ADJ-003: Margin Credit Application