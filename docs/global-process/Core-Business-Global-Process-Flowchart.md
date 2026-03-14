# Core Business Global Process Flowchart - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
BA + QA Lead + Automation Tester

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.2 Calculation Process

## Core Business Global Process Flowchart

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CORE BUSINESS GLOBAL PROCESS                         │
│                    INITIAL MARGIN CALCULATION PROCESS                      │
└─────────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────────┐
│ 1. DATA COLLECTION AND PREPARATION                                          │
├─────────────────────────────────────────────────────────────────────────────┤
│ • 9:00 p.m. HKT: Initial Margin Risk Parameter File (IMRPF) dissemination  │
│   - Global parameters (HVaR_WGT, SVaR_WGT, HVaR_Scen_Count, etc.)           │
│   - FieldType 1: HVaR Scenarios                                             │
│   - FieldType 2: SVaR Scenarios                                             │
│   - FieldType 3: Flat Rate Scenarios                                        │
│   - FieldType 4: Beta hedge information                                     │
│   - FieldType 5: Instrument delta information                               │
│   - FieldType 6: Price threshold and add-on%                                │
│   - FieldType 7: Corporate action position margin scenarios                │
│                                                                             │
│ • 11:45 a.m., 5:00 p.m., 9:00 p.m. HKT: Marginable Position Report (RMAMP01)│
│   - InstrumentID, Quantity, Contract value, Market value                    │
│                                                                             │
│ • Position Data Processing:                                                 │
│   - FX conversion for non-HKD instruments                                   │
│   - Specific stock/cash collateral cover exclusion                           │
│   - Multi-counter eligible securities combination                           │
│   - Corporate action position adjustment                                    │
│   - Cross-day position netting                                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│ 2. MARKET RISK COMPONENT IDENTIFICATION                                     │
├─────────────────────────────────────────────────────────────────────────────┤
│ • For each instrument in portfolio:                                         │
│   - Identify applicable FieldType(s) from IMRPF                            │
│   - Map instrument codes to InstrumentID in IMRPF                           │
│   - Decompose corporate action entitled instruments (FieldType 7)          │
│                                                                             │
│ • Identify holiday add-on applicability:                                    │
│   - Apply to all instruments except those with FieldType 7                 │
│                                                                             │
│ • Identify margin adjustments:                                             │
│   - Rounding on aggregated market-risk-component margin                     │
│   - Consideration on favorable MTM                                          │
│   - Application of margin credit                                             │
│                                                                             │
│ • Identify other risk components:                                          │
│   - MTM requirement (calculated or retrieved)                               │
│   - Position limit add-on (from report)                                     │
│   - Credit risk add-on (from report, if applicable)                         │
│   - Ad-hoc add-on (from report, if applicable)                              │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│ 3. MARKET RISK COMPONENT CALCULATION                                         │
├─────────────────────────────────────────────────────────────────────────────┤
│ 3.1 Portfolio Margin Calculation                                            │
│   • Group instruments: IPO stocks + structured products, others            │
│   • HVaR Component: Average of worst 6 scenarios (99.4% confidence)         │
│   • SVaR Component: Average of worst 21 scenarios (98% confidence)         │
│   • Portfolio Margin Floor: Max(gross long MV, gross short MV) × floor rate│
│   • Portfolio Margin: Max(HVaR×HVaR_WGT + SVaR×SVaR_WGT, Portfolio floor)  │
│                                                                             │
│ 3.2 Flat Rate Margin Calculation                                            │
│   • Aggregate absolute market value by sub-margin group                    │
│   • Take higher of long and short for each group                            │
│   • Apply flat margin rate (FieldType 3)                                    │
│   • Apply flat rate margin multiplier (DWH0081C)                            │
│                                                                             │
│ 3.3 Liquidation Risk Add-on (LRA) Calculation                               │
│   • Instrument-level LRA:                                                   │
│     - Calculate delta-equivalent position market values                     │
│     - Apply bucket rates and thresholds (FieldType 5)                       │
│   • Portfolio-level LRA:                                                     │
│     - Calculate beta hedge position market values                           │
│     - Apply hedging instrument bucket rate (FieldType 5)                    │
│   • Total LRA = Instrument-level LRA + Portfolio-level LRA                  │
│                                                                             │
│ 3.4 Structured Product Add-on Calculation                                   │
│   • Only for long positions with price < threshold (FieldType 6)           │
│   • Calculation: Quantity × Tick size multiplier × Minimum tick size       │
│                                                                             │
│ 3.5 Corporate Action Position Margin Calculation                             │
│   • Apply positive net market value to scenario 4 (FieldType 7)            │
│   • Apply negative net market value to scenario 3 (FieldType 7)            │
│   • Add results from scenarios 3 and 4                                      │
│                                                                             │
│ 3.6 Holiday Add-on Calculation                                              │
│   • Base = Portfolio margin + Flat rate margin                              │
│   • Holiday_Factor = sqrt(H) - 1 (H = consecutive HK holidays)              │
│   • Holiday add-on = Base × Holiday_Factor                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│ 4. MARGIN ADJUSTMENT PROCESS                                                 │
├─────────────────────────────────────────────────────────────────────────────┤
│ 4.1 Aggregation                                                              │
│   • Aggregated margin = Portfolio margin + Flat rate margin +              │
│     Liquidation risk add-on + Structured product add-on +                    │
│     Corporate action position margin + Holiday add-on                       │
│                                                                             │
│ 4.2 Rounding                                                                 │
│   • Rounded margin = Round up(Aggregated margin, Rounding parameter)        │
│                                                                             │
│ 4.3 Favorable MTM Consideration                                             │
│   • Favorable MTM = Market valuePortfolio – Contract valuePortfolio         │
│   • Net margin = Max(0, Rounded margin – Favorable MTM)                     │
│                                                                             │
│ 4.4 Margin Credit Application                                                │
│   • Net margin after credit = Max(0, Net margin – Margin credit)             │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│ 5. TOTAL MTM AND MARGIN REQUIREMENT CALCULATION                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ • Total MTM and margin requirement =                                         │
│   Net margin after credit +                                                  │
│   MTM requirement +                                                          │
│   Position limit add-on +                                                    │
│   Credit risk add-on +                                                       │
│   Ad-hoc add-on                                                              │
│                                                                             │
│ • Generate MTM and Margin Requirement Report                                │
│   - Disseminate to CPs via Report Access Platform (RAP)                      │
└─────────────────────────────────────────────────────────────────────────────┘
                                    ↓
