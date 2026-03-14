# Generic Checker Prompt Generator

## Purpose
This prompt generates a complete set of checker prompts for validating LLM outputs against any original MD (Markdown) specification document.

## Instructions

You are an expert prompt engineering assistant. Your task is to analyze the provided original MD file and generate a comprehensive checker prompts set for validating LLM outputs. Follow these steps:

### Step 1: Analyze Original MD Structure

1. **Identify Document Type**:
   - Determine if the MD is a specification, guide, requirement document, or other type
   - Identify the domain (e.g., software development, business process, technical specification)

2. **Extract Key Components**:
   - **Prompts/Instructions**: Identify all prompts or instruction sections
   - **Output Requirements**: Extract expected output formats and structures
   - **Validation Criteria**: Identify validation rules and quality standards
   - **Dependencies**: Map dependencies between different sections or prompts
   - **File Naming Conventions**: Extract naming patterns and directory structures

3. **Identify Validation Points**:
   - **Structural Requirements**: Required fields, formats, organization
   - **Content Requirements**: Rule alignment, completeness, accuracy
   - **Reference Requirements**: Traceability, cross-references, dependencies
   - **Quality Metrics**: Confidence levels, coverage, validity

### Step 2: Design Checker Prompts

For each identified prompt in the original MD, create a corresponding checker prompt:

#### Template for Checker Prompt

```markdown
### Checker Prompt for [Original Prompt Name]

#### Role
You are an expert validation assistant specializing in [domain].

#### Task
Validate the output of [Original Prompt Name] against the original requirements.

#### Input Analysis
1. Review the original MD requirements for [specific section]
2. Analyze the Marker LLM output
3. Understand the expected structure and content

#### Validation Process

**1. Structure Validation**:
- Verify [specific structural requirements]
- Check [formatting requirements]
- Validate [organization requirements]

**2. Content Validation**:
- Verify alignment with [specific rules/requirements]
- Check [content quality criteria]
- Validate [completeness requirements]

**3. Reference Validation**:
- Verify [reference requirements]
- Check [traceability requirements]
- Validate [dependency requirements]

#### Confidence Level Assessment
Evaluate against these criteria (1-5 scale):
- **Structural Completeness**: [specific criteria]
- **Content Accuracy**: [specific criteria]
- **Reference Integrity**: [specific criteria]
- [Additional criteria as needed]

Calculate overall confidence level (average of criteria scores).

#### Difference Analysis
- Identify discrepancies between Marker output and requirements
- Highlight missing or incorrect information
- Provide specific examples

#### Optimization Suggestions
- Provide actionable recommendations
- Suggest corrections for identified issues
- Ensure suggestions don't negatively affect passed outputs

#### Output Requirements
- Generate structured validation report
- Include confidence level assessment
- Provide detailed difference analysis
- Include optimization suggestions
- Maintain preservation section for passed content
```

### Step 3: Generate Supporting Templates

Create the following supporting templates with complete structures:

