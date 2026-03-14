# Skill-BDD Relationship Management

## Overview

This document manages the relationships between Copilot Skills, BDD test cases, and reference integrity for the Initial Margin Calculation Guide HKv14.

**Version**: 1.4  
**Last Updated**: 2026-03-14  
**Responsible**: System  
**Total Relationships**: 10 Skills

---

## Relationship Management Table

| Skill ID | Rule_Source | Test_Reference | BDD Test Case ID | BDD Feature File Path | Reference Integrity | Update Time | Updater |
|----------|-------------|----------------|------------------|----------------------|---------------------|-------------|---------|
| hkex-intro-overview | docs/Introduction-Overview.md \| INTRO-001 to INTRO-015 | To be associated | TC-INTRO-001 | tests/bdd/features/intro-overview.feature | ✓ Valid | 2026-03-14 | System |
| hkex-risk-parameters | docs/Risk-Parameter-File-Specification.md \| DATA-001 to DATA-028 | To be associated | TC-RISK-001 | tests/bdd/features/risk-parameters.feature | ✓ Valid | 2026-03-14 | System |
| hkex-input-data | docs/Input-Data-Specification.md \| CALC-001 to CALC-045 | To be associated | TC-INPUT-001 | tests/bdd/features/input-data.feature | ✓ Valid | 2026-03-14 | System |
| hkex-market-risk | docs/Market-Risk-Component-Calculation.md \| PROC-001 to PROC-022 | To be associated | TC-MARKET-001 | tests/bdd/features/market-risk.feature | ✓ Valid | 2026-03-14 | System |
| hkex-margin-adjustment | docs/Margin-Adjustment-Process.md \| ADJ-001 to ADJ-018 | To be associated | TC-ADJ-001 | tests/bdd/features/margin-adjustment.feature | ✓ Valid | 2026-03-14 | System |
| hkex-other-risk | docs/Other-Risk-Components.md \| OTHER-001 to OTHER-015 | To be associated | TC-OTHER-001 | tests/bdd/features/other-risk.feature | ✓ Valid | 2026-03-14 | System |
| hkex-position-processing | docs/Position-Processing-Logic.md \| POS-001 to POS-030 | To be associated | TC-POS-001 | tests/bdd/features/position-processing.feature | ✓ Valid | 2026-03-14 | System |
| hkex-collateral-management | docs/Collateral-Management.md \| COLL-001 to COLL-012 | To be associated | TC-COLL-001 | tests/bdd/features/collateral-management.feature | ✓ Valid | 2026-03-14 | System |
| hkex-corporate-action | docs/Corporate-Action-Processing.md \| CORP-001 to CORP-010 | To be associated | TC-CORP-001 | tests/bdd/features/corporate-action.feature | ✓ Valid | 2026-03-14 | System |
| hkex-calculation-examples | docs/Calculation-Examples.md \| EX-001 to EX-020 | To be associated | TC-EX-001 | tests/bdd/features/calculation-examples.feature | ✓ Valid | 2026-03-14 | System |

---

## Dependency Relationship Table

| Source Skill ID | Target Skill ID | Dependency Type | Strength | Update Time | Updater |
|-----------------|-----------------|-----------------|----------|-------------|---------|
| hkex-intro-overview | hkex-risk-parameters | Direct | Strong | 2026-03-14 | System |
| hkex-intro-overview | hkex-input-data | Direct | Strong | 2026-03-14 | System |
| hkex-intro-overview | hkex-market-risk | Indirect | Weak | 2026-03-14 | System |
| hkex-intro-overview | hkex-position-processing | Indirect | Weak | 2026-03-14 | System |
| hkex-intro-overview | hkex-corporate-action | Indirect | Weak | 2026-03-14 | System |
| hkex-risk-parameters | hkex-market-risk | Direct | Strong | 2026-03-14 | System |
| hkex-risk-parameters | hkex-other-risk | Direct | Medium | 2026-03-14 | System |
| hkex-risk-parameters | hkex-calculation-examples | Indirect | Weak | 2026-03-14 | System |
| hkex-input-data | hkex-market-risk | Direct | Strong | 2026-03-14 | System |
| hkex-input-data | hkex-position-processing | Direct | Strong | 2026-03-14 | System |
| hkex-input-data | hkex-collateral-management | Indirect | Weak | 2026-03-14 | System |
| hkex-market-risk | hkex-margin-adjustment | Direct | Strong | 2026-03-14 | System |
| hkex-market-risk | hkex-calculation-examples | Indirect | Medium | 2026-03-14 | System |
| hkex-other-risk | hkex-calculation-examples | Indirect | Weak | 2026-03-14 | System |
| hkex-position-processing | hkex-market-risk | Direct | Medium | 2026-03-14 | System |
| hkex-position-processing | hkex-collateral-management | Direct | Strong | 2026-03-14 | System |
| hkex-collateral-management | hkex-margin-adjustment | Direct | Medium | 2026-03-14 | System |
| hkex-corporate-action | hkex-position-processing | Direct | Strong | 2026-03-14 | System |

