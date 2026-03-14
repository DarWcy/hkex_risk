# HKEX 香港交易所
## HKSCC - VaR Platform Initial Margin Calculation Guide
### INITIAL MARGIN CALCULATION GUIDE
Hong Kong Exchanges and Clearing Limited
VaR Platform
Version 1.4
Oct 2025

### Disclaimer
HKEX endeavors to ensure the accuracy and reliability of the information provided but takes no responsibility for any errors or omissions or for any losses arising from decisions, action, or inaction.

# TABLE OF CONTENTS
1. INTRODUCTION ............................................................................................................... 4
2. INITIAL MARGIN RISK PARAMETER FILE ....................................................................... 5
2.1 Layout of Initial Margin Risk Parameter File ................................................................ 5
2.2 Specifications of Initial Margin Risk Parameter File ..................................................... 6
3. CALCULATION OF TOTAL MTM AND MARGIN REQUIREMENT ..................................... 8
3.1 Required Inputs........................................................................................................... 8
3.1.1 Risk Parameters and Margin Adjustments............................................................ 8
3.1.2 Positions .............................................................................................................. 8
3.2 Calculation Process .................................................................................................... 9
3.2.1 Overview of the Calculation Process for Total MTM and Margin Requirement ..... 9
3.2.2 Identify Applicable Market Risk Components for Each Instrument in Portfolio .... 10
3.2.3 Identify Margin Adjustments and Other Risk Components .................................. 11
3.2.4 Calculate Market Risk Components ................................................................... 11
3.2.4.1 Portfolio Margin .............................................................................................. 11
3.2.4.1.1 Historical Value-at-Risk Component (“HVaR”) ......................................... 11
3.2.4.1.2 Stress Value-at-Risk Component (“SVaR”) .............................................. 13
3.2.4.1.3 Portfolio Margin Floor .............................................................................. 14
3.2.4.2 Flat Rate Margin ............................................................................................ 15
3.2.4.3 Liquidation Risk Add-on (“LRA”) ..................................................................... 16
3.2.4.3.1 Instrument-level LRA .............................................................................. 16
3.2.4.3.2 Portfolio-level LRA .................................................................................. 17
3.2.4.4 Structured Product Add-on ............................................................................. 18
3.2.4.5 Corporate Action Position Margin ................................................................... 19
3.2.4.6 Holiday Add-on .............................................................................................. 19
3.2.5 Aggregate Market Risk Components and Perform Margin Adjustments ............. 20
3.2.5.1 Rounding on Aggregated Market-risk-component Margin .............................. 20
3.2.5.2 Consideration on Favorable MTM .................................................................. 20
3.2.5.3 Application of Margin Credit ........................................................................... 21
3.2.6 Calculate or Retrieve Other Risk Components from Report ............................... 21
3.2.6.1 MTM Requirement ......................................................................................... 21
3.2.6.2 Position Limit Add-on ..................................................................................... 21
3.2.6.3 Credit Risk Add-on ......................................................................................... 22
3.2.6.4 Ad-hoc Add-on ............................................................................................... 22
3.2.7 Summary of Market Risk Components with Margin Adjustments and Other Risk Components ....................................................................................................... 22
3.2.8 Derive Total MTM and Margin Requirement from Results under §3.2.5 & §3.2.6 22
4. APPENDIX ...................................................................................................................... 23
4.1 Detailed Calculation on Position Limit Add-on ........................................................... 23
4.2 Guarantee Fund Risk Collateral ................................................................................ 24
4.3 Specific Stock / Cash Collateral Position Cover ........................................................ 24
4.3.1 Specific Stock Collateral for Short Position ......................................................... 24
4.3.2 Specific Cash Collateral Position Cover ............................................................. 27
4.4 Corporate Action Position Adjustment ....................................................................... 28
4.4.1 Position Quantity Adjustment for Bonus Share / Stock Split / Stock Consolidation 30
4.4.2 Create Benefit Entitlement Position for Cash Dividend ....................................... 30
4.4.3 Create Benefit Entitlement Position for Stock Dividend ...................................... 31
4.4.4 Create Benefit Entitlement Position for Rights Issue / Open Offer ...................... 32
4.4.5 Combined Effects on Position Adjustment for Combination of Corporate Actions 32
4.4.6 Position Adjustment for Stock Conversion .......................................................... 33
4.5 Cross-day Position Netting ........................................................................................ 33
4.6 Cross-currency Netting on MTM Requirement .......................................................... 34
4.7 Intra-day MTM Requirement Calculation ................................................................... 35
4.7.1 Intra-day MTM Requirement Calculation (11:00 a.m. HKT) ................................ 35
4.7.2 Intra-day MTM Requirement Calculation (2:00 p.m. HKT) .................................. 37

# 1. INTRODUCTION
Hong Kong Securities Clearing Company Limited (“HKSCC”) adopts VaR Platform to determine the initial margin (“IM”) requirement of Clearing Participants’ (“CPs”) portfolios. The model contains portfolio margin component for Primary Tier (“Tier P”) instruments, flat rate margin component for Non-constituent Tier (“Tier N”) instruments, corporate action position margin component and other margin add-on components.

The VaR Platform is developed in accordance with the regulatory requirements and international best practices (e.g., CPMI-IOSCO Principles for Financial Market Infrastructures). To promote transparency of the model, a file containing the key risk parameters required for calculating IM (a.k.a., “Initial Margin Risk Parameter File”, or “IMRPF”) will be disseminated to all HKSCC’s CPs on a daily basis upon the launch of VaR Platform.

This document outlines how to use the Initial Margin Risk Parameter File to calculate the total MTM and margin requirement of a portfolio for HKSCC clearable instruments in Hong Kong market.

# 2. INITIAL MARGIN RISK PARAMETER FILE
## 2.1 Layout of Initial Margin Risk Parameter File
An Initial Margin Risk Parameter File¹ (i.e., RPF01) will be generated in csv format and could be downloaded by CPs on each business day². The layout of the file is shown below:

**RPF01**:
This file includes instrument price returns for historical Value-at-Risk (“HVaR”) scenarios, stress Value-at-Risk (“SVaR”) scenarios, flat rate margin scenarios, beta hedge information for liquidation risk add-on, instrument delta information for liquidation risk add-on, price threshold and add-on% for structured product add-on and corporate action position margin scenarios.

| Valuation_DT | 1/4/2019 | | | | | | | | | | |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| HVaR_WGT | 0.75 | | | | | | | | | | |
| SVaR_WGT | 0.25 | | | | | | | | | | |
| HVaR Scen_Count | 1000 | | | | | | | | | | |
| SVaR Soen Count | 1018 | | | | | | | | | | |
| STV_Count | 200 | | | | | | | | | | |
| HVaR CL | 0.994 | | | | | | | | | | |
| SVaR CL | 0.98 | | | | | | | | | | |
| HVaR_Measure | 4 | | | | | | | | | | |
| | 4 | | | | | | | | | | |
| SVaR_Measure | | | | | | | | | | | |
| Rounding Holiday_Factor | 10000 0.7320508075 | | | | | | | | | | |
| Instrumentld | FieldType | | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
| 700 | 1 | 0.01391 | -0.01422 | 0.006132 | 0.006687 | 0.013556 | 0.01391 | 0.006132 | 0.006687 | 0.013556 | 0.013556 |
| 1299 | 1 | 0.01125 | 0.008827 | | -0.00875-0.003115 | 0.006901 | 0.01125 | | -0.00875-0.003115 | 0.006901 | 0.006901 |
| 1876 | 1 | 0.011128 | -0.014789 | 0.006009 | 0.007356 | 0.015725 | 0.012936 | 0.005825 | 0.008292 | 0.00976 | 0.010167 |
| 2823 | 1 | 0.011628 | -0.003311 | | 0.001658-0.009852 | -0.001639 | 0.011628 | 0.001658 | -0.009852 | -0.001639-0,001639 | |
| 3690 | | 10.012241 | -0.016268 | 0.00661 | 0.008092 | 0.017298 | 0.01423 | 0.006408 | 0.009121 | 0.010736 | 0.011184 |
| 26883 | 1 | 0.136461 | -0.129264 | 0.034216 | 0.046343 | 0.134202 | 0.136462 | 0.034217 | 0.046342 | 0.1342030.134203 | |
| 60954 | | 1-0.104288 | -0.083417 | 0.0819 | 0.029439 | -0.060245-0.104288 | | 0.0819 | 0.029439 | -0.060245-0.060244 | |
| 700 | | 20.041026 | 0.092873 -0.067737 | | | | -0.030462-0.0000310.0406715 | | 0.04069180.0406778 | 0.0406596 0,0406699 | |
| 1299 | | 20.037588 | 0.048124 | | | | -0.042722 -0.042776-0.0000080.0372818 | | 0.0372680.0372632 | 0.03728580.0372862 | |
| 1876 | | 20.040616 | 0.076156 | -0.069769 | -0.038382 | | -0.0000350.028877 | 0.034181 | 0.034576 | 0.034561 | 0.04067 |
| 2823 | | 20.026217 | 0.043137 | -0.036832 | -0.031046 | | 0.0000210.025982 0.02599140.0259828 | | | 0.0259850.0259961 | |
| 3690 | 2 | 0.044678 | 0.083772-0.076746 | | | | -0.04222 -0.0000390.0317650.0375990.038034 | | | 0.0380170.044737 | |
| 26883 | | 20.254769 | 0.660324 | | | | | | -0.53 -0.131 0.00340.256511 0.2275 025227 0.25259 .252738 | | |
| 60954 | | 2-0.321378 | -0.4374470.399873 | | 0.404237 | | 0.000022 -0.318807 -0.318531 -0.318547 -0.318514 -0.318721 | | | | |
| 658 | 3 | 0.12 | | | | | | | | | |
| 3456 | 3 | 0.3 | | | | | | | | | |
| 3457 | 3 | 0.55 | | | | | | | | | |
| 3606 | 3 | 0.12 | | | | | | | | | |
| 700 | 4 | 0.0022 | 0.9300000000 | | 400 | | | | | | |
| 1299 | 4 | 0.0025 | 1.1100000000 | | 80 | | | | | | |
| 1876 | 4 | 0.002 | 1.2 200000000 | | 30 | | | | | | |
| 2823 | 4 | 0.002 | | 1250000000 | 30 | | | | | | |
| 2800 | 4 | 0.002 | | 1250000000 | 30 | | | | | | |
| 3690 | 4 | 0.0022 | | 1.3300000000 | 70 | | | | | | |
| 26883 | 5 | 700 | 0.0446 100 -0.789588 100 | | 0.1784 | | | | | | |
| 60954 | 5 | 1299 | -0.63167 | | | | | | |
| 26883 | 6 | 0.02 | 0.5 | | | | | | | | |
| 700 | 7 | | 4 | -0.5 | 0.5 | | | | | | |
| 1299 | 7 | 3 | 0 | -1 | 0 | | | | | | |
| 3606 | 7 | 2 | 0.5 | 0 | 0.5 | | | | | | |

¹ The number of scenario types is subject to change from time to time and will be reflected in the IMRPF. HKSCC will notify CPs before any change is made in accordance with applicable General Rules of CCASS/CCASS Operational Procedures.
² The dissemination time is around 9:00 p.m. HKT subject to system finalization.

