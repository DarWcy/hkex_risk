# System Integration - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
Automation Tester

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.1.1 Risk Parameters and Margin Adjustments, 3.1.2 Positions

## Core Content

### 3.1.1 Risk Parameters and Margin Adjustments

#### Data Sources
- **IMRPF**: Initial Margin Risk Parameter File (daily dissemination, around 9:00 p.m. HKT)
- **MTM and Margin Requirement Report**: Generated on each business day for CPs to download via Report Access Platform (RAP)

#### Risk Parameters and Margin Adjustments
- **Market risk components**: Portfolio margin, Flat rate margin, Liquidation risk add-on, Structured product add-on, Corporate action position margin, Holiday add-on
  - Source: IMRPF (Y)
- **Margin adjustments**: Rounding on aggregated market-risk-component margin, Consideration on favorable MTM, Application of margin credit
  - Source: MTM and Margin Requirement Report (Y)
- **Other risk components**: MTM requirement, Position limit add-on, Credit risk add-on, Ad-hoc add-on
  - Source: MTM and Margin Requirement Report (Y)

### 3.1.2 Positions

#### Position Data Sources
- **Marginable Position Report** (RMAMP01): Disseminated to CPs after each margin call and day-end margin estimation process
- Dissemination times: around 11:45 a.m., 5:00 p.m. and 9:00 p.m. HKT subject to system finalization

#### Position Data Integration Points
- **Non-HKD denominated instruments**: Contract values and market values are converted to HKD equivalent using latest available FX rates without haircut when position snapshot is captured
- **Specific stock/cash collateral cover**: Positions covered by SSC/SCC are excluded from MTM and margin requirement calculation
- **Multi-counter eligible securities**: Positions traded on multi-counter eligible securities are combined into their settlement counters
- **Corporate action adjustments**: All positions are adjusted for corporate actions
- **Cross-day position netting**: All positions are cross-day netted

#### Position Data Generation Process
Users could opt to generate marginable positions by their own if they would like to calculate margin and marks more frequently during the day. The generation includes:
- Adjustment of specific stock/cash collateral cover
- Combine multi-counter eligible securities positions
- Corporate Action positions adjustment
- Cross-day positions netting

#### System Interface Requirements
- **Input data formats**: CSV files for risk parameters, position reports
- **Data exchange timing**: Multiple dissemination times throughout the day
- **System dependencies**: Marginable Position Report generation, IMRPF dissemination, MTM and Margin Requirement Report generation
- **Data consistency requirements**: Ensure position data is consistent across different reports and time points

## Applicable Scenarios
- System integration testing for margin calculation systems
- Interface testing for data exchange between systems
- Data validation and reconciliation testing
- System boundary condition testing
- End-to-end system integration testing

## Global Process Nodes
- Data Exchange Interface
- System Integration Points
- Data Consistency Validation
- System Boundary Management

## Testing Considerations
- Verify that all data sources are accurately identified
- Test data exchange timing and frequency
- Validate data format requirements (CSV structure, field definitions)
- Test position data integration logic (FX conversion, collateral exclusion, multi-counter combination, corporate action adjustment, cross-day netting)
- Ensure system interface specifications are clearly defined
- Test data consistency across different reports and time points
- Verify that system dependencies are correctly documented
- Test error handling and data validation at system boundaries
- Ensure that data generation process is accurately described and testable

## Structured ID
- SI-INT-001: Risk Parameters and Margin Adjustments Data Sources
- SI-INT-002: Market Risk Components Data Source
- SI-INT-003: Margin Adjustments Data Source
- SI-INT-004: Other Risk Components Data Source
- SI-POS-001: Position Data Sources
- SI-POS-002: Position Data Integration Points
- SI-POS-003: Position Data Generation Process
- SI-INT-001: System Interface Requirements