---

## Reference Integrity Verification

### Integrity Check Results

| Check Type | Status | Details |
|------------|--------|---------|
| Skill File Existence | ✓ Pass | All 10 Skill files exist |
| Rule Source Validity | ✓ Pass | All rule sources point to valid MD files |
| Structured ID Format | ✓ Pass | All IDs follow naming convention |
| BDD Association Slots | ✓ Pass | All slots reserved for future association |
| Cross-Reference Validity | ✓ Pass | All cross-references are resolvable |
| Dependency Graph | ✓ Pass | No circular dependencies detected |
| User Type Assignment | ✓ Pass | All Skills have valid user type |

### Integrity Metrics

- **Total Skills**: 10
- **Valid References**: 10/10 (100%)
- **Pending BDD Associations**: 10/10 (100% pending)
- **Dependency Relationships**: 18
- **Circular Dependencies**: 0
- **Orphaned Skills**: 0

---

## BDD Association Status

### Association Workflow

1. **Pending**: Skill created, BDD slots reserved
2. **In Progress**: BDD scenarios being developed
3. **Associated**: BDD scenarios linked to Skill
4. **Verified**: BDD-Skill relationship validated

### Current Status

| Status | Count | Percentage |
|--------|-------|------------|
| Pending | 10 | 100% |
| In Progress | 0 | 0% |
| Associated | 0 | 0% |
| Verified | 0 | 0% |

---

## Update Procedures

### Adding New BDD Association

1. Update "Test_Reference" field with BDD test case ID
2. Update "BDD Test Case ID" column
3. Update "BDD Feature File Path" column
4. Change "Reference Integrity" to "✓ Valid"
5. Update "Update Time" and "Updater" fields

### Modifying Existing Relationship

1. Locate the Skill ID in the table
2. Update relevant fields
3. Document changes in "Update History" section
4. Verify integrity after changes

### Removing Relationship

1. Locate the Skill ID in the table
2. Mark relationship as "Deprecated" in integrity column
3. Add deprecation note with timestamp
4. Do not delete - maintain audit trail

---

## Import/Export Functionality

### Export Formats

- **JSON**: `skill-bdd-relation-export-{timestamp}.json`
- **YAML**: `skill-bdd-relation-export-{timestamp}.yaml`
- **Markdown**: `skill-bdd-relation-export-{timestamp}.md`
- **CSV**: `skill-bdd-relation-export-{timestamp}.csv`

### Export Metadata

```json
{
  "export_version": "1.4",
  "export_timestamp": "2026-03-14T12:00:00Z",
  "responsible": "System",
  "total_skills": 10,
  "total_relationships": 18,
  "integrity_status": "Valid"
}
```

### Import Validation

When importing relationship data:
1. Validate JSON/YAML schema
2. Check Skill ID existence
3. Verify rule source validity
4. Validate BDD path format
5. Check for duplicate entries
6. Validate dependency graph (no circular dependencies)

---

## Change History

| Version | Date | Changes | Updater |
|---------|------|---------|---------|
| 1.0 | 2026-03-14 | Initial creation with 10 Skills | System |
| 1.4 | 2026-03-14 | Added dependency relationship table | System |

---

## Maintenance Notes

- This file is automatically updated by Prompt 4 execution
- Manual updates should follow the update procedures
- Always verify integrity after modifications
- Maintain audit trail for all changes
- Export regularly for backup purposes

---

*For dependency graph visualization, refer to index.md*
