---

# CTO Demo Prompt Set - 15-Minute Quick Start

**Version**: 1.0.0
**Last Updated**: 2026-03-18
**Author**: System Administrator

## Overview

This prompt set is designed for a 19-minute demonstration to C-level executives, showcasing the key capabilities of the knowledge base system. The demo focuses on the most impactful features that highlight business value and technical innovation.

## Demo Sequence (19 Minutes)

### 1. System Overview (2 minutes)
- **Prompt 1**: Generate executive summary of the knowledge base system
- **Input**: System architecture description
- **Output**: Executive-level overview with key metrics and benefits

### 2. Business Rule Extraction (3 minutes)
- **Prompt 2**: Extract atomic rules from sample business document
- **Input**: Sample business document snippet
- **Output**: Structured atomic rules with unique identifiers
- **File Operation**: Save extracted rules to `extracted_rules.json`

### 3. AI Capability Demonstration (4 minutes)
- **Prompt 3**: Generate Copilot Skills from extracted rules
- **Input**: Extracted atomic rules
- **Output**: Ready-to-use Copilot Skills with natural language interaction
- **File Operation**: Save Copilot Skill to `lme_market_data_assistant.md`

### 4. Test Automation (3 minutes)
- **Prompt 4**: Generate BDD test scenarios
- **Input**: Extracted atomic rules
- **Output**: Gherkin-style BDD scenarios for test automation
- **File Operation**: Save BDD scenarios to `lme_market_data_validation.feature`

### 5. Validation and Quality Assurance (3 minutes)
- **Prompt 5**: Validate generated outputs using LLM Checker
- **Input**: Generated test scenarios
- **Output**: Validation report with confidence scores
- **File Operation**: Save validation report to `validation_report.json`

### 6. Checker Report Generation (2 minutes)
- **Prompt 6**: Generate comprehensive checker report
- **Input**: Validation report from Prompt 5
- **Output**: Detailed checker report with findings and recommendations
- **File Operation**: Save checker report to `checker_report.md`

### 7. Executive Summary of Checker Report (2 minutes)
- **Prompt 7**: Create executive summary of checker report
- **Input**: Detailed checker report from Prompt 6
- **Output**: Executive-friendly summary for C-level presentation
- **File Operation**: Save executive summary to `executive_summary.md`

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
- **File Writing**: Save the output to `extracted_rules.json`
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
- **File Writing**: Save the output to `lme_market_data_assistant.md`
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
- **File Writing**: Save the output to `lme_market_data_validation.feature`
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
- **File Writing**: Save the output to `validation_report.json`
```

### Prompt 6: Checker Report Generation

```markdown
# Checker Report Generator

## Objective
Generate a comprehensive checker report from the validation results.

## Input
```
{"validation_report": {
  "scenarios": [
    {
      "id": "SCENARIO-001",
      "name": "Calculate equity initial margin",
      "confidence": 0.98,
      "status": "PASS",
      "issues": []
    },
    {
      "id": "SCENARIO-002",
      "name": "Calculate options initial margin (10% rule)",
      "confidence": 0.97,
      "status": "PASS",
      "issues": []
    },
    {
      "id": "SCENARIO-003",
      "name": "Calculate options initial margin ($5 per contract rule)",
      "confidence": 0.96,
      "status": "PASS",
      "issues": []
    }
  ],
  "summary": {
    "total_scenarios": 3,
    "passed": 3,
    "failed": 0,
    "average_confidence": 0.97
  }
}}
```

## Output Requirements
- Generate a comprehensive checker report
- Include detailed findings for each scenario
- Add recommendations for improvement
- Format as professional report
- Include executive summary section
- Add visual elements (tables, charts) where appropriate
- Provide actionable insights
- **File Writing**: Save the output to `checker_report.md`
```

### Prompt 7: Executive Summary of Checker Report

```markdown
# Executive Summary of Checker Report

## Objective
Create an executive-friendly summary of the checker report for C-level presentation.

## Input
```
# Checker Report: Margin Calculation Validation

## Executive Summary
This report validates the margin calculation rules and associated test scenarios. All 3 test scenarios passed with high confidence scores, demonstrating strong compliance with regulatory requirements.

## Detailed Findings
- **Scenario 1**: Equity initial margin calculation - PASS (98% confidence)
- **Scenario 2**: Options initial margin (10% rule) - PASS (97% confidence)
- **Scenario 3**: Options initial margin ($5 per contract rule) - PASS (96% confidence)

## Recommendations
1. Implement automated validation for all margin calculation rules
2. Establish regular audit procedures for margin requirements
3. Develop additional test scenarios for edge cases

## Conclusion
The margin calculation system demonstrates strong compliance with regulatory requirements and business rules. The high confidence scores indicate reliable rule extraction and test generation capabilities.
```

## Output Requirements
- Maximum 150 words
- Focus on key findings and business impact
- Use executive-friendly language
- Highlight compliance status and confidence scores
- Include actionable recommendations
- Emphasize business value and risk mitigation
- **File Writing**: Save the output to `executive_summary.md`
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
   - Generate and display checker report (2 min)
   - Present executive summary of checker report (2 min)
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

## Run with File Output

### File Writing Capabilities

Each prompt in this demo sequence includes file writing instructions to persist generated content. The following files will be created during execution:

| Step | Prompt | Output File | Description |
|------|--------|-------------|-------------|
| 2 | Business Rule Extraction | `extracted_rules.json` | Structured atomic rules with confidence scores |
| 3 | Copilot Skill Generation | `lme_market_data_assistant.md` | Ready-to-use Copilot Skill documentation |
| 4 | BDD Test Generation | `lme_market_data_validation.feature` | Gherkin-style test scenarios |
| 5 | Validation | `validation_report.json` | Validation results with confidence scores |
| 6 | Checker Report | `checker_report.md` | Comprehensive checker report |
| 7 | Executive Summary | `executive_summary.md` | Executive-friendly summary |

### Execution Commands

To run the modified prompts with file writing capabilities:

```bash
# Step 2: Extract rules and save to file
# The LLM will generate rules and write to extracted_rules.json

# Step 3: Generate Copilot Skill and save to file
# The LLM will generate skill and write to lme_market_data_assistant.md

# Step 4: Generate BDD scenarios and save to file
# The LLM will generate scenarios and write to lme_market_data_validation.feature

# Step 5: Validate and save report
# The LLM will validate and write to validation_report.json

# Step 6: Generate checker report
# The LLM will generate report and write to checker_report.md

# Step 7: Generate executive summary
# The LLM will generate summary and write to executive_summary.md
```

### File Output Structure

Each file operation follows this pattern:
1. Generate content using the specified prompt
2. Format content according to requirements
3. Write to designated file path
4. Confirm successful write operation

### Verification

After execution, verify files were created:

```bash
ls -la *.json *.md *.feature
```