## 2.2 Specifications of Initial Margin Risk Parameter File
| Field Name | Description | Format |
| --- | --- | --- |
| Valuation_DT | Valuation date | DD/MM/YYYY |
| HVaR_WGT | Weighting of the historical Value-at-Risk (“HVaR”) component in the initial margin model | DECIMALS (X,10) ³; |
| SVaR_WGT | Weighting of the stress Value-at-Risk (“SVaR”) component in the initial margin model | DECIMALS (X,10); |
| HVaR_Scen_Count | Number of scenarios used for calculating HVaR component | INTEGER (X,0) ³; e.g., a value of 1000 means 1000 risk scenarios for HVaR calculation. |
| SVaR_Scen_Count | Number of scenarios used for calculating SVaR component | INTEGER (X,0); e.g., a value of 1018 means 1018 risk scenarios for Stress VaR calculation. |
| STV_Count ⁴ | Number of stress test scenarios | INTEGER (X,0); e.g., a value of 200 means 200 stress test scenarios for STV. |
| HVaR_CL | Confidence level applied to HVaR | DECIMALS (X,10); e.g., a value of 0.994 means 99.4% confidence level. |
| SVaR_CL | Confidence level applied to SVaR | DECIMALS (X,10); e.g., a value of 0.98 means 98% confidence level. |
| HVaR_Measure | Risk measure type for HVaR component | 4 – FHS ES (Discrete) ⁵ |
| SVaR_Measure | Risk measure type for SVaR component | 4 – FHS ES (Discrete) |
| Rounding | Rounding parameter for margin calculation | INTEGER (X,0); e.g., a value of 10,000 means to round up the figure to 10,000. |
| Holiday_Factor | Scaling factor for calculating holiday add- on. It is calculated as square root(H) – 1, where H is the number of consecutive Hong Kong holidays excluding Saturdays and Sundays | DECIMALS (X,10) |
| InstrumentID | Instrument identifier e.g. Stock code, or underlying stock code for corporate action position margin instruments like distribution in specie (“DSP”), cash dividend (“DIV”), rights issue (“SRI”), etc. | TEXT |

The second number in INTEGER() and DECIMALS() refers to the maximum decimal places supported by IMRPF.
³ For potential future use only.
⁵ FHS ES stands for Filtered Historical Simulation Expected Shortfall, also known as Conditional Value-at-Risk (“CVaR”) or Expected Tail Loss (“ETL”) or average tail loss. It is the risk measure calculated based on Exponential Weighted Moving Average (“EWMA”) rescaled historical returns in the look back period. “Discrete” meaning only discrete data points on the distribution tail will be selected for calculation. There is no interpolation required between discrete data points.

| Field Name | Description | Format |
| --- | --- | --- |
| FieldType | Label to indicate the record type: 1 – HVaR Scenarios 2 – SVaR Scenarios 3 – Flat Rate Scenarios 4 – Beta hedge information for liquidation risk add-on 5 – Instrument delta information for liquidation risk add-on 6 – Price threshold and add-on% for structured product add-on 7 – Corporate action position margin scenarios | INTEGER (X,0) |
| FieldType 1 Columns | Scenario returns for each instrument in HVaR component On the right of “FieldType 1”: - total number of scenarios should be same as “HVaR_Scen_Count” | DECIMALS (X,10) |
| FieldType 2 Columns | Scenario returns for each instrument in SVaR component On the right of “FieldType 2”: - total number of scenarios should be same as “SVaR_Scen_Count” | DECIMALS (X,10) |
| FieldType 3 Columns | Return for each instrument in flat rate margin component | DECIMALS (X,10) |
| FieldType 4 Columns | On the right of “FieldType 4”: <br>- 1st column: Bucket rate <br>- 2nd column: Instrument beta <br>- 3rd column: Delta equivalent position market value threshold <br>- 4th column: Cash delta per quantity (i.e., market price) | 1:DECIMALS (X,10)<br>2:DECIMALS (X,10)<br>3:INTEGER (X,0)<br>4:DECIMALS (X,10) |
| FieldType 5 Columns | On the right of “FieldType 5”: <br>- 1st column: Underlying group <br>- 2nd column: Delta <br>- 3rd column: Conversion ratio <br>- 4th column: Cash delta per quantity | 1:TEXT<br>2:DECIMALS (X,10)<br>3:DECIMALS (X,10)<br>4:DECIMALS (X,10) |
| FieldType 6 Columns | On the right of “FieldType 6”: <br>- 1st column: Price threshold <br>- 2nd column: One-tenth of tick size multiplier | 1:DECIMALS (X,10)<br>2:DECIMALS (X,10) |
| FieldType 7 Columns | On the right of “FieldType 7”: <br>- 1st column: Benefit entitlement type <br>- 2nd column: Price of the benefit entitlement (Shows 1 for cash dividend) <br>- 3rd column: Short position add- on% <br>- 4th column: Long position add- on% | 1:INTEGER (X,0) ¹<br>2:DECIMALS (X,10)<br>3:DECIMALS (X,10)<br>4:DECIMALS (X,10) |
| Numbers next to “FieldType” | Scenario numbers | INTEGER (X,0) |

¹ 1 – Distribution in specie 2 – Rights issue 3 – Cash dividend

# 3. CALCULATION OF TOTAL MTM AND MARGIN REQUIREMENT
## 3.1 Required Inputs
### 3.1.1 Risk Parameters and Margin Adjustments
To derive total MTM and margin requirement, the risk parameters (including market risk and other risk components) and margin adjustments below are required. The sources are stated as follows:

|  |  | Source |  |
| --- | --- | --- | --- |
|  |  | IMRPF | MTM ⁶ and Margin Requirement Report ⁷ |
| Market risk component | Portfolio margin | Y | - |
| | Flat rate margin | Y | - |
| | Liquidation risk add-on | Y | - |
| | Structured product add-on | Y | - |
| | Corporate action position margin ⁸ | Y | - |
| | Holiday add-on | Y | - |
| Margin adjustment | Rounding on aggregated market- risk-component margin | Y | - |
| | Consideration on favorable MTM | - | Y |
| | Application of margin credit | - | Y |
| Other risk component | MTM requirement | - | Y |
| | Position limit add-on | - | Y |
| | Credit risk add-on | - | Y |
| | Ad-hoc add-on | - | Y |

⁶ MTM refers to “Mark-to-Market” a.k.a. the Marks.
⁷ The report will be generated on each business day for CPs to download via Report Access Platform (“RAP”).
⁸ Please note that corporate action position margin will be determined on a case-by-case basis. HKSCC will notify CPs in advance, if applicable.

### 3.1.2 Positions
The following position details of portfolios are required to calculate total MTM and margin requirement:
- InstrumentID (e.g., 700 for Tencent Holdings)
- Quantity⁹ (e.g. -1,000,000 means to deliver 1,000,000 shares)
- Contract value¹⁰ in HKD equivalent (e.g., In VaR Platform, -384,000,000 means the CP has a receivable of $384,000,000)
- Market value¹¹ in HKD equivalent

The above information for CPs’ entire portfolios could be retrieved from “Marginable Position Report” (“RMAMP01”), which will be disseminated to CPs after each margin call and day-end margin estimation process¹². When using the information in the “Marginable Position Report”, please note that:

⁹ Positive value means it is a long position. Negative value means it is a short position.
¹⁰ Negative value means it is a receivable for CP in VaR Platform.
¹¹ Market value = Position quantity x Instrument market price. The sign is determined by the position quantity. (i.e., Negative quantity means a short position and that market value is also negative.)
¹² The dissemination time is around 11:45 a.m., 5:00 p.m. and 9:00 p.m. HKT subject to system finalization.

- For non-HKD denominated instruments, contract values and market values are converted to HKD equivalent using the latest available FX rates without haircut when the position snapshot is captured;
- Positions covered by specific stock / cash collateral are excluded¹³;
- Positions traded on multi-counter eligible securities are combined into their settlement counters¹⁴;
- All positions are adjusted for corporate actions¹⁵; and
- All positions are cross-day netted¹⁶.

¹³ Please refer to Appendix 4.3 for Specific Stock Collateral / Specific Cash Collateral covered position exclusion logic
¹⁴ Please refer to Appendix 4.4 for the multi-counter eligible securities positions combine logic
¹⁵ Please refer to Appendix 4.5 for the corporate action position adjustment logic
¹⁶ Please refer to Appendix 4.6 for the cross-day position netting logic

In addition, users could opt to generate the marginable positions by their own if they would like to calculate margin and marks more frequently during the day. The generation of marginable position will include three main steps:
(i) Adjustment of specific stock / cash collateral cover,
(ii) Combine multi-counter eligible securities positions,
(iii) Corporate Action positions adjustment; and
(iv) Cross-day positions netting.

Appendix 4.3 to 4.6 demonstrates the detailed steps for reference.

A sample portfolio is shown below for illustration of calculation in the subsequent section:

| InstrumentID | Quantity | Contract value in HKD Equivalent | Market value in HKD Equivalent |
| --- | --- | --- | --- |
| 658 | -10,000,000 | -62,000,000 | -60,000,000 |
| 700 | -1,000,000 | -384,000,000 | -400,000,000 |
| 1299 | 1,000,000 | 80,000,000 | 80,000,000 |
| 1876 | 100,000 | 2,700,000 | 3,000,000 |
| 2823 | 1,000,000 | 30,000,000 | 30,000,000 |
| 3456 | 10,000 | 910,000 | 750,000 |
| 3457 | -50,000 | -360,000 | -300,000 |
| 3606 | 1,000,000 | 28,000,000 | 30,000,000 |
| 3690 | 100,000 | 6,900,000 | 7,000,000 |
| 26883 | 110,000,000 | 3,000,000 | 2,000,000 |
| DSP700 | -1,000,000 | 0 | -4,000,000 |
| DIV1299 | 1,000,000 | -1,000,000 | 0 |
| SRI3606 | 2,000,000 | 0 | 1,000,000 |
| 60954 | 120,000,000 | 8,000,000 | 10,000,000 |

## 3.2 Calculation Process
### 3.2.1 Overview of the Calculation Process for Total MTM and Margin Requirement
Total MTM and margin requirement is calculated according to the steps as follows:
- Identify applicable market risk components for each instrument in the portfolio (See §3.2.2);
- Identify margin adjustments and other risk components (See §3.2.3);
- Calculate market risk components (See §3.2.4);
- Aggregate market risk components and perform margin adjustments (See §3.2.5);
- Calculate or retrieve other risk components from report (See §3.2.6); and
- Derive total MTM and margin requirement by adding results from §3.2.5 & §3.2.6 (See §3.2.8).

### 3.2.2 Identify Applicable Market Risk Components for Each Instrument in Portfolio
Users shall identify applicable margin components by using the CP-specific “Marginable Position Report” and “Initial Margin Risk Parameter File” according to the steps as follows:
**Step 1**: Identify all corresponding FieldType(s) in the “Initial Margin Risk Parameter File” for each instrument shown in the “Marginable Position Report”.

