# Core Business Global Process - Initial Margin Calculation Guide HKv14

## Document Information

| Attribute | Value |
|-----------|-------|
| **Document Title** | Core Business Global Process |
| **Source Document** | Initial Margin Calculation Guide HKv14 |
| **Source Version** | 1.4 |
| **Source Date** | October 2025 |
| **Publisher** | Hong Kong Securities Clearing Company Limited (HKSCC) |
| **This Document Version** | 1.0.0 |
| **Last Updated** | 2025-03-13 |

### Target Audience
- Business Analysts (BA)
- QA Leads
- Automation Testers

### Rule Traceability
- **Original Document**: Initial Margin Calculation Guide HKv14
- **Release Version**: 1.4
- **Date**: Oct 2025
- **Original Sections**: 3.2 Calculation Process, All Sections

---

## Executive Summary

This document defines the **core business global process** for Initial Margin (IM) calculation on the VaR Platform. The process encompasses six major stages from data collection through final margin requirement calculation, with comprehensive exception handling for special scenarios.

### Process Objectives
1. **Accuracy**: Calculate initial margin requirements precisely per regulatory standards
2. **Completeness**: Cover all instrument types and risk components
3. **Timeliness**: Process data at defined cutoff times (9:00 p.m., 11:45 a.m., 5:00 p.m. HKT)
4. **Transparency**: Disseminate risk parameters and results to Clearing Participants

---

## Process Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        CORE BUSINESS GLOBAL PROCESS                         │
│                    INITIAL MARGIN CALCULATION PROCESS                       │
└─────────────────────────────────────────────────────────────────────────────┘

    ┌─────────────────────┐
    │ 1. DATA COLLECTION  │
    │   AND PREPARATION   │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ 2. MARKET RISK      │
    │ COMPONENT           │
    │ IDENTIFICATION      │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ 3. MARKET RISK      │
    │ COMPONENT           │
    │ CALCULATION         │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ 4. MARGIN           │
    │ ADJUSTMENT          │
    │ PROCESS             │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ 5. TOTAL MTM AND    │
    │ MARGIN REQUIREMENT  │
    │ CALCULATION         │
    └──────────┬──────────┘
               │
               ▼
    ┌─────────────────────┐
    │ 6. EXCEPTION        │
    │ HANDLING AND        │
    │ SPECIAL SCENARIOS   │
    └─────────────────────┘
