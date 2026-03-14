# Generic Checker Prompt Generator - Usage Guide

## Overview

This guide explains how to use the `generic-checker-prompt-generator.md` to create checker prompts for any original MD specification document.

## When to Use

Use this generator when you need to:
- Create a new checker system for a different domain or project
- Adapt the existing checker system to new requirements
- Generate checker prompts for additional prompts in the original MD
- Standardize validation across multiple similar projects

## Prerequisites

Before using the generator, ensure you have:
1. **Original MD File**: Complete specification document with prompts
2. **Domain Understanding**: Knowledge of the domain/context
3. **Validation Requirements**: Clear understanding of what needs validation
4. **Output Directory**: `governance/checker/` directory structure

## Usage Steps

### Step 1: Prepare Input

1. **Locate Original MD**: Identify the path to your original MD file
   ```
   Example: docs/specifications/api-spec.md
   ```

2. **Identify Domain**: Determine the domain/context
   ```
   Example: "REST API Development", "Data Pipeline Design", "Business Process Automation"
   ```

3. **Define Validation Focus**: Choose validation scope
   ```
   Options: Structure / Content / Reference / All
   ```

### Step 2: Execute Generator

1. **Load Generator Prompt**: Open `generic-checker-prompt-generator.md`

2. **Fill Input Parameters**:
   ```markdown
   **Original MD File**: [Your MD file path]
   **Domain**: [Your domain]
   **Validation Focus**: [Your focus]
   ```

3. **Run LLM**: Execute the generator prompt with your LLM

4. **Review Output**: Check generated files for completeness and accuracy

### Step 3: Customize Generated Files

1. **Review Checker Prompts**:
   - Verify each prompt aligns with original MD requirements
   - Adjust validation criteria as needed
   - Add domain-specific validation rules

2. **Customize Templates**:
   - Adapt analysis template to your specific needs
   - Modify output template for your reporting requirements
   - Update feedback templates for your review process

3. **Configure Settings**:
   - Adjust confidence level thresholds
   - Define severity levels for your context
   - Set up review workflow stages

### Step 4: Validate Generated System

1. **Test with Sample Data**:
   - Use known good outputs to verify validation logic
   - Test with known bad outputs to verify error detection
   - Validate confidence level calculations

2. **Review Documentation**:
   - Ensure how-to guide is clear and complete
   - Verify all examples are relevant
   - Check troubleshooting section

3. **Iterate**:
   - Refine prompts based on test results
   - Update templates based on usage feedback
   - Improve documentation

## File Structure After Generation

```
governance/checker/
├── prompts/
│   ├── checker-prompts.md          # Generated checker prompts
│   ├── checker-prompt.md           # (if single prompt system)
│   └── generic-checker-prompt-generator.md  # This generator
├── templates/
│   ├── checker-input-template.md   # Input preparation template
│   ├── checker-output-template.md  # Output format template
│   ├── diff-analysis-template.md   # Difference analysis template
│   ├── feedback-template-initial-review.md
│   ├── feedback-template-peer-review.md
│   ├── feedback-template-final-approval.md
│   └── feedback-template-general.md
├── outputs/
│   └── output-template.md          # Validation report template
├── analysis/
│   └── analysis-template.md        # Analysis template
└── config/
    ├── confidence-level-config.md  # Confidence level settings
    └── review-feedback-config.md   # Review process config
```

## Customization Guidelines

### Adapting Validation Criteria

1. **Domain-Specific Rules**:
   ```markdown
   # Add domain-specific validation rules
   - For API specs: Validate endpoint formats, HTTP methods
   - For data pipelines: Validate data flow, transformation logic
   - For business processes: Validate workflow steps, decision points
   ```

2. **Custom Confidence Metrics**:
   ```markdown
   # Define custom metrics for your domain
   - API Compliance: Endpoint naming, parameter validation
   - Data Quality: Schema compliance, data type correctness
   - Process Integrity: Step sequence, decision coverage
   ```

3. **Specialized Templates**:
   ```markdown
   # Create domain-specific template sections
   - API Testing: Add endpoint test cases section
   - Data Validation: Add data quality metrics section
   - Process Verification: Add workflow validation section
   ```

### Extending the System