Please note that Instrument Code in the “Marginable Position Report” is the same as InstrumentID in the “Initial Margin Risk Parameter File” for each tradeable instrument. For corporate action entitled instruments, the instrument code would be decomposed into two fields in FieldType 7 (See §2.2).

For example, Instrument Code 658 is found in the “Marginable Position Report”. Users shall find out “658” under the column InstrumentID and identify the corresponding FieldType(s) associated with the instrument in the “Initial Margin Risk Parameter File”. In this case, FieldType 3 is identified for the instrument.

For example, a corporate action entitled instrument “DSP700” is found in the “Marginable Position Report”, users shall find out “700” under the column InstrumentID and “1” under the next column in FieldType 7.

After repeating the aforementioned step for each instrument, user should identify the instruments subject to holiday add-on¹⁷. The holiday add-on will apply to all instruments except for those having FieldType 7 (i.e. instruments subject to corporate action position margin). Finally, the identification result of the sample portfolio is shown as follows:

| Code / InstrumentID | Portfolio margin |  | Flat rate margin | Liquidation risk add-on |  | Structured product add-on | Corporate action position margin | Holiday add-on |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
|  | HVaR 1 | SVaR 2 | 3 | 4 | 5 | 6 | 7 | Holiday_factor |
| 658 | - | - | Y | - | - | - | - | Y |
| 700 | Y | Y | - | Y | - | - | - | Y |
| 1299 | Y | Y | - | Y | - | - | - | Y |
| 1876 | Y | Y | - | Y | - | - | - | Y |
| 2823 | Y | Y | - | Y | - | - | - | Y |
| 3456 | - | - | Y | - | - | - | - | Y |
| 3457 | - | - | Y | - | - | - | - | Y |
| 3606 | - | - | Y | - | - | - | - | Y |
| 3690 | Y | Y | - | Y | - | - | - | Y |
| 26883 | Y | Y | - | - | Y | Y | - | Y |
| DSP700 | - | - | - | - | - | - | Y | - |
| DIV1299 | - | - | - | - | - | - | Y | - |
| SRI3606 | - | - | - | - | - | - | Y | - |
| 60954 | Y | Y | - | - | Y | - | - | Y |

¹⁷ Please note that the holiday add-on will not be applicable upon the launch of VaR Platform. HKSCC will notify CPs before the implementation.

For example, users should only include the InstrumentID 658 and 3606 for flat rate margin calculation according to the identification results shown in the above table (see §3.2.4.2 for calculation process on flat rate margin in details).

**Step 2**: Identify applicable margin components for each instrument by referring to the FieldType definitions stated in §2.2.

### 3.2.3 Identify Margin Adjustments and Other Risk Components
Users shall follow the rules below to determine which instrument should be included in the calculation of other risk components:
- Positions limit add-on applies to all Hong Kong market instruments; and
- Credit risk add-on and ad-hoc add-on are not applicable to any instruments from the Initial Margin Risk Parameter File. Instead, users shall refer to the add-on amounts directly from the “MTM and Margin Requirement Report”.

The margin adjustments below are applied on a portfolio basis (See §3.2.8 for details):
- Rounding on aggregated market-risk-component margin;
- Consideration on favorable MTM; and
- Application of margin credit.

### 3.2.4 Calculate Market Risk Components
#### 3.2.4.1 Portfolio Margin
The portfolio margin is the weighted average of the following two components, subject to the portfolio margin floor:
(i) Historical Value-at-Risk (“HVaR”) component; and
(ii) Stress Value-at-Risk (“SVaR”) component.

For the calculation of (i) and (ii), it is required to treat each \(IPO ^{18}\) stock and its relevant structured product(s) ¹⁹ as an individual portfolio and group other non-IPO related instruments together as another separate portfolio.

¹⁸ CPs could refer to the IPO Indicator Report (“DWH0303”) on Report Access Platform (“RAP”) daily to identify the stocks that are subject to IPO segregation and its relevant structured product(s) required to be grouped as an individual portfolio when calculating HVaR and SVaR (i.e., stocks which are newly listed within the recent 180 calendar days, subject to SFC approval).
¹⁹ If the underlying (as shown under Column 1 of FieldType 5 in the IMRPF) of an instrument in FieldType 5 is an IPO stock, this instrument is a relevant structured product.

##### 3.2.4.1.1 Historical Value-at-Risk Component (“HVaR”)
HVaR is calculated according to the steps as follows:
**Step 1**: Calculate the portfolio returns of positions in each scenario under FieldType 1 identified as per instructions in §3.2.2.

For example:
\[
\begin{aligned}
& Portfolio return ^{20} in scenario 1 for IPO instrument group 1876 \\
& =( Market value _{1876} × Return _{1876} ) \\
& =(3,000,000 × 0.011128) \\
& =33,384
\end{aligned}
\]

\[
\begin{aligned}
& Portfolio return ^{21} in scenario 1 for IPO instrument group 3690 \\
& =( Market value 3690 × Return _{3690} ) \\
& =(7,000,000 × 0.012241) \\
& =85,687
\end{aligned}
\]

\[
\begin{aligned}
& Portfolio return ^{22} in scenario 1 for non-IPO instruments \\
& =( Market value _{700} × Return _{700})+( Market value _{1299} × Return _{1299})+( Market value _{2823} × Return _{2823})+( Market value _{26883} × Return _{26883})+( Market value _{60954} × Return _{60954}) \\
& =(-400,000,000 × 0.01391)+(80,000,000 × 0.01125)+(30,000,000 × 0.011628)+(2,000,000 × 0.136461)+(10,000,000 × -0.104288) \\
& =-5,085,118
\end{aligned}
\]

²⁰ Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.
²¹ Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.
²² Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.

**Step 2**: Repeat step 1 for all HVaR scenarios under FieldType 1 (i.e., 1,000 referring to HVaR_Scen_Count in the Initial Margin Risk Parameter File).

A set of scenario returns under FieldType 1 will be obtained as follows:

| FieldType 1 | Scenario 1 | Scenario 2 | … | Scenario 1,000 |
| --- | --- | --- | --- | --- |
| Portfolio return for IPO stock 1876 | 33,384 | -44,367 | … | -9 |
| Portfolio return for IPO stock 3690 | 85,687 | -113,876 | … | -21 |
| Portfolio return for non-IPO instruments | -5,805,118 | 5,202,132 | … | 6,738 |

**Step 3**: Calculate HVaR component of the portfolios by averaging the worst 6 scenarios ²³, where HVaR_Measure parameter indicates an ES (Discrete) risk measure, and HVaR_CL parameter indicates a confidence level of 99.4%.

²³ (1-99.4% (HVaR_CL)) x 1,000 (HVaR_Scen_Count) scenarios = 6 scenarios, rounding up to the nearest integer.

\[HVaR for IPO instrument group 1876=-7,546.5\]
\[HVaR for IPO instrument group 3690=-19,369\]
\[HVaR for non-IPO instruments =-4,793,885.67\]

##### 3.2.4.1.2 Stress Value-at-Risk Component (“SVaR”)
SVaR is calculated according to the steps as follows:
**Step 1**: Calculate the portfolio return of positions for each scenario under FieldType 2 identified as per instructions in §3.2.2.

For example:
\[
\begin{aligned}
& Portfolio return ^{24} in scenario 1 for IPO instrument group 1876 \\
& =( Market value _{1876} × Return _{1876} ) \\
& =(3,000,000 × 0.040616) \\
& =121,848
\end{aligned}
\]

\[
\begin{aligned}
& Portfolio return ^{25} in scenario 1 for IPO instrument group 3690 \\
& =( Market value _{3690} × Return _{3690} ) \\
& =(7,000,000 × 0.044678) \\
& =312,746
\end{aligned}
\]

\[
\begin{aligned}
& Portfolio return ^{26} in scenario 1 for non-IPO instruments \\
&=( Market value _{700} × Return _{700})+( Market value _{1299} × Return _{1299})+( Market value _{2823} × Return _{2823})+( Market value _{26883} × Return _{26883})+( Market value _{60954} × Return _{60954} ) \\
& =(-400,000,000 × 0.041026)+(80,000,000 × 0.037588)+(30,000,000 × 0.026217)+(2,000,000 × 0.254769)+(10,000,000 × -0.321378) \\
& =-15,321,092
\end{aligned}
\]

²⁴ Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.
²⁵ Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.
²⁶ Round off any (Market valuei x Returni) term to the nearest integer if the result is a decimal number.

**Step 2**: Repeat step 1 for all SVaR scenarios under FieldType 2 (i.e., 1,018 referring to SVaR_Scen_Count in the Initial Margin Risk Parameter File).

A set of scenario returns under FieldType 2 will be obtained as follows:

| FieldType 2 | Scenario 1 | Scenario 2 | … | Scenario 1,018 |
| --- | --- | --- | --- | --- |
| Portfolio return for IPO stock 1876 | 121,848 | 228,468 | … | -166,599 |
| Portfolio return for IPO stock 3690 | 312,746 | 586,404 | … | -427,602 |
| Portfolio return for non-IPO instruments | -15,321,092 | -35,058,992 | … | 25,818,414 |

**Step 3**: Calculate SVaR component of the portfolio is the average of the worst 21 scenarios ²⁷, where SVaR_Measure parameter indicates an ES (Discrete) risk measure, and SVaR_CL parameter indicates a confidence level of 98%.

²⁷ (1-98% (SVaR_CL)) x 1,018 (SVaR_Scen_Count) scenarios = 21 scenarios, rounding up to the nearest integer.

\[SVaR for IPO instrument group 1876=-23,535.29\]
\[SVaR for IPO instrument group 3690=-60,407.67\]
\[SVaR for non-IPO instruments =-16,147,985.33\]

##### 3.2.4.1.3 Portfolio Margin Floor
Portfolio margin floor is the product of:
(i) Portfolio margin floor base; and
(ii) Portfolio margin floor rate²⁸.

Where the portfolio margin floor base is the higher of gross long and short market value of positions under FieldType 1 or 2, and the current portfolio margin floor rate is available at HKEX website²⁹. In this example, the portfolio margin floor rate is set as 2.5% as an example for illustration of the calculation method.

²⁸ The portfolio margin floor rate, a.k.a Tier P minimum margin level, is subject to change from time to time. HKSCC will issue circulars to notify CPs before any change is made.
²⁹ https://www.hkex.com.hk/Services/Clearing/Securities/Risk-Management/Margin?sc_lang=en

The portfolio margin floor is calculated according to the steps as follows:
**Step 1**: Calculate the portfolio margin floor base.
\[
\begin{aligned}
& Portfolio margin floor base \\
&= Maximum [Absolute value of (Market value_{1299}) + Absolute value of (Market value_{1876}) + Absolute value of (Market value_{2823}) + Absolute value of (Market value_{3690}) + Absolute value of (Market value_{26883}) + Absolute value of (Market value_{60954}) , Absolute value of (Market value_{700})] \\
&= Maximum [(80,000,000 + 3,000,000 + 30,000,000 + 7,000,000 + 2,000,000 + 10,000,000) , 400,000,000] \\
&= Maximum [132,000,000 , 400,000,000] \\
&= 400,000,000
\end{aligned}
\]

