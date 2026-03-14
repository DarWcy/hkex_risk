# BDD Relationship Manager

## Overview
This document manages the relationships between BDD scenarios, requirements, knowledge base rules, and Copilot Skills.

## Relationship Table

| BDD Feature ID | Test Case ID | Requirement ID | Skill ID | Rule Basis | Global Process Node | Review Status | Confidence Level | Status |
|---------------|-------------|---------------|----------|------------|---------------------|---------------|------------------|--------|
| FT-IM-CALC-001 | TC-IM-CALC-001 | REQ-001 | SKILL-001 | IO-INTRO-001 (v1.4) | VaR Platform Overview | Pending Review | Medium (3) | Active |
| FT-IM-CALC-002 | TC-IM-CALC-002 | REQ-001 | SKILL-001 | IO-INTRO-001 (v1.4) | VaR Platform Overview | Pending Review | Medium (3) | Active |
| FT-IM-CALC-003 | TC-IM-CALC-003 | REQ-001 | SKILL-001 | IO-INTRO-001 (v1.4) | VaR Platform Overview | Pending Review | Medium (3) | Active |
| FT-IM-CALC-004 | TC-IM-CALC-004 | REQ-001 | SKILL-001 | IO-INTRO-001 (v1.4) | VaR Platform Overview | Pending Review | Medium (3) | Active |
| FT-RISK-PARAM-001 | TC-RISK-PARAM-001 | REQ-002 | SKILL-001 | IO-INTRO-005 (v1.4) | Risk Parameter Dissemination Process | Pending Review | Medium (3) | Active |
| FT-RISK-PARAM-002 | TC-RISK-PARAM-002 | REQ-002 | SKILL-001 | IO-INTRO-005 (v1.4) | Risk Parameter Dissemination Process | Pending Review | Medium (3) | Active |
| FT-RISK-PARAM-003 | TC-RISK-PARAM-003 | REQ-003 | SKILL-001 | IO-INTRO-004 (v1.4) | Margin Calculation Framework Definition | Pending Review | Medium (3) | Active |
| FT-COMPLIANCE-001 | TC-COMPLIANCE-001 | REQ-004 | SKILL-001 | IO-INTRO-003 (v1.4) | Regulatory Compliance Assessment | Pending Review | Medium (3) | Active |
| FT-COMPLIANCE-002 | TC-COMPLIANCE-002 | REQ-004 | SKILL-001 | IO-INTRO-003 (v1.4) | Regulatory Compliance Assessment | Pending Review | Medium (3) | Active |
| FT-COMPLIANCE-003 | TC-COMPLIANCE-003 | REQ-004 | SKILL-001 | IO-INTRO-003 (v1.4) | Regulatory Compliance Assessment | Pending Review | Medium (3) | Active |

## Reference Bidirectional Consistency

| BDD Feature ID | Skill ID | Test_Reference Match | Rule_Source Match | Status |
|---------------|----------|---------------------|-------------------|--------|
| FT-IM-CALC-001 | hkex-intro-overview | Pending | Pending | Pending |
| FT-IM-CALC-002 | hkex-intro-overview | Pending | Pending | Pending |
| FT-IM-CALC-003 | hkex-intro-overview | Pending | Pending | Pending |
| FT-IM-CALC-004 | hkex-intro-overview | Pending | Pending | Pending |
| FT-RISK-PARAM-001 | hkex-intro-overview | Pending | Pending | Pending |
| FT-RISK-PARAM-002 | hkex-intro-overview | Pending | Pending | Pending |
| FT-RISK-PARAM-003 | hkex-intro-overview | Pending | Pending | Pending |
| FT-COMPLIANCE-001 | hkex-intro-overview | Pending | Pending | Pending |
| FT-COMPLIANCE-002 | hkex-intro-overview | Pending | Pending | Pending |
| FT-COMPLIANCE-003 | hkex-intro-overview | Pending | Pending | Pending |

## Update History

| Date | Action | BDD Feature IDs | Description | Author |
|------|--------|----------------|-------------|--------|
| 2026-03-14 | Created | All | Initial BDD scenarios generation | System Administrator |

## Change Tracking

| BDD Feature ID | Last Updated | Review Status | Confidence Level | Status | Change Type | Reason |
|---------------|-------------|---------------|------------------|--------|-------------|--------|
| FT-IM-CALC-001 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-IM-CALC-002 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-IM-CALC-003 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-IM-CALC-004 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-RISK-PARAM-001 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-RISK-PARAM-002 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-RISK-PARAM-003 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-COMPLIANCE-001 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-COMPLIANCE-002 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |
| FT-COMPLIANCE-003 | 2026-03-14 | Pending Review | Medium (3) | Active | Created | Initial generation |

## Rollback Plan

### Version Control
- All BDD scenarios are versioned in Git
- Each major change should be tagged
- Use git revert for rollback if needed

### Rollback Steps
1. Identify the version to rollback to
2. Use git revert or git checkout to restore previous version
3. Update relationship manager accordingly
4. Verify consistency with requirements and rules
5. Document rollback in change history

## Validation Checklist

- [x] All BDD scenarios follow Gherkin syntax
- [x] All BDD scenarios are rule-aligned
- [x] All BDD scenarios include global process nodes
- [x] All BDD scenarios reference rule paragraph IDs
- [x] All BDD scenarios include reference verification slots
- [x] All BDD scenarios include relationship slots
- [x] All BDD scenarios include update marking
- [x] All step definitions are created
- [x] Behave configuration is set up
- [x] Relationship manager is updated
- [x] Change history is documented
- [x] Template learning is complete
- [x] Difference analysis is generated
