# Difference Analysis Report Template

## Overview

This template is used to document and analyze differences between the marker LLM output and the checker LLM validation results. It provides a structured format for identifying discrepancies, assessing risks, and offering optimization suggestions.

## Report Header

**Report Date:** [YYYY-MM-DD]
**Validation Scope:** [Prompt 6 / Prompt 7 / Both]
**Marker LLM Model:** [Model Name]
**Checker LLM Model:** [Model Name]
**Confidence Level:** [0-5]

## 1. Executive Summary

**Overall Status:** [PASS / FAIL / PARTIAL]
**Key Findings:**
- [Key finding 1]
- [Key finding 2]
- [Key finding 3]

**Recommended Actions:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

## 2. Difference Identification

### 2.1 Structural Differences

| Category | Marker Output | Checker Expected | Severity | Location |
|----------|---------------|------------------|----------|----------|
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |

### 2.2 Content Differences

| Category | Marker Output | Checker Expected | Severity | Location |
|----------|---------------|------------------|----------|----------|
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |

### 2.3 Reference Differences

| Category | Marker Output | Checker Expected | Severity | Location |
|----------|---------------|------------------|----------|----------|
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |
| [Category] | [Marker Content] | [Expected Content] | [Critical/Major/Minor] | [File:Line] |

## 3. Risk Analysis

### 3.1 Impact Assessment

| Risk ID | Description | Impact | Likelihood | Severity | Mitigation Strategy |
|---------|-------------|--------|------------|----------|---------------------|
| R-001 | [Risk Description] | [Impact Description] | [High/Medium/Low] | [High/Medium/Low] | [Mitigation Strategy] |
| R-002 | [Risk Description] | [Impact Description] | [High/Medium/Low] | [High/Medium/Low] | [Mitigation Strategy] |

### 3.2 Compliance Risks

- [Compliance risk 1]
- [Compliance risk 2]
- [Compliance risk 3]

### 3.3 Operational Risks

- [Operational risk 1]
- [Operational risk 2]
- [Operational risk 3]

## 4. Optimization Analysis

### 4.1 Structural Improvements

| Improvement ID | Description | Implementation Effort | Expected Benefit | Priority |
|----------------|-------------|----------------------|------------------|----------|
| IMP-001 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |
| IMP-002 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |

### 4.2 Content Improvements

| Improvement ID | Description | Implementation Effort | Expected Benefit | Priority |
|----------------|-------------|----------------------|------------------|----------|
| IMP-003 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |
| IMP-004 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |

### 4.3 Reference Improvements

| Improvement ID | Description | Implementation Effort | Expected Benefit | Priority |
|----------------|-------------|----------------------|------------------|----------|
| IMP-005 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |
| IMP-006 | [Improvement Description] | [Low/Medium/High] | [Description] | [High/Medium/Low] |

## 5. Passed Content Preservation

### 5.1 Passed Test Cases

| Test Case ID | Status | Reason for Passing |
|-------------|--------|--------------------|
| [Test Case ID] | PASSED | [Reason] |
| [Test Case ID] | PASSED | [Reason] |

### 5.2 Passed BDD Scenarios

| BDD Scenario ID | Status | Reason for Passing |
|----------------|--------|--------------------|
| [BDD Scenario ID] | PASSED | [Reason] |
| [BDD Scenario ID] | PASSED | [Reason] |

### 5.3 Preservation Guidelines

- [Guideline 1: How to preserve passed content]
- [Guideline 2: How to avoid modifying passed content]
- [Guideline 3: How to integrate changes without affecting passed content]

## 6. Implementation Plan

### 6.1 Prioritized Actions

| Action ID | Description | Priority | Responsible | Deadline |
|-----------|-------------|----------|-------------|----------|
| ACT-001 | [Action Description] | [High/Medium/Low] | [Responsible Party] | [Deadline] |
| ACT-002 | [Action Description] | [High/Medium/Low] | [Responsible Party] | [Deadline] |

### 6.2 Verification Steps

1. [Verification step 1]
2. [Verification step 2]
3. [Verification step 3]

### 6.3 Rollback Plan

- [Rollback step 1]
- [Rollback step 2]
- [Rollback step 3]

## 7. Conclusion

### 7.1 Summary of Analysis

[Detailed summary of the difference analysis, including key findings, risks, and recommendations]

### 7.2 Confidence Level Impact

[Analysis of how the identified differences affect the overall confidence level]

### 7.3 Future Recommendations

- [Recommendation 1]
- [Recommendation 2]
- [Recommendation 3]

## 8. Appendices

### 8.1 Full Difference Table

[Comprehensive table of all identified differences]

### 8.2 Rule References

[List of rule references used in the analysis]

### 8.3 Validation Logs

[Relevant validation logs and debug information]

## Usage Instructions

1. Fill in the report header with the appropriate information
2. Identify and document all differences between marker and checker outputs
3. Assess the risks associated with each difference
4. Provide specific optimization suggestions
5. Identify and document passed content to be preserved
6. Create an implementation plan for addressing the differences
7. Include a comprehensive conclusion and recommendations
8. Save the report as `{prompt}-diff-analysis.md` in the analysis directory