#### 1. Analysis Template
Structure for detailed difference analysis:
```markdown
# Difference Analysis Report

## Analysis Overview
- **Analysis ID**: [Unique identifier]
- **Analysis Date**: YYYY-MM-DD
- **Analyst**: [Name]
- **Scope**: [What was analyzed]
- **Focus Area**: [Structure/Content/Reference/All]

## Original MD Reference
- **Original MD File**: [Path to original MD file]
- **Key Requirements**: [Summary of key requirements]
- **Validation Criteria**: [Specific validation rules]

## Structural Analysis

### Component Validation
| Component | Required | Present | Format Correct | Comments |
|-----------|----------|---------|----------------|----------|
| | | | | |

### Structure Issues
| Issue ID | Description | Severity | Impact | Priority |
|----------|-------------|----------|--------|----------|
| | | | | |

## Content Analysis

### Content Validation
| Requirement | Fulfilled | Fulfillment Level | Evidence | Comments |
|-------------|-----------|------------------|----------|----------|
| | | | | |

### Content Issues
| Issue ID | Description | Severity | Impact | Priority |
|----------|-------------|----------|--------|----------|
| | | | | |

## Reference Analysis

### Reference Validation
| Reference Type | Required | Present | Valid | Comments |
|-----------------|----------|---------|-------|----------|
| | | | | |

### Reference Issues
| Issue ID | Description | Severity | Impact | Priority |
|----------|-------------|----------|--------|----------|
| | | | | |

## Confidence Level Assessment

### Overall Confidence Level
- **Overall Score**: [1-5]
- **Confidence Level**: [Excellent/Good/Medium/Poor/Very Poor]

### Breakdown by Criteria
| Criterion | Score | Weight | Weighted Score | Comments |
|-----------|-------|--------|----------------|----------|
| Structural Completeness | | | | |
| Content Accuracy | | | | |
| Reference Integrity | | | | |
| Scenario Coverage | | | | |
| Parameter Validity | | | | |

## Difference Analysis

### Key Differences
| Difference ID | Type | Description | Marker Output | Expected |
|----------------|------|-------------|---------------|----------|
| | | | | |

### Impact Assessment
- **Quality Impact**: [Description]
- **Functionality Impact**: [Description]
- **Risk Level**: [Critical/High/Medium/Low]

## Optimization Suggestions

### Critical Improvements (Priority 1)
| Suggestion ID | Description | Expected Impact | Implementation Effort |
|----------------|-------------|-----------------|----------------------|
| | | | |

### Minor Improvements (Priority 2)
| Suggestion ID | Description | Expected Impact | Implementation Effort |
|----------------|-------------|-----------------|----------------------|
| | | | |

## Preservation Section

### Passed Content Identification
- **Items to Preserve**: [List of items that should be preserved]
- **Low-Risk Changes**: [Changes that can be made without affecting passed content]
- **Preservation Strategy**: [How to preserve passed content]

## Conclusion
- **Summary**: [Summary of findings]
- **Key Recommendations**: [Top 3 recommendations]
- **Next Steps**: [Proposed actions]
```

#### 2. Output Template
Structure for validation output reports:
```markdown
# Validation Report

## Validation Overview
- **Report ID**: [Unique identifier]
- **Validation Date**: YYYY-MM-DD
- **Overall Status**: [Pass/Fail/Conditional]
- **Scope**: [What was validated]
- **Validation Method**: [Method used]

## Marker Output Reference
- **Marker Prompt**: [Which marker prompt was used]
- **Marker Output File**: [Path to marker output]
- **Output Type**: [Test Cases/BDD Scenarios/etc.]

## Validation Results

### Overall Statistics
- **Total Items**: [Number]
- **Passed**: [Number]
- **Failed**: [Number]
- **Conditional**: [Number]
- **Pass Rate**: [Percentage]

### Item-by-Item Results
| Item ID | Status | Confidence Level | Issues Found | Comments |
|---------|--------|------------------|--------------|----------|
| | | | | |

## Confidence Level Assessment

### Confidence Level Distribution
| Confidence Level | Count | Percentage |
|------------------|-------|------------|
| Excellent (4-5) | | |
| Good (3-3.9) | | |
| Medium (2-2.9) | | |
| Poor (1-1.9) | | |

### Overall Confidence Metrics
- **Average Confidence Level**: [Score]
- **Median Confidence Level**: [Score]
- **Minimum Confidence Level**: [Score]
- **Maximum Confidence Level**: [Score]

## Difference Analysis

### Structural Differences
| Difference ID | Location | Description | Impact |
|----------------|----------|-------------|--------|
| | | | |

### Content Differences
| Difference ID | Location | Description | Impact |
|----------------|----------|-------------|--------|
| | | | |

### Reference Differences
| Difference ID | Location | Description | Impact |
|----------------|----------|-------------|--------|
| | | | |

## Optimization Suggestions

### High Priority (Critical)
| Suggestion | Rationale | Expected Benefit | Implementation Effort |
|------------|-----------|------------------|----------------------|
| | | | |

### Medium Priority (Important)
| Suggestion | Rationale | Expected Benefit | Implementation Effort |
|------------|-----------|------------------|----------------------|
| | | | |

### Low Priority (Optional)
| Suggestion | Rationale | Expected Benefit | Implementation Effort |
|------------|-----------|------------------|----------------------|
| | | | |

## Preservation Section

### Passed Content
- **Items to Preserve**: [List of items that passed validation]
- **Preservation Strategy**: [How to preserve these items]
- **Modification Guidelines**: [Guidelines for making changes to passed content]

## Risk Assessment

### Critical Risks
| Risk ID | Description | Likelihood | Impact | Mitigation |
|---------|-------------|------------|--------|------------|
| | | | | |

### High Risks
| Risk ID | Description | Likelihood | Impact | Mitigation |
|---------|-------------|------------|--------|------------|
| | | | | |

### Medium/Low Risks
| Risk ID | Description | Likelihood | Impact | Mitigation |
|---------|-------------|------------|--------|------------|
| | | | | |

## Human Review Recommendations

### Review Focus Areas
- **Primary Focus**: [Key areas for human review]
- **Secondary Focus**: [Additional areas to consider]
- **Items Requiring Special Attention**: [Specific items that need careful review]

### Review Process Recommendations
- **Recommended Reviewers**: [Roles/skills needed]
- **Review Timeline**: [Suggested timeline]
- **Review Checklist**: [Key points to check]

## Implementation Guide

### Recommended Actions
1. [Action 1]
2. [Action 2]
3. [Action 3]

### Implementation Timeline
- **Phase 1**: [Timeline and actions]
- **Phase 2**: [Timeline and actions]
- **Phase 3**: [Timeline and actions]

### Rollback Plan
- **Rollback Triggers**: [Conditions that would trigger rollback]
- **Rollback Steps**: [Steps to roll back changes]
- **Rollback Verification**: [How to verify successful rollback]

## Conclusion
- **Summary**: [Summary of validation]
- **Key Findings**: [Most important findings]
- **Recommendations**: [Top recommendations]
- **Next Steps**: [Proposed next steps]

## Appendices
- **Appendix A**: [Additional details]
- **Appendix B**: [Supporting data]
```

