---

# CTO Demo Prompt Set - 15-Minute Quick Start

**Version**: 1.0.0
**Last Updated**: 2026-03-18
**Author**: System Administrator

## Overview

This prompt set is designed for a 15-minute demonstration to C-level executives, showcasing the key capabilities of the knowledge base system. The demo focuses on the most impactful features that highlight business value and technical innovation.

## Demo Sequence (15 Minutes)

### 1. System Overview (2 minutes)
- **Prompt 1**: Generate executive summary of the knowledge base system
- **Input**: System architecture description
- **Output**: Executive-level overview with key metrics and benefits

### 2. Business Rule Extraction (3 minutes)
- **Prompt 2**: Extract atomic rules from sample business document
- **Input**: Sample business document snippet
- **Output**: Structured atomic rules with unique identifiers

### 3. AI Capability Demonstration (4 minutes)
- **Prompt 3**: Generate Copilot Skills from extracted rules
- **Input**: Extracted atomic rules
- **Output**: Ready-to-use Copilot Skills with natural language interaction

### 4. Test Automation (3 minutes)
- **Prompt 4**: Generate BDD test scenarios
- **Input**: Extracted atomic rules
- **Output**: Gherkin-style BDD scenarios for test automation

### 5. Validation and Quality Assurance (3 minutes)
- **Prompt 5**: Validate generated outputs using LLM Checker
- **Input**: Generated test scenarios
- **Output**: Validation report with confidence scores

## Detailed Prompts

### Prompt 1: Executive Summary Generation

```markdown
# Executive Summary Generator

## Objective
Generate a concise executive summary of the knowledge base system for C-level presentation.

## Input
```
The knowledge base system is a traceable, verifiable, updatable, and scalable business knowledge management platform that:
- Extracts atomic business rules from documentation
- Generates AI-powered Copilot Skills for natural language interaction
- Creates test automation assets (BDD scenarios)
- Validates outputs through an LLM Checker System
- Supports multi-format documents (PDF, Word, Excel, Email)
- Provides real-time monitoring and security features
```

## Output Requirements
- Maximum 200 words
- Focus on business value and ROI
- Include key metrics and competitive advantages
- Use executive-friendly language
- Highlight time and cost savings
```

### Prompt 2: Business Rule Extraction

```markdown
# Business Rule Extraction

## Objective
Extract atomic business rules from a sample financial document.

## Input
```
Sample Document Snippet:
"Initial Margin Requirements: For equity positions, the initial margin requirement is 25% of the total position value. For options positions, the initial margin requirement is the greater of 10% of the underlying value or $5 per contract."
```

## Output Requirements
- Extract atomic rules with unique identifiers
- Structure rules with conditions and actions
- Ensure each rule contains only one requirement
- Format as JSON for easy integration
- Include confidence scores for each rule
```

### Prompt 3: Copilot Skill Generation

```markdown
# Copilot Skill Generator

## Objective
Generate a Copilot Skill from extracted business rules for natural language interaction.

## Input
```
{
  "rules": [
    {
      "id": "RULE-001",
      "name": "Equity Initial Margin Calculation",
      "condition": "Equity position",
      "action": "Calculate initial margin as 25% of total position value",
      "confidence": 0.95
    },
    {
      "id": "RULE-002",
      "name": "Options Initial Margin Calculation",
      "condition": "Options position",
      "action": "Calculate initial margin as greater of 10% of underlying value or $5 per contract",
      "confidence": 0.95
    }
  ]
}
```

## Output Requirements
- Generate a Copilot Skill for margin calculation
- Include natural language examples
- Format as markdown for immediate use
- Add skill trigger phrases
- Include usage instructions
```

### Prompt 4: BDD Test Scenario Generation

```markdown
# BDD Test Scenario Generator

## Objective
Generate Gherkin-style BDD test scenarios for margin calculation rules.

## Input
```
{
  "rules": [
    {
      "id": "RULE-001",
      "name": "Equity Initial Margin Calculation",
      "condition": "Equity position",
      "action": "Calculate initial margin as 25% of total position value",
      "confidence": 0.95
    },
    {
      "id": "RULE-002",
      "name": "Options Initial Margin Calculation",
      "condition": "Options position",
      "action": "Calculate initial margin as greater of 10% of underlying value or $5 per contract",
      "confidence": 0.95
    }
  ]
}
```

## Output Requirements
- Generate Gherkin-style BDD scenarios
- Include Given-When-Then structure
- Add concrete examples with numbers
- Format as .feature file content
- Include scenario outlines for data-driven testing
```

### Prompt 5: Output Validation

```markdown
# LLM Checker Validation

## Objective
Validate generated BDD scenarios using LLM Checker System.

## Input
```
Feature: Margin Calculation Validation
  As a risk analyst
  I want to verify margin calculations
  So that I can ensure compliance with regulatory requirements

  Scenario: Calculate equity initial margin
    Given a client has an equity position of $10,000
    When the initial margin requirement is 25%
    Then the initial margin should be $2,500

  Scenario: Calculate options initial margin (10% rule)
    Given a client has an options position with underlying value of $5,000
    When the initial margin requirement is the greater of 10% or $5 per contract
    And there are 10 contracts
    Then the initial margin should be $500

  Scenario: Calculate options initial margin ($5 per contract rule)
    Given a client has an options position with underlying value of $1,000
    When the initial margin requirement is the greater of 10% or $5 per contract
    And there are 100 contracts
    Then the initial margin should be $500
```

## Output Requirements
- Validate BDD scenarios against original rules
- Check for completeness and correctness
- Provide confidence scores for each scenario
- Identify any potential issues or gaps
- Generate a validation report with recommendations
```

## Demo Preparation Checklist

1. **Before Demo**
   - Prepare sample business document snippet
   - Set up environment with all required tools
   - Test each prompt to ensure it works within time constraints
   - Prepare slides with key talking points

2. **During Demo**
   - Start with system overview (2 min)
   - Show rule extraction (3 min)
   - Demonstrate Copilot Skill interaction (4 min)
   - Showcase BDD test generation (3 min)
   - Present validation results (3 min)
   - Leave time for Q&A

3. **After Demo**
   - Provide executive summary document
   - Follow up with detailed technical documentation
   - Schedule deeper technical review if requested

## Expected Outcomes

- **Business Value**: Demonstrate how the system reduces time-to-market and improves compliance
- **Technical Innovation**: Showcase AI-powered capabilities and automation
- **ROI**: Highlight time and cost savings from automated rule extraction and testing
- **Scalability**: Emphasize how the system grows with business needs
- **Competitive Advantage**: Position as a cutting-edge solution for business knowledge management

## Technical Requirements

- LLM API access (for both generation and validation)
- Git repository access
- Basic command line familiarity
- Internet connection
- Presentation software (optional for slides)