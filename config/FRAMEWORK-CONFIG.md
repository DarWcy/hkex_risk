# Framework Structure Configuration

## Project Metadata
- Project Name: Initial Margin Calculation Guide HKv14
- Business Domain: Financial Risk Management
- Source Document: Initial Margin Calculation Guide HKv14.pdf
- Source Version: 1.4

## Structure Template Selection
- Template Type: Brownfield
- Existing Structure Path: ./

## Layer Configuration

### Layer 1 - docs/
- Enabled: true
- Existing Files: Introduction-Overview.md, Risk-Parameter-File-Specification.md, Input-Data-Specification.md, Market-Risk-Component-Calculation.md, Margin-Adjustment-Process.md, Other-Risk-Components.md, Position-Processing-Logic.md, Collateral-Management.md, Corporate-Action-Processing.md, Calculation-Examples.md
- Naming Pattern: Module-SubTopic.md

### Layer 2 - docs/global-process/
- Enabled: true
- Process Flow Source: Core-Business-Global-Process-Flowchart.md

### Layer 3 - docs/source-files/
- Enabled: true
- Source Files: Initial Margin Calculation Guide HKv14.pdf

### Layer 4 - copilot-skills/
- Enabled: true
- Skill Naming Pattern: hkex-{module}-{capability}
- Script Language: Python

### Layer 5 - tests/
- Enabled: true
- Test Framework: Behave/BDD
- Test Case Pattern: TC-{module}-{number}

### Layer 6 - config/
- Enabled: true
- Version Format: MAJOR.MINOR.PATCH

### Layer 7 - governance/
- Enabled: true
- Fallback Levels: View/Edit/Audit/Decision

## Custom Directories (Optional)
- 

## Exclusions
- chat-prompt-en.md
- chat-prompt.md
- Prompt-1-Universal-Template.md

## Custom Requirements (Manual Entry)

### Domain-Specific Requirements
- Financial risk management compliance requirements
- HKEX-specific rules and processes

### Business Process Requirements
- Completeness and accuracy of margin calculation processes
- Exception handling and fallback mechanisms

### Technical Requirements
- Python script automation
- BDD test framework integration

### Compliance Requirements
- Compliance with financial regulatory requirements
- Audit trail and record keeping

### Testing Requirements
- Test cases covering all calculation logic
- Boundary condition testing
