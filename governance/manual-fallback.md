# Manual Fallback Mechanism

## Overview
This document defines the manual fallback procedures for the Initial Margin Calculation Guide HKv14 knowledge base system.

## Fallback Trigger Matrix

| Condition | Fallback Level | Action | Responsible Role |
|-----------|---------------|--------|------------------|
| AI Skill malfunction | View | Switch to manual document review | Business Analyst |
| Script execution failure | Edit | Manual data synchronization | Technical Developer |
| Rule version conflict | Audit | Manual version reconciliation | Configuration Manager |
| Critical calculation error | Decision | Emergency rollback procedure | Project Manager |

## Fallback Procedures

### Level 1: View Fallback
**Trigger:** AI Skill provides incorrect or incomplete information

**Procedure:**
1. Document the issue in the audit log
2. Switch to manual document review
3. Reference the original source documents in docs/source-files/
4. Escalate to technical team if needed

### Level 2: Edit Fallback
**Trigger:** Automated scripts fail to execute

**Procedure:**
1. Identify the failed script and error details
2. Execute manual data synchronization
3. Update the relationship tables manually
4. Document the workaround in the issue log

### Level 3: Audit Fallback
**Trigger:** Version conflicts or data inconsistencies

**Procedure:**
1. Suspend automated updates
2. Perform manual version reconciliation
3. Verify data integrity across all layers
4. Resume automated processes after verification

### Level 4: Decision Fallback
**Trigger:** Critical system failure or major rule changes

**Procedure:**
1. Activate emergency response team
2. Execute emergency rollback to last known good state
3. Notify all stakeholders
4. Conduct post-incident review

## Audit Trail Requirements

### Required Records
- All fallback activations with timestamp
- Responsible person identification
- Root cause analysis
- Resolution steps taken
- Verification of resolution

### Retention Period
- Critical incidents: 7 years
- Standard incidents: 3 years
- Minor issues: 1 year

## Escalation Path

1. **Level 1** → Business Analyst
2. **Level 2** → Technical Developer
3. **Level 3** → Configuration Manager
4. **Level 4** → Project Manager

## Contact Information

- Emergency Contact: [Name] - [Phone]
- Technical Support: [Email]
- Business Support: [Email]