**Step 2**: Calculate portfolio margin floor by applying the 2.5% margin floor rate to the base.
\[Portfolio margin floor base x Portfolio margin floor rate =400,000,000 × 2.5 \% =10,000,000\]

As a result, the portfolio margin will be:
\[
\begin{aligned}
& = Maximum [Sum of (HVaR × HVaR_WGT + SVaR × SVaR_WGT), Portfolio margin floor] \\
& = Maximum [Absolute value of ((-7,546.5 × 75 \%)+(-23,535.29 × 25 \%)+(-19,369 × 75 \%)+(-60,407.67 × 25 \%)+(-4,793,885.67 × 75 \%)+(-16,147,985.33 × 25 \%)), 10,000,000] \\
& = Maximum [Absolute value of ((-11,543.70)+(-29,628.67)+(-7,632,410.59)), 10,000,000] \\
& =10,000,000
\end{aligned}
\]
*(Round off to the nearest integer if the result is a decimal number.)*

#### 3.2.4.2 Flat Rate Margin
Flat rate margin is calculated according to the steps as follows:
**Step 1**: Aggregate absolute market value of long positions and absolute market value of short positions separately for each position identified as per instructions in §3.2.2. and compare the total absolute market value of long positions and short positions separately for each sub-margin group of flat rate margin calculations defined on HKEX website³¹.

³¹ https://www.hkex.com.hk/Services/Clearing/Securities/Risk-Management/Margin?sc_lang=en

For example:
**Sub-group 1 positions**
| InstrumentID | Quantity | Absolute market value of long positions in HKD equivalent | Absolute market value of short positions in HKD equivalent |
| --- | --- | --- | --- |
| 658 | < 0 | 0 | 60,000,000 |
| 3606 |  0 | 30,000,000 | 0 |
| Total | | 30,000,000 | 60,000,000 |

For the sub-group 1 positions above, the total absolute short market value is higher than the total absolute long market value. Therefore, all short sub-group 1 positions will be included in the flat rate margin calculation while all long sub-group 1 positions will be excluded.

**Sub-group 2 positions**
| InstrumentID | Quantity | Contract value in HKD Equivalent | Market value in HKD Equivalent |
| --- | --- | --- | --- |
| 3456 | 10,000 | 910,000 | 750,000 |

**Sub-group 3 positions**
| InstrumentID | Quantity | Contract value in HKD Equivalent | Market value in HKD Equivalent |
| --- | --- | --- | --- |
| 3457 | -50,000 | -360,000 | -300,000 |

Similarly for sub-group 2 and sub-group 3 to take the higher of long and short absolute market value for each of them, all long sub-group 2 positions and all short sub-group 3 positions will be included in the flat rate margin calculation.

**Step 2**: Sum the product of absolute position market value and the flat margin rate under FieldType 3.

**Step 3**: Apply flat rate margin multiplier³² by referring to the “Daily Participant Margin Multiplier Report” (“DWH0081C”) to obtain the flat rate margin after margin multiplier.

³² Flat rate margin multiplier varies among CPs. Please refer to Daily Participant Margin Multiplier Report (DWH0081C).

For example, assigning a flat rate margin multiplier of 2 is assigned,
\[=(60,000,000 × 12 \%+750,000 × 30 \%+300,000 × 55 \%) × 2 =\underline{15,180,000}\]

#### 3.2.4.3 Liquidation Risk Add-on (“LRA”)
LRA consists of two components identified as per instructions in §3.2.2:
- Instrument-level LRA; and
- Portfolio-level LRA.

### 3.2.4.3.1 Instrument-level LRA
Instrument-level LRA is calculated according to the steps as follows:
Step 1: Calculate the delta-equivalent position market values for each underlying group. Users could find out the underlying group of a particular structured product by referring to the first column on the right of \("FieldType =5 "\) in the Initial Margin Risk Parameter File.
Taking Instrument 26883 as an example, users could refer to the Initial Margin Risk Parameter File and locate Instrument 700 is its corresponding underlying group.
Similarly, the underlying stock for Instrument 60954 is Instrument 1299.
In case the users only hold the stock without the corresponding structured product (i.e., no information of that particular instrument under FieldType 5), the users shall calculate the market value of delta-equivalent position by using the information under FieldType 4.

See the treatment of instruments 1876, 2823, 3690 in the example as follows:

| InstrumentID | Quantity (A) | Cash delta per quantity (B) | Market value of delta equivalent position in HKD equivalent (C)=(A)x(B) |
| --- | --- | --- | --- |
| 700 | -1,000,000 | 400 | -400,000,000 |
| 26883 | 110,000,000 | 0.1784 | 19,624,000 |
| | Total for the underlying group 700 | | -380,376,000 |
| 1299 | 1,000,000 | 80 | 80,000,000 |
| 60954 | 120,000,000 | -0.63167 | -75,800,400 |
| Total for the underlying group 1299 | | | 4,199,600 |
| 1876 | 100,000 | 30 | 3,000,000 |
| Not applicable | | | 0 |
| Total for the underlying group 1876 | | | 3,000,000 |
| 2823 | 1,000,000 | 30 | 30,000,000 |
| Not applicable | | | 0 |
| Total for the underlying group 2823 | | | 30,000,000 |
| 3690 | 100,000 | 70 | 7,000,000 |
| Not applicable | | | 0 |
| Total for the underlying group 3690 | | | 7,000,000 |

Step 2: Calculate the instrument-level LRA based on the respective bucket rates and the portion of delta-equivalent position market value which exceeds the thresholds for each underlying group and subsequently aggregate the LRAs for all underlying groups shown as follows:

| Underlying Group | Market value of delta equivalent position in HKD equivalent (A) | Threshold in HKD equivalent (B) | Bucket rate (C) | Liquidation risk add-on (D) = Maximum [Absolute value of ((A))-(B) , 0] x (C) |
| --- | --- | --- | --- | --- |
| 700 | -380,376,000 | 300,000,000 | 0.0022 | 176,827.2 |
| 1299 | 4,199,600 | 100,000,000 | 0.0025 | 0 |
| 1876 | 3,000,000 | 200,000,000 | 0.002 | 0 |
| 2823 | 30,000,000 | 250,000,000 | 0.002 | 0 |
| 3690 | 7,000,000 | 300,000,000 | 0.0022 | 0 |
| | Total | | | 176,827.2 |

Instrument-level \(LRA =176,827\) (rounded off to the nearest integer)

### 3.2.4.3.2 Portfolio-level LRA
Portfolio-level LRA is calculated according to the steps as follows:
Step 1: Calculate market values of beta hedge positions for each of the underlying groups and subsequently aggregate the results.

| Underlying group | Market value of delta equivalent position in HKD Equivalent (A) | Beta (B) | Market value of beta hedge position (C) = (A) x (B) |
| --- | --- | --- | --- |
| 700 | -380,376,000 | 0.9 | -342,338,400 |
| 1299 | 4,199,600 | 1.1 | 4,619,560 |
| 1876 | 3,000,000 | 1.2 | 3,600,000 |
| 2823 | 30,000,000 | 1.0 | 30,000,000 |
| 3690 | 7,000,000 | 1.3 | 9,100,000 |
| | Total | | -295,018,840 |

Step 2: Calculate portfolio-level LRA with the aid of a portfolio hedging instrument.
The sample portfolio’s hedging instrument is currently set as the Tracker Fund of Hong Kong (2800.HK)³³
\[Hedging market value threshold =250,000,000\]
\[Hedging instrument bucket rate =0.002\]

³³ The Tracker Fund of Hong Kong (2800.HK) is set as the default portfolio hedging instrument and subject to change from time to time. HKSCC will issue circulars to notify the market before any change is made.

Portfolio-level liquidation risk add-on
= Maximum [0 , Absolute value of (Total market value of beta hedge position) – Hedging market value threshold] x Hedging instrument bucket rate
\[=Maximum [0,(295,018,840-250,000,000)] × 0.002 = 90,037.68 \approx 90,038\]

As a result, the liquidation risk add-on will be:
\[LRA = Instrument-level\ LRA + Portfolio-level\ LRA =176,827+90,038 =266,865\]

### 3.2.4.4 Structured Product Add-on
Structured product add-on includes structured products which
- The instrument market prices are smaller than their corresponding price thresholds (i.e., all instruments listed under FieldType 6 as per instruction in §3.2.2); and
- The instruments are under long positions.

Structured product add-on is calculated according to the steps as follows:
Step 1: Identify the position of all instruments under FieldType 6.
In the sample portfolio, InstrumentID 26883 is identified under FieldType 6 as per the table shown in §3.2.2.
As there is a positive quantity of InstrumentID 26883 (i.e., 110,000,000), the instrument is under long position and should be included in the subsequent calculation for structured product add-on³⁴.

³⁴ If the quantity of InstrumentID 26883 is negative e.g., -100 it will be excluded from the calculation of structured product add-on.

Step 2: Calculate the structured product add-on by using the formula as follows:
\[= Quantity \times Tick\ size\ multiplier ^{35} \times Minimum\ tick\ size ^{36}\]

The calculation process is shown as follows:

| InstrumentID | Quantity (A) | Tick size multiplier (B) | Minimum tick size (C) | Structured product add-on (D) = (A) x (B) x (C) |
| --- | --- | --- | --- | --- |
| 26883 | 110,000,000 | 5 | 0.001 | 550,000 |
| | Total | | | 550,000 |

³⁵ Tick size multiplier of the respective instrument is calculated by 10 times the value as shown under Column 2 of FieldType 6 in the IMRPF of that instrument (i.e., 10 x 0.5 = 5 in this illustration).
³⁶ The current minimum tick size is set as 0.001. HKSCC will notify the market before any change is made.

### 3.2.4.5 Corporate Action Position Margin
Corporate action position margin is calculated according to the steps as follows:
Step 1: Calculate the net market value of positions for each scenario under FieldType 7 identified as per instructions in §3.2.2.
The result of sample portfolio is shown as follows:

| InstrumentID | Quantity | Contract value in HKD equivalent (A) | Market value in HKD equivalent (B) | Net market value (C) = (B) - (A) |
| --- | --- | --- | --- | --- |
| DSP700 | < 0 | 0 | -4,000,000 | -4,000,000 |
| DIV1299 |  0 | -1,000,000 | 0 | 1,000,000 |
| SRI3606 |  0 | 0 | 1,000,000 | 1,000,000 |

Step 2: Apply positive net market value positions to scenario 4 under FieldType 7.
Step 3: Apply negative net market value positions to scenario 3 under FieldType 7.
Step 4: Add the results obtained from steps 2 and 3.

Corporate Action Position Margin³⁷
= Absolute value of (net market value₍DSP700₎) x scenario 3 + Absolute value of (net market value₍DIV1299₎) x scenario 4 + Absolute value of (net market value₍SRI3606₎) x scenario 4
= Absolute value of (-4,000,000 x -0.5) + Absolute value of (1,000,000 x 0) + Absolute value of (1,000,000 x 0.5)
\[=2,500,000\]

³⁷ Round off any (net market valuei x scenarioj) term to the nearest integer if the result is a decimal number.

