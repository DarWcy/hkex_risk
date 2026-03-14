# Examples - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
Automation Tester + QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.2.4, 3.2.5, 4.1

## Core Content

### Example 1: Portfolio Margin Calculation

#### Input Data
- Portfolio consists of 5 instruments (non-IPO related)
- Instrument 1: 700 (Tencent Holdings), Quantity: -1,000,000, Market value: -384,000,000
- Instrument 2: 9988 (Alibaba Group), Quantity: 500,000, Market value: 250,000,000
- Instrument 3: 939 (China Construction Bank), Quantity: -2,000,000, Market value: -600,000,000
- Instrument 4: 1398 (ICBC), Quantity: 1,500,000, Market value: 450,000,000
- Instrument 5: 2318 (Ping An Insurance), Quantity: -800,000, Market value: -320,000,000

#### Step-by-Step Calculation

**Step 1: Calculate HVaR Component**
- Retrieve HVaR scenario returns (FieldType 1) for each instrument
- Calculate scenario P&L for each scenario: P&L = Σ(Position market value × Scenario return)
- Sort scenario P&L in ascending order (worst to best)
- Select worst 6 scenarios
- HVaR component = Average of worst 6 scenario P&L
- Example: HVaR component = -45,000,000 (average of worst 6 scenarios)

**Step 2: Calculate SVaR Component**
- Retrieve SVaR scenario returns (FieldType 2) for each instrument
- Calculate scenario P&L for each scenario: P&L = Σ(Position market value × Scenario return)
- Sort scenario P&L in ascending order (worst to best)
- Select worst 21 scenarios
- SVaR component = Average of worst 21 scenario P&L
- Example: SVaR component = -60,000,000 (average of worst 21 scenarios)

**Step 3: Calculate Portfolio Margin Floor**
- Gross long market value = 250,000,000 + 450,000,000 = 700,000,000
- Gross short market value = |-384,000,000| + |-600,000,000| + |-320,000,000| = 1,304,000,000
- Portfolio margin floor base = Max(700,000,000, 1,304,000,000) = 1,304,000,000
- Portfolio margin floor rate = 2.5%
- Portfolio margin floor = 1,304,000,000 × 2.5% = 32,600,000

**Step 4: Calculate Portfolio Margin**
- HVaR_WGT = 0.75, SVaR_WGT = 0.25
- Weighted average = |-45,000,000| × 0.75 + |-60,000,000| × 0.25 = 48,750,000
- Portfolio margin = Max(48,750,000, 32,600,000) = 48,750,000

#### Expected Result
Portfolio margin = 48,750,000

### Example 2: Margin Adjustment Process

#### Input Data
- Aggregated market-risk-component margin = 48,750,000
- Market value of portfolio = -604,000,000
- Contract value of portfolio = -700,000,000
- Margin credit = 5,000,000
- Rounding parameter = 10,000

#### Step-by-Step Calculation

**Step 1: Rounding on Aggregated Margin**
- Aggregated margin = 48,750,000
- Rounded margin = Round up(48,750,000, 10,000) = 48,800,000

**Step 2: Calculate Favorable MTM**
- Favorable MTM = Market value – Contract value
- Favorable MTM = -604,000,000 - (-700,000,000) = 96,000,000
- Since result is positive, it refers to favorable MTM

**Step 3: Apply Favorable MTM**
- Net margin = Max(0, Rounded aggregated margin – Favorable MTM)
- Net margin = Max(0, 48,800,000 – 96,000,000) = 0

**Step 4: Apply Margin Credit**
- Net margin after credit = Max(0, Net margin – Margin credit)
- Net margin after credit = Max(0, 0 – 5,000,000) = 0

#### Expected Result
Net margin after credit = 0

### Example 3: Liquidation Risk Add-on Calculation

#### Input Data
- Instrument 1: 700 (Tencent Holdings), Quantity: -1,000,000, Market value: -384,000,000
- Instrument 2: 700C (Tencent Call Option), Quantity: 500,000, Market value: 50,000,000
- Delta for 700C: 0.5
- Underlying group: 700
- Bucket rates: 20% for first 100M, 30% for next 200M, 40% for above 300M
- Thresholds: 100M, 300M

#### Step-by-Step Calculation

**Step 1: Calculate Delta-Equivalent Position Market Values**
- Delta-equivalent market value for 700 = |-384,000,000| × 1.0 = 384,000,000
- Delta-equivalent market value for 700C = |50,000,000| × 0.5 = 25,000,000
- Total delta-equivalent market value = 384,000,000 + 25,000,000 = 409,000,000

**Step 2: Calculate Instrument-level LRA**
- Portion ≤ 100M: 100,000,000 × 20% = 20,000,000
- Portion 100M-300M: 200,000,000 × 30% = 60,000,000
- Portion > 300M: 109,000,000 × 40% = 43,600,000
- Instrument-level LRA = 20,000,000 + 60,000,000 + 43,600,000 = 123,600,000

#### Expected Result
Instrument-level LRA = 123,600,000

### Example 4: Holiday Add-on Calculation

#### Input Data
- Portfolio margin = 48,750,000
- Flat rate margin = 15,000,000
- Number of consecutive Hong Kong holidays (H) = 4 (excluding Saturdays and Sundays)

#### Step-by-Step Calculation

**Step 1: Calculate Holiday Add-on Base**
- Holiday add-on base = Portfolio margin + Flat rate margin
- Holiday add-on base = 48,750,000 + 15,000,000 = 63,750,000

**Step 2: Calculate Holiday Factor**
- Holiday_Factor = sqrt(H) - 1
- Holiday_Factor = sqrt(4) - 1 = 2 - 1 = 1

**Step 3: Calculate Holiday Add-on**
- Holiday add-on = Holiday add-on base × Holiday_Factor
- Holiday add-on = 63,750,000 × 1 = 63,750,000

#### Expected Result
Holiday add-on = 63,750,000

### Example 5: Total MTM and Margin Requirement Calculation

#### Input Data
- Net margin after credit = 0
- MTM requirement = 5,000,000
- Position limit add-on = 2,000,000
- Credit risk add-on = 0
- Ad-hoc add-on = 0

#### Step-by-Step Calculation

**Step 1: Sum All Components**
- Total MTM and margin requirement = Net margin after credit + MTM requirement + Position limit add-on + Credit risk add-on + Ad-hoc add-on
- Total MTM and margin requirement = 0 + 5,000,000 + 2,000,000 + 0 + 0 = 7,000,000

#### Expected Result
Total MTM and margin requirement = 7,000,000

## Applicable Scenarios
- Test case design for margin calculation systems
- Result verification for margin calculations
- Step-by-step calculation validation
- Regression testing for margin calculation systems
- User training and documentation

## Global Process Nodes
- Calculation Example Execution
- Result Verification
- Test Case Validation
- Regression Testing

## Testing Considerations
- Verify that all calculation steps are accurately documented
- Test that intermediate results are correctly calculated
- Validate that final results match expected values
- Ensure that examples cover various scenarios and edge cases
- Test that examples are traceable to business rules
- Verify that examples are comprehensive and representative
- Ensure that examples can be used for regression testing

## Structured ID
- EX-PORT-001: Portfolio Margin Calculation Example
- EX-ADJ-001: Margin Adjustment Process Example
- EX-LRA-001: Liquidation Risk Add-on Calculation Example
- EX-HOLI-001: Holiday Add-on Calculation Example
- EX-TOTAL-001: Total MTM and Margin Requirement Calculation Example