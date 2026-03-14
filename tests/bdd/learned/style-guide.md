# BDD Template Style Guide

## Overview

This style guide documents the learned patterns and conventions from user-provided BDD templates. It serves as a reference for generating BDD scenarios that match user expectations and organizational standards.

## Template Types

### Type A - Business Analyst (BA)

**Characteristics**:
- Business-focused language
- Low technical terminology
- Simple sentence structures
- Emphasis on business rules and processes

**Example Pattern**:
```gherkin
Feature: Margin Calculation
  As a risk manager
  I want to calculate initial margin
  So that I can ensure sufficient collateral

  Scenario: Calculate margin for long position
    Given a client has a long position of 100 shares
    When the margin rate is 10%
    Then the initial margin should be calculated correctly
```

### Type B - QA Lead

**Characteristics**:
- Quality-focused language
- Medium technical terminology
- Structured sentence patterns
- Emphasis on test coverage and validation

**Example Pattern**:
```gherkin
Feature: IM-CALC-001 Margin Calculation Validation
  Background:
    Given the system is configured with margin rates
    And the client account is active

  @smoke @critical
  Scenario: Validate margin calculation for valid position
    Given position quantity is 100
    And position price is $50.00
    When the margin calculation is triggered
    Then the calculated margin should equal $500.00
    And the calculation should be logged
```

### Type C - Automation Tester

**Characteristics**:
- Technical language
- High technical terminology
- Precise sentence structures
- Emphasis on automation and CI/CD integration

**Example Pattern**:
```gherkin
Feature: [API] Margin Calculation Endpoint

  @automated @api @regression
  Scenario Outline: Calculate margin via API
    Given the API endpoint "/api/v1/margin/calculate" is available
    And the request payload contains:
      | field    | value      |
      | position | <position> |
      | price    | <price>    |
      | rate     | <rate>     |
    When a POST request is sent
    Then the response status should be 200
    And the response should contain:
      | field         | value           |
      | margin_amount | <expected>      |
      | currency      | USD             |

    Examples:
      | position | price | rate | expected |
      | 100      | 50.00 | 0.10 | 500.00   |
      | 200      | 25.00 | 0.15 | 750.00   |
```

### Type D - General/Mixed

**Characteristics**:
- Balanced language
- Medium technical terminology
- Flexible sentence structures
- Adaptable to various contexts

**Example Pattern**:
```gherkin
Feature: Margin Calculation - General

  Scenario: Basic margin calculation
    Given a position exists
    When margin is calculated
    Then the result should be correct
```

## Common Patterns

### Gherkin Keyword Usage

| Keyword | Usage Frequency | Context |
|---------|----------------|---------|
| Given   | High           | Preconditions |
| When    | High           | Actions |
| Then    | High           | Assertions |
| And     | Medium         | Additional steps |
| But     | Low            | Negative conditions |
| *       | Rare           | Bullet points |

### Tag Conventions

**By Type**:
- `@business` - Business rules
- `@technical` - Technical implementation
- `@smoke` - Smoke tests
- `@regression` - Regression tests
- `@critical` - Critical path
- `@automated` - Automated tests

**By Component**:
- `@api` - API tests
- `@ui` - UI tests
- `@integration` - Integration tests
- `@unit` - Unit tests

### Data Table Formats

**Horizontal Tables**:
```gherkin
Given the following data:
  | Field  | Value |
  | Name   | Test  |
  | Status | Active|
```

**Vertical Tables**:
```gherkin
Given the configuration:
  | Name   | Test Account |
  | Type   | Margin       |
  | Status | Active       |
```

## Best Practices

1. **Consistency**: Use consistent language and structure across scenarios
2. **Clarity**: Write clear, unambiguous steps
3. **Reusability**: Design steps for reuse across scenarios
4. **Traceability**: Link scenarios to requirements and rules
5. **Maintainability**: Keep scenarios focused and concise

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-14 | Initial style guide creation |
