# Exit Criteria and Optimization Mechanism

## Overview

This document defines the exit criteria for the marker-checker confidence level loop and the optimization mechanism for cases where confidence level requirements are not met after multiple iterations including human review feedback.

## Exit Criteria Definition

### 1. Maximum Iteration Limit

**Maximum Iterations**: 3 rounds of marker-checker-review cycles

**Iteration Counting**:
- Round 1: Initial marker output → checker validation → human review
- Round 2: Revised marker output → checker validation → human review
- Round 3: Final revised marker output → checker validation → human review

**Exit Trigger**: After Round 3, if confidence level is still below threshold, trigger exit mechanism

### 2. Confidence Level Thresholds

**Minimum Acceptable Confidence Level**: 3.0 (Medium)

**Confidence Level Requirements**:
- **Excellent (4.0-5.0)**: Pass - No further action needed
- **Good (3.0-3.9)**: Pass - Minor improvements optional
- **Medium (2.0-2.9)**: Fail - Requires optimization
- **Poor (1.0-1.9)**: Fail - Requires significant optimization

**Exit Trigger**: If confidence level < 3.0 after maximum iterations

### 3. Stagnation Detection

**Stagnation Criteria**: No improvement in confidence level for 2 consecutive iterations

**Stagnation Detection**:
- Compare confidence level scores across iterations
- If difference < 0.2 for 2 consecutive iterations, mark as stagnated
- Trigger exit mechanism even if maximum iterations not reached

**Exit Trigger**: Stagnation detected regardless of iteration count

### 4. Human Review Consensus

**Consensus Requirement**: All three review stages (Initial → Peer Review → Final Approval) must agree on action

**Consensus Scenarios**:
- **Pass Consensus**: All reviewers agree to accept output
- **Fail Consensus**: All reviewers agree to reject output
- **Mixed Consensus**: Reviewers disagree, escalate to project manager

**Exit Trigger**: Fail consensus or unresolved mixed consensus after escalation

## Exit Mechanism Workflow

### Phase 1: Exit Condition Assessment

1. **Check Iteration Count**:
   - Verify if maximum iterations (3) reached
   - Document iteration history

2. **Check Confidence Level**:
   - Calculate current confidence level
   - Compare against threshold (3.0)
   - Document confidence level trend

3. **Check Stagnation**:
   - Analyze confidence level improvement trend
   - Identify if stagnation detected
   - Document stagnation evidence

4. **Check Review Consensus**:
   - Review feedback from all three stages
   - Determine if consensus reached
   - Document consensus status

5. **Trigger Decision**:
   - If any exit criteria met, proceed to Phase 2
   - If none met, continue iteration loop

### Phase 2: Analysis Report Generation

1. **Comprehensive Analysis**:
   - Compile all validation reports from all iterations
   - Aggregate human review feedback
   - Identify persistent issues across iterations

2. **Root Cause Analysis**:
   - Analyze why confidence level not improving
   - Identify underlying causes (e.g., ambiguous requirements, insufficient data, model limitations)
   - Document root cause findings

3. **Impact Assessment**:
   - Evaluate impact of current confidence level on system
   - Assess risks of proceeding with current output
   - Document impact analysis