1. **Additional Prompts**:
   - Follow the template structure for new prompts
   - Maintain consistency with existing prompts
   - Update how-to guide

2. **New Validation Types**:
   - Add new validation sections to prompts
   - Create corresponding template sections
   - Update configuration files

3. **Integration Points**:
   - Define integration with existing tools
   - Add automation scripts
   - Update documentation

## Best Practices

### 1. Maintain Consistency
- Use consistent terminology across all files
- Follow established naming conventions
- Maintain uniform formatting

### 2. Document Changes
- Track all customizations
- Document rationale for changes
- Update version information

### 3. Test Thoroughly
- Validate with diverse test cases
- Test edge cases and error conditions
- Verify integration points

### 4. Review Regularly
- Periodically review validation criteria
- Update based on feedback
- Refine confidence level thresholds

### 5. Preserve Passed Content
- Always include preservation mechanisms
- Document what should not be changed
- Provide clear guidance on minimal changes

## Common Patterns

### Pattern 1: API Specification Validation

**Original MD**: API endpoint specifications
**Checker Focus**: 
- Structure: Endpoint format, HTTP methods, parameters
- Content: Request/response schemas, examples
- Reference: Link to API documentation, version control

### Pattern 2: Data Pipeline Validation

**Original MD**: Data transformation specifications
**Checker Focus**:
- Structure: Pipeline stages, data flow
- Content: Transformation logic, data types
- Reference: Source/target systems, data lineage

### Pattern 3: Business Process Validation

**Original MD**: Business workflow specifications
**Checker Focus**:
- Structure: Process steps, decision points
- Content: Business rules, compliance requirements
- Reference: Regulatory documents, policy references

## Troubleshooting

### Issue: Generated Prompts Too Generic

**Solution**:
- Add more specific domain context to input
- Include examples in the original MD
- Customize validation criteria post-generation

### Issue: Templates Don't Match Needs

**Solution**:
- Modify template sections to match your workflow
- Add/remove sections as needed
- Update field names to match your terminology

### Issue: Confidence Levels Not Accurate

**Solution**:
- Adjust scoring criteria in configuration
- Add domain-specific metrics
- Calibrate based on test results

## Examples

### Example 1: API Development Project

```markdown
**Original MD File**: docs/api/api-specification-v2.md
**Domain**: "REST API Development"
**Validation Focus**: "All"

Generated Files:
- Checker prompts for API endpoint validation
- Templates for request/response validation
- Configuration for API compliance checking
```

### Example 2: Data Engineering Project

```markdown
**Original MD File**: docs/data/pipeline-specification.md
**Domain**: "Data Pipeline Engineering"
**Validation Focus**: "Structure and Content"

Generated Files:
- Checker prompts for data flow validation
- Templates for data quality assessment
- Configuration for data lineage tracking
```

### Example 3: Business Process Automation

```markdown
**Original MD File**: docs/process/workflow-automation.md
**Domain**: "Business Process Automation"
**Validation Focus**: "Content and Reference"

Generated Files:
- Checker prompts for workflow validation
- Templates for compliance checking
- Configuration for process integrity
```

## Integration with Existing Systems

### Git Integration
- Add generated files to version control
- Create commit hooks for validation
- Set up CI/CD pipelines

### Documentation Integration
- Link checker documentation to main docs
- Include validation in development workflow
- Update README with checker usage

### Tool Integration
- Integrate with IDE plugins
- Connect to code review tools
- Link to project management systems

## Maintenance

### Regular Updates
- Review and update prompts quarterly
- Update templates based on usage feedback
- Refresh documentation

### Version Control
- Tag stable versions
- Maintain changelog
- Document breaking changes

### Continuous Improvement
- Collect usage metrics
- Gather user feedback
- Iterate on design

## Support and Resources

### Internal Resources
- Review existing checker implementations
- Consult domain experts
- Reference similar projects

### External Resources
- Prompt engineering best practices
- Validation pattern libraries
- Domain-specific guidelines

## Conclusion

The generic checker prompt generator provides a flexible framework for creating validation systems across different domains and projects. By following this guide, you can quickly establish robust validation processes that ensure quality and consistency in your LLM outputs.

Remember to:
- Customize for your specific needs
- Test thoroughly before deployment
- Maintain documentation
- Iterate based on feedback