```

---

## Process Stage 1: Data Collection and Preparation

### 1.1 Initial Margin Risk Parameter File (IMRPF) Dissemination

**Timing**: 9:00 p.m. HKT daily

**Content**:
| FieldType | Description | Structured ID |
|-----------|-------------|---------------|
| Global Parameters | HVaR_WGT, SVaR_WGT, HVaR_Scen_Count, etc. | DC-IMRPF-001 |
| FieldType 1 | HVaR Scenarios | DC-IMRPF-002 |
| FieldType 2 | SVaR Scenarios | DC-IMRPF-003 |
| FieldType 3 | Flat Rate Scenarios | DC-IMRPF-004 |
| FieldType 4 | Beta hedge information | DC-IMRPF-005 |
| FieldType 5 | Instrument delta information | DC-IMRPF-006 |
| FieldType 6 | Price threshold and add-on% | DC-IMRPF-007 |
| FieldType 7 | Corporate action position margin scenarios | DC-IMRPF-008 |

**Related Module**: [Risk-Parameter-File-Specification.md](../Risk-Parameter-File-Specification.md)

### 1.2 Marginable Position Report (RMAMP01)

**Timing**: 11:45 a.m., 5:00 p.m., 9:00 p.m. HKT

**Data Elements**:
- InstrumentID
- Quantity
- Contract value
- Market value

**Related Module**: [Input-Data-Specification.md](../Input-Data-Specification.md)

### 1.3 Position Data Processing

**Processing Steps**:
1. **FX Conversion**: Convert non-HKD instruments to HKD
2. **Collateral Exclusion**: Exclude specific stock/cash collateral cover
3. **Multi-counter Combination**: Combine eligible securities across counters
4. **Corporate Action Adjustment**: Adjust positions for corporate actions
5. **Cross-day Netting**: Net positions across trading days

**Related Module**: [Position-Processing-Logic.md](../Position-Processing-Logic.md)

---

## Process Stage 2: Market Risk Component Identification

### 2.1 Instrument FieldType Mapping

**For each instrument in portfolio**:
- Identify applicable FieldType(s) from IMRPF
- Map instrument codes to InstrumentID in IMRPF
- Decompose corporate action entitled instruments (FieldType 7)

**Decision Point**: Is instrument subject to FieldType 7?
- **Yes**: Apply corporate action position margin calculation
- **No**: Continue with standard risk component identification

### 2.2 Holiday Add-on Applicability

**Rule**: Apply to all instruments except those with FieldType 7

**Related Module**: [Other-Risk-Components.md](../Other-Risk-Components.md)

### 2.3 Margin Adjustment Identification

**Components to Identify**:
- Rounding on aggregated market-risk-component margin
- Favorable MTM consideration
- Margin credit application

**Related Module**: [Margin-Adjustment-Process.md](../Margin-Adjustment-Process.md)

### 2.4 Other Risk Component Identification

**Components**:
- MTM requirement (calculated or retrieved)
- Position limit add-on (from report)
- Credit risk add-on (from report, if applicable)
- Ad-hoc add-on (from report, if applicable)

**Related Module**: [Other-Risk-Components.md](../Other-Risk-Components.md)

---

## Process Stage 3: Market Risk Component Calculation

### 3.1 Portfolio Margin Calculation

**Step-by-Step Process**:

1. **Instrument Grouping**
   - Group 1: IPO stocks + structured products
   - Group 2: All other instruments

2. **HVaR Component Calculation**
   ```
   HVaR = Average of worst 6 scenarios (99.4% confidence)
   ```
   **Structured ID**: MRCC-HVaR-001

3. **SVaR Component Calculation**
   ```
   SVaR = Average of worst 21 scenarios (98% confidence)
   ```
   **Structured ID**: MRCC-SVaR-001

4. **Portfolio Margin Floor Calculation**
   ```
   Floor = Max(gross long MV, gross short MV) × floor rate
   ```
   **Structured ID**: MRCC-FLOOR-001

5. **Portfolio Margin Final Calculation**
   ```
   Portfolio Margin = Max(HVaR × HVaR_WGT + SVaR × SVaR_WGT, Portfolio floor)
   ```
   **Structured ID**: MRCC-PM-001

**Related Module**: [Market-Risk-Component-Calculation.md](../Market-Risk-Component-Calculation.md)

### 3.2 Flat Rate Margin Calculation

**Process**:
1. Aggregate absolute market value by sub-margin group
2. Take higher of long and short for each group
3. Apply flat margin rate (FieldType 3)
4. Apply flat rate margin multiplier (DWH0081C)

**Structured ID**: MRCC-FRM-001

**Related Module**: [Market-Risk-Component-Calculation.md](../Market-Risk-Component-Calculation.md)

### 3.3 Liquidation Risk Add-on (LRA) Calculation

**Instrument-level LRA**:
```
LRA_instrument = Sum of (delta-equivalent position MV × bucket rate)
```
**Structured ID**: MRCC-LRA-INST-001

**Portfolio-level LRA**:
```
LRA_portfolio = Sum of (beta hedge position MV × hedging instrument bucket rate)
```
**Structured ID**: MRCC-LRA-PORT-001

**Total LRA**:
```
Total LRA = Instrument-level LRA + Portfolio-level LRA
```
**Structured ID**: MRCC-LRA-TOTAL-001

**Related Module**: [Market-Risk-Component-Calculation.md](../Market-Risk-Component-Calculation.md)

### 3.4 Structured Product Add-on Calculation

**Applicability**: Only for long positions with price < threshold (FieldType 6)

**Calculation**:
```
Structured Product Add-on = Quantity × Tick size multiplier × Minimum tick size
```
**Structured ID**: MRCC-SPA-001

**Related Module**: [Market-Risk-Component-Calculation.md](../Market-Risk-Component-Calculation.md)

### 3.5 Corporate Action Position Margin Calculation

**Process**:
1. Apply positive net market value to scenario 4 (FieldType 7)
2. Apply negative net market value to scenario 3 (FieldType 7)
3. Add results from scenarios 3 and 4

**Structured ID**: MRCC-CAPM-001

**Related Module**: [Corporate-Action-Processing.md](../Corporate-Action-Processing.md)

### 3.6 Holiday Add-on Calculation

**Base Calculation**:
```
Base = Portfolio margin + Flat rate margin
```

**Holiday Factor**:
```
Holiday_Factor = sqrt(H) - 1
Where H = consecutive HK holidays
```

**Holiday Add-on**:
```
Holiday add-on = Base × Holiday_Factor
```
**Structured ID**: MRCC-HA-001

**Related Module**: [Other-Risk-Components.md](../Other-Risk-Components.md)

---

## Process Stage 4: Margin Adjustment Process

### 4.1 Aggregation

**Formula**:
```
Aggregated margin = Portfolio margin + 
                    Flat rate margin + 
                    Liquidation risk add-on + 
                    Structured product add-on + 
                    Corporate action position margin + 
                    Holiday add-on
