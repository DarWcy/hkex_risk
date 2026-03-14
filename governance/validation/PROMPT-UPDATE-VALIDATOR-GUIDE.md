# Prompt Update Validator and Auto-Commit Guide

## Overview

The Prompt Update Validator is an automated tool that ensures the integrity of the `chat-prompt-en.md` file and creates automatic git commits when updates are made. This tool helps prevent prompt loss and maintains proper documentation of all changes.

## Features

- **Prompt Integrity Validation**: Ensures all 15 prompts are present and properly formatted
- **Section Validation**: Verifies all required sections exist in the document
- **Update Record Checking**: Confirms that update records are added for each change
- **Duplicate Detection**: Identifies duplicate prompts or sections
- **Automatic Git Commits**: Creates commits with descriptive messages
- **Validation Reports**: Generates detailed JSON reports for audit purposes

## Installation

The validator scripts are located in the `governance/` directory:

- `prompt-update-validator.py` - Python version (cross-platform)
- `prompt-update-validator.ps1` - PowerShell version (Windows)

## Usage

### Windows (PowerShell)

```powershell
# Navigate to project root
cd c:\Codes\hkex_risk

# Run validation (normal mode)
.\governance\prompt-update-validator.ps1

# Run validation with force commit (skips update record check)
.\governance\prompt-update-validator.ps1 -Force
```

### Python (Cross-platform)

```bash
# Navigate to project root
cd c:\Codes\hkex_risk

# Run validation (normal mode)
python governance/prompt-update-validator.py

# Run validation with force commit
python governance/prompt-update-validator.py --force
```

## Validation Rules

### Required Prompts
The validator checks for all 15 prompts:
- Prompt 1: Structured MD Knowledge Base Generation with Paragraph IDs
- Prompt 2: Framework Structure Creation and Configuration
- Prompt 3: Copilot Skill Modular Generation + BDD Association + Structured Reference + Script Pre-embedding
- Prompt 4: Copilot Skill Index + Relationship + Reference/Script Management + Usage Guidelines
- Prompt 5: Skill Automation Script Generation + Git/Verification Linkage
- Prompt 6: Structured Iterative Test Case Generation + Relationship + Reference Pre-embedding
- Prompt 7: BDD/Behave Scenario Generation + Multi-dimensional Relationships + Reference Bidirectional Traceability
- Prompt 8: New Business Document Addition - Knowledge Base Incremental Update Process Generation + Reference/Script Synchronization
- Prompt 9: Update Existing Business Document - Knowledge Base Synchronization Update Process Generation + Reference/Script Synchronization
- Prompt 10: Test Execution and Results Validation + Coverage Analysis
- Prompt 11: BDD Scenario Execution and Reporting + Automation Integration
- Prompt 12: Skill Validation and Quality Assurance + Governance
- Prompt 13: Performance Monitoring and Optimization + Resource Management
- Prompt 14: Documentation Generation and Publishing + Knowledge Base Maintenance
- Prompt 15: Audit and Compliance + Risk Management

### Required Sections
The validator checks for these required sections:
- Global Rules for Prompt Management
- Knowledge Base Foundation Prompts
- Update Records
- Version History
- Directory Structure Summary
- Quick Reference

### Update Record Requirements
Before running the validator, you must add an update record in the "Update Records" section of `chat-prompt-en.md`:

```markdown
### Update YYYY-MM-DD - Brief Description
- **Date**: YYYY-MM-DD
- **Author**: Your Name or Identifier
- **Description**: Clear description of what was changed
- **Impact**: Potential impact on downstream processes or dependencies
- **Validation**: Steps taken to validate the changes
```

## Validation Process

### Step 1: Make Changes to chat-prompt-en.md
Edit the prompt file as needed, ensuring you follow the global rules and maintain all 15 prompts.

### Step 2: Add Update Record
Add a new update record in the "Update Records" section with today's date.

### Step 3: Run Validator
Execute the validation script:
```powershell
.\governance\prompt-update-validator.ps1
```

### Step 4: Review Results
The validator will display:
- Total prompts expected and found
- Validation status (PASSED/FAILED)
- Update record status (EXISTS/MISSING)
- Any issues or missing prompts
- Validation report location

### Step 5: Automatic Commit
If validation passes and update record exists, the validator will automatically create a git commit with a descriptive message.

## Validation Reports

The validator creates detailed JSON reports in the `governance/` directory with the format:
`prompt-validation-YYYYMMDD-HHmmss.json`

Each report contains:
- Timestamp
- Prompt file path
- Validation results
- Update record status
- Total prompts expected and found
- Ready for commit status

## Troubleshooting

### Validation Failed
- Check for missing prompts in the output
- Verify all required sections are present
- Ensure no duplicate prompts exist
- Review the validation report for specific issues

### Update Record Missing
- Add an update record with today's date in the "Update Records" section
- Include all required fields: Date, Author, Description, Impact, Validation

### Git Commit Failed
- Ensure you're in a git repository
- Check git configuration (user.name, user.email)
- Verify you have write permissions to the repository

## Best Practices

1. **Always Add Update Records**: Document every change with a proper update record
2. **Run Validator After Changes**: Validate your changes before committing
3. **Review Validation Reports**: Keep track of validation history
4. **Maintain Prompt Integrity**: Never delete prompts without explicit approval
5. **Follow Global Rules**: Adhere to the global rules defined in the document

## Integration with Workflow

### Before Committing
```powershell
# 1. Make changes to chat-prompt-en.md
# 2. Add update record
# 3. Run validator
.\governance\prompt-update-validator.ps1

# 4. If validation passes, commit is created automatically
# 5. If validation fails, fix issues and run again
```

### Continuous Integration
The validator can be integrated into CI/CD pipelines to ensure prompt integrity across all commits.

## Support

For issues or questions:
- Check the validation report for detailed error information
- Review the global rules in `chat-prompt-en.md`
- Consult the project documentation in `README.md`

## Version History

- **v1.0** (2024-01-01): Initial release with prompt integrity validation and auto-commit functionality
