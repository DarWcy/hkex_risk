# Reference Tables - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
Automation Tester + QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 2.2, 3.2.4, 4.1

## Core Content

### 2.2 Specifications of Initial Margin Risk Parameter File

#### Global Parameters Table
| Parameter | Type | Description | Example Value |
|-----------|------|-------------|---------------|
| Valuation_DT | DATE | Valuation date (DD/MM/YYYY) | 01/01/2026 |
| HVaR_WGT | DECIMALS (X,10) | Weighting of the historical Value-at-Risk component | 0.75 |
| SVaR_WGT | DECIMALS (X,10) | Weighting of the stress Value-at-Risk component | 0.25 |
| HVaR_Scen_Count | INTEGER (X,0) | Number of scenarios used for calculating HVaR component | 500 |
| SVaR_Scen_Count | INTEGER (X,0) | Number of scenarios used for calculating SVaR component | 500 |
| STV_Count | INTEGER (X,0) | Number of stress test scenarios | 10 |
| HVaR_CL | DECIMALS (X,10) | Confidence level applied to HVaR | 0.994 |
| SVaR_CL | DECIMALS (X,10) | Confidence level applied to SVaR | 0.98 |
| HVaR_Measure | INTEGER (X,0) | Risk measure type for HVaR component | 4 (FHS ES (Discrete)) |
| SVaR_Measure | INTEGER (X,0) | Risk measure type for SVaR component | 4 (FHS ES (Discrete)) |
| Rounding | INTEGER (X,0) | Rounding parameter for margin calculation | 10,000 |
| Holiday_Factor | DECIMALS (X,10) | Scaling factor for calculating holiday add-on | sqrt(H) - 1 |
| InstrumentID | TEXT | Instrument identifier | 700 |

#### FieldType Definitions Table
| FieldType | Description | Usage |
|-----------|-------------|-------|
| 1 | HVaR Scenarios | Scenario returns for each instrument in HVaR component |
| 2 | SVaR Scenarios | Scenario returns for each instrument in SVaR component |
| 3 | Flat Rate Scenarios | Return for each instrument in flat rate margin component |
| 4 | Beta hedge information | Beta hedge information for liquidation risk add-on |
| 5 | Instrument delta information | Instrument delta information for liquidation risk add-on |
| 6 | Price threshold and add-on% | Price threshold and add-on% for structured product add-on |
| 7 | Corporate action position margin | Corporate action position margin scenarios |

### 3.2.4 Calculate Market Risk Components

#### Portfolio Margin Parameters Table
| Parameter | Description | Calculation Method |
|-----------|-------------|-------------------|
| HVaR component | Historical Value-at-Risk component | Average of worst 6 scenarios (99.4% confidence level) |
| SVaR component | Stress Value-at-Risk component | Average of worst 21 scenarios (98% confidence level) |
| HVaR_WGT | Weighting for HVaR component | 0.75 (example) |
| SVaR_WGT | Weighting for SVaR component | 0.25 (example) |
| Portfolio margin floor base | Higher of gross long and short market value | Max(gross long MV, gross short MV) |
| Portfolio margin floor rate | Floor rate available at HKEX website | 2.5% (example) |
| Portfolio margin | Final portfolio margin | Max(HVaR×HVaR_WGT + SVaR×SVaR_WGT, Portfolio margin floor) |

#### Liquidation Risk Add-on Parameters Table
| Parameter | Description | Calculation Method |
|-----------|-------------|-------------------|
| Delta-equivalent position | Market value adjusted by delta | Position market value × Delta |
| Underlying group | Grouping of instruments by underlying | Refer to FieldType 5 first column |
| Bucket rates | Rates for different buckets | Refer to FieldType 5 |
| Thresholds | Thresholds for bucket application | Refer to FieldType 5 |
| Hedging market value threshold | Threshold for portfolio-level LRA | Refer to FieldType 5 |
| Hedging instrument bucket rate | Rate for hedging instrument | Refer to FieldType 5 |

#### Holiday Add-on Parameters Table
| Parameter | Description | Calculation Method |
|-----------|-------------|-------------------|
| Holiday_Factor | Scaling factor for holiday add-on | sqrt(H) - 1, where H = number of consecutive Hong Kong holidays excluding Saturdays and Sundays |
| Holiday add-on base | Base for holiday add-on calculation | Portfolio margin + Flat rate margin |
| Holiday add-on | Final holiday add-on | Holiday add-on base × Holiday_Factor |

### 4. APPENDIX

#### Position Limit Add-on Parameters Table
| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| Apportioned liquid capital | Apportioned liquid capital of CP | 75,000,000 |
| Liquid capital multiplier | Multiplier for apportioned liquid capital | 4 |
| Apportioned liquid capital cap | Cap for apportioned liquid capital | 280,000,000 |
| Add-on% | Percentage for position limit add-on | 25% |
| NMV | Net market value of portfolio | Absolute value in case of net short position |

#### Guarantee Fund Risk Collateral Parameters Table
| Parameter | Description | Example Value |
|-----------|-------------|---------------|
| Guarantee Fund expected uncollateralised loss | Expected uncollateralised loss of CP group | Calculated value |
| Guarantee Fund risk pre-defined limit | Pre-defined limit for guarantee fund risk | HKD 3,650,000,000 |
| Guarantee Fund risk collateral | Final guarantee fund risk collateral | EUL - Pre-defined limit |

## Applicable Scenarios
- Lookup table reference for margin calculation systems
- Parameter definition verification for margin calculations
- Configuration data validation for margin calculation systems
- Test data preparation for margin calculation testing
- Parameter reconciliation for margin calculation systems

## Global Process Nodes
- Parameter Configuration
- Lookup Table Management
- Data Reference
- Configuration Validation

## Testing Considerations
- Verify that all parameter definitions are accurate and complete
- Test that parameter values are correctly referenced in calculations
- Validate that lookup tables are correctly structured and accessible
- Ensure that parameter dependencies are correctly documented
- Test that parameter updates are correctly propagated through the system
- Verify that parameter validation rules are correctly applied
- Ensure that parameter values are traceable to source documents

## Structured ID
- RT-GLOB-001: Global Parameters Table
- RT-GLOB-002: FieldType Definitions Table
- RT-PORT-001: Portfolio Margin Parameters Table
- RT-LRA-001: Liquidation Risk Add-on Parameters Table
- RT-HOLI-001: Holiday Add-on Parameters Table
- RT-POS-001: Position Limit Add-on Parameters Table
- RT-GF-001: Guarantee Fund Risk Collateral Parameters Table