### 3.2.4.6 Holiday Add-on³⁸
Holiday add-on only includes positions subject to portfolio margin or flat rate margin identified as per instructions in §3.2.2.
Holiday add-on is calculated according to the steps as follows:
Step 1: Calculate the base of holiday add-on by adding portfolio margin to flat rate margin.
\[Base\ of\ holiday\ add-on = Portfolio\ margin + Flat\ rate\ margin =10,000,000+15,180,000 =25,180,000\]

Step 2: Calculate holiday add-on by multiplying the base of holiday add-on by Holiday_Factor parameter³⁹.
\[Holiday\ add-on =25,180,000 × 0.7320508075=18,433,039\]

³⁸ Please note that the holiday add-on will not be applicable upon the launch of VaR Platform. HKSCC will notify CPs before the implementation.
³⁹ The Holiday_Factor parameter is 0.7320508075 which implies the number of consecutive holidays is 3. Please refer to §2.2 for the conversion methodology.

## 3.2.5 Aggregate Market Risk Components and Perform Margin Adjustments
The market risk components are aggregated with margin adjustments as follows:
- Rounding on aggregated market-risk-component margin
- Consideration on favourable MTM⁴⁰
- Application of margin credit

⁴⁰ Favorable MTM and MTM requirement are mutually exclusive. See §3.2.5.2 for details.

### 3.2.5.1 Rounding on Aggregated Market-risk-component Margin
Margin rounding is performed on all market risk components according to the steps as follows:
Step 1: Calculate aggregated margin derived from market risk components.
\[
\begin{aligned}
&Aggregated\ market-risk-component\ margin = Portfolio\ margin + Flat\ rate\ margin + Liquidation\ risk\ add-on + Structured\ product\ add-on + Corporate\ action\ position\ margin + Holiday\ add-on \\
&=10,000,000+15,180,000+266,865+550,000+2,500,000+18,433,039 = 46,929,904
\end{aligned}
\]

Step 2: Round up the aggregated margin with reference to the rounding parameter stated in the Initial Margin Risk Parameter File (e.g., 10,000 in the sample Initial Margin Risk Parameter File).
In our example, 46,929,904 is to be rounded up to the nearest 10,000.
\[Rounded\ aggregated\ market-risk-component\ margin =\underline{46,930,000}\]

### 3.2.5.2 Consideration on Favorable MTM
Favorable MTM (or MTM requirement)⁴¹ could be determined by the steps as follows:
Step 1: Calculate favorable MTM (or MTM requirement) by using the formula as follows:
Favorable MTM (or MTM requirement)⁴² = Market value₍Portfolio₎ - Contract value₍Portfolio₎
\[=(-300,550,000)-(-287,850,000) =-12,700,000\]

The negative number refers to a MTM requirement, which its absolute value will be added after applying margin credit (See §3.2.6.1). In such case, favorable MTM is zero.

Step 2: Deduct favorable MTM from rounded aggregated market-risk-component margin to derive net margin.
\[
\begin{aligned}
&Net\ margin =Maximum(0, Rounded\ aggregated\ market-risk-component\ margin - Favorable\ MTM) \\
&= Maximum [0,(46,930,000-0)] =\underline{46,930,000}
\end{aligned}
\]

⁴¹ Favorable MTM and MTM requirement are mutually exclusive. In the MTM and Margin Requirement Report, absolute value of favorable MTM (or MTM requirement) will be shown.
⁴² The aggregated value of HKD equivalent contract value and HKD equivalent market value. Numbers are rounded off on position level. Please refer to Appendix 4.6 for calculation logic that involve multiple currencies in the portfolio.

### 3.2.5.3 Application of Margin Credit
A margin credit (normally 5,000,000)⁴³ is granted to each CP and applied for margin calculation⁴⁴.
Net margin after credit is calculated as follows:
\[
\begin{aligned}
&Net\ margin\ after\ credit = Maximum [0,(Net\ margin - Margin\ credit )] \\
&= Maximum [0,(46,930,000-5,000,000)] =41,930,000
\end{aligned}
\]

