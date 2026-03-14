# Prompt Template Creation Guide

## Overview

This guide documents all templates that must be created by their corresponding prompts, including complete template content and creation instructions.

## Template Creation by Prompt

### Prompt 6: Test Case Generation - Required Templates

When executing Prompt 6, the following templates MUST be created with complete content:

#### 1. Test Case Review Template
**File**: `governance/reviews/testcase-review-template.md`

```markdown
# Test Case Review Template

## Review Information
- **Review ID**: REV-TC-[YYYYMMDD]-[NNN]
- **Test Case ID**: [TC-XXX-XXX]
- **Review Date**: [YYYY-MM-DD]
- **Reviewer**: [Name]
- **Review Stage**: □ Initial □ Peer Review □ Final Approval
- **Status**: □ Pending □ In Review □ Approved □ Rejected □ Needs Revision

## Test Case Details
- **Test Scenario**: [Test scenario description]
- **Rule Basis**: [MD file path] + [Paragraph ID] + [Version]
- **Global Process Node**: [Process node]
- **User Type Template**: □ Type A (BA) □ Type B (QA Lead) □ Type C (Automation Tester) □ Type D (General)

## Review Criteria

### 1. Rule Alignment
- [ ] Test case strictly aligns with rule constraints
- [ ] No scenario designs outside rules
- [ ] Covers positive, negative, and exception scenarios
- [ ] Correctly marks global process nodes
- [ ] References proper rule paragraph IDs

### 2. Completeness
- [ ] Preconditions are clear and testable
- [ ] Test steps are executable and unambiguous
- [ ] Expected results are rule-based and precise
- [ ] All required fields are completed
- [ ] Relationships are properly documented

### 3. Quality
- [ ] Grammar and spelling are correct
- [ ] Formatting is consistent
- [ ] Language is clear and professional
- [ ] Parameters use only valid values
- [ ] No undefined values introduced

### 4. Traceability
- [ ] Reference verification slots are included
- [ ] Relationships with requirements are documented
- [ ] Relationships with skills are documented
- [ ] Relationships with BDD scenarios are documented
- [ ] Rule basis is properly referenced

## Feedback

### Strengths

### Areas for Improvement

### Specific Comments

## Confidence Level Assessment
- **Initial Confidence**: [1-5]
- **Final Confidence**: [1-5]
- **Confidence Rationale**:

## Failure Analysis (if applicable)
- **Failure Type**: □ Rule Misalignment □ Incomplete Coverage □ Ambiguous Steps □ Incorrect Parameters □ Other
- **Root Cause**:
- **Recommended Fix**:

## Decision
- **Decision**: □ Approve □ Reject □ Request Revision
- **Revision Comments**:

## Sign-off
- **Reviewer Signature**: _________________________
- **Date**: _________________________

## Revision History
| Date | Reviewer | Change | Status |
|------|----------|--------|--------|
|      |          |        |        |
```

#### 2. Feedback Collection Template
**File**: `governance/reviews/feedback-template.md`

```markdown
# Feedback Collection Template

## Feedback Information
- **Feedback ID**: FDB-[YYYYMMDD]-[NNN]
- **Subject**: [Test Case/BDD Scenario]
- **Subject ID**: [TC-XXX-XXX / FT-XXX-XXX]
- **Feedback Date**: [YYYY-MM-DD]
- **Provider**: [Name]
- **Recipient**: [Name]

## Feedback Type
- □ Review Feedback
- □ Quality Assurance Feedback
- □ Execution Feedback
- □ Template Feedback
- □ Other: _________________

## Feedback Categories

### 1. Rule Alignment
- **Score**: [1-5]
- **Comments**:

### 2. Completeness
- **Score**: [1-5]
- **Comments**:

### 3. Quality
- **Score**: [1-5]
- **Comments**:

### 4. Traceability
- **Score**: [1-5]
- **Comments**:

### 5. Executability (for BDD)
- **Score**: [1-5]
- **Comments**:

## Overall Feedback

### Strengths

### Areas for Improvement

### Specific Recommendations

## Confidence Impact
- **Previous Confidence**: [1-5]
- **Recommended Confidence**: [1-5]
- **Rationale**:

## Action Items
| Action | Responsible | Deadline | Status |
|--------|-------------|----------|--------|
|        |             |          |        |

## Follow-up
- **Follow-up Date**: [YYYY-MM-DD]
- **Follow-up Status**: □ Pending □ In Progress □ Completed □ Cancelled
- **Follow-up Comments**:

## Acknowledgment
- **Recipient Acknowledgment**: _________________________
- **Date**: _________________________
```

#### 3. Confidence Level Assessment Guide
**File**: `governance/reviews/confidence-assessment.md`

```markdown
# Confidence Level Assessment Guide

## Overview
This guide provides a structured approach to assess and calculate confidence levels for test cases and BDD scenarios based on rule alignment, review feedback, and quality metrics.

## Confidence Level Scale

| Level | Score | Description | Color Code |
|-------|-------|-------------|------------|
| Very Low | 1 | Significant issues, major rule misalignment, requires substantial revision | Red |
| Low | 2 | Multiple issues, moderate rule misalignment, requires significant revision | Orange |
| Medium | 3 | Minor issues, good rule alignment, requires minor revision | Yellow |
| High | 4 | Very few issues, strong rule alignment, minimal revision needed | Light Green |
| Very High | 5 | No issues, perfect rule alignment, ready for production | Dark Green |

## Confidence Level Calculation

### Formula
```
Confidence Score = (Rule Alignment Score × 0.4) + (Quality Score × 0.3) + (Traceability Score × 0.2) + (Executability Score × 0.1)
```

### Component Scores

#### 1. Rule Alignment (40%)
- **5**: Perfect alignment with all rule points
- **4**: Strong alignment with minor gaps
- **3**: Good alignment with some gaps
- **2**: Moderate alignment with significant gaps
- **1**: Poor alignment with major gaps

#### 2. Quality (30%)
- **5**: Excellent quality, no issues
- **4**: Very good quality, minor issues
- **3**: Good quality, some issues
- **2**: Fair quality, multiple issues
- **1**: Poor quality, significant issues

#### 3. Traceability (20%)
- **5**: Complete traceability, all relationships documented
- **4**: Strong traceability, minor gaps
- **3**: Good traceability, some gaps
- **2**: Moderate traceability, significant gaps
- **1**: Poor traceability, major gaps

#### 4. Executability (10%) (for BDD only)
- **5**: Fully executable, no issues
- **4**: Highly executable, minor issues
- **3**: Executable, some issues
- **2**: Partially executable, significant issues
- **1**: Not executable, major issues

## Confidence Level Assessment Process

### 1. Initial Assessment
- **When**: After test case/BDD generation
- **Who**: Generator or initial reviewer
- **Purpose**: Establish baseline confidence level
- **Method**: Apply calculation formula based on initial quality checks

### 2. Review-Based Assessment
- **When**: After peer review
- **Who**: Reviewer
- **Purpose**: Update confidence level based on review feedback
- **Method**: Adjust component scores based on review comments and recalculate

### 3. Final Assessment
- **When**: After final approval
- **Who**: Approver
- **Purpose**: Establish final confidence level for production use
- **Method**: Final adjustment based on all feedback and revisions

## Confidence Level Integration

### Test Case Integration
- Include confidence level in test case template
- Track confidence level changes in review history
- Use confidence level to prioritize test execution

### BDD Integration
- Include confidence level in BDD feature files
- Track confidence level in BDD relationship manager
- Use confidence level to prioritize BDD execution

### Change History Integration
- Record confidence level changes in change history
- Link confidence level changes to specific revisions
- Use confidence level trends to improve generation process

## Confidence Level Thresholds

### Minimum Thresholds
- **Production Use**: Minimum confidence level of 4
- **Staging Use**: Minimum confidence level of 3
- **Development Use**: Minimum confidence level of 2

### Quality Gates
- **Test Case Approval**: Confidence level ≥ 4
- **BDD Approval**: Confidence level ≥ 4
- **Regression Testing**: Confidence level ≥ 3
```

#### 4. Failure Analysis Template
**File**: `governance/reviews/failure-analysis-template.md`

```markdown
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

### 3. Preventive Measures
- **Measure 1**: [Description of preventive measure]
- **Responsible**: [Name]
- **Deadline**: [YYYY-MM-DD]

## Sign-off
- **Analyst Signature**: _________________________
- **Date**: _________________________

## Revision History
| Date | Reviewer | Change | Status |
|------|----------|--------|--------|
|      |          |        |        |
```

### Prompt 7: BDD Scenario Generation - Required Templates

When executing Prompt 7, the following template MUST be created with complete content:

#### 1. BDD Review Template
**File**: `governance/reviews/bdd-review-template.md`

```markdown
# BDD Review Template

## Review Information
- **Review ID**: REV-BDD-[YYYYMMDD]-[NNN]
- **BDD Feature ID**: [FT-XXX-XXX]
- **Test Case ID**: [TC-XXX-XXX]
- **Review Date**: [YYYY-MM-DD]
- **Reviewer**: [Name]
- **Review Stage**: □ Initial □ Peer Review □ Final Approval
- **Status**: □ Pending □ In Review □ Approved □ Rejected □ Needs Revision

## BDD Details
- **Feature Description**: [Feature description]
- **Rule Basis**: [MD file path] + [Paragraph ID] + [Version]
- **Global Process Node**: [Process node]
- **Gherkin Syntax**: □ Correct □ Needs Improvement

## Review Criteria

### 1. Rule Alignment
- [ ] BDD scenario strictly aligns with test case
- [ ] BDD scenario strictly aligns with rule points
- [ ] No scenario designs outside rules
- [ ] Correctly marks global process nodes
- [ ] References proper rule paragraph IDs

### 2. Executability
- [ ] Gherkin syntax is correct
- [ ] Steps are executable and unambiguous
- [ ] Background is properly defined
- [ ] Examples (if any) are valid
- [ ] Parameters use only valid values

### 3. Completeness
- [ ] All required sections are included
- [ ] Feature description is clear
- [ ] Scenarios are well-defined
- [ ] Expected results are precise
- [ ] Rule basis is properly referenced

### 4. Traceability
- [ ] Reference verification slots are included
- [ ] Relationships with requirements are documented
- [ ] Relationships with skills are documented
- [ ] Relationships with test cases are documented
- [ ] Bidirectional traceability is maintained

## Feedback

### Strengths

### Areas for Improvement

### Specific Comments

## Confidence Level Assessment
- **Initial Confidence**: [1-5]
- **Final Confidence**: [1-5]
- **Confidence Rationale**:

## Failure Analysis (if applicable)
- **Failure Type**: □ Rule Misalignment □ Syntax Error □ Execution Failure □ Other
- **Root Cause**:
- **Recommended Fix**:

## Decision
- **Decision**: □ Approve □ Reject □ Request Revision
- **Revision Comments**:

## Sign-off
- **Reviewer Signature**: _________________________
- **Date**: _________________________

## Revision History
| Date | Reviewer | Change | Status |
|------|----------|--------|--------|
|      |          |        |        |
```

**Note**: Prompt 7 should reference the shared templates created by Prompt 6:
- `governance/reviews/feedback-template.md`
- `governance/reviews/confidence-assessment.md`
- `governance/reviews/failure-analysis-template.md`

## Implementation Instructions

### For Prompt 6 Execution

When executing Prompt 6, include the following instruction:

```
**Template Creation**: MUST create the following templates with complete content:
1. Create `governance/reviews/testcase-review-template.md` with the complete template structure defined above
2. Create `governance/reviews/feedback-template.md` with the complete template structure defined above
3. Create `governance/reviews/confidence-assessment.md` with the complete template structure defined above
4. Create `governance/reviews/failure-analysis-template.md` with the complete template structure defined above

Each template must include all sections, fields, and example values as specified in the template content.
```

### For Prompt 7 Execution

When executing Prompt 7, include the following instruction:

```
**Template Creation**: MUST create the following template with complete content:
1. Create `governance/reviews/bdd-review-template.md` with the complete template structure defined above

**Shared Templates**: Reference the following templates created by Prompt 6:
- `governance/reviews/feedback-template.md`
- `governance/reviews/confidence-assessment.md`
- `governance/reviews/failure-analysis-template.md`

If these shared templates don't exist, create them using the complete template content from Prompt 6.
```

## Quality Assurance

### Template Completeness Checklist

- [ ] All templates are created with complete content
- [ ] All sections are included in each template
- [ ] All fields are documented with examples
- [ ] File locations are correct
- [ ] Template naming follows conventions
- [ ] Templates are ready for immediate use

### Template Validation

Before considering template creation complete:
1. Verify all required templates exist
2. Verify all templates have complete content
3. Verify templates follow the specified structure
4. Verify templates are in the correct location
5. Verify templates are usable without modification

## Conclusion

All templates must be created by their corresponding prompts with complete, usable content. This ensures consistency across the system and eliminates the need for manual template creation.
