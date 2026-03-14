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

Create the following supporting templates:

#### 1. Analysis Template
Structure for detailed difference analysis:
```markdown
## Analysis Overview
- Analysis ID, Date, Analyst
- Scope and Focus

## Structural Analysis
- Component validation table
- Structure issues table

## Content Analysis
- Content validation table
- Content issues table

## Reference Analysis
- Reference validation table
- Reference issues table

## Confidence Level Assessment
- Overall confidence score
- Breakdown by item

## Difference Analysis
- Key differences
- Impact assessment

## Optimization Suggestions
- Critical improvements
- Minor improvements

## Preservation Section
- Passed content identification
- Low-risk changes

## Conclusion
- Summary and recommendations
```

#### 2. Output Template
Structure for validation output reports:
```markdown
## Validation Overview
- Report ID, Date, Status
- Scope and Method

## Validation Results
- Overall status and statistics
- Item-by-item results

## Confidence Level Assessment
- Breakdown and distribution

## Difference Analysis
- Structural, content, reference differences

## Optimization Suggestions
- Prioritized recommendations

## Preservation Section
- Passed content

## Risk Assessment
- Critical, moderate, low risks

## Human Review Recommendations
- Review focus areas and process

## Implementation Guide
- Recommended actions and rollback plan

## Conclusion
- Summary and next steps
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

Generate the following files:

### 1. Checker Prompts File
- **File Name**: `checker-prompts.md`
- **Location**: `governance/checker/prompts/`
- **Content**: All checker prompts for each identified prompt in original MD

### 2. Analysis Template
- **File Name**: `analysis-template.md`
- **Location**: `governance/checker/analysis/`
- **Content**: Structured template for difference analysis

### 3. Output Template
- **File Name**: `output-template.md`
- **Location**: `governance/checker/outputs/`
- **Content**: Structured template for validation reports

### 4. Configuration Files
- **Confidence Level Config**: `governance/checker/config/confidence-level-config.md`
- **Review Process Config**: `governance/checker/config/review-feedback-config.md`

### 5. How-To Guide
- **File Name**: `CHECKER-HOW-TO.md`
- **Location**: `governance/checker/`
- **Content**: Complete usage guide with examples

### 6. Feedback Templates
- **Initial Review**: `governance/checker/templates/feedback-template-initial-review.md`
- **Peer Review**: `governance/checker/templates/feedback-template-peer-review.md`
- **Final Approval**: `governance/checker/templates/feedback-template-final-approval.md`
- **General Feedback**: `governance/checker/templates/feedback-template-general.md`

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