```
**Structured ID**: MA-AGG-001

### 4.2 Rounding

**Formula**:
```
Rounded margin = Round up(Aggregated margin, Rounding parameter)
```
**Structured ID**: MA-ROUND-001

### 4.3 Favorable MTM Consideration

**Favorable MTM Calculation**:
```
Favorable MTM = Market value_Portfolio - Contract value_Portfolio
```

**Net Margin Calculation**:
```
Net margin = Max(0, Rounded margin - Favorable MTM)
```
**Structured ID**: MA-FMTM-001

### 4.4 Margin Credit Application

**Formula**:
```
Net margin after credit = Max(0, Net margin - Margin credit)
```
**Structured ID**: MA-CREDIT-001

**Related Module**: [Margin-Adjustment-Process.md](../Margin-Adjustment-Process.md)

---

## Process Stage 5: Total MTM and Margin Requirement Calculation

### 5.1 Final Calculation

**Formula**:
```
Total MTM and margin requirement = Net margin after credit +
                                   MTM requirement +
                                   Position limit add-on +
                                   Credit risk add-on +
                                   Ad-hoc add-on
```
**Structured ID**: TMR-FINAL-001

### 5.2 Report Generation and Dissemination

**Output**: MTM and Margin Requirement Report

**Distribution**: Disseminate to CPs via Report Access Platform (RAP)

**Timing**: After each calculation cycle (11:45 a.m., 5:00 p.m., 9:00 p.m. HKT)

**Related Module**: [Calculation-Examples.md](../Calculation-Examples.md)

---

## Process Stage 6: Exception Handling and Special Scenarios

### 6.1 Position Limit Add-on

**Calculation**:
```
Based on apportioned liquid capital and liquid capital cap
Apply add-on% to rounded margin
```
**Structured ID**: EH-PLA-001

### 6.2 Guarantee Fund Risk Collateral

**Process**:
1. Calculate Expected Uncollateralised Loss (EUL)
2. Guarantee Fund risk collateral = EUL - Pre-defined limit

**Structured ID**: EH-GFRC-001

### 6.3 Specific Stock/Cash Collateral Position Cover

**Rule**: Exclude covered positions from calculation

**Applicability**: Positions prior to settlement date

**Structured ID**: EH-SSCC-001

**Related Module**: [Collateral-Management.md](../Collateral-Management.md)

### 6.4 Corporate Action Position Adjustment

**Adjustment Types**:
- Bonus share/stock split/stock consolidation
- Cash dividend/stock dividend/rights issue/open offer
- Stock conversion

**Structured ID**: EH-CAPA-001

**Related Module**: [Corporate-Action-Processing.md](../Corporate-Action-Processing.md)

### 6.5 Cross-day Position Netting

**Process**: Net positions across trading days

**Structured ID**: EH-CDPN-001

### 6.6 Cross-currency Netting on MTM Requirement

**Process**: Net MTM requirements across different currencies

**Structured ID**: EH-CCNM-001

### 6.7 Intra-day MTM Requirement Calculation

**Timing**:
- 11:00 a.m. HKT calculation
- 2:00 p.m. HKT calculation

**Structured ID**: EH-IDMTM-001

**Related Module**: [Margin-Adjustment-Process.md](../Margin-Adjustment-Process.md)

---

## Module Mapping Matrix

| Process Stage | Primary Module | Supporting Modules | Structured IDs |
|---------------|----------------|-------------------|----------------|
| 1. Data Collection | Risk-Parameter-File-Specification.md | Input-Data-Specification.md, Position-Processing-Logic.md | DC-IMRPF-001 to DC-IMRPF-008 |
| 2. Risk Identification | Market-Risk-Component-Calculation.md | Other-Risk-Components.md, Margin-Adjustment-Process.md | - |
| 3. Risk Calculation | Market-Risk-Component-Calculation.md | Corporate-Action-Processing.md, Other-Risk-Components.md | MRCC-HVaR-001 to MRCC-HA-001 |
| 4. Margin Adjustment | Margin-Adjustment-Process.md | Input-Data-Specification.md | MA-AGG-001 to MA-CREDIT-001 |
| 5. Total Calculation | Calculation-Examples.md | All calculation modules | TMR-FINAL-001 |
| 6. Exception Handling | Other-Risk-Components.md | Collateral-Management.md, Corporate-Action-Processing.md, Position-Processing-Logic.md | EH-PLA-001 to EH-IDMTM-001 |

---

## Process Flow Relationships

### Primary Flow
```
Data Collection → Risk Component Identification → Risk Component Calculation → Margin Adjustment → Total Margin Calculation
```

### Supporting Processes
- **Exception Handling**: Parallel to main flow, handles special scenarios
- **Validation Rules**: Applies throughout all process steps
- **System Integration**: Interfaces with data sources and report generation

### Decision Points

| Decision Point | Condition | True Path | False Path |
|----------------|-----------|-----------|------------|
| Holiday Add-on | FieldType 7? | Skip holiday add-on | Apply holiday add-on |
| Portfolio Floor | Weighted avg > Floor? | Use weighted avg | Use floor |
| Favorable MTM | FMTM > 0? | Subtract from margin | Ignore |
| Margin Credit | Credit > Net margin? | Zero margin | Subtract credit |

### Key Dependencies

| Dependency | Source | Timing | Impact if Missing |
|------------|--------|--------|-------------------|
| IMRPF | Risk Parameter System | 9:00 p.m. HKT | Cannot calculate risk components |
| Position Data | Trading System | 11:45/17:00/21:00 HKT | Cannot calculate portfolio margin |
| Market Data | Market Data Feed | Real-time | Incorrect market values |
| Reference Data | Security Master | Daily | Incorrect instrument mapping |

---

## Timing and Scheduling

### Daily Schedule

| Time (HKT) | Process Step | System | Output |
|------------|--------------|--------|--------|
| 21:00 | IMRPF dissemination | Risk Parameter System | IMRPF file |
| 21:00 | Position data collection | Trading System | Position snapshot |
| 21:00-21:30 | Risk component calculation | VaR Platform | Risk components |
| 21:30-22:00 | Margin adjustment | VaR Platform | Adjusted margin |
| 22:00 | Report generation | Report System | MTM and Margin Report |
| 11:45 | Intra-day calculation | VaR Platform | Intra-day margin |
| 17:00 | Intra-day calculation | VaR Platform | Intra-day margin |

---

## Testing Considerations

### For QA Leads

**Process Validation Points**:
1. Verify all six process stages are executed in sequence
2. Confirm decision points follow correct logic
3. Validate exception handling triggers appropriately
4. Check timing adherence for scheduled processes

**Integration Testing**:
- End-to-end flow from data collection to report generation
- Exception scenario handling
- Error recovery procedures

### For Automation Testers

**Automated Test Scenarios**:
1. **Happy Path**: Complete process execution with valid data
2. **Edge Cases**: Boundary values for each calculation
3. **Exception Scenarios**: Each exception handling path
4. **Timing Tests**: Process execution within SLA windows

**Test Data Requirements**:
- Valid IMRPF with all FieldTypes
- Position data covering all instrument types
- Market data for FX conversion
- Corporate action scenarios

---

## Global Process Nodes

### Primary Nodes
1. **Data Collection Node**: VaR Platform Overview
2. **Risk Identification Node**: Regulatory Compliance Assessment
3. **Calculation Node**: Margin Calculation Framework Definition
4. **Adjustment Node**: Risk Parameter Dissemination Process
5. **Reporting Node**: Report Generation and Distribution
6. **Exception Node**: Special Scenario Handling

### Node Relationships
```
Data Collection Node → Risk Identification Node → Calculation Node → Adjustment Node → Reporting Node
                                      ↓
                              Exception Node (parallel)
```

---

## Version History

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0.0 | 2025-03-13 | AI Assistant | Initial creation from Core-Business-Global-Process-Flowchart.md |

---

## Related Documents

- [Core-Business-Global-Process-Flowchart.md](./Core-Business-Global-Process-Flowchart.md) - Visual flowchart representation
- [process-relationships.md](./process-relationships.md) - Detailed process-to-rule mapping
- [Module files in docs/](../) - Detailed rule specifications

---

**Document Owner**: BA Lead  
**Review Cycle**: Monthly  
**Next Review Date**: 2025-04-13
