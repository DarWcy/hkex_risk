# Test Case Index

**Last Updated**: 2026-03-14
**Total Test Cases**: 3
**Coverage**: Initial Margin Calculation, Compliance

## Test Case Summary by Module

| Module | Count | Priority Distribution | Automation Status |
|--------|-------|----------------------|-------------------|
| IM-CALC | 2 | High: 2 | Ready: 2 |
| COMPLIANCE | 1 | Critical: 1 | Ready: 1 |

## Detailed Test Case List

### Initial Margin Calculation (IM-CALC)

| ID | Title | Type | Priority | Status | BDD Scenario | Rule Reference |
|----|-------|------|----------|--------|--------------|----------------|
| [TC-IM-CALC-001](TC-IM-CALC-001.md) | Calculate portfolio margin for Tier P instruments | Positive | High | Draft | FT-IM-CALC-001 | IO-INTRO-001 v1.4 |
| [TC-IM-CALC-002](TC-IM-CALC-002.md) | Calculate portfolio margin for Tier Q instruments | Positive | High | Draft | FT-IM-CALC-002 | IO-INTRO-002 v1.4 |

### Compliance (COMPLIANCE)

| ID | Title | Type | Priority | Status | BDD Scenario | Rule Reference |
|----|-------|------|----------|--------|--------------|----------------|
| [TC-COMPLIANCE-001](TC-COMPLIANCE-001.md) | Validate Risk Parameter File format and content | Positive + Negative | Critical | Draft | FT-COMPLIANCE-001 | COMP-001 v1.4 |

## Relationship Matrix

### Test Case to BDD Mapping

| Test Case ID | BDD Feature File | BDD Scenario ID | Coverage Status |
|--------------|------------------|-----------------|-----------------|
| TC-IM-CALC-001 | FT-IM-CALC-001.feature | FT-IM-CALC-001 | Covered |
| TC-IM-CALC-002 | FT-IM-CALC-002.feature | FT-IM-CALC-002 | Covered |
| TC-COMPLIANCE-001 | FT-COMPLIANCE-001.feature | FT-COMPLIANCE-001 | Covered |

### Test Case to Requirement Mapping

| Test Case ID | Requirement ID | Requirement Description | Verification Status |
|--------------|----------------|------------------------|---------------------|
| TC-IM-CALC-001 | REQ-001 | VaR Platform calculates Tier P margin | Pending |
| TC-IM-CALC-002 | REQ-002 | VaR Platform calculates Tier Q margin | Pending |
| TC-COMPLIANCE-001 | REQ-COMP-001 | Risk Parameter File validation | Pending |

### Test Case to Skill Mapping

| Test Case ID | Skill ID | Skill Name | Reference Status |
|--------------|----------|------------|------------------|
| TC-IM-CALC-001 | SKILL-001 | VaR Platform Overview | Linked |
| TC-IM-CALC-002 | SKILL-001 | VaR Platform Overview | Linked |
| TC-COMPLIANCE-001 | SKILL-COMP-001 | Risk Parameter Validation | Linked |

## Dependency Graph

```
TC-COMPLIANCE-001 (Risk Parameter Validation)
    ├── Blocks → TC-IM-CALC-001
    └── Blocks → TC-IM-CALC-002

TC-IM-CALC-001 (Tier P Calculation)
    └── Related To → TC-IM-CALC-002
```

## Execution Status Summary

| Status | Count | Percentage |
|--------|-------|------------|
| Draft | 3 | 100% |
| Under Review | 0 | 0% |
| Approved | 0 | 0% |
| Rejected | 0 | 0% |
| **Total** | **3** | **100%** |

## Priority Distribution

| Priority | Count | Percentage |
|----------|-------|------------|
| Critical | 1 | 33.3% |
| High | 2 | 66.7% |
| Medium | 0 | 0% |
| Low | 0 | 0% |

## Test Type Distribution

| Type | Count | Percentage |
|------|-------|------------|
| Positive | 2 | 66.7% |
| Negative | 0 | 0% |
| Positive + Negative | 1 | 33.3% |
| Exception | 0 | 0% |

## Automation Status

| Status | Count | Percentage |
|--------|-------|------------|
| Ready for Automation | 3 | 100% |
| Automated | 0 | 0% |
| Manual Only | 0 | 0% |
| Not Automatable | 0 | 0% |

## Review Status

| Test Case ID | Review ID | Confidence Level | Status |
|--------------|-----------|------------------|--------|
| TC-IM-CALC-001 | REV-TC-20260314-001 | 4/5 | Draft |
| TC-IM-CALC-002 | - | 4/5 | Draft |
| TC-COMPLIANCE-001 | - | 5/5 | Draft |

## Next Steps

1. **Review Test Cases**: Submit for QA review
2. **Add More Coverage**: Create test cases for remaining BDD scenarios
3. **Automation**: Begin automation script development
4. **Execution**: Execute test cases in DEV environment

## Change History

| Date | Change | Description | Updated By |
|------|--------|-------------|------------|
| 2026-03-14 | Created | Initial test case index created | System |
| 2026-03-14 | Added | TC-IM-CALC-001, TC-IM-CALC-002, TC-COMPLIANCE-001 | System |

## Related Documents

- [BDD Features](../bdd/features/)
- [Test Case Review Template](../../governance/reviews/templates/test/testcase-review-template.md)
- [Skill-BDD Relation](../skill-bdd-relation.md)
- [BDD Relation Manager](../bdd-relation-manager.md)