⁴³ Such amount may be reduced for risk management purpose. HKSCC will notify CPs in advance.
⁴⁴ Please refer to the session “Risk Management of CNS Trades in Hong Kong Market” in HKEX website. (https://www.hkex.com.hk/Services/Clearing/Securities/Risk-Management/Risk-Management-of-CNS-Trades-in-Hong-KongMarket?sc_lang=en)

## 3.2.6 Calculate or Retrieve Other Risk Components from Report
### 3.2.6.1 MTM Requirement⁴⁵
In our example, a MTM requirement of 12,700,000 is figured out as per §3.2.5.2.

⁴⁵ Please refer to Appendix 4.7 for intra-day calculation logic.

### 3.2.6.2 Position Limit Add-on
Position limit add-on is applicable to all non-custodian CPs (See §4.1 for detailed calculation). CPs could refer to the “MTM and Margin Requirement Report” for the amount of positions limit add-on to be charged.
For illustration purpose, position limit add-on for the sample portfolio is assumed to be 487,332.

### 3.2.6.3 Credit Risk Add-on⁴⁶
Credit risk add-on is only applicable to specific CPs who will be notified by HKSCC individually. Those CPs could refer to the “MTM and Margin Requirement Report” for the amount to be charged.
For illustration purpose, credit risk add-on for the sample portfolio is assumed to be 12,000,000.

⁴⁶ Please note that the credit risk add-on will not be applicable upon the launch of VaR Platform. HKSCC will notify CPs before the implementation.

### 3.2.6.4 Ad-hoc Add-on
Ad-hoc add-on is only applicable to specific CPs who will be notified by HKSCC individually. Those CPs could refer to the “MTM and Margin Requirement Report” for the amount to be charged.
For illustration purpose, ad-hoc add-on for the sample portfolio is assumed to be 600,000.

### 3.2.7 Summary of Market Risk Components with Margin Adjustments and Other Risk Components
| Category | Item | Results in HKD equivalent |
| --- | --- | --- |
| Market risk components | Portfolio margin | 10,000,000 |
| | Flat rate margin | 15,180,000 |
| | Liquidation risk add-on | 266,865 |
| | Structured product add-on | 550,000 |
| | Corporate action position margin | 2,500,000 |
| | Holiday add-on | 18,433,039 |
| | Aggregated market-risk-component margin | 46,929,904 |
| Margin adjustments | Net margin after credit | 41,930,000 |
| Other risk components | MTM requirement | 12,700,000 |
| | Position limit add-on | 487,332 |
| | Credit risk add-on | 12,000,000 |
| | Ad-hoc add-on | 600,000 |

### 3.2.8 Derive Total MTM and Margin Requirement from Results under §3.2.5 & §3.2.6
Eventually, total MTM and margin requirement could be derived by adding the net margin after credit to other risk components.
\[
\begin{aligned}
&Total\ MTM\ and\ margin\ requirement = Net\ margin\ after\ credit + MTM\ requirement + Position\ limit\ add-on + Credit\ risk\ add-on + Ad-hoc\ add-on \\
&= 41,930,000+12,700,000+487,332+12,000,000+600,000 = \underline{67,717,332}
\end{aligned}
\]

# 4. APPENDIX
## 4.1 Detailed Calculation on Position Limit Add-on
Position limit add-on assumes hypothetical conditions as follows:
- Apportioned liquid capital of \(CP=75,000,000\)
- Liquid capital multiplier ⁴⁷=4
- Apportioned liquid capital cap⁴⁸=280,000,000
- Rounded aggregated market-risk-component margin =46,930,000
- Net margin after credit =41,930,000
- Add-on %⁴⁹=25 %

⁴⁷ Apportioned liquid capital multiplier is CP-specific. HKSCC will notify CPs before any change is made in accordance with applicable CCASS rules/operational procedures.
⁴⁸ Apportioned liquid capital cap is currently not applicable. HKSCC will issue circulars to notify the market before any change is made.
⁴⁹ The add-on% is subject to change from time to time. HKSCC will issue circulars to notify the market before any change is made.

Position limit add-on is calculated according to the steps as follows:
Step 1: Sum the market values in HKD equivalent of all positions in the portfolio as follows:

| InstrumentID | Market value in HKD equivalent |
| --- | --- |
| 658 | -60,000,000 |
| 700 | -400,000,000 |
| 1299 | 80,000,000 |
| 1876 | 3,000,000 |
| 2823 | 30,000,000 |
| 3456 | 750,000 |
| 3457 | -300,000 |
| 3606 | 30,000,000 |
| 3690 | 7,000,000 |
| 26883 | 2,000,000 |
| DSP700 | -4,000,000 |
| DIV1299 | 0 |
| SRI3606 | 1,000,000 |
| 60954 | 10,000,000 |
| Total | -300,550,000 |

Step 2: Calculate net market value (“NMV”) of the portfolio by taking absolute value in case of net short position.
\[NMV = Absolute\ value\ of\ (-300,550,000)=300,550,000\]

Step 3: Calculate position limit add-on by using the formula as follows:
\[
\begin{aligned}
&Position\ limit\ add-on = If (NMV = 0, 0, Maximum \{NMV – Minimum [(Apportioned\ liquid\ capital \times liquid\ capital\ multiplier) , Apportioned\ liquid\ capital\ cap] , 0\} / NMV \times Round\ up(Portfolio\ margin + Flat\ rate\ margin + Corporate\ action\ position\ margin + Liquidation\ risk\ add-on + Structured\ product\ add-on, Rounding\ parameter) \times If (Net\ margin\ after\ credit > 0, Add-on\%, 1+ Add-on\%)) \\
&= Maximum \{300,550,000 – Minimum [(75,000,000 \times 4) , 280,000,000] , 0\} / 300,550,000 \times Round\ up(28,496,865 , 10,000) \times 25\% \\
&= Maximum [(300,550,000 – 280,000,000) , 0] / 300,550,000 \times 28,500,000 \times 25\% \\
&= 20,550,000 / 300,550,000 \times 28,500,000 \times 25\% = 487,332
\end{aligned}
\]
(rounded off to the nearest integer for decimal numbers)

## 4.2 Guarantee Fund Risk Collateral
Guarantee Fund Risk Collateral, a.k.a. default fund add-on, is the amount of Expected Uncollateralised Loss (EUL) of the CP group in excess of 50% of the Guarantee Fund threshold that will be collected from the CPs of the concerned CP group should the overall Guarantee Fund size reached the Guarantee Fund threshold. Guarantee Fund Risk Collateral for each of the CPs will be proportional to their share of the EUL of the CP Group. Please note that it will not be aggregated to total MTM and margin requirement.

Definition refer to CCASS Operational Procedures §10.11 is as follows:
\[Guarantee\ Fund\ risk\ collateral = Guarantee\ Fund\ expected\ uncollateralised\ loss^{50} - Guarantee\ Fund\ risk\ predefined\ limit^{51}\]

⁵⁰ CP can refer to the field “Daily EUL” in Default Fund Requirement Report (“RMADF01”).
⁵¹ The current Guarantee Fund risk pre-defined limit is HKD3,650,000,000. HKSCC will issue circulars to notify the market before any change is made.

## 4.3 Specific Stock / Cash Collateral Position Cover
Positions covered by Specific Stock Collateral (“SSC”) or Specific Cash Collateral (“SCC”) shall be excluded from the MTM and margin requirement calculation. Please note that SSC and SCC could only be arranged to cover positions prior to the settlement date (i.e., Current business date < Settlement date) and capped by the position quantity / position amount. Any excess collateral⁵² will be ignored.

⁵² Any excess SSC pledged will not be on-hold by CCMS. SCC will be collected in full amount by CCMS according to the CP’s input even the input amount is in excess to the position amount. Excess SCC will be refunded to the CP in next business day.

### 4.3.1 Specific Stock Collateral for Short Position
SSC are pledged in CCMS according to the corresponding settlement counter stock code⁵³ and settlement date. Position cover follows the same manner.

⁵³ Different currency counters of a multi-counter eligible security would share the same settlement counter stock code.

Supposing a CP holds short positions with \(Quantity <0\) on 5 Nov 2019:
**Current business date: 05-Nov-2019**

| Trade date | Settlement date | Stock code | Quantity | Amount ⁵⁴ | Currency | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| 04-Nov-2019 | 06-Nov-2019 | 5 | -4,000 | -240,000 | HKD | |
| 01-Nov-2019 | 05-Nov-2019 | 388 | -1,500 | -360,000 | HKD | |
| 04-Nov-2019 | 06-Nov-2019 | 700 | -1,000 | -300,000 | HKD | Multi-counter eligible security of settlement counter stock code 700. Average position price HKD 300 |
| 04-Nov-2019 | 06-Nov-2019 | 700 | -10 | 2,700 ⁵⁵ | CNY | Multi-counter eligible security of settlement counter stock code 700. Average position price HKD 297 assuming CNY 1 equals HKD 1.1 |
| 04-Nov-2019 | 06-Nov-2019 | 941 | -1,000 | -65,000 | HKD | Multi-counter eligible security of settlement counter stock code 941. Average position price HKD 65 |
| 04-Nov-2019 | 06-Nov-2019 | 941 | -1,000 | -60,000 | CNY | Multi-counter eligible security of settlement counter stock code 941. Average position price HKD 66 assuming CNY 1 equals HKD 1.1 |
| 05-Nov-2019 | 07-Nov-2019 | 2828 | -2,000 | -120,000 | HKD | |

⁵⁴ Contract values of position. Negative value means it is a receivable for CP, vice versa.
⁵⁵ This is an abnormal position with a short position and a payable amount. However, SSC remains applicable to such position.

Supposing the CP tries to pledge a quantity of 1,500 for each of the following stocks, 5, 700, 941 and 2828, multi-counter eligible securities are considered the same stock, as per the same settlement date as SSC, the **covered positions** are shown as follows:
**Current business date: 05-Nov-2019**

| Trade date | Settlement date | Stock code | Quantity | Amount | Currency | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| 04-Nov-2019 | 06-Nov-2019 | 5 | -1,500 | -90,000 | HKD | Pro-rata cover on amount based on covered quantity |
| 04-Nov-2019 | 06-Nov-2019 | 700 | -1,000 | -300,000 | HKD | The position is covered before 700 in CNY because of higher average position price. 500 quantity of 700 stock collateral remaining |
| 04-Nov-2019 | 06-Nov-2019 | 700 | -10 | 2,700 | CNY | The position is covered after 700 in HKD because of lower average position price. 490 quantity of 700 stock collateral remaining The position is fully covered. Excess collateral is ignored. |
| 04-Nov-2019 | 06-Nov-2019 | 941 | -500 | -32,500 | HKD | The position is covered after 941 in CNY because of lower average position price. Partial covered 500 quantity. |
| 04-Nov-2019 | 06-Nov-2019 | 941 | -1,000 | -60,000 | CNY | The position is covered before 941 in HKD because of higher average position price. 500 quantity of 941 stock collateral remaining |
| 05-Nov-2019 | 07-Nov-2019 | 2828 | -1,500 | -90,000 | HKD | Pro-rata cover on amount based on covered quantity |

The resulting **uncovered positions** are shown as follows:

| Trade date | Settlement date | Stock code | Quantity | Amount | Currency | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| 04-Nov-2019 | 06-Nov-2019 | 5 | -2,500 | -150,000 | HKD | Pro-rata reduction on amount based on covered quantity |
| 01-Nov-2019 | 05-Nov-2019 | 388 | -1,500 | -360,000 | HKD | Not allowed to be covered as Settlement Date = Business Date |
| 04-Nov-2019 | 06-Nov-2019 | 700 | 0 | 0 | HKD | The position is fully covered. Excess collateral is ignored. |
| 04-Nov-2019 | 06-Nov-2019 | 700 | 0 | 0 | CNY | The position is fully covered. Excess collateral is ignored. |
| 04-Nov-2019 | 06-Nov-2019 | 941 | -500 | -32,500 | HKD | The position is covered after 941 in CNY because of lower average position price |
| 04-Nov-2019 | 06-Nov-2019 | 941 | 0 | 0 | CNY | The position is covered before 941 in HKD because of higher average position price. |
| 05-Nov-2019 | 07-Nov-2019 | 2828 | -500 | -30,000 | HKD | Pro-rata reduction on amount based on covered quantity |

In case of a half trading day (e.g. 24 Dec 2019), for each stock, there could be 2 positions with different trade dates but having the same settlement date.
If both the positions have \(quantity <0\) , then the position with higher position average price will be covered first (i.e., Position average price = Absolute value of (Amount / Quantity)).
Nevertheless, if there are two positions, one with \(quantity >0\) while the other one with \(quantity <0\) , only the one with \(quantity <0\) will undergo the position cover before cross-day position netting.

**Example of half trading day position cover**:
Current business date: 24-Dec-2019

| Trade date | Settlement date | Stock code | Currency | Quantity | Amount (HKD equivalent) | Average price (HKD equivalent) |
| --- | --- | --- | --- | --- | --- | --- |
| 23-Dec-2019 | 30-Dec-2019 | 5 | HKD | -4,000 | -240,000 | 60 |
| 24-Dec-2019 | 30-Dec-2019 | 5 | HKD | 2,000 | 126,000 | 63 |
| 23-Dec-2019 | 30-Dec-2019 | 700 | HKD | -1,000 | -330,000 | 330 |
| 24-Dec-2019 | 30-Dec-2019 | 700 | CNY | -2,000 | -720,000 | 360 |

Supposing the CP tries to pledge a quantity of 2,500 for each of the stocks, i.e. 5 and 700, the resulting **uncovered positions** are shown as follows:

| Trade date | Settlement date | Stock code | Currency | Quantity | Amount | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| 23-Dec- 2019 | 30-Dec-2019 | 5 | HKD | -1,500 | -90,000 | Pro-rata reduction on amount based on covered quantity |
| 24-Dec- 2019 | 30-Dec-2019 | 5 | HKD | 2,000 | 126,000 | SSC is not accepted as quantity > 0 |
| 23-Dec- 2019 | 30-Dec-2019 | 700 | HKD | -500 | -165,000 | Because of the lower position average price, this position is covered by the remaining SSC in the quantity of 500. Pro-rata reduction on amount based on covered quantity. |
| 24-Dec- 2019 | 30-Dec-2019 | 700 | CNY | 0 | 0 | Because of the higher position average price, this position is firstly covered by the SSC in the quantity of 2,500. The position is fully covered. Excess collateral (i.e., 500) is ignored. |

The resulting positions after SSC position cover will be used for deriving the marginable position for MTM and margin requirement calculation.

### 4.3.2 Specific Cash Collateral Position Cover
SCC are arranged in CCMS according to corresponding settlement counter stock code⁵⁶, currency and trade date. Position cover follows the same manner.

⁵⁶ Different currency counters of a multi-counter eligible security would share the same settlement counter stock code.

Supposing a CP holds some long positions with \(Quantity >0\) and \(Amount >0\) on 5 Nov 2019:
**Current business date: 05-Nov-2019**

| Trade date | Settlement date | Stock code | Quantity | Amount | Currency |
| --- | --- | --- | --- | --- | --- |
| 04-Nov-2019 | 06-Nov-2019 | 5 | 4,000 | 240,000 | HKD |
| 01-Nov-2019 | 05-Nov-2019 | 388 | 1,500 | 360,000 | HKD |
| 04-Nov-2019 | 06-Nov-2019 | 700 | 100 | 30,000 | HKD |
| 05-Nov-2019 | 07-Nov-2019 | 5 | 2,000 | 180,000 | HKD |

Supposing the CP tries to arrange $60,000 for each of the stocks as per the same trade date as SCC, the resulting **uncovered positions** are shown as follows:

| Trade date | Settlement date | Stock code | Quantity | Amount | Currency | Remarks |
| --- | --- | --- | --- | --- | --- | --- |
| 04-Nov-2019 | 06-Nov-2019 | 5 | 3,000 | 180,000 | HKD | Pro-rata reduction on Quantity based on covered Amount |
| 01-Nov-2019 | 05-Nov-2019 | 388 | 1,500 | 360,000 | HKD | Not allowed to be covered as SCC is arranged on Settlement Date = Business Date |
| 04-Nov-2019 | 06-Nov-2019 | 700 | 0 | 0 | HKD | The position is fully covered. Excess collateral is ignored. |
| 05-Nov-2019 | 07-Nov-2019 | 5 | 1,334 | 120,000 | HKD | Pro-rata reduction on Quantity based on covered Amount |

The resulting positions after SCC position cover will be used for deriving the marginable position for MTM and margin requirement calculation.

## 4.4 Combine multi-counter eligible securities positions
Positions traded on the different currency counters of a multi-counter eligible security should be combined into a single risk position expressed in terms of the settlement counter⁵⁷ for risk calculation. Please note that the combination of multi-counter eligible securities positions should be performed after considering SSC / SCC.

⁵⁷ HKSCC would review the risk currency to be used for the multi-counter eligible securities from time to time and will issue circulars to notify the market before any change is made.

**Example**:
Business date: 3-Jun-2024

| Trade date | Settlement date | Traded Stock code | Quantity | Amount⁵⁸ | Currency | Risk Currency |
| --- | --- | --- | --- | --- | --- | --- |
| 3-Jun-2024 | 5-Jun-2024 | 388 | -1,000 | -300,000 | HKD | HKD |
| 3-Jun-2024 | 5-Jun-2024 | 388 | 2,500 | 675,000 | CNY | HKD |
| 3-Jun-2024 | 5-Jun-2024 | 700 | 500 | 150,000 | HKD | HKD |
| 3-Jun-2024 | 5-Jun-2024 | 700 | -1,000 | -270,000 | CNY | HKD |

⁵⁸ Contract values of position. Negative value means it is a receivable for CP, vice versa.

**Settlement counter stock codes**: 388, 700
\[FX^{59}: CNY 1= HKD 1.1\]
\[FX haircut CNY-HKD ^{59}=3 \%\]

⁵⁹ The same FX and FX haircut rate apply for (i) combining multi-counter eligible securities positions into risk currency of HKD and (ii) converting FX for marks and margin requirement to CNY for collection from ChinaClear. The CNY-HKD FX haircut rate for ChinaClear would reference to the base haircut rate applicable to HK market:
- Normal scenario: Haircut (ChinaClear) = Base haircut + 1% buffer
- Extreme scenario (i.e. base haircut =4.45% ): HKSCC would increase the buffer to 1.2% or higher (+0.2% for each increment)
*Note: On a monthly basis, HKSCC would notify ChinaClear in advance on the haircut rate to be effective.*

The **combined risk positions** would be:

| Trade date | Settlement date | Stock code | Quantity | Amount | Currency |
| --- | --- | --- | --- | --- | --- |
| 3-Jun-2024 | 5-Jun-2024 | 388 | -1,000 +2,500 =1,500 | -300,000 +675,000 * 1.1*(1+3%) = 464,775 | HKD |
| 3-Jun-2024 | 5-Jun-2024 | 700 | 500 -1,000 =-500 | 150,000 -270,000*1.1 *(1-3%) =-138,090 | HKD |

*Positions with a payable contract value would subject to a positive FX haircut to magnify it while positions with a receivable contract value would subject to a negative FX haircut to diminish it when converting the contract values into the risk currency.*

The resulting positions after the combination of multi-counter eligible securities positions will be used for deriving the marginable position for MTM and margin requirement calculation.

## 4.5 Corporate Action Position Adjustment
When an instrument (a stock) undergoes corporate action(s), it is possible that some benefit entitlements would be distributed to the CPs (shareholders) or would cause a change in number of shares. The market price of the instrument would react to such kind of corporate actions since the ex-date and therefore the original traded positions should be adjusted to capture the changes. It is also possible that more than one corporate action will appear for the same instrument on the different ex-dates. In this case, each corporate action shall be adjusted separately according the trade date of the position. Please note that all corporate action position adjustments should be performed after the combination of multi-counter eligible securities positions.

There are five types of corporate actions that require position adjustment⁶⁰:
- Bonus share / Stock split / Stock consolidation
- Cash dividend
- Stock dividend
- Rights issue / Open offer
- Stock conversion

⁶⁰ Round down to integer for positive position quantity. Round up to integer for negative position quantity.

A “Corporate Action Position Adjustment Report” will be generated in csv format and could be downloaded by CPs on each business day⁶¹. The layout of the file is shown below:

| Business Date | Ex-Date | Market | Instrument Code | Converted Instrument Code | Quantity Conversion Ratio | Instrument Code for Cash Dividend | Cash Dividend Amount | Instrument Code for Stock Dividend | Entitled Stock Quantity | Instrument Code for Rights | Rights Quantity |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 05/11/2019 | 05/11/2019 | HKMK | 5 | 5 | 2 | DIV5 | -0.78 | DSPS | 0.13 | SRI5 | 1.5 |
| 05/11/2019 | 05/11/2019 | HKMK | 8359 | 150 | 1 | | | | | | |

⁶¹ The dissemination time is around 10:00 a.m. HKT subject to system finalization.

### Corporate Action Position Adjustment Report specification
| Field Name | Description | Format |
| --- | --- | --- |
| Business Date | Report generation date | DD/MM/YYYY |
| Ex-Date | Market ex-date of the corporate action. Only the positions traded before ex-date will be subject to corporate action adjustment | YYYYMMDD |
| Market | Market of the instrument | TEXT (30) |
| Instrument Code | Instrument identifier for the corporate action announcement stock | TEXT (20) |
| Converted Instrument Code | Instrument identifier for the corporate action announcement stock after the corporate action that would change Instrument Code or position quantity | TEXT (10) |
| Quantity Conversion Ratio | Position quantity conversion ratio used for Bonus share / Stock split / Stock consolidation / Stock conversion. | DECIMALS (X,10); e.g., a value of 2 means every 1 position quantity held before the corporate action will be adjusted to 2 after the corporate action |
| Instrument Code for Cash Dividend | Instrument identifier for cash dividend | TEXT (23); e.g. a label of DIV5 means a cash dividend distributed by the stock of instrument code 5 |
| Cash Dividend Amount | Cash dividend amount in HKD equivalent | DECIMALS (X,10); e.g., a value of -0.78 means every 1 position quantity held before the corporate action will be entitled to HKD 0.78 cash dividend |
| Instrument Code for Stock Dividend | Instrument identifier for stock dividend | TEXT (23); e.g. a label of DSP5 means a stock dividend distributed by the stock of instrument code 5 |
| Entitled Stock Quantity | Entitled stock quantity | DECIMALS (X,10); e.g., a value of 0.13 means every 1 position quantity held before the corporate action will be entitled to 0.13 quantity of the stock dividend |
| Instrument Code for Rights | Instrument identifier for Rights issue / Open offer | TEXT (23); e.g. a label of SRI5 means a rights issue distributed by the stock of instrument code 5 |
| Rights Quantity | Rights quantity | DECIMALS (X,10); e.g., a value of 1.5 means every 1 position quantity held before the corporate action will be entitled to 1.5 quantity of the rights issue |

### 4.5.1 Position Quantity Adjustment for Bonus Share / Stock Split / Stock Consolidation
**Example**: Corporate Action Report entry for stock split (Instrument 5, conversion ratio=2)
Supposing a CP trades instrument 5 with the following original positions:

| Trade date | Instrument code (X) | Quantity (Y) | Contract value (Z) |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400 | 24,000 |
| 05/11/2019 | 5 | -600 | -20,000 |

Only the position traded **before ex-date (04/11/2019)** is subject to the position quantity adjustment. New quantity = original quantity × conversion ratio; contract value remains unchanged.

**Adjusted positions**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400×2=800 | 24,000 |
| 05/11/2019 | 5 | -600 | -20,000 |

*Note: Please repeat the position adjustment if more than one corporate actions with different ex-dates for the same instrument are required.*

### 4.5.2 Create Benefit Entitlement Position for Cash Dividend
**Example**: Corporate Action Report entry for cash dividend (Instrument 5, DIV5, amount=-0.78)
Original positions for Instrument 5 (same as above). Only the position traded before ex-date is required to create the cash dividend benefit position:
- Instrument code = Cash Dividend Code (DIV5)
- Quantity = 0 (fixed for cash dividend)
- Contract value = original quantity × cash dividend amount

**Adjusted positions**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400 | 24,000 |
| 04/11/2019 | DIV5 | 0 | 400×(-0.78) = -312 |
| 05/11/2019 | 5 | -600 | -20,000 |

### 4.5.3 Create Benefit Entitlement Position for Stock Dividend
**Example**: Corporate Action Report entry for stock dividend (Instrument 5, DSP5, entitled quantity=0.13)
Original positions for Instrument 5 (same as above). Only the position traded before ex-date is required to create the stock dividend benefit position:
- Instrument code = Stock Dividend Code (DSP5)
- Quantity = original quantity × entitled stock quantity
- Contract value = 0 (fixed for stock dividend)

**Adjusted positions**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400 | 24,000 |
| 04/11/2019 | DSP5 | 400×0.13=52 | 0 |
| 05/11/2019 | 5 | -600 | -20,000 |

### 4.5.4 Create Benefit Entitlement Position for Rights Issue / Open Offer
**Example**: Corporate Action Report entry for rights issue (Instrument 5, SRI5, rights quantity=1.5)
Original positions for Instrument 5 (same as above). Only the position traded before ex-date is required to create the rights issue benefit position:
- Instrument code = Rights Code (SRI5)
- Quantity = original quantity × rights quantity
- Contract value = 0 (fixed for rights issue)

**Adjusted positions**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400 | 24,000 |
| 04/11/2019 | SRI5 | 400×1.5=600 | 0 |
| 05/11/2019 | 5 | -600 | -20,000 |

### 4.5.5 Combined Effects on Position Adjustment for Combination of Corporate Actions
**Example**: Combined corporate actions (stock split + cash dividend + stock dividend + rights issue) for Instrument 5 (conversion ratio=2, cash dividend amount=-0.78, entitled stock quantity=0.13, rights quantity=1.5)
Supposing a CP trades instrument 5 with the following original positions:

| Trade date | Instrument code (X) | Quantity (Y) | Contract value (Z) |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 400 | 24,000 |
| 05/11/2019 | 5 | -600 | -20,000 |

Only the position traded **before ex-date (04/11/2019)** is subject to position quantity adjustment and benefit entitlement creation. The adjustments follow the same rules as individual corporate actions:
1. **Position quantity adjustment**: Original quantity × conversion ratio (400×2=800)
2. **Cash dividend position**: DIV5, quantity=0, contract value=original quantity×cash dividend amount (400×(-0.78)=-312)
3. **Stock dividend position**: DSP5, quantity=original quantity×entitled stock quantity (400×0.13=52), contract value=0
4. **Rights issue position**: SRI5, quantity=original quantity×rights quantity (400×1.5=600), contract value=0

**Adjusted positions**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 5 | 800 | 24,000 |
| 04/11/2019 | DIV5 | 0 | -312 |
| 04/11/2019 | DSP5 | 52 | 0 |
| 04/11/2019 | SRI5 | 600 | 0 |
| 05/11/2019 | 5 | -600 | -20,000 |

*Note: Please repeat the position adjustment if more than one corporate actions with different ex-dates for the same instrument are required.*

### 4.5.6 Position Adjustment for Stock Conversion
**Example**: Corporate Action Report entry for stock conversion (Instrument 8359 → Converted Instrument 150, conversion ratio=1)
Supposing a CP trades instrument 8359 with the following original position:

| Trade date | Instrument code (X) | Quantity (Y) | Contract value (Z) |
| --- | --- | --- | --- |
| 04/11/2019 | 8359 | 5,000 | 6,650 |

Only the position traded **before ex-date (04/11/2019)** is subject to adjustment:
- Instrument code = Converted Instrument Code (150)
- New quantity = original quantity × conversion ratio (5,000×1=5,000)
- Contract value remains unchanged (6,650)

**Adjusted position**:
| Trade date | Instrument code | Quantity | Contract value |
| --- | --- | --- | --- |
| 04/11/2019 | 150 | 5,000 | 6,650 |

## 4.6 Cross-day Position Netting
For margin calculation, CPs’ positions will be netted across days at instrument level. Thus, all positions quantities and contract values of the same instrument with different trade dates, settlement dates will be added together to come up with one cross-day netted quantity and contract value for each instrument. Please note that all cross-day position netting should be performed after considering SSC / SCC and corporate action adjustments.

**Example**:
CP’s positions before cross-day netting (Instrument 5, unsettled):

| Trade date | Settlement date | Instrument Code (A) | Quantity (B) | Contract value (C) |
| --- | --- | --- | --- | --- |
| 01-Nov-2019 | 05-Nov-2019 | 5 | 400 | 24,000 |
| 04-Nov-2019 | 06-Nov-2019 | 5 | -800 | -49,600 |
| 05-Nov-2019 | 07-Nov-2019 | 5 | 1200 | 73,200 |

**Cross-day netted position**:
| Instrument Code (D) = Grouped by (A) | Quantity (E) = Sum of (B) | Contract value (F) = Sum of (C) |
| --- | --- | --- |
| 5 | 400 + (-800) + 1200 = 800 | 24,000 + (-49,600) + 73,200 = 47,600 |

**Marginable position** (market price of Instrument 5 = HKD70):
| Instrument Code (D) | Quantity (E) | Contract value (F) | Market value (G)=(E) × Market price |
| --- | --- | --- | --- |
| 5 | 800 | 47,600 | 800×70=56,000 |

## 4.7 Cross-currency Netting on MTM Requirement
Favorable MTM / MTM requirement on positions will always be netted off against each other on its risk currency first. If there is net favorable MTM in one currency, it could be used to offset against the net MTM requirement in other currencies. The net favorable MTM in original currency is converted to HKD equivalent by using the exchange rate with haircut applied to mark down the amount. The net MTM requirement in original currency is converted to HKD equivalent by using the exchange rate with haircut applied to mark up the amount.

**Example**: Two CPs (A and B) are counterparties on all positions.
### Clearing Participant A
| Instrument Code | Position long/ (short) quantity | Position contract value | Risk Currency | Instrument price⁶² | Position market value | MTM | FX rate⁶³ | Haircut rate⁶⁴ |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | 100 | 40,000 | HKD | 380 | 38,000 | -2,000 | 1 | 0 |
| 80737 | -5,000 | -15,000 | CNY | 3.5 | -17,500 | 2,500 | 1.15 | 3% |
| 3188 | -600 | -25,200 | CNY | 40 | -24,000 | -1,200 | 1.15 | 3% |
| 3167 | 100 | 900 | USD | 9.5 | 950 | -50 | 7.8 | 1% |

⁶² For multi-counter eligible securities, the price should refer to the counter of risk currency.
⁶³ HKEX plans to provide the information in a separate file to facilitate relevant calculation.
⁶⁴ Please refer to Collateral Parameters Information List (“CCMIR02”).

**MTM calculation (HKD equivalent)**:
\[
\begin{aligned}
&= MTM_{HKD} + [Net\ MTM_{CNY} × FX\ rate × (1+Haircut\ rate)] + [Net\ MTM_{USD} × FX\ rate × (1-Haircut\ rate)] \\
&= (-2,000) + [(2,500-1,200) ×1.15×1.03] + [(-50)×7.8×0.99] \\
&= -2,000 + (1,300×1.1845) + (-50×7.722) \\
&= -2,000 + 1,539.85 - 386.1 \\
&= -846.25
\end{aligned}
\]
- Favorable MTM for Clearing Participant A = HKD0 (negative MTM = MTM requirement)
- MTM requirement for Clearing Participant A = HKD846 (rounded up)

### Clearing Participant B (counterparty of A)
| Instrument Code | Position long/ (short) quantity | Position contract value | Risk Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | -100 | -40,000 | HKD | 380 | -38,000 | 2,000 | 1 | 0 |
| 80737 | 5,000 | 15,000 | CNY | 3.5 | 17,500 | -2,500 | 1.15 | 3% |
| 3188 | 600 | 25,200 | CNY | 40 | 24,000 | 1,200 | 1.15 | 3% |
| 3167 | -100 | -900 | USD | 9.5 | -950 | 50 | 7.8 | 1% |

**MTM calculation (HKD equivalent)**:
\[
\begin{aligned}
&= MTM_{HKD} + [Net\ MTM_{CNY} × FX\ rate × (1-Haircut\ rate)] + [Net\ MTM_{USD} × FX\ rate × (1+Haircut\ rate)] \\
&= 2,000 + [(-2,500+1,200) ×1.15×0.97] + [(50)×7.8×1.01] \\
&= 2,000 + (-1,300×1.1155) + (50×7.878) \\
&= 2,000 - 1,450.15 + 393.9 \\
&= 943.75
\end{aligned}
\]
- Favorable MTM for Clearing Participant B = HKD944 (rounded up)
- MTM requirement for Clearing Participant B = HKD0

## 4.8 Intra-day MTM Requirement Calculation
Upon the launch of VaR Platform, there would be a scheduled intra-day MTM run at around 11:00 a.m. HKT on each business day. There would also be another round of intra-day MTM run at around 2:00 p.m. HKT if there is a holiday margin call arrangement on the full trading day before long holiday⁶⁵.

⁶⁵ HKSCC will identify the applicable long holiday and issue circulars to notify the market in advance.

There are multiple batch settlement runs in CCASS to settle the stock positions during the day. CPs could deliver stocks to settle their short positions. CPs could also arrange cash prepayments and withdraw the settled long positions resulting allocated shares intra-day. All these settlement activities would result in a change in marginable positions for MTM and margin calculation.

### 4.8.1 Intra-day MTM Requirement Calculation (11:00 a.m. HKT)
Since the settlement of stock positions occurs during intra-day while money settlement occurs at day-end, unposted debit and unposted credit would be resulted during intra-day MTM requirement calculation to reflect the outstanding risk exposure.
- Unposted debit: The pending collection amount from the CP resulting from the settled stock positions that the counterparty has delivered.
- Unposted credit: The pending refund amount to the CP resulting from the settled stock positions that the CP has delivered.

Unposted debit has to be included as a marginable long position during intra-day MTM requirement calculation. While for any unposted credit and cash prepayment arranged by the CPs, an offset ratio will be calculated to adjust the existing marginable long positions.

**Example**: Two CPs (A and B) are counterparties; positions #700 and #9167 are to be settled today.
- CP B delivered 50 shares of #700 → Unposted debit (HKD20,000) for CP A; Unposted credit (HKD20,000) for CP B.
- CP A made cash prepayment (HKD11,755) → Covers 25% of total gross payable settlement amount (HKD47,020) → Offset ratio=25%.
- CP B’s unposted credit (HKD20,000) → Covers 100% of total gross payable settlement amount (HKD17,250) → Offset ratio=100%.

#### Clearing Participant A
**Marginable positions before cash prepayment offset**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | 100 | 20,000 | HKD | 380 | 38,000 | -18,000 | 1 | 0 | Y |
| 80737 | -5,000 | -15,000 | CNY | 3.5 | -17,500 | 2,500 | 1.15 | 3% | N |
| 9167 | 100 | 900 | USD | 9.5 | 950 | -50 | 7.8 | 1% | Y |
| Unposted debit | 0 | 20,000 | HKD | 0 | 0 | 20,000 | 1 | 0 | Y |

**Marginable positions after cash prepayment offset (offset ratio=25%)**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | 100×(1-25%)=75 | 20,000×(1-25%)=15,000 | HKD | 380 | 28,500 | -13,500 | 1 | 0 | Y |
| 80737 | -5,000 | -15,000 | CNY | 3.5 | -17,500 | 2,500 | 1.15 | 3% | N |
| 9167 | 100×(1-25%)=75 | 900×(1-25%)=675 | USD | 9.5 | 712.5 | -37.5 | 7.8 | 1% | Y |
| Unposted debit | 0 | 20,000×(1-25%)=15,000 | HKD | 0 | 0 | 15,000 | 1 | 0 | Y |

**MTM calculation (HKD equivalent)**:
\[
\begin{aligned}
&= (MTM_{700} + MTM_{Unposted\ debit}) + [MTM_{80737} × FX\ rate × (1+Haircut\ rate)] + [MTM_{9167} × FX\ rate × (1-Haircut\ rate)] \\
&= (-13,500 + 15,000) + (2,500×1.15×1.03) + (-37.5×7.8×0.99) \\
&= 1,500 + 2,961.25 - 293.025 \\
&= 4,168.225
\end{aligned}
\]
- Favorable MTM for Clearing Participant A = HKD0
- MTM requirement for Clearing Participant A = HKD4,168 (rounded up)

#### Clearing Participant B
**Marginable positions before unposted credit offset**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | -50 | -20,000 | HKD | 380 | -19,000 | -1,000 | 1 | 0 | Y |
| 80737 | 5,000 | 15,000 | CNY | 3.5 | 17,500 | -2,500 | 1.15 | 3% | Y |
| 9167 | -100 | -900 | USD | 9.5 | -950 | 50 | 7.8 | 1% | Y |

**Marginable positions after unposted credit offset (offset ratio=100%)**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | -50 | -20,000 | HKD | 380 | -19,000 | -1,000 | 1 | 0 | Y |
| 80737 | 5,000×(1-100%)=0 | 15,000×(1-100%)=0 | CNY | 3.5 | 0 | 0 | 1.15 | 3% | Y |
| 9167 | -100 | -900 | USD | 9.5 | -950 | 50 | 7.8 | 1% | Y |

**MTM calculation (HKD equivalent)**:
\[
\begin{aligned}
&= MTM_{700} + [MTM_{80737} × FX\ rate × (1-Haircut\ rate)] + [MTM_{9167} × FX\ rate × (1+Haircut\ rate)] \\
&= -1,000 + (0×1.15×0.97) + (50×7.8×1.01) \\
&= -1,000 + 0 + 393.9 \\
&= -606.1
\end{aligned}
\]
- Favorable MTM for Clearing Participant B = HKD606 (rounded up)
- MTM requirement for Clearing Participant B = HKD0

### 4.8.2 Intra-day MTM Requirement Calculation (2:00 p.m. HKT)
Since the collection time of the intra-day MTM and the settlement obligation are the same upon the launch of VaR Platform, any stock position to be settled today including unposted debit, unposted credit, cash prepayment and allocated shares are excluded from the intra-day MTM and margin requirement calculation to avoid the collection of MTM and margin requirement from those positions which will be settled at the time of collection.

#### Clearing Participant A
**Marginable positions before excluding due positions**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | 100 | 20,000 | HKD | 380 | 38,000 | -18,000 | 1 | 0 | Y |
| 80737 | -5,000 | -15,000 | CNY | 3.5 | -17,500 | 2,500 | 1.15 | 3% | N |
| 9167 | 100 | 900 | USD | 9.5 | 950 | -50 | 7.8 | 1% | Y |
| Unposted debit | 0 | 20,000 | HKD | 0 | 0 | 20,000 | 1 | 0 | Y |

**Marginable positions after excluding due positions**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80737 | -5,000 | -15,000 | CNY | 3.5 | -17,500 | 2,500 | 1.15 | 3% | N |

**MTM calculation (HKD equivalent)**:
\[= 2,500 ×1.15×1.03 = 2,961.25\]
- Favorable MTM for Clearing Participant A = HKD0
- MTM requirement for Clearing Participant A = HKD2,961 (rounded up)

#### Clearing Participant B
**Marginable positions before excluding due positions**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 700 | -50 | -20,000 | HKD | 380 | -19,000 | -1,000 | 1 | 0 | Y |
| 80737 | 5,000 | 15,000 | CNY | 3.5 | 17,500 | -2,500 | 1.15 | 3% | N |
| 9167 | -100 | -900 | USD | 9.5 | -950 | 50 | 7.8 | 1% | Y |

**Marginable positions after excluding due positions**:
| Instrument Code | Position long/ (short) quantity | Position contract value | Currency | Instrument price | Position market value | MTM | FX rate | Haircut rate | Due today |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 80737 | 5,000 | 15,000 | CNY | 3.5 | 17,500 | -2,500 | 1.15 | 3% | N |

**MTM calculation (HKD equivalent)**:
\[= -2,500 ×1.15×0.97 = -2,788.75\]
- Favorable MTM for Clearing Participant B = HKD2,789 (rounded up)
- MTM requirement for Clearing Participant B = HKD0