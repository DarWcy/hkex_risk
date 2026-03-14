# Data Specification - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
QA Lead

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 2. INITIAL MARGIN RISK PARAMETER FILE, 3.1.2 Positions

## Core Content

### 2. INITIAL MARGIN RISK PARAMETER FILE

#### 2.1 Layout of Initial Margin Risk Parameter File
- An Initial Margin Risk Parameter File (RPF01) is generated in csv format
- Could be downloaded by CPs on each business day (dissemination time: around 9:00 p.m. HKT subject to system finalization)
- File includes instrument price returns for historical Value-at-Risk (HVaR) scenarios, stress Value-at-Risk (SVaR) scenarios, flat rate margin scenarios, beta hedge information for liquidation risk add-on, instrument delta information for liquidation risk add-on, price threshold and add-on% for structured product add-on and corporate action position margin scenarios

#### 2.2 Specifications of Initial Margin Risk Parameter File

##### Global Parameters
- **Valuation_DT**: Valuation date (DD/MM/YYYY)
- **HVaR_WGT**: Weighting of the historical Value-at-Risk component (DECIMALS (X,10))
- **SVaR_WGT**: Weighting of the stress Value-at-Risk component (DECIMALS (X,10))
- **HVaR_Scen_Count**: Number of scenarios used for calculating HVaR component (INTEGER (X,0))
- **SVaR_Scen_Count**: Number of scenarios used for calculating SVaR component (INTEGER (X,0))
- **STV_Count**: Number of stress test scenarios (INTEGER (X,0))
- **HVaR_CL**: Confidence level applied to HVaR (DECIMALS (X,10))
- **SVaR_CL**: Confidence level applied to SVaR (DECIMALS (X,10))
- **HVaR_Measure**: Risk measure type for HVaR component (4 – FHS ES (Discrete))
- **SVaR_Measure**: Risk measure type for SVaR component (4 – FHS ES (Discrete))
- **Rounding**: Rounding parameter for margin calculation (INTEGER (X,0))
- **Holiday_Factor**: Scaling factor for calculating holiday add-on (DECIMALS (X,10))
- **InstrumentID**: Instrument identifier (TEXT)

##### FieldType Definitions
- **FieldType 1**: HVaR Scenarios - Scenario returns for each instrument in HVaR component
- **FieldType 2**: SVaR Scenarios - Scenario returns for each instrument in SVaR component
- **FieldType 3**: Flat Rate Scenarios - Return for each instrument in flat rate margin component
- **FieldType 4**: Beta hedge information for liquidation risk add-on
- **FieldType 5**: Instrument delta information for liquidation risk add-on
- **FieldType 6**: Price threshold and add-on% for structured product add-on
- **FieldType 7**: Corporate action position margin scenarios

### 3.1.2 Positions

#### Required Position Details
- **InstrumentID**: Instrument identifier (e.g., 700 for Tencent Holdings)
- **Quantity**: Position quantity (e.g., -1,000,000 means to deliver 1,000,000 shares)
- **Contract value**: Contract value in HKD equivalent (e.g., -384,000,000 means the CP has a receivable of $384,000,000)
- **Market value**: Market value in HKD equivalent

#### Position Data Sources
- Retrieved from "Marginable Position Report" (RMAMP01)
- Disseminated to CPs after each margin call and day-end margin estimation process
- Dissemination times: around 11:45 a.m., 5:00 p.m. and 9:00 p.m. HKT subject to system finalization

#### Position Data Characteristics
- Positive quantity means long position, negative quantity means short position
- Negative contract value means receivable for CP in VaR Platform
- Market value = Position quantity × Instrument market price (sign determined by position quantity)
- For non-HKD denominated instruments, contract values and market values are converted to HKD equivalent using latest available FX rates without haircut
- Positions covered by specific stock/cash collateral are excluded
- Positions traded on multi-counter eligible securities are combined into their settlement counters
- All positions are adjusted for corporate actions
- All positions are cross-day netted

#### Position Data Generation Process
Users could opt to generate marginable positions by their own if they would like to calculate margin and marks more frequently during the day. The generation includes:
- Adjustment of specific stock/cash collateral cover
- Combine multi-counter eligible securities positions
- Corporate Action positions adjustment
- Cross-day positions netting

## Applicable Scenarios
- Data validation for margin calculation systems
- Specification verification for risk parameter files
- Position data quality assurance
- Interface testing for margin calculation systems
- Data source validation and reconciliation

## Global Process Nodes
- Risk Parameter File Generation
- Position Data Collection
- Data Validation and Processing
- Margin Calculation Preparation

## Testing Considerations
- Verify that all field specifications are accurately documented
- Test data type constraints (INTEGER, DECIMALS, TEXT formats)
- Validate data source references and timing
- Ensure position data characteristics are clearly defined
- Test position data generation process steps
- Verify currency conversion logic
- Validate collateral exclusion logic
- Test multi-counter position combination logic
- Ensure corporate action adjustment logic is documented
- Validate cross-day netting process

## Structured ID
- DS-FILE-001: Risk Parameter File Layout
- DS-FILE-002: Global Parameter Specifications
- DS-FILE-003: FieldType Definitions
- DS-POS-001: Position Details Requirements
- DS-POS-002: Position Data Sources
- DS-POS-003: Position Data Characteristics
- DS-POS-004: Position Data Generation Process