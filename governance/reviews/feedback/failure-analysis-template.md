# Failure Analysis Template

## Analysis Information
- **Analysis ID**: FAIL-[YYYYMMDD]-[NNN]
- **Subject**: [Test Case/BDD Scenario]
- **Subject ID**: [TC-XXX-XXX / FT-XXX-XXX]
- **Analysis Date**: [YYYY-MM-DD]
- **Analyst**: [Name]
- **Failure Type**: □ Rule Misalignment □ Incomplete Coverage □ Ambiguous Steps □ Incorrect Parameters □ Syntax Errors □ Execution Failure □ Other

## Failure Context

### 1. Basic Information
- **Rule Basis**: [MD file path] + [Paragraph ID] + [Version]
- **Global Process Node**: [Process node]
- **User Type Template**: □ Type A (BA) □ Type B (QA Lead) □ Type C (Automation Tester) □ Type D (General)
- **Confidence Level Before Failure**: [1-5]

### 2. Failure Description
- **Failure Observed**: [Describe the failure as observed]
- **Expected Behavior**: [Describe what should have happened]
- **Actual Behavior**: [Describe what actually happened]
- **Impact**: □ Low □ Medium □ High □ Critical

## Root Cause Analysis

### 1. Primary Root Cause
- **Root Cause**: [Describe the primary root cause]
- **Evidence**: [Provide evidence supporting the root cause]
- **Contributing Factors**:
  - [Factor 1]
  - [Factor 2]
  - [Factor 3]

### 2. Secondary Root Causes
- **Root Cause 2**: [Describe secondary root cause]
- **Evidence 2**: [Provide evidence]
- 
- **Root Cause 3**: [Describe tertiary root cause]
- **Evidence 3**: [Provide evidence]

## Why Failed Analysis

### 1. Rule Alignment Issues
- **Misaligned Rule Points**:
  - [Rule point 1]: [Description of misalignment]
  - [Rule point 2]: [Description of misalignment]
- **Why Not Match**:
  - [Explanation of why the test case/BDD does not match the rule]
  - [Specific rule requirements that are not met]

### 2. Quality Issues
- **Quality Problems**:
  - [Issue 1]: [Description]
  - [Issue 2]: [Description]
- **Why Not Match**:
  - [Explanation of quality issues causing failure]

### 3. Traceability Issues
- **Traceability Gaps**:
  - [Gap 1]: [Description]
  - [Gap 2]: [Description]
- **Why Not Match**:
  - [Explanation of traceability issues causing failure]

### 4. Executability Issues (for BDD)
- **Executability Problems**:
  - [Issue 1]: [Description]
  - [Issue 2]: [Description]
- **Why Not Match**:
  - [Explanation of executability issues causing failure]

## Impact Assessment

### 1. Immediate Impact
- **Test Execution**: □ Blocked □ Delayed □ Affected
- **Quality Assurance**: □ Compromised □ Partially Affected □ Unaffected
- **Release Timeline**: □ Delayed □ At Risk □ Unaffected

### 2. Long-term Impact
- **Maintenance**: □ Increased □ Moderate □ Minimal
- **Technical Debt**: □ High □ Medium □ Low
- **Process Improvement**: □ Needed □ Recommended □ Not Needed

## Recommended Fixes

### 1. Immediate Fixes
- **Fix 1**: [Description of immediate fix]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

- **Fix 2**: [Description of immediate fix]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

### 2. Root Cause Fixes
- **Fix 1**: [Description of root cause fix]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

- **Fix 2**: [Description of root cause fix]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

### 3. Preventive Measures
- **Measure 1**: [Description of preventive measure]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

- **Measure 2**: [Description of preventive measure]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

## Verification Plan

### 1. Fix Verification
- **Test Cases to Run**:
  - [Test case 1]
  - [Test case 2]
- **Acceptance Criteria**:
  - [Criteria 1]
  - [Criteria 2]

### 2. Regression Testing
- **Test Scope**:
  - [Scope description]
- **Test Cases**:
  - [Test case 1]
  - [Test case 2]

## Confidence Level Recovery
- **Expected Confidence After Fix**: [1-5]
- **Recovery Plan**:
  - [Step 1]
  - [Step 2]
  - [Step 3]

## Documentation Updates
- **Files to Update**:
  - [File 1]
  - [File 2]
- **Update Details**:
  - [Update 1]
  - [Update 2]

## Conclusion

### Summary
[Provide a brief summary of the failure analysis, including root causes, impacts, and recommended fixes.]

### Lessons Learned
- [Lesson 1]
- [Lesson 2]
- [Lesson 3]

### Follow-up Actions
| Action | Responsible | Deadline | Status |
|--------|-------------|----------|--------|
|        |             |          |        |

## Sign-off
- **Analyst**: _________________________
- **Date**: _________________________

- **Reviewer**: _________________________
- **Date**: _________________________
