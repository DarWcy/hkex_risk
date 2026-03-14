# Governance Directory

This directory contains all governance, audit, process documentation, and quality assurance materials for the HKEX Risk project.

## Directory Structure

```
governance/
├── README.md                              # This file
├── DIRECTORY-STRUCTURE-PROPOSAL.md        # Directory structure proposal document
│
├── analysis/                              # Analysis and research documents
│   ├── prompts/                           # Prompt logic and consistency analysis
│   │   ├── prompt-3-4-5-logic-analysis.md
│   │   ├── prompt-6-7-analysis.md
│   │   └── prompt-consistency-analysis.md
│   ├── outputs/                           # Output analysis and reviews
│   │   ├── PROMPT5-INPUT.md
│   │   ├── PROMPT5-OUTPUT.md
│   │   ├── PROMPT6-INPUT.md
│   │   ├── PROMPT6-OUTPUT.md
│   │   ├── PROMPT7-INPUT.md
│   │   └── PROMPT7-OUTPUT.md
│   └── templates/                         # Template analysis and mapping
│       ├── template-prompt-mapping.md
│       └── prompt-template-creation-guide.md
│
├── reviews/                               # Review system
│   ├── templates/                         # Review templates by artifact type
│   │   ├── skills/                        # Skill review templates
│   │   ├── test/                          # Test-related templates
│   │   ├── code/                          # Code review templates
│   │   ├── docs/                          # Documentation templates
│   │   ├── framework/                     # Framework templates
│   │   └── governance/                    # Governance templates
│   ├── feedback/                          # Feedback and assessment templates
│   └── executions/                        # Actual review executions by prompt
│       ├── prompt1/
│       ├── prompt2/
│       ├── prompt3/
│       ├── prompt4/
│       ├── prompt5/
│       ├── prompt6/
│       ├── prompt7/
│       ├── prompt8-9/
│       ├── prompt10-11/
│       ├── prompt12-13/
│       └── prompt14-15/
│
├── checker/                               # LLM Checker System
│   ├── prompts/                           # Checker prompts
│   ├── templates/                         # Checker templates
│   ├── analysis/                          # Analysis templates
│   ├── outputs/                           # Output templates
│   ├── config/                            # Configuration files
│   ├── CHECKER-HOW-TO.md                  # How-to guide
│   ├── CHECKER-FLOWCHART.md               # Process flowchart
│   └── PRESERVATION-GUIDE.md              # Preservation guide
│
├── templates/                             # Universal templates
│   ├── prompts/                           # Prompt templates
│   └── guides/                            # Guide templates
│
├── validation/                            # Validation tools
│   ├── prompt-update-validator.py
│   ├── prompt-update-validator.ps1
│   ├── PROMPT-UPDATE-VALIDATOR-GUIDE.md
│   └── permission-management.md
│
└── process/                               # Process documentation
    ├── EXECUTION-VERIFICATION-TABLE.md
    ├── IMPLEMENTATION-SUMMARY.md
    ├── audit-trail.md
    ├── change-history.md
    └── manual-fallback.md
```

## Quick Navigation

### For Analysis Documents
- **Prompt Analysis**: `analysis/prompts/`
- **Output Analysis**: `analysis/outputs/`
- **Template Mapping**: `analysis/templates/`

### For Review Activities
- **Review Templates**: `reviews/templates/[category]/`
- **Review Executions**: `reviews/executions/prompt[N]/`
- **Feedback Forms**: `reviews/feedback/`

### For Quality Assurance
- **Checker System**: `checker/`
- **Validation Tools**: `validation/`
- **Process Docs**: `process/`

## File Naming Conventions

### Analysis Files
- `prompt-[N]-analysis.md` - Analysis of specific prompt
- `prompt-[N]-[M]-[type]-analysis.md` - Analysis spanning multiple prompts

### Review Files
- `prompt[N]-review.md` - Review execution for specific prompt
- `[artifact-type]-review-template.md` - Template for reviewing specific artifact types
- `[artifact-type]-usage-guide.md` - Usage guide for artifact reviews

### Checker Files
- `checker-[type]-template.md` - Checker input/output templates
- `feedback-template-[stage].md` - Feedback templates by review stage
- `[artifact-type]-[purpose]-template.md` - Specialized templates

## Maintenance

This directory structure is maintained according to the [DIRECTORY-STRUCTURE-PROPOSAL.md](DIRECTORY-STRUCTURE-PROPOSAL.md). Any changes to the structure should be documented there and reflected in this README.
