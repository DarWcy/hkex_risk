# Checker Output Template

## Overview

This template is used to structure the output of the LLM Checker system. It includes validation results, confidence level assessment, difference analysis, and optimization suggestions.

## Output Sections

### 1. Validation Summary

**Validation Date:** [YYYY-MM-DD]
**Validation Scope:** [Prompt 6 / Prompt 7 / Both]
**Overall Status:** [PASS / FAIL / PARTIAL]
**Confidence Level:** [0-5]
**Marker LLM Model:** [Model Name]
**Checker LLM Model:** [Model Name]

### 2. Structural Validation Results

**Test Case Structure:**
- [ ] Format compliance
- [ ] Required fields presence
- [ ] Relationship mapping integrity
- [ ] ID uniqueness

**BDD Scenario Structure:**
- [ ] Gherkin syntax compliance
- [ ] Feature file structure
- [ ] Step definition completeness
- [ ] Tag consistency

### 3. Content Validation Results

**Rule Alignment:**
- [ ] Rule compliance
- [ ] Parameter validity
- [ ] Traceability completeness
- [ ] Language consistency

**Test Case Content:**
- [ ] Scenario clarity
- [ ] Precondition completeness
- [ ] Test step executability
- [ ] Expected result specificity

**BDD Scenario Content:**
- [ ] Scenario clarity
- [ ] Step definition adequacy
- [ ] Background appropriateness
- [ ] Example coverage

### 4. Reference Validation Results

**Rule References:**
- [ ] MD file path validity
- [ ] Paragraph ID existence
- [ ] Rule version consistency

**Skill References:**
- [ ] Skill ID validity
- [ ] Test_Reference consistency
- [ ] Cross-reference integrity

### 5. Confidence Level Assessment

**Confidence Score Calculation:**
- Structural Validation: [0-5]
- Content Validation: [0-5]
- Reference Validation: [0-5]
- Overall Confidence: [0-5]

**Confidence Level Interpretation:**
- High (4-5): Outputs fully align with rules and structure
- Medium (2-3): Minor discrepancies that don't affect functionality
- Low (0-1): Significant issues requiring revision

### 6. Difference Analysis

**Identified Discrepancies:**

| Category | Issue | Severity | Location |
|----------|-------|----------|----------|
| [Category] | [Issue Description] | [Critical/Major/Minor] | [File:Line] |
| [Category] | [Issue Description] | [Critical/Major/Minor] | [File:Line] |

**Impact Assessment:**
- [Description of potential impact on functionality]

### 7. Optimization Suggestions

**Structural Improvements:**
- [Suggestion 1]
- [Suggestion 2]

**Content Improvements:**
- [Suggestion 1]
- [Suggestion 2]

**Reference Improvements:**
- [Suggestion 1]
- [Suggestion 2]

**Implementation Guidelines:**
- Make targeted changes to address specific issues
- Preserve valid content that already meets requirements
- Maintain consistency with existing structure
- Follow naming conventions and formatting standards

### 8. Passed Content Preservation

**Passed Test Cases:**
- [Test Case ID 1]
- [Test Case ID 2]

**Passed BDD Scenarios:**
- [BDD Scenario ID 1]
- [BDD Scenario ID 2]

**Preservation Instructions:**
- Do not modify the content of passed test cases and scenarios
- Only apply changes to identified issues
- Maintain original structure and formatting for passed content

### 9. Conclusion

**Summary of Findings:**
[Brief summary of validation results and key findings]

**Recommended Actions:**
1. [Action 1]
2. [Action 2]
3. [Action 3]

**Next Steps:**
- Implement optimization suggestions
- Re-validate after changes
- Document validation results
- Update confidence level assessment

## Usage Instructions

1. Fill in the validation results based on checker analysis
2. Calculate and document the confidence level
3. Provide detailed difference analysis for any issues
4. Offer specific optimization suggestions
5. Identify and preserve passed content
6. Include clear recommendations for next steps
7. Save the output as `{prompt}-checker-output.md` in the outputs directory