#### 3. Feedback Template - Initial Review
```markdown
# Initial Review Feedback

## Review Information
- **Reviewer**: [Name]
- **Review Date**: YYYY-MM-DD
- **Document Being Reviewed**: [Document name]
- **Document Version**: [Version]
- **Review Type**: [Technical/Content/Compliance]

## Overall Assessment
- **Overall Rating**: [1-5]
- **Overall Status**: [Approve/Request Changes/Reject]
- **Confidence Level in Assessment**: [High/Medium/Low]

## Detailed Review

### Strengths
1. [Strength 1]
2. [Strength 2]
3. [Strength 3]

### Areas for Improvement
1. [Area 1]
2. [Area 2]
3. [Area 3]

### Specific Comments

#### Section 1: [Section Name]
- **Status**: [Accept/Needs Work]
- **Comments**: [Specific feedback]

#### Section 2: [Section Name]
- **Status**: [Accept/Needs Work]
- **Comments**: [Specific feedback]

## Action Items
| Item | Description | Priority | Due Date | Assigned To |
|------|-------------|----------|----------|-------------|
| | | | | |

## Recommendations
- **Immediate Actions**: [What to do right away]
- **Short-term Improvements**: [What to do soon]
- **Long-term Considerations**: [What to consider for the future]

## Approval Decision
- **Decision**: [Approve/Request Changes/Reject]
- **Rationale**: [Explanation of decision]
- **Next Steps**: [What happens next]

## Signature
- **Reviewer Signature**: [Signature]
- **Date**: YYYY-MM-DD
```

