# LLM Checker System - How To Guide

## Overview

The LLM Checker System is designed to validate the outputs of the first LLM (marker) using a second LLM (checker). This system ensures that the generated test cases and BDD scenarios align with the original business rules and follow the required structure.

## Directory Structure

```
governance/checker/
├── prompts/          # Checker prompt templates
│   ├── checker-prompt.md             # Main checker prompt file
│   ├── generic-checker-prompt-generator.md      # Generic prompt generator
│   └── generic-checker-prompt-generator-usage.md # Generator usage guide
├── templates/        # Input/output templates
│   ├── feedback-template-initial-review.md    # Initial review feedback template
│   ├── feedback-template-peer-review.md       # Peer review feedback template
│   ├── feedback-template-final-approval.md    # Final approval feedback template
│   ├── feedback-template-general.md           # General feedback template
│   ├── checker-input-template.md            # Checker input template
│   ├── checker-output-template.md           # Checker output template
│   └── diff-analysis-template.md            # Difference analysis template
├── outputs/          # Checker execution outputs
│   └── output-template.md               # Output validation report template
├── analysis/         # Difference analysis reports
│   └── analysis-template.md             # Analysis template
└── config/           # Configuration files
    ├── confidence-level-config.md    # Confidence level assessment configuration
    └── review-feedback-config.md    # Review and feedback configuration
```

## Components

### 1. Checker Prompt

The checker prompt is designed to analyze the marker's output against the original business rules and structural requirements. The system includes a comprehensive prompt file:

- **checker-prompt.md**: Contains dedicated prompts for validating Prompt 6 (test cases) and Prompt 7 (BDD scenarios), including detailed validation criteria and output requirements.

#### Checker Prompt Structure

The checker prompt includes:

1. **Input Analysis**: Instructions to review original MD files and marker output
2. **Validation Process**: Detailed validation steps for structure, content, and references
3. **Confidence Level Assessment**: Criteria for evaluating output quality
4. **Difference Analysis**: Methods to identify discrepancies
5. **Optimization Suggestions**: Recommendations for improvements
6. **Output Requirements**: Structured format for validation reports

#### Prompt Variants

- **Prompt 6 Validator**: Focuses on test case structure, content, and reference validation
- **Prompt 7 Validator**: Focuses on BDD scenario syntax, alignment with test cases, and bidirectional traceability

### 2. Input Templates

- **Marker Output**: Output files from Prompt 6 (test cases) and Prompt 7 (BDD scenarios)
- **Original Rules**: Business rules from the knowledge base
- **Validation Criteria**: Structural and content validation rules
- **Checker Input Template**: Standardized format for preparing input data

### 3. Output Templates

- **Validation Reports**: Detailed validation results using output-template.md
- **Difference Analysis**: Comparison between marker output and expected structure using analysis-template.md
- **Optimization Suggestions**: Improvements while preserving passed outputs
- **Analysis Templates**: Structured format for detailed analysis using analysis-template.md

## Execution Flow

### Step 1: Prepare Input Files

1. **Marker Output Files**:
   - `governance/PROMPT6-OUTPUT.md` (test cases)
   - `governance/PROMPT7-OUTPUT.md` (BDD scenarios)

2. **Original Rules**:
   - Relevant MD files from `docs/source-files/`

3. **Checker Prompt**:
   - `governance/checker/prompts/checker-prompt.md` - Select the appropriate prompt variant

4. **Input Templates**:
   - Use `governance/checker/templates/checker-input-template.md` to prepare structured input

5. **Configuration**:
   - `governance/checker/config/confidence-level-config.md` - Confidence level settings
   - `governance/checker/config/review-feedback-config.md` - Review process configuration

### Step 2: Execute Checker

1. **Load Input Files**
2. **Select Prompt Variant**: Choose the appropriate prompt for Prompt 6 or 7 validation
3. **Run Checker LLM** with the prepared prompt
4. **Generate Validation Reports**: Use `output-template.md` for structured output
5. **Analyze Differences**: Use `analysis-template.md` for detailed analysis
6. **Provide Optimization Suggestions**: Include preservation of passed content

### Step 3: Review Results

1. **Validation Status**: Check if outputs pass validation
2. **Difference Analysis**: Review identified discrepancies
3. **Optimization Suggestions**: Evaluate proposed improvements
4. **Confidence Level**: Assess the overall confidence in the outputs

### Step 4: Human Review Process

The checker system includes a structured three-stage human review process to ensure quality and accuracy of validation results.

#### Stage 1: Initial Review

**Reviewers**: QA Lead, Business Analyst

