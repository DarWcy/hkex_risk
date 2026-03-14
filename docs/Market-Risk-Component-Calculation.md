# Process Flow - Initial Margin Calculation Guide HKv14 Version 1.4

## Target Audience
BA

## Rule Traceability
- Original Document: Initial Margin Calculation Guide HKv14
- Release Version: 1.4
- Date: Oct 2025
- Original Sections: 3.2 Calculation Process

## Core Content

### 3.2 Calculation Process

#### 3.2.1 Overview of the Calculation Process for Total MTM and Margin Requirement
Total MTM and margin requirement is calculated according to the following steps:
1. Identify applicable market risk components for each instrument in the portfolio
2. Identify margin adjustments and other risk components
3. Calculate market risk components
4. Aggregate market risk components and perform margin adjustments
5. Calculate or retrieve other risk components from report
6. Derive total MTM and margin requirement

#### 3.2.2 Identify Applicable Market Risk Components for Each Instrument in Portfolio
- Step 1: Identify all corresponding FieldType(s) in the Initial Margin Risk Parameter File for each instrument shown in the Marginable Position Report
- Instrument Code in Marginable Position Report is the same as InstrumentID in Initial Margin Risk Parameter File for each tradeable instrument
- For corporate action entitled instruments, the instrument code would be decomposed into two fields in FieldType 7
- After repeating the aforementioned step for each instrument, identify the instruments subject to holiday add-on
- Holiday add-on will apply to all instruments except for those having FieldType 7 (i.e., instruments subject to corporate action position margin)
- Step 2: Identify applicable margin components for each instrument by referring to the FieldType definitions

#### 3.2.3 Identify Margin Adjustments and Other Risk Components
- Position limit add-on applies to all Hong Kong market instruments
- Credit risk add-on and ad-hoc add-on are not applicable to any instruments from the Initial Margin Risk Parameter File
- Users shall refer to the add-on amounts directly from the MTM and Margin Requirement Report
- Margin adjustments are applied on a portfolio basis:
  - Rounding on aggregated market-risk-component margin
  - Consideration on favorable MTM
  - Application of margin credit

#### 3.2.6 Calculate or Retrieve Other Risk Components from Report
- MTM requirement: Calculated from §3.2.5.2 or retrieved from report
- Position limit add-on: Applicable to all non-custodian CPs, refer to MTM and Margin Requirement Report
- Credit risk add-on: Only applicable to specific CPs notified by HKSCC individually
- Ad-hoc add-on: Only applicable to specific CPs notified by HKSCC individually

#### 3.2.8 Derive Total MTM and Margin Requirement from Results under §3.2.5 & §3.2.6
- Total MTM and margin requirement is derived by adding the net margin after credit to other risk components
- Total MTM and margin requirement = Net margin after credit + MTM requirement + Position limit add-on + Credit risk add-on + Ad-hoc add-on

## Applicable Scenarios
- Business process understanding for margin calculation
- Workflow analysis for margin calculation systems
- Requirement verification for margin calculation implementation
- Process flow validation for margin calculation
- Business scenario mapping for margin calculation

## Global Process Nodes
- Market Risk Component Identification
- Margin Component Calculation
- Margin Adjustment Processing
- Risk Component Aggregation
- Total Margin Calculation
- Margin Call Generation

## Testing Considerations
- Verify that all process steps are accurately described
- Test that process flow follows logical sequence
- Validate that all decision points are clearly defined
- Ensure that process dependencies are correctly identified
- Test that process handles all applicable scenarios
- Verify that process exceptions are properly handled
- Validate that process outputs are clearly defined
- Test that process integrates correctly with other systems

## Structured ID
- PF-OVER-001: Calculation Process Overview
- PF-IDENT-001: Market Risk Components Identification
- PF-IDENT-002: Margin Adjustments Identification
- PF-OTHER-001: Other Risk Components Identification
- PF-TOTAL-001: Total MTM and Margin Requirement Derivation