#### 4. Feedback Template - Peer Review
```markdown
# Peer Review Feedback

## Review Information
- **Reviewer**: [Name]
- **Review Date**: YYYY-MM-DD
- **Document Being Reviewed**: [Document name]
- **Document Version**: [Version]
- **Initial Reviewer**: [Name of initial reviewer]
- **Initial Review Date**: YYYY-MM-DD

## Validation of Initial Review
- **Initial Review Validation**: [Validated/Partially Validated/Not Validated]
- **Agreement with Initial Assessment**: [Full Agreement/Partial Agreement/Disagreement]
- **Areas of Agreement**: [List]
- **Areas of Disagreement**: [List]

## Peer Assessment
- **Overall Rating**: [1-5]
- **Overall Status**: [Concur with Initial/Request Additional Changes/Alternative Recommendation]
- **Confidence Level**: [High/Medium/Low]

## Additional Findings

### New Strengths Identified
1. [Strength 1]
2. [Strength 2]

### Additional Concerns
1. [Concern 1]
2. [Concern 2]

### Technical Comments
- **Technical Accuracy**: [Comments]
- **Implementation Feasibility**: [Comments]
- **Best Practices**: [Comments]

## Recommended Adjustments to Initial Review
| Adjustment ID | Description | Rationale | Priority |
|----------------|-------------|-----------|----------|
| | | | |

## Consensus Recommendation
- **Consensus Status**: [Reached/Not Reached/Need Further Discussion]
- **Recommended Path Forward**: [What should happen next]
- **Escalation Needed**: [Yes/No]
- **Escalation Rationale**: [If yes, explain]

## Signature
- **Peer Reviewer Signature**: [Signature]
- **Date**: YYYY-MM-DD
```

#### 5. Feedback Template - Final Approval
```markdown
# Final Approval Feedback

## Approval Information
- **Approver**: [Name]
- **Approval Date**: YYYY-MM-DD
- **Document Being Approved**: [Document name]
- **Document Version**: [Version]
- **Initial Reviewer**: [Name]
- **Peer Reviewer**: [Name]

## Review Summary
- **Initial Review Status**: [Summary]
- **Peer Review Status**: [Summary]
- **Consensus Reached**: [Yes/No]
- **Outstanding Issues**: [Number]

## Final Assessment
- **Overall Rating**: [1-5]
- **Approval Decision**: [Approve/Approve with Conditions/Reject]
- **Confidence Level**: [High/Medium/Low]

## Conditions (if applicable)
| Condition ID | Description | Required Action | Deadline |
|--------------|-------------|-----------------|----------|
| | | | |

## Risk Assessment
- **Implementation Risk**: [Low/Medium/High]
- **Quality Risk**: [Low/Medium/High]
- **Schedule Risk**: [Low/Medium/High]
- **Risk Mitigation**: [Strategy]

## Approval Rationale
- **Key Factors Considered**: [List]
- **Decision Rationale**: [Detailed explanation]
- **Alternative Approaches Considered**: [List]

## Implementation Guidance
- **Immediate Next Steps**: [List]
- **Implementation Timeline**: [Timeline]
- **Success Metrics**: [How to measure success]
- **Monitoring Requirements**: [What to monitor]

## Post-Approval Review
- **Review Date**: [When to review again]
- **Review Criteria**: [What to review]
- **Success Conditions**: [What constitutes success]

## Signature
- **Approver Signature**: [Signature]
- **Date**: YYYY-MM-DD

## Acknowledgment
- **Document Owner Acknowledgment**: [Signature]
- **Date**: YYYY-MM-DD
```

#### 6. Feedback Template - General
```markdown
# General Feedback Template

## Feedback Information
- **Feedback Provider**: [Name]
- **Feedback Date**: YYYY-MM-DD
- **Feedback Type**: [Review/Comment/Suggestion/Question]
- **Topic**: [What this feedback is about]
- **Context**: [Background context]

## Overall Feedback
- **Overall Sentiment**: [Positive/Neutral/Negative/Mixed]
- **Priority**: [High/Medium/Low]
- **Confidence Level**: [High/Medium/Low]

## Detailed Feedback

### What's Working Well
1. [Item 1]
2. [Item 2]
3. [Item 3]

### Areas for Improvement
1. [Item 1]
2. [Item 2]
3. [Item 3]

### Specific Comments
| Section/Item | Comment | Suggestion |
|--------------|---------|------------|
| | | |

## Questions (if any)
| Question | Context | Priority |
|----------|---------|----------|
| | | |

## Suggestions (if any)
| Suggestion | Rationale | Expected Benefit | Effort |
|------------|-----------|------------------|--------|
| | | | |

## Action Items
| Action | Description | Assigned To | Due Date | Priority |
|--------|-------------|-------------|----------|----------|
| | | | | |

## Follow-up
- **Follow-up Required**: [Yes/No]
- **Follow-up Date**: YYYY-MM-DD
- **Follow-up Person**: [Name]
- **Follow-up Topic**: [What to follow up on]

## Signature
- **Feedback Provider Signature**: [Signature]
- **Date**: YYYY-MM-DD
```