**Process**:
1. Review checker validation results
2. Assess accuracy of identified differences
3. Evaluate quality of optimization suggestions
4. Provide initial feedback using [feedback-template-initial-review.md](file:///c:/Codes/hkex_risk/governance/checker/templates/feedback-template-initial-review.md)

**Output**: Initial review report with feedback

#### Stage 2: Peer Review

**Reviewers**: Senior QA, Technical Lead

**Process**:
1. Review initial review findings
2. Validate feedback accuracy
3. Assess impact of proposed changes
4. Provide peer review comments using [feedback-template-peer-review.md](file:///c:/Codes/hkex_risk/governance/checker/templates/feedback-template-peer-review.md)

**Output**: Peer review report with additional insights

#### Stage 3: Final Approval

**Reviewers**: Project Manager, System Owner

**Process**:
1. Review all previous feedback
2. Assess overall impact and risk
3. Approve or reject proposed changes
4. Document approval decision using [feedback-template-final-approval.md](file:///c:/Codes/hkex_risk/governance/checker/templates/feedback-template-final-approval.md)

**Output**: Final approval decision with implementation authorization

### Step 5: Implement Changes

1. **Review Approval**: Check if changes are approved
2. **Apply Approved Changes**: Implement approved optimizations
3. **Preserve Passed Content**: Ensure passed content remains intact
4. **Document Changes**: Record all modifications

## Configuration

### Confidence Level Settings

- **High (4-5)**: Outputs fully align with rules and structure
- **Medium (2-3)**: Minor discrepancies that don't affect functionality
- **Low (0-1)**: Significant issues requiring revision

### Review Process Configuration

The review process is configured in [review-feedback-config.md](file:///c:/Codes/hkex_risk/governance/checker/config/review-feedback-config.md) and includes:

- **Three-Stage Review**: Initial → Peer Review → Final Approval
- **Review Criteria**: Accuracy, quality, completeness, and impact assessment
- **Feedback Collection**: Structured feedback templates for each review stage
- **Confidence Level Adjustment**: Review-based confidence level adjustments

### Validation Rules

1. **Structural Validation**:
   - Test case format compliance
   - BDD scenario Gherkin syntax
   - Relationship mapping integrity

2. **Content Validation**:
   - Rule alignment
   - Parameter validity
   - Traceability completeness

3. **Reference Validation**:
   - Rule source references
   - Skill ID references
   - Test reference consistency

## File Naming Conventions

### Input Files
- `{prompt}-input.md` - Checker input for specific prompt
- `{prompt}-marker-output.md` - Marker output to validate
- `checker-prompt.md` - Main checker prompt file

### Output Files
- `{prompt}-checker-output.md` - Checker validation results
- `{prompt}-diff-analysis.md` - Difference analysis report
- `{prompt}-optimization.md` - Optimization suggestions
- `output-template.md` - Output validation report template
- `analysis-template.md` - Analysis template

### Template Files
- `checker-input-template.md` - Checker input template
- `checker-output-template.md` - Checker output template
- `diff-analysis-template.md` - Difference analysis template
- `feedback-template-*.md` - Feedback templates for different review stages

## Example Workflow

### 1. Validate Prompt 6 Output (Test Cases)

1. **Prepare Input**:
   - Marker Output: `governance/PROMPT6-OUTPUT.md`
   - Original MD Files: Relevant files from `docs/source-files/`
   - Checker Prompt: Use Prompt 6 Validator from `governance/checker/prompts/checker-prompt.md`

2. **Execute Checker**:
   - Run Checker LLM with the prepared prompt
   - Generate validation report using `output-template.md`
   - Create difference analysis using `analysis-template.md`

3. **Output Files**:
   - Validation Report: `governance/checker/outputs/prompt6-checker-output.md`
   - Difference Analysis: `governance/checker/analysis/prompt6-diff-analysis.md`
   - Optimization Suggestions: `governance/checker/outputs/prompt6-optimization.md`

4. **Review Process**:
   - Initial Review: Use `feedback-template-initial-review.md`
   - Peer Review: Use `feedback-template-peer-review.md`
   - Final Approval: Use `feedback-template-final-approval.md`

### 2. Validate Prompt 7 Output (BDD Scenarios)

1. **Prepare Input**:
   - Marker Output: `governance/PROMPT7-OUTPUT.md`
   - Test Cases: `governance/PROMPT6-OUTPUT.md` (for alignment check)
   - Original MD Files: Relevant files from `docs/source-files/`
   - Checker Prompt: Use Prompt 7 Validator from `governance/checker/prompts/checker-prompt.md`

2. **Execute Checker**:
   - Run Checker LLM with the prepared prompt
   - Generate validation report using `output-template.md`
   - Create difference analysis using `analysis-template.md`

3. **Output Files**:
   - Validation Report: `governance/checker/outputs/prompt7-checker-output.md`
   - Difference Analysis: `governance/checker/analysis/prompt7-diff-analysis.md`
   - Optimization Suggestions: `governance/checker/outputs/prompt7-optimization.md`

4. **Review Process**:
   - Initial Review: Use `feedback-template-initial-review.md`
   - Peer Review: Use `feedback-template-peer-review.md`
   - Final Approval: Use `feedback-template-final-approval.md`

## Optimization Guidelines

1. **Preserve Passed Outputs**:
   - Do not modify outputs that already meet requirements
   - Only suggest changes for identified issues

2. **Minimal Changes**:
   - Make targeted changes to address specific issues
   - Avoid broad restructuring of valid content

3. **Clear Justification**:
   - Provide detailed reasoning for each suggested change
   - Reference specific validation rules

## Troubleshooting

### Common Issues

1. **Structural Errors**:
   - Missing required fields
   - Incorrect formatting
   - Invalid references

2. **Content Errors**:
   - Rule violations
   - Invalid parameters
   - Incomplete traceability

3. **Reference Errors**:
   - Broken rule references
   - Mismatched skill IDs
   - Inconsistent test references

### Resolution Steps

1. **Identify Issue**:
   - Locate the specific error in the validation report
   - Understand the root cause

2. **Apply Fix**:
   - Make targeted changes to address the issue
   - Preserve valid content

3. **Re-validate**:
   - Run the checker again to verify the fix
   - Ensure no new issues were introduced

## Best Practices

1. **Regular Validation**:
   - Validate marker outputs immediately after generation
   - Establish a validation pipeline in the workflow

2. **Consistent Format**:
   - Maintain consistent input/output formats
   - Follow naming conventions strictly

3. **Documentation**:
   - Document all validation results
   - Track optimization suggestions and their implementation

4. **Continuous Improvement**:
   - Refine validation rules based on feedback
   - Update checker prompts to address new edge cases

5. **Review Process Best Practices**:
   - **Complete All Review Stages**: Ensure all three review stages are completed
   - **Use Structured Templates**: Use provided feedback templates for consistency
   - **Document Decisions**: Record all review decisions and justifications
   - **Maintain Traceability**: Link feedback to specific validation results
   - **Timely Reviews**: Complete reviews within established timelines
   - **Quality Feedback**: Provide specific, actionable, and constructive feedback
   - **Escalation Awareness**: Know when and how to escalate issues
   - **Continuous Learning**: Use review insights to improve the checker system

## Review Process Usage

### When to Conduct Reviews

- **After Checker Execution**: Always conduct reviews after checker generates validation reports
- **Before Implementation**: Complete all review stages before implementing changes
- **On Disagreement**: Escalate when reviewers disagree significantly
- **On Critical Issues**: Immediately escalate critical issues identified during review

### Review Quality Assurance

- **Reviewer Training**: Ensure reviewers are trained on review process and criteria
- **Template Compliance**: Use provided feedback templates consistently
- **Feedback Quality**: Provide specific, actionable, and well-justified feedback
- **Documentation**: Maintain complete records of all reviews and decisions
- **Follow-up**: Ensure review recommendations are tracked and implemented

## Generic Checker Prompt Generator

For creating checker systems for different domains or projects, use the **Generic Checker Prompt Generator**:

### Available Files

- **Generator Prompt**: `governance/checker/prompts/generic-checker-prompt-generator.md`
- **Usage Guide**: `governance/checker/prompts/generic-checker-prompt-generator-usage.md`

### When to Use

Use the generator when you need to:
- Create a new checker system for a different domain
- Adapt the existing system to new requirements
- Generate checker prompts for additional prompts
- Standardize validation across multiple projects

### Quick Start

1. **Prepare Input**:
   ```markdown
   **Original MD File**: [Your MD file path]
   **Domain**: [Your domain/context]
   **Validation Focus**: [Structure/Content/Reference/All]
   ```

2. **Execute Generator**:
   - Load `generic-checker-prompt-generator.md`
   - Fill in input parameters
   - Run with your LLM

3. **Review Output**:
   - Check generated checker prompts
   - Customize templates as needed
   - Validate the generated system

### Generated Components

The generator creates:
- **Checker Prompts**: Domain-specific validation prompts
- **Analysis Template**: Structured difference analysis
- **Output Template**: Validation report format
- **Configuration Files**: Confidence level and review settings
- **How-To Guide**: Usage documentation
- **Feedback Templates**: Review process templates

For detailed instructions, see [generic-checker-prompt-generator-usage.md](file:///c:/Codes/hkex_risk/governance/checker/prompts/generic-checker-prompt-generator-usage.md).

## Conclusion

The LLM Checker System provides a robust framework for validating marker outputs, ensuring they meet the required standards and align with business rules. By following this guide, you can effectively use the checker to improve output quality while preserving valid content.

For creating checker systems for new domains or projects, use the Generic Checker Prompt Generator to quickly establish validation processes tailored to your specific needs.