# Skill Reference Maintenance Specifications

## Overview

This document defines the structured format of Reference fields, synchronous update rules, and verification methods to ensure full-link traceability consistency across all Copilot Skills.

**Version**: 1.4  
**Last Updated**: 2026-03-14  
**Applicable Skills**: All 10 Skills in the Initial Margin Calculation Guide HKv14

---

## Reference Field Structure

### Structured Reference Format

The `Structured Reference` field in each Skill contains four sub-fields:

```markdown
### Structured Reference
#### Rule_Source
{MD file full path} | {rule paragraph structured ID} | {rule version} | {original document storage path}

#### Test_Reference
{BDD test case ID} | {feature file path}

#### Verify_Reference
{multi-model verification configuration ID} | {manual audit record path}

#### Update_History
{creation time} | {creator} | {associated Git Commit ID} | {import source (if applicable)}
```

### Field Specifications

#### Rule_Source

**Format**: `{file_path} | {paragraph_ids} | {version} | {original_path}`

**Components**:
- **file_path**: Relative path to MD file (e.g., `docs/Introduction-Overview.md`)
- **paragraph_ids**: Range of structured IDs (e.g., `INTRO-001 to INTRO-015`)
- **version**: Document version (e.g., `1.4`)
- **original_path**: Path to original source document (e.g., `docs/source-files/Initial Margin Calculation Guide HKv14.pdf`)

**Example**:
```
docs/Introduction-Overview.md | INTRO-001 to INTRO-015 | 1.4 | docs/source-files/Initial Margin Calculation Guide HKv14.pdf
```

**Validation Rules**:
1. File must exist at specified path
2. Paragraph IDs must exist in the file
3. Version must match current document version
4. Original document must be accessible

#### Test_Reference

**Format**: `{test_case_id} | {feature_file_path}`

**Components**:
- **test_case_id**: BDD test case identifier (e.g., `TC-INTRO-001`)
- **feature_file_path**: Path to Gherkin feature file (e.g., `tests/bdd/features/intro-overview.feature`)

**States**:
- **To be associated**: `to be associated | to be associated` (default)
- **Associated**: `TC-XXX-001 | tests/bdd/features/xxx.feature`

**Example**:
```
TC-INTRO-001 | tests/bdd/features/intro-overview.feature
```

**Validation Rules**:
1. Test case ID must follow naming convention
2. Feature file must exist when associated
3. Test case must be valid BDD scenario

#### Verify_Reference

**Format**: `{config_id} | {audit_path}`

**Components**:
- **config_id**: Verification configuration identifier
- **audit_path**: Path to manual audit records

**States**:
- **To be defined**: `to be defined | to be defined` (default)
- **Defined**: `VERIFY-XXX-001 | governance/audit/xxx.md`

**Example**:
```
VERIFY-INTRO-001 | governance/audit/intro-overview-audit.md
```

**Validation Rules**:
1. Config ID must be unique
2. Audit path must be valid when defined
3. Must reference valid verification configuration

#### Update_History

**Format**: `{timestamp} | {updater} | {commit_id} | {import_source}`

**Components**:
- **timestamp**: ISO 8601 format (e.g., `2026-03-14 11:13:57`)
- **updater**: Person or system making the update
- **commit_id**: Associated Git commit hash (or `N/A`)
- **import_source**: Source of import if applicable (or `N/A`)

**Example**:
```
2026-03-14 11:13:57 | System | N/A | N/A
```

**Validation Rules**:
1. Timestamp must be valid datetime
2. Updater must be identifiable
3. Commit ID must be valid Git hash when applicable

---

## Synchronous Update Rules

### Update Triggers

**Trigger 1: Source Document Changes**

When source documents are updated:

1. **Detection**: Monitor source document changes
2. **Impact Analysis**: Identify affected Skills
3. **Update Rule_Source**: Update version and paragraph IDs if needed
4. **Update Update_History**: Append new entry
5. **Verification**: Validate all references still valid

**Update Sequence**:
```
Source Document Change
    ↓
Prompt 1: Regenerate MD files
    ↓
Prompt 3: Update affected Skills
    ↓
Update Rule_Source.version
    ↓
Update Update_History
    ↓
Verify reference integrity
```

**Trigger 2: BDD Association**

When BDD scenarios are associated:

1. **Association**: Link test case to Skill
2. **Update Test_Reference**: Add test case ID and feature file path
3. **Update Update_History**: Record association timestamp
4. **Verification**: Validate test case exists and is valid

**Update Sequence**:
```
BDD Scenario Created
    ↓
Assign Test Case ID
    ↓
Update Test_Reference
    ↓
Update Update_History
    ↓
Verify BDD association
```

**Trigger 3: Verification Configuration**

When verification is performed:

1. **Execution**: Run multi-model verification
2. **Update Verify_Reference**: Add config ID and audit path
3. **Update Update_History**: Record verification timestamp
4. **Verification**: Validate verification results

**Update Sequence**:
```
Verification Executed
    ↓
Generate Config ID
    ↓
Update Verify_Reference
    ↓
Update Update_History
    ↓
Verify verification completeness
```

### Update Rules

**Rule 1: Append-Only History**
- Update_History is append-only
- Never delete or modify existing entries
- Always add new entries for changes

**Rule 2: Version Consistency**
- Rule_Source.version must match source document version
- Update immediately when source changes
- Maintain version history in Update_History

**Rule 3: Reference Validity**
- All references must be valid at all times
- Broken references must be fixed immediately
- Use "to be associated/defined" for pending items

**Rule 4: Atomic Updates**
- Update all related fields together
- Maintain consistency across fields
- Rollback on validation failure

---

## Verification Methods

### Method 1: Automated Reference Validation

**Purpose**: Verify all references are valid and resolvable

**Process**:
```python
# Pseudo-code for reference validation
def validate_references(skill_file):
    # Parse Structured Reference
    ref = parse_structured_reference(skill_file)
    
    # Validate Rule_Source
    assert file_exists(ref.rule_source.file_path)
    assert paragraph_ids_exist(ref.rule_source.paragraph_ids)
    assert version_matches(ref.rule_source.version)
    
    # Validate Test_Reference (if associated)
    if ref.test_reference.is_associated:
        assert test_case_exists(ref.test_reference.test_case_id)
        assert feature_file_exists(ref.test_reference.feature_file_path)
    
    # Validate Verify_Reference (if defined)
    if ref.verify_reference.is_defined:
        assert config_exists(ref.verify_reference.config_id)
        assert audit_file_exists(ref.verify_reference.audit_path)
    
    # Validate Update_History
    assert valid_timestamp(ref.update_history.timestamp)
    assert valid_updater(ref.update_history.updater)
    
    return True
```

**Execution**:
```bash
# Run reference validation
python scripts/validate-references.py --skills-dir copilot-skills/skill-definitions/
```

### Method 2: Cross-Reference Resolution

**Purpose**: Verify cross-references between Skills and documents

**Process**:
1. Extract all Rule_Source references from Skills
2. Verify each MD file exists
3. Verify each paragraph ID exists in the file
4. Check for orphaned references
5. Generate cross-reference report

**Execution**:
```bash
# Run cross-reference check
python scripts/check-cross-references.py --index tests/index.md
```

### Method 3: Dependency Relationship Validation

**Purpose**: Verify dependency relationships are valid

**Process**:
1. Load dependency graph from skill-bdd-relation.md
2. Check for circular dependencies
3. Verify all dependencies are resolvable
4. Validate dependency types and strengths
5. Generate dependency report

**Execution**:
```bash
# Run dependency validation
python scripts/validate-dependencies.py --relation tests/skill-bdd-relation.md
```

### Method 4: Full-Link Traceability Check

**Purpose**: Verify complete traceability from source to output

**Check Points**:
1. Source document → MD file (Prompt 1)
2. MD file → Skill (Prompt 3)
3. Skill → BDD scenario (association)
4. Skill → Verification (multi-model)
5. All links are bidirectional

**Execution**:
```bash
# Run full traceability check
python scripts/check-traceability.py --full-pipeline
```

---

## Dependency Relationship Maintenance Specifications

### Dependency Types

**Type 1: Direct Dependency**
- Definition: Skill A directly depends on Skill B
- Strength: Strong, Medium, or Weak
- Example: hkex-market-risk depends on hkex-risk-parameters

**Type 2: Indirect Dependency**
- Definition: Skill A depends on Skill B through intermediate Skills
- Strength: Typically Weak
- Example: hkex-margin-adjustment indirectly depends on hkex-intro-overview

**Type 3: Contextual Dependency**
- Definition: Skills in the same business domain
- Strength: Weak
- Example: All risk-related Skills

### Dependency Maintenance Rules

**Rule 1: Dependency Documentation**
- All dependencies must be documented in skill-bdd-relation.md
- Include dependency type and strength
- Update timestamp and updater for all changes

**Rule 2: Dependency Validation**
- Validate dependencies during each Prompt 4 execution
- Check for circular dependencies
- Ensure all dependencies are resolvable

**Rule 3: Dependency Updates**
- Update dependencies when business logic changes
- Propagate updates to affected Skills
- Maintain audit trail of changes

**Rule 4: Dependency Graph Maintenance**
- Keep dependency graph visualization current
- Update mermaid diagram in index.md
- Reflect all dependency changes

### Dependency Update Process

**Adding New Dependency**:
1. Identify source and target Skills
2. Determine dependency type and strength
3. Add entry to dependency relationship table
4. Update dependency graph visualization
5. Validate no circular dependencies created

**Modifying Dependency**:
1. Locate existing dependency in table
2. Update type, strength, or other attributes
3. Update timestamp and updater
4. Re-validate dependency graph
5. Document reason for change

**Removing Dependency**:
1. Locate dependency in table
2. Mark as "Deprecated" (do not delete)
3. Add deprecation note with reason
4. Update timestamp
5. Verify no Skills are orphaned

---

## Import/Export Specifications

### Export Format

**JSON Export**:
```json
{
  "export_metadata": {
    "version": "1.4",
    "timestamp": "2026-03-14T12:00:00Z",
    "responsible": "System"
  },
  "references": [
    {
      "skill_id": "hkex-intro-overview",
      "rule_source": {
        "file_path": "docs/Introduction-Overview.md",
        "paragraph_ids": "INTRO-001 to INTRO-015",
        "version": "1.4",
        "original_path": "docs/source-files/Initial Margin Calculation Guide HKv14.pdf"
      },
      "test_reference": {
        "test_case_id": "to be associated",
        "feature_file_path": "to be associated"
      },
      "verify_reference": {
        "config_id": "to be defined",
        "audit_path": "to be defined"
      },
      "update_history": [
        {
          "timestamp": "2026-03-14 11:13:57",
          "updater": "System",
          "commit_id": "N/A",
          "import_source": "N/A"
        }
      ]
    }
  ]
}
```

### Import Validation

**Validation Steps**:
1. Validate JSON schema
2. Check skill_id existence
3. Validate file paths
4. Verify paragraph ID formats
5. Check version formats
6. Validate timestamp formats
7. Check for duplicate entries

**Import Process**:
```bash
# Import references
python scripts/import-references.py --input references-import.json --validate

# Merge with existing
python scripts/merge-references.py --existing tests/skill-bdd-relation.md --imported references-import.json
```

---

## Change History

| Version | Date | Changes | Updater |
|---------|------|---------|---------|
| 1.0 | 2026-03-14 | Initial creation | System |
| 1.4 | 2026-03-14 | Added comprehensive reference specifications | System |

---

## Best Practices

### Reference Maintenance

1. **Regular Validation**: Run reference validation weekly
2. **Immediate Updates**: Update references immediately when source changes
3. **Audit Trail**: Maintain complete audit trail in Update_History
4. **Backup**: Export references regularly for backup
5. **Documentation**: Document all reference changes

### Dependency Management

1. **Minimal Dependencies**: Keep dependencies minimal and necessary
2. **Clear Documentation**: Document rationale for each dependency
3. **Regular Review**: Review dependency graph monthly
4. **Impact Analysis**: Analyze impact before adding dependencies
5. **Version Control**: Track all dependency changes

### Quality Assurance

1. **Automated Checks**: Use automated validation scripts
2. **Manual Review**: Periodically review references manually
3. **Integration Tests**: Include reference checks in integration tests
4. **Performance Monitoring**: Monitor reference validation performance
5. **Error Tracking**: Track and resolve reference errors promptly

---

*This specification is maintained by Prompt 4 execution. Update when reference structure or rules change.*