#### 7. Exit Report Template
```markdown
# Exit Report - Marker-Checker Confidence Level Loop

## 1. Exit Summary

### 1.1 Exit Trigger
- **Exit Criteria Met**: [Specific criteria that triggered exit]
  - Maximum iterations reached: [Yes/No]
  - Confidence level below threshold: [Yes/No]
  - Stagnation detected: [Yes/No]
  - Review consensus not reached: [Yes/No]

### 1.2 Iteration History
| Iteration | Date | Confidence Level | Key Issues | Review Status | Improvement |
|-----------|------|------------------|-------------|----------------|-------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### 1.3 Final Confidence Level
- **Overall Score**: [1-5]
- **Structural Completeness**: [1-5]
- **Content Accuracy**: [1-5]
- **Reference Integrity**: [1-5]
- **Scenario Coverage**: [1-5]
- **Parameter Validity**: [1-5]

### 1.4 Exit Analysis
- **Exit Date**: YYYY-MM-DD
- **Exit Reason**: [Primary reason for exit]
- **Total Iterations**: [Number]
- **Duration**: [Time period]

## 2. Comprehensive Analysis

### 2.1 Persistent Issues
| Issue ID | Description | Frequency | Severity | Affected Iterations |
|-----------|-------------|------------|----------|---------------------|
| | | | | |

### 2.2 Root Cause Analysis

#### 2.2.1 Primary Root Causes
| Root Cause ID | Description | Evidence | Impact |
|---------------|-------------|----------|--------|
| | | | |

#### 2.2.2 Contributing Factors
| Factor ID | Description | Impact Level |
|-----------|-------------|--------------|
| | | |

### 2.3 Impact Assessment

#### 2.3.1 System Impact
- **Quality Impact**: [Description of quality impact]
- **Functionality Impact**: [Description of functionality impact]
- **Performance Impact**: [Description of performance impact]
- **Risk Level**: [Critical/High/Medium/Low]

#### 2.3.2 Process Impact
- **Workflow Impact**: [Description of workflow impact]
- **Resource Impact**: [Description of resource impact]
- **Timeline Impact**: [Description of timeline impact]
- **Cost Impact**: [Description of cost impact]

## 3. Human Review Summary

### 3.1 Initial Review Feedback
- **Reviewer**: [Name]
- **Review Date**: YYYY-MM-DD
- **Overall Assessment**: [Pass/Fail/Conditional]
- **Key Findings**: [Summary of findings]
- **Confidence Level**: [1-5]
- **Recommendations**: [List of recommendations]

### 3.2 Peer Review Feedback
- **Reviewer**: [Name]
- **Review Date**: YYYY-MM-DD
- **Overall Assessment**: [Pass/Fail/Conditional]
- **Validation of Initial Review**: [Validated/Partially Validated/Not Validated]
- **Additional Findings**: [Summary of additional findings]
- **Confidence Level**: [1-5]
- **Recommendations**: [List of recommendations]

### 3.3 Final Approval Feedback
- **Approver**: [Name]
- **Approval Date**: YYYY-MM-DD
- **Approval Decision**: [Approved/Rejected/Conditional]
- **Approval Rationale**: [Explanation of decision]
- **Confidence Level**: [1-5]
- **Conditions** (if applicable): [List of conditions]

### 3.4 Review Consensus
- **Consensus Status**: [Reached/Not Reached/Partial]
- **Areas of Agreement**: [List of agreed points]
- **Areas of Disagreement**: [List of disagreed points]
- **Escalation Required**: [Yes/No]
- **Escalation Outcome**: [If escalated, document outcome]

## 4. Optimization Strategy

### 4.1 Strategy Selection

#### 4.1.1 Strategy Options Evaluated
| Strategy | Pros | Cons | Feasibility | Expected Impact |
|----------|-------|-------|--------------|-----------------|
| Requirement Refinement | | | | |
| Prompt Engineering Improvement | | | | |
| Model Enhancement | | | | |
| Hybrid Approach | | | | |
| Acceptance with Mitigation | | | | |

#### 4.1.2 Selected Strategy
- **Strategy Name**: [Name of selected strategy]
- **Strategy Type**: [Requirement Refinement / Prompt Engineering / Model Enhancement / Hybrid / Acceptance with Mitigation]
- **Selection Rationale**: [Detailed explanation of why this strategy was chosen]
- **Expected Confidence Level Improvement**: [Expected improvement amount]

### 4.2 Implementation Plan

#### 4.2.1 Phase 1: [Phase Name]
- **Timeline**: [Start date - End date]
- **Actions**:
  1. [Action 1]
  2. [Action 2]
  3. [Action 3]
- **Responsible**: [Name/Role]
- **Resources Required**: [List of resources]
- **Success Criteria**: [Specific criteria for phase success]

#### 4.2.2 Phase 2: [Phase Name]
- **Timeline**: [Start date - End date]
- **Actions**:
  1. [Action 1]
  2. [Action 2]
  3. [Action 3]
- **Responsible**: [Name/Role]
- **Resources Required**: [List of resources]
- **Success Criteria**: [Specific criteria for phase success]

#### 4.2.3 Phase 3: [Phase Name]
- **Timeline**: [Start date - End date]
- **Actions**:
  1. [Action 1]
  2. [Action 2]
  3. [Action 3]
- **Responsible**: [Name/Role]
- **Resources Required**: [List of resources]
- **Success Criteria**: [Specific criteria for phase success]

### 4.3 Resource Requirements

#### 4.3.1 Time Requirements
- **Total Estimated Time**: [Number of hours/days]
- **Phase 1 Time**: [Hours/days]
- **Phase 2 Time**: [Hours/days]
- **Phase 3 Time**: [Hours/days]
- **Contingency Time**: [Additional time buffer]

#### 4.3.2 Expertise Requirements
- **Required Skills**: [List of skills needed]
- **Team Members**: [List of team members and roles]
- **External Resources**: [Any external expertise needed]
- **Training Requirements**: [Any training needed]

#### 4.3.3 Tool Requirements
- **Software Tools**: [List of software needed]
- **Hardware Requirements**: [List of hardware needed]
- **Licenses**: [Any licenses required]
- **Access Requirements**: [Any system access needed]

## 5. Expected Outcomes

### 5.1 Success Criteria

#### 5.1.1 Confidence Level Targets
- **Target Overall Confidence Level**: [1-5]
- **Target Structural Completeness**: [1-5]
- **Target Content Accuracy**: [1-5]
- **Target Reference Integrity**: [1-5]
- **Target Scenario Coverage**: [1-5]
- **Target Parameter Validity**: [1-5]

#### 5.1.2 Quality Metrics
- **Target Error Reduction**: [Percentage reduction]
- **Target Issue Resolution**: [Number of issues to resolve]
- **Target Improvement Areas**: [List of areas to improve]
- **Measurement Method**: [How success will be measured]

#### 5.1.3 Timeline Targets
- **Implementation Start Date**: YYYY-MM-DD
- **Implementation End Date**: YYYY-MM-DD
- **Validation Date**: YYYY-MM-DD
- **Total Duration**: [Time period]

### 5.2 Risk Mitigation

#### 5.2.1 Potential Risks
| Risk ID | Description | Probability | Impact | Risk Level |
|----------|-------------|--------------|----------|
| | | | |

#### 5.2.2 Mitigation Strategies
| Risk ID | Mitigation Strategy | Owner | Timeline |
|----------|-------------------|--------|----------|
| | | | |

#### 5.2.3 Contingency Plans
| Risk ID | Contingency Plan | Trigger | Owner |
|----------|-----------------|---------|--------|
| | | | |

## 6. Approval and Next Steps

### 6.1 Approval Required

#### 6.1.1 Level 1 Approval: Project Lead
- **Approver**: [Name]
- **Approval Required**: [Yes/No]
- **Approval Deadline**: YYYY-MM-DD
- **Approval Criteria**: [Specific criteria for approval]
- **Approval Status**: [Pending/Approved/Rejected]

#### 6.1.2 Level 2 Approval: Department Manager (if required)
- **Approver**: [Name]
- **Approval Required**: [Yes/No]
- **Approval Deadline**: YYYY-MM-DD
- **Approval Criteria**: [Specific criteria for approval]
- **Approval Status**: [Pending/Approved/Rejected]

#### 6.1.3 Level 3 Approval: Executive Sponsor (if required)
- **Approver**: [Name]
- **Approval Required**: [Yes/No]
- **Approval Deadline**: YYYY-MM-DD
- **Approval Criteria**: [Specific criteria for approval]
- **Approval Status**: [Pending/Approved/Rejected]

### 6.2 Next Steps

#### 6.2.1 Immediate Actions (Next 1-3 days)
1. [Action 1]
2. [Action 2]
3. [Action 3]

#### 6.2.2 Short-term Actions (Next 1-2 weeks)
1. [Action 1]
2. [Action 2]
3. [Action 3]

#### 6.2.3 Long-term Actions (Next 1-3 months)
1. [Action 1]
2. [Action 2]
3. [Action 3]

## 7. Appendices

### 7.1 Detailed Iteration Reports

#### 7.1.1 Iteration 1 Details
- **Date**: YYYY-MM-DD
- **Confidence Level**: [Score]
- **Validation Report**: [Link to report]
- **Initial Review**: [Link to review]
- **Peer Review**: [Link to review]
- **Final Approval**: [Link to approval]
- **Key Issues**: [List]
- **Improvement Actions**: [List]

#### 7.1.2 Iteration 2 Details
- **Date**: YYYY-MM-DD
- **Confidence Level**: [Score]
- **Validation Report**: [Link to report]
- **Initial Review**: [Link to review]
- **Peer Review**: [Link to review]
- **Final Approval**: [Link to approval]
- **Key Issues**: [List]
- **Improvement Actions**: [List]

#### 7.1.3 Iteration 3 Details
- **Date**: YYYY-MM-DD
- **Confidence Level**: [Score]
- **Validation Report**: [Link to report]
- **Initial Review**: [Link to review]
- **Peer Review**: [Link to review]
- **Final Approval**: [Link to approval]
- **Key Issues**: [List]
- **Improvement Actions**: [List]

### 7.2 Supporting Analysis

#### 7.2.1 Root Cause Analysis Details
- [Detailed root cause analysis methodology]
- [Evidence and data supporting analysis]
- [Expert consultation results]

#### 7.2.2 Impact Analysis Details
- [Detailed impact assessment methodology]
- [Risk assessment results]
- [Stakeholder impact analysis]

### 7.3 Optimization Strategy Details

#### 7.3.1 Strategy Evaluation Matrix
- [Detailed comparison of strategy options]
- [Cost-benefit analysis]
- [Feasibility assessment]

#### 7.3.2 Implementation Plan Details
- [Detailed project plan]
- [Resource allocation plan]
- [Risk management plan]

### 7.4 Approval Records

#### 7.4.1 Level 1 Approval
- **Approver Signature**: [Signature]
- **Approval Date**: YYYY-MM-DD
- **Comments**: [Any comments]

#### 7.4.2 Level 2 Approval (if applicable)
- **Approver Signature**: [Signature]
- **Approval Date**: YYYY-MM-DD
- **Comments**: [Any comments]

#### 7.4.3 Level 3 Approval (if applicable)
- **Approver Signature**: [Signature]
- **Approval Date**: YYYY-MM-DD
- **Comments**: [Any comments]

## 8. Conclusion

### 8.1 Summary
- **Exit Trigger**: [Summary of why exit was triggered]
- **Final Confidence Level**: [Summary of final confidence level]
- **Selected Strategy**: [Summary of optimization strategy]
- **Expected Outcome**: [Summary of expected improvements]

### 8.2 Key Recommendations
1. [Recommendation 1]
2. [Recommendation 2]
3. [Recommendation 3]

### 8.3 Lessons Learned
1. [Lesson 1]
2. [Lesson 2]
3. [Lesson 3]

### 8.4 Future Improvements
1. [Improvement 1]
2. [Improvement 2]
3. [Improvement 3]

---

**Report ID**: EXIT-REPORT-[YYYYMMDD]-[SEQ]
**Report Date**: YYYY-MM-DD
**Report Author**: [Name]
**Report Version**: [Version]
**Next Review Date**: YYYY-MM-DD
```