4. **Generate Exit Report**:
   - Create comprehensive exit analysis report
   - Include all findings and recommendations
   - Format using [analysis-template.md](file:///c:/Codes/hkex_risk/governance/checker/analysis/analysis-template.md)

### Phase 3: Optimization Strategy Development

1. **Strategy Selection**:
   - Based on root cause analysis, select appropriate optimization strategy
   - Choose from predefined strategies or develop custom approach
   - Document strategy selection rationale

2. **Optimization Plan Creation**:
   - Develop detailed optimization plan
   - Include specific actions, timelines, and responsibilities
   - Define success criteria for optimization

3. **Resource Assessment**:
   - Identify required resources (time, expertise, tools)
   - Assess resource availability
   - Plan resource allocation

4. **Generate Optimization Proposal**:
   - Create structured optimization proposal
   - Include implementation steps and expected outcomes
   - Format using [output-template.md](file:///c:/Codes/hkex_risk/governance/checker/outputs/output-template.md)

## Optimization Strategies

### Strategy 1: Requirement Refinement

**When to Use**: Root cause indicates ambiguous or unclear requirements

**Actions**:
1. **Requirement Clarification**:
   - Review original MD specifications
   - Identify ambiguous sections
   - Clarify with stakeholders

2. **Requirement Enhancement**:
   - Add specific examples
   - Include edge cases
   - Provide detailed explanations

3. **Requirement Validation**:
   - Validate enhanced requirements
   - Get stakeholder approval
   - Update original MD if needed

**Expected Outcome**: Clearer requirements lead to better marker outputs

### Strategy 2: Prompt Engineering Improvement

**When to Use**: Root cause indicates prompt design issues

**Actions**:
1. **Prompt Analysis**:
   - Analyze marker prompt structure
   - Identify weak or ambiguous instructions
   - Review prompt engineering best practices

2. **Prompt Refinement**:
   - Improve prompt clarity
   - Add specific examples
   - Include formatting requirements

3. **Prompt Testing**:
   - Test refined prompts with sample inputs
   - Validate output quality
   - Iterate based on test results

**Expected Outcome**: Better prompts lead to higher quality marker outputs

### Strategy 3: Model Enhancement

**When to Use**: Root cause indicates model limitations

**Actions**:
1. **Model Evaluation**:
   - Evaluate current model performance
   - Identify specific limitations
   - Compare with alternative models

2. **Model Selection**:
   - Research alternative models
   - Evaluate model capabilities
   - Select appropriate model

3. **Model Integration**:
   - Integrate new model
   - Update configuration
   - Train team on new model

**Expected Outcome**: Better model leads to improved output quality

### Strategy 4: Hybrid Approach

**When to Use**: Root cause indicates multiple contributing factors

**Actions**:
1. **Multi-Strategy Implementation**:
   - Combine requirement refinement
   - Include prompt engineering improvements
   - Consider model enhancement

2. **Phased Implementation**:
   - Implement strategies in phases
   - Measure impact of each phase
   - Adjust based on results

3. **Integrated Testing**:
   - Test combined approach
   - Validate overall improvement
   - Document results

**Expected Outcome**: Comprehensive improvement across multiple areas

### Strategy 5: Acceptance with Mitigation

**When to Use**: Root cause indicates fundamental limitations that cannot be resolved

**Actions**:
1. **Risk Assessment**:
   - Assess risks of accepting current output
   - Identify mitigation measures
   - Document risk analysis

2. **Mitigation Planning**:
   - Develop mitigation strategies
   - Implement additional quality checks
   - Plan manual review processes

3. **Acceptance Decision**:
   - Get stakeholder approval
   - Document acceptance rationale
   - Define monitoring requirements

**Expected Outcome**: Acceptable output with managed risks

## Optimization Proposal Template

```markdown
# Optimization Proposal

## 1. Exit Summary

### 1.1 Exit Trigger
- **Exit Criteria Met**: [Specific criteria triggered]
- **Iteration Count**: [Number of iterations completed]
- **Final Confidence Level**: [Confidence level score]
- **Stagnation Detected**: [Yes/No]

### 1.2 Exit Analysis
- **Root Cause**: [Identified root cause]
- **Persistent Issues**: [List of issues across iterations]
- **Impact Assessment**: [Impact analysis]

## 2. Optimization Strategy

### 2.1 Selected Strategy
- **Strategy Name**: [Strategy name]
- **Strategy Type**: [Requirement Refinement / Prompt Engineering / Model Enhancement / Hybrid / Acceptance with Mitigation]
- **Selection Rationale**: [Why this strategy was chosen]

### 2.2 Implementation Plan
- **Phase 1**: [Actions and timeline]
- **Phase 2**: [Actions and timeline]
- **Phase 3**: [Actions and timeline]

### 2.3 Resource Requirements
- **Time Required**: [Estimated time]
- **Expertise Needed**: [Required skills]
- **Tools Required**: [Required tools]

## 3. Expected Outcomes

### 3.1 Success Criteria
- **Target Confidence Level**: [Target score]
- **Target Timeline**: [Target date]
- **Quality Metrics**: [Specific quality improvements]

### 3.2 Risk Mitigation
- **Potential Risks**: [Identified risks]
- **Mitigation Measures**: [Mitigation strategies]
- **Contingency Plans**: [Backup plans]

## 4. Approval and Next Steps

### 4.1 Approval Required
- **Approver**: [Required approver]
- **Approval Deadline**: [Deadline]
- **Approval Criteria**: [Approval requirements]

### 4.2 Next Steps
1. [Immediate action]
2. [Follow-up action]
3. [Long-term action]

## 5. Appendices

### 5.1 Iteration History
- **Iteration 1**: [Confidence level, key issues]
- **Iteration 2**: [Confidence level, key issues]
- **Iteration 3**: [Confidence level, key issues]

### 5.2 Review Feedback Summary
- **Initial Review**: [Summary of feedback]
- **Peer Review**: [Summary of feedback]
- **Final Approval**: [Summary of feedback]

### 5.3 Supporting Analysis
- [Attach detailed analysis reports]
```

## Implementation Process

### Step 1: Exit Detection

1. **Monitor Iterations**:
   - Track iteration count
   - Monitor confidence level trends
   - Check for stagnation

2. **Evaluate Exit Criteria**:
   - Compare against all exit criteria
   - Determine if exit triggered
   - Document evaluation results

### Step 2: Analysis and Reporting

1. **Generate Exit Report**:
   - Use analysis-template.md
   - Include comprehensive findings
   - Document root causes

2. **Review with Stakeholders**:
   - Present exit report
   - Discuss findings
   - Get input on optimization approach

### Step 3: Strategy Development

1. **Select Optimization Strategy**:
   - Based on root cause analysis
   - Consider resource constraints
   - Evaluate expected outcomes

2. **Develop Optimization Proposal**:
   - Use optimization proposal template
   - Include detailed implementation plan
   - Define success criteria

### Step 4: Approval and Implementation

1. **Get Approval**:
   - Present optimization proposal
   - Obtain stakeholder approval
   - Document approval decision

2. **Implement Optimization**:
   - Follow implementation plan
   - Monitor progress
   - Adjust as needed

### Step 5: Validation

1. **Validate Optimization**:
   - Run marker-checker cycle again
   - Measure improvement
   - Compare against success criteria

2. **Document Results**:
   - Record optimization outcomes
   - Update documentation
   - Share lessons learned

## Monitoring and Tracking

### Iteration Tracking

Track the following metrics for each iteration:
- **Iteration Number**
- **Confidence Level Score**
- **Key Issues Identified**
- **Human Review Feedback**
- **Improvement Actions Taken**
- **Confidence Level Change**

### Exit Condition Monitoring

Monitor the following indicators:
- **Iteration Count**: Approaching maximum (3)
- **Confidence Level Trend**: Improving, stable, or declining
- **Stagnation Detection**: No improvement for 2 consecutive iterations
- **Review Consensus**: Agreement or disagreement among reviewers

### Optimization Tracking

Track the following metrics for optimization:
- **Strategy Selected**
- **Implementation Timeline**
- **Resource Utilization**
- **Confidence Level Improvement**
- **Success Criteria Achievement**

## Escalation Path

### Level 1: Project Lead
- **Trigger**: Exit criteria met
- **Action**: Review exit report, approve optimization strategy
- **Timeline**: Within 2 business days

### Level 2: Department Manager
- **Trigger**: Optimization strategy requires significant resources
- **Action**: Approve resource allocation, authorize implementation
- **Timeline**: Within 3 business days

### Level 3: Executive Sponsor
- **Trigger**: Fundamental limitations or acceptance with mitigation
- **Action**: Approve acceptance with mitigation, authorize exceptional measures
- **Timeline**: Within 5 business days

## Documentation Requirements

### Required Documentation

1. **Exit Report**:
   - Comprehensive analysis of exit conditions
   - Root cause analysis
   - Impact assessment

2. **Optimization Proposal**:
   - Selected strategy and rationale
   - Implementation plan
   - Expected outcomes

3. **Approval Records**:
   - Approval decisions
   - Approver signatures
   - Approval dates

4. **Implementation Records**:
   - Implementation steps taken
   - Results achieved
   - Lessons learned

### Documentation Storage

- **Location**: `governance/checker/exit-reports/`
- **Naming**: `exit-report-[YYYYMMDD]-[SEQ].md`
- **Retention**: Keep all exit reports for audit trail

## Continuous Improvement

### Process Improvement

1. **Analyze Exit Patterns**:
   - Identify common exit triggers
   - Analyze root causes
   - Find patterns in optimization strategies

2. **Refine Criteria**:
   - Adjust exit criteria based on experience
   - Update confidence level thresholds
   - Refine stagnation detection

3. **Improve Strategies**:
   - Enhance existing optimization strategies
   - Develop new strategies
   - Document best practices

### Knowledge Sharing

1. **Share Lessons Learned**:
   - Document insights from exit cases
   - Share with team
   - Update training materials

2. **Update Guidelines**:
   - Incorporate lessons into guidelines
   - Update templates
   - Improve documentation

## Conclusion

This exit criteria and optimization mechanism provides a structured approach to handling cases where confidence level requirements are not met after multiple iterations. By following this process, teams can:

- Identify root causes of quality issues
- Develop targeted optimization strategies
- Implement improvements systematically
- Validate effectiveness of optimizations
- Continuously improve the overall process

The mechanism ensures that quality issues are addressed systematically and that the marker-checker system continues to improve over time.
