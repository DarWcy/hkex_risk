# Checker Input Template

## Overview

This template is used to prepare input data for the LLM Checker system. It includes the marker output to validate, original business rules, and validation criteria.

## Input Sections

### 1. Marker Output

**Prompt 6 Output (Test Cases):**
```markdown
[Paste content from governance/PROMPT6-OUTPUT.md]
```

**Prompt 7 Output (BDD Scenarios):**
```markdown
[Paste content from governance/PROMPT7-OUTPUT.md]
```

### 2. Original Business Rules

**Relevant MD Files:**
- File: `docs/source-files/[filename].md`
- Rule Paragraph IDs: [List relevant paragraph IDs]

**Rule Content:**
```markdown
[Paste relevant rule content with structured IDs]
```

### 3. Validation Criteria

**Structural Requirements:**
- [ ] Test case format compliance
- [ ] BDD scenario Gherkin syntax
- [ ] Required fields presence
- [ ] Relationship mapping integrity

**Content Requirements:**
- [ ] Rule alignment
- [ ] Parameter validity
- [ ] Traceability completeness
- [ ] Language consistency (English only)

**Reference Requirements:**
- [ ] Rule source references
- [ ] Skill ID references
- [ ] Test reference consistency
- [ ] Cross-reference validity

### 4. Configuration

**Confidence Level Thresholds:**
- High: 4-5
- Medium: 2-3
- Low: 0-1

**Validation Rules:**
- Strict rule alignment
- No undefined parameters
- Complete traceability
- Consistent formatting

**Output Requirements:**
- Detailed validation report
- Difference analysis (if applicable)
- Optimization suggestions
- Confidence level assessment

### 5. Execution Context

**Execution Date:** [YYYY-MM-DD]
**Marker LLM Model:** [Model Name]
**Checker LLM Model:** [Model Name]
**Validation Scope:** [Prompt 6 / Prompt 7 / Both]

### 6. Instructions for Checker

You are acting as an LLM Checker tasked with validating the output of a Marker LLM. Your role is to:

1. **Analyze** the marker output against the original business rules
2. **Validate** structural compliance, content accuracy, and reference integrity
3. **Calculate** a confidence level based on validation results
4. **Generate** a detailed validation report
5. **Provide** optimization suggestions for any issues found
6. **Ensure** that passed outputs are not negatively affected by your suggestions

**Key Guidelines:**
- Focus on rule alignment and structural compliance
- Preserve valid content that already meets requirements
- Provide specific, targeted suggestions for improvements
- Reference specific rule paragraph IDs in your analysis
- Maintain English language consistency throughout

**Output Format:**
- Validation report with clear pass/fail status
- Confidence level assessment
- Detailed difference analysis (if applicable)
- Optimization suggestions with justification
- Preservation of passed content

## Usage Instructions

1. Fill in the marker output sections with the actual content from PROMPT6-OUTPUT.md and PROMPT7-OUTPUT.md
2. Add the relevant business rules from the MD files
3. Set the appropriate validation criteria
4. Configure the confidence level thresholds
5. Provide execution context information
6. Use this template as input for the checker LLM