### Step 4: Define Validation Rules

Based on the original MD, define:

1. **Structural Validation Rules**:
   - Required fields and formats
   - Organization and hierarchy
   - Naming conventions

2. **Content Validation Rules**:
   - Rule alignment requirements
   - Completeness criteria
   - Accuracy standards

3. **Reference Validation Rules**:
   - Traceability requirements
   - Cross-reference validation
   - Dependency checking

4. **Quality Assessment Criteria**:
   - Confidence level definitions (1-5 scale)
   - Severity levels (Critical/High/Medium/Low)
   - Pass/Fail criteria

### Step 5: Generate Configuration Files

Create configuration files for:

1. **Confidence Level Configuration**:
   - Scoring criteria and weights
   - Threshold definitions
   - Adjustment rules

2. **Review Process Configuration**:
   - Review workflow stages
   - Reviewer roles and responsibilities
   - Feedback collection mechanisms

### Step 6: Create Usage Documentation

Generate documentation including:

1. **How-To Guide**:
   - Directory structure
   - Component descriptions
   - Execution flow
   - File naming conventions
   - Example workflows

2. **Best Practices**:
   - Validation guidelines
   - Optimization recommendations
   - Troubleshooting tips

## Output Requirements

Generate the following files with the complete templates as defined in Step 3:

### 1. Checker Prompts File
- **File Name**: `checker-prompts.md`
- **Location**: `governance/checker/prompts/`
- **Content**: All checker prompts for each identified prompt in original MD

### 2. Analysis Template
- **File Name**: `analysis-template.md`
- **Location**: `governance/checker/analysis/`
- **Content**: Complete difference analysis template as defined above

### 3. Output Template
- **File Name**: `output-template.md`
- **Location**: `governance/checker/outputs/`
- **Content**: Complete validation report template as defined above

### 4. Configuration Files
- **Confidence Level Config**: `governance/checker/config/confidence-level-config.md`
- **Review Process Config**: `governance/checker/config/review-feedback-config.md`
- **Exit Criteria Config**: `governance/checker/config/exit-criteria-and-optimization.md`

### 5. How-To Guide
- **File Name**: `CHECKER-HOW-TO.md`
- **Location**: `governance/checker/`
- **Content**: Complete usage guide with examples

### 6. Feedback Templates
- **Initial Review**: `governance/checker/templates/feedback-template-initial-review.md` - complete template as defined above
- **Peer Review**: `governance/checker/templates/feedback-template-peer-review.md` - complete template as defined above
- **Final Approval**: `governance/checker/templates/feedback-template-final-approval.md` - complete template as defined above
- **General Feedback**: `governance/checker/templates/feedback-template-general.md` - complete template as defined above