┌─────────────────────────────────────────────────────────────────────────────┐
│ 6. EXCEPTION HANDLING AND SPECIAL SCENARIOS                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 6.1 Position Limit Add-on                                                    │
│   • Calculate based on apportioned liquid capital and liquid capital cap   │
│   • Apply add-on% to rounded margin                                          │
│                                                                             │
│ 6.2 Guarantee Fund Risk Collateral                                           │
│   • Calculate Expected Uncollateralised Loss (EUL)                          │
│   • Guarantee Fund risk collateral = EUL – Pre-defined limit                │
│                                                                             │
│ 6.3 Specific Stock/Cash Collateral Position Cover                            │
│   • Exclude covered positions from calculation                               │
│   • Apply to positions prior to settlement date                              │
│                                                                             │
│ 6.4 Corporate Action Position Adjustment                                      │
│   • Bonus share/stock split/stock consolidation                              │
│   • Cash dividend/stock dividend/rights issue/open offer                     │
│   • Stock conversion                                                         │
│                                                                             │
│ 6.5 Cross-day Position Netting                                               │
│   • Net positions across trading days                                        │
│                                                                             │
│ 6.6 Cross-currency Netting on MTM Requirement                               │
│   • Net MTM requirements across different currencies                         │
│                                                                             │
│ 6.7 Intra-day MTM Requirement Calculation                                    │
│   • 11:00 a.m. HKT calculation                                               │
│   • 2:00 p.m. HKT calculation                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Module Mapping

| Process Step | Related Module | Module File |
|--------------|----------------|-------------|
| 1. Data Collection and Preparation | Risk Parameter File Specification | Risk-Parameter-File-Specification.md |
| 2. Market Risk Component Identification | Market Risk Component Calculation | Market-Risk-Component-Calculation.md |
| 3. Market Risk Component Calculation | Market Risk Component Calculation | Market-Risk-Component-Calculation.md |
| 4. Margin Adjustment Process | Margin Adjustment Process | Margin-Adjustment-Process.md |
| 5. Total MTM and Margin Requirement Calculation | Calculation Examples | Calculation-Examples.md |
| 6. Exception Handling and Special Scenarios | Other Risk Components | Other-Risk-Components.md |

## Process Flow Relationships

### Primary Flow
1. Data Collection → Risk Component Identification → Risk Component Calculation → Margin Adjustment → Total Margin Calculation

### Supporting Processes
- Exception Handling: Parallel to main flow, handles special scenarios
- Validation Rules: Applies throughout all process steps
- System Integration: Interfaces with data sources and report generation

### Decision Points
- Holiday add-on applicability (FieldType 7 check)
- Portfolio margin floor application (floor vs weighted average)
- Favorable MTM consideration (positive vs negative)
- Margin credit application (net margin vs credit amount)

### Key Dependencies
- IMRPF availability (9:00 p.m. HKT)
- Marginable Position Report availability (11:45 a.m., 5:00 p.m., 9:00 p.m. HKT)
- FX rates for currency conversion
- Corporate action data for position adjustment
- Holiday calendar for holiday add-on calculation

## Applicable Scenarios
- End-to-end margin calculation process
- Business process understanding for BA
- System integration testing for Automation Tester
- Validation rule verification for QA Lead
- Exception scenario handling
- Process flow optimization

## Global Process Nodes
- Data Collection and Preparation
- Market Risk Component Identification
- Market Risk Component Calculation
- Margin Adjustment Process
- Total MTM and Margin Requirement Calculation
- Exception Handling and Special Scenarios

## Testing Considerations
- Verify that all process steps are accurately documented
- Test process flow with various input scenarios
- Validate that decision points are correctly implemented
- Ensure that process dependencies are correctly identified
- Test that exception handling is properly integrated
- Verify that process outputs match expected results
- Ensure that process is traceable to business rules

## Structured ID
- GP-DATA-001: Data Collection and Preparation
- GP-IDENT-001: Market Risk Component Identification
- GP-CALC-001: Market Risk Component Calculation
- GP-ADJ-001: Margin Adjustment Process
- GP-TOTAL-001: Total MTM and Margin Requirement Calculation
- GP-EXCEP-001: Exception Handling and Special Scenarios