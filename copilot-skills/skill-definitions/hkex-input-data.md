# Input Data Specification Skill

## Skill ID
hkex-input-data

## Description
This Skill provides information about Input Data Specification based on the Initial Margin Calculation Guide HKv14.

## Trigger Words
- "What is Input Data Specification?"
- "Explain Input Data Specification"
- "How does Input Data Specification work?"
- "Input Data Specification calculation"
- "Input Data Specification requirements"

## User Type Target
Type C

## Skill Source
Source 1

## Structured Reference
### Rule_Source
docs/Input-Data-Specification.md | CALC-001 to CALC-045 | 1.4 | docs/source-files/Initial Margin Calculation Guide HKv14.pdf

### Test_Reference
to be associated | to be associated

### Verify_Reference
to be defined | to be defined

### Update_History
2026-03-14 11:13:57 | System | N/A | N/A

## BDD Association Pre-embedding
to be associated | after association: TC-XXX-001, tests/xxx/xxx.feature

## Script
### Automation_Script (GitHub Copilot)
`python
# Skill: hkex-input-data
# Description: Input Data Specification
# User Type: Type C

def validate_skill():
    """Validate Skill content and references"""
    # TODO: Implement validation logic
    pass

def update_relationships():
    """Update BDD relationships"""
    # TODO: Implement relationship update logic
    pass
`

### Operation_Guide (M365 Copilot)
"""
To use this Skill:
1. Ask a question about Input Data Specification
2. The Skill will provide information based on the Initial Margin Calculation Guide HKv14
3. For more detailed information, refer to the associated MD file
"""

## Example Response
This is an example response for Input Data Specification based on the rule content.

## Update Marking Slots
[Update History Slot]
[Relationship Update Slot]
[Reference Update Slot]
