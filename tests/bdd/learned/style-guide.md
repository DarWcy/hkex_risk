# BDD Style Guide

## Overview
This style guide documents the learned patterns and best practices for BDD scenario writing based on system templates.

## General Principles

### 1. Gherkin Syntax
- Use Given/When/Then format consistently
- Start each step with a capital letter
- Keep steps concise and unambiguous
- Use present tense
- Avoid technical jargon when possible

### 2. Scenario Structure
- **Given**: Preconditions and setup
- **When**: Actions or events
- **Then**: Expected outcomes
- **Background**: Common preconditions for all scenarios

### 3. Naming Conventions
- **Feature ID**: `FT-[module]-[number]`
- **Scenario Names**: Clear and descriptive
- **Step Names**: Action-oriented and specific

## Template-Specific Patterns

### Type A (BA) - Business-Focused
- **Focus**: Business rule verification
- **Language**: Formal and business-oriented
- **Structure**: Tabular with clear rule references
- **Pattern**: "Verify [system] [action] for [object]"

### Type B (QA Lead) - Quality-Focused
- **Focus**: Quality assurance and test management
- **Language**: Formal and detailed
- **Structure**: Tabular with priority and test type
- **Pattern**: "Verify [system] [action] for [object]"

### Type C (Automation Tester) - Automation-Focused
- **Focus**: Executable scenarios and automation
- **Language**: Technical and precise
- **Structure**: Gherkin with parameterization
- **Pattern**: "Given [Condition]; When [Action]; Then [Result]"

### Type D (Mixed/General) - Universal
- **Focus**: Balanced coverage
- **Language**: Formal and clear
- **Structure**: Tabular with automation status
- **Pattern**: "Verify [system] [action] for [object]"

## Best Practices

### 1. Rule Alignment
- Each scenario should reference specific rule paragraph IDs
- Scenarios should not include content outside the rules
- Use rule-based precise assertions

### 2. Traceability
- Include requirement ID, skill ID, and BDD scenario ID
- Reference global process nodes
- Maintain bidirectional consistency with references

### 3. Maintainability
- Use reusable step definitions
- Keep scenarios focused and atomic
- Include update marking for future modifications
- Document relationships and references

### 4. Clarity
- Use descriptive scenario names
- Keep steps simple and direct
- Avoid ambiguity in expected results
- Document assumptions and preconditions

### 5. Consistency
- Follow the same structure for all scenarios
- Use consistent naming conventions
- Maintain consistent language style
- Align with template patterns

## Common Mistakes to Avoid

1. **Vague Steps**: Steps should be specific and actionable
2. **Overly Complex Scenarios**: Keep scenarios focused on one rule verification point
3. **Missing Rule References**: Always reference rule paragraph IDs
4. **Inconsistent Formatting**: Follow the style guide consistently
5. **Technical Jargon**: Use business-friendly language when possible
6. **Ambiguous Assertions**: Expected results should be measurable and clear
7. **Missing Relationships**: Always include requirement and skill references
8. **Unclear Preconditions**: Preconditions should be specific and verifiable

## Example Scenario

```gherkin
Feature: VaR Platform Portfolio Margin Calculation
  
  @im-calc @tier-p
  Scenario: Calculate portfolio margin for Tier P instruments
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Tier P instrument portfolio data is loaded
    When user loads Risk Parameter File
    And user inputs Tier P instrument portfolio
    And user calculates portfolio margin
    Then portfolio margin is calculated for Tier P instruments
    And calculation is based on IO-INTRO-001 (v1.4)
  
  Background:
    Given Global Process Node: VaR Platform Overview
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-001 / Skill ID: SKILL-001 / BDD Scenario ID: FT-IM-CALC-001
  
  # Update Marking
  # [RESERVED FOR UPDATES]
```

## Version History

| Version | Date | Changes | Author |
|---------|------|---------|--------|
| 1.0 | 2026-03-14 | Initial version | System Administrator |