### 7. Exit Report Template
- **Exit Report**: `governance/checker/templates/exit-report-template.md` - complete template as defined above

## Input

**Original MD File**: [Path to original MD file]
**Domain**: [Domain/Context of the MD file]
**Validation Focus**: [Structure/Content/Reference/All]

## Example Usage

### Input
Original MD: `chat-prompt-en.md`
Domain: "GitHub Copilot Skills Development"
Validation Focus: "All"

### Expected Output
1. Checker prompts for Prompt 6 (Test Case Generation)
2. Checker prompts for Prompt 7 (BDD Scenario Generation)
3. Analysis templates for difference assessment
4. Output templates for validation reports
5. Configuration files for confidence levels and review process
6. How-to guide with example workflows

## Quality Assurance

1. **Completeness**: Ensure all prompts in original MD have corresponding checker prompts
2. **Consistency**: Maintain consistent validation criteria across all prompts
3. **Clarity**: Provide clear, specific validation instructions
4. **Actionability**: Include actionable optimization suggestions
5. **Preservation**: Ensure passed content identification mechanisms

## Notes

- All generated content must be in English only
- Follow existing naming conventions from original MD
- Maintain consistency with established patterns
- Include preservation mechanisms to protect passed outputs
- Provide clear examples and usage guidelines
