# Skill Verification Configuration

## Overview

This document defines the multi-model verification configuration for Copilot Skills, including input format specifications, verification dimensions, and result judgment standards.

**Version**: 1.4  
**Last Updated**: 2026-03-14  
**Applicable Skills**: All 10 Skills in the Initial Margin Calculation Guide HKv14

---

## Input Format Specifications

### Skill Input Format

**Required Fields**
```json
{
  "skill_id": "string (required)",
  "description": "string (required)",
  "trigger_words": ["array of strings (required)"],
  "user_type": "Type A/B/C/D (required)",
  "rule_version": "string (required)",
  "structured_reference": {
    "rule_source": "string (required)",
    "test_reference": "string (optional)",
    "verify_reference": "string (optional)",
    "update_history": "string (required)"
  },
  "bdd_association": "string (optional)",
  "script": {
    "automation_script": "string (optional)",
    "operation_guide": "string (optional)"
  }
}
```

**Field Validation Rules**

| Field | Type | Constraints | Validation Rule |
|-------|------|-------------|-----------------|
| skill_id | string | Format: `{business}-{module}-{capability}` | Must match naming convention |
| description | string | Length: 50-500 characters | Must be descriptive |
| trigger_words | array | Min: 3 items | Must cover core concepts |
| user_type | enum | Values: Type A, B, C, D | Must be valid type |
| rule_version | string | Format: `X.Y` | Must follow versioning |
| rule_source | string | Format: `path \| IDs \| version \| original` | Must be complete |

### BDD Input Format

**Feature File Format**
```gherkin
Feature: [Feature ID] - [Description]
  Background:
    Given [precondition]
  
  Scenario: [Scenario ID] - [Description]
    Given [step]
    When [action]
    Then [expected result]
    And [Rule_Source: MD file \| paragraph ID]
```

**Required Elements**
- Feature ID (format: FT-{module}-{sequence})
- Rule_Source reference in each scenario
- Skill ID mapping in tags
- Structured paragraph IDs

---

## Verification Dimensions

### Dimension 1: Content Accuracy Verification

**Objective**: Ensure Skill responses align with source documents

**Verification Points**
1. **Rule Alignment**
   - Check: Skill content matches source document rules
   - Method: Compare Skill response with Rule_Source
   - Standard: 100% alignment required

2. **Completeness Check**
   - Check: All relevant rules are covered
   - Method: Cross-reference with source document
   - Standard: No missing critical information

3. **Accuracy Validation**
   - Check: No incorrect or misleading information
   - Method: Expert review and automated validation
   - Standard: Zero tolerance for inaccuracies

**Verification Process**
```
1. Extract Rule_Source from Skill
2. Locate source document and paragraph
3. Compare Skill content with source
4. Document discrepancies
5. Calculate accuracy score
```

**Pass Criteria**
- Accuracy Score: 100%
- No critical discrepancies
- All rules covered

### Dimension 2: Reference Integrity Verification

**Objective**: Ensure all references are valid and resolvable

**Verification Points**
1. **Rule_Source Validity**
   - Check: MD file exists and is accessible
   - Check: Paragraph IDs exist in the file
   - Check: Version matches current document
   - Method: Automated file system checks

2. **Test_Reference Validity**
   - Check: Test case ID format is valid
   - Check: Feature file exists (when associated)
   - Method: File existence and format validation

3. **Cross-Reference Validity**
   - Check: All cross-references are resolvable
   - Check: No broken links
   - Method: Link resolution testing

**Verification Process**
```
1. Parse all reference fields
2. Verify file existence
3. Validate ID formats
4. Check version consistency
5. Generate integrity report
```

**Pass Criteria**
- All references valid: 100%
- No broken links
- Version consistency: 100%

### Dimension 3: Dependency Integrity Verification

**Objective**: Ensure dependency graph is valid and consistent

**Verification Points**
1. **Circular Dependency Check**
   - Check: No circular dependencies exist
   - Method: Graph cycle detection algorithm
   - Standard: Zero circular dependencies

2. **Dependency Resolution**
   - Check: All dependencies are resolvable
   - Check: Target Skills exist
   - Method: Dependency graph traversal

3. **Dependency Consistency**
   - Check: Dependency types are valid
   - Check: Strength ratings are consistent
   - Method: Rule-based validation

**Verification Process**
```
1. Load dependency graph
2. Run cycle detection
3. Verify all dependencies
4. Check type consistency
5. Generate dependency report
```

**Pass Criteria**
- Circular dependencies: 0
- All dependencies resolvable: 100%
- Type consistency: 100%

### Dimension 4: Script Execution Result Verification

**Objective**: Ensure automation scripts execute correctly

**Verification Points**
1. **Script Syntax**
   - Check: Python syntax is valid
   - Check: No import errors
   - Method: Static code analysis

2. **Script Execution**
   - Check: Script runs without errors
   - Check: Output is correct
   - Method: Automated test execution

3. **Error Handling**
   - Check: Exceptions are handled properly
   - Check: Error messages are clear
   - Method: Fault injection testing

**Verification Process**
```
1. Validate script syntax
2. Execute script in test environment
3. Verify output correctness
4. Test error handling
5. Generate execution report
```

**Pass Criteria**
- Syntax validation: 100%
- Execution success: 100%
- Error handling: Proper

---

## Result Judgment Standards

### Overall Verification Score

**Calculation Formula**
```
Overall Score = (Content Accuracy × 0.35) +
                (Reference Integrity × 0.25) +
                (Dependency Integrity × 0.20) +
                (Script Execution × 0.20)
```

**Score Interpretation**

| Score Range | Grade | Status | Action Required |
|-------------|-------|--------|-----------------|
| 95-100% | A | Pass | None |
| 85-94% | B | Pass with Minor Issues | Address minor issues |
| 75-84% | C | Conditional Pass | Address issues before deployment |
| 65-74% | D | Fail | Major remediation required |
| Below 65% | F | Critical Fail | Complete rework required |

### Dimension-Specific Standards

**Content Accuracy**
- A (95-100%): All content accurate, complete coverage
- B (85-94%): Minor inaccuracies, good coverage
- C (75-84%): Some inaccuracies, partial coverage
- D (65-74%): Major inaccuracies, incomplete coverage
- F (Below 65%): Critical inaccuracies, poor coverage

**Reference Integrity**
- A (95-100%): All references valid, no broken links
- B (85-94%): Minor reference issues
- C (75-84%): Some broken references
- D (65-74%): Major reference issues
- F (Below 65%): Critical reference failures

**Dependency Integrity**
- A (95-100%): No circular deps, all resolvable
- B (85-94%): Minor dependency issues
- C (75-84%): Some dependency issues
- D (65-74%): Major dependency issues
- F (Below 65%): Critical dependency failures

**Script Execution**
- A (95-100%): All scripts execute correctly
- B (85-94%): Minor execution issues
- C (75-84%): Some execution failures
- D (65-74%): Major execution issues
- F (Below 65%): Critical execution failures

---

## Verification Execution

### Pre-Verification Checklist

- [ ] All source documents are accessible
- [ ] All Skill files are available
- [ ] All configuration files are valid
- [ ] Verification environment is ready
- [ ] Test data is prepared

### Verification Steps

**Step 1: Content Accuracy Verification**
```bash
# Run content accuracy checks
python scripts/verify-content-accuracy.py --skills-dir copilot-skills/skill-definitions/

# Generate accuracy report
python scripts/generate-accuracy-report.py --output reports/content-accuracy.md
```

**Step 2: Reference Integrity Verification**
```bash
# Run reference integrity checks
python scripts/verify-reference-integrity.py --index tests/index.md

# Generate integrity report
python scripts/generate-integrity-report.py --output reports/reference-integrity.md
```

**Step 3: Dependency Integrity Verification**
```bash
# Run dependency checks
python scripts/verify-dependencies.py --relation tests/skill-bdd-relation.md

# Generate dependency report
python scripts/generate-dependency-report.py --output reports/dependency-integrity.md
```

**Step 4: Script Execution Verification**
```bash
# Run script tests
python scripts/test-script-execution.py --scripts-dir copilot-skills/scripts/

# Generate execution report
python scripts/generate-execution-report.py --output reports/script-execution.md
```

**Step 5: Overall Verification Report**
```bash
# Compile all reports
python scripts/compile-verification-report.py --output reports/verification-summary.md

# Calculate overall score
python scripts/calculate-verification-score.py --output reports/verification-score.json
```

### Post-Verification Actions

**If Pass (Grade A or B)**
1. Archive verification reports
2. Update verification status in Skill metadata
3. Proceed with deployment

**If Conditional Pass (Grade C)**
1. Document all issues
2. Create remediation plan
3. Fix issues and re-verify
4. Obtain approval for deployment

**If Fail (Grade D or F)**
1. Halt deployment
2. Conduct root cause analysis
3. Implement major fixes
4. Complete re-verification required

---

## Verification Automation

### Automated Verification Pipeline

```yaml
# verification-pipeline.yaml
pipeline:
  name: "Skill Verification Pipeline"
  
  stages:
    - name: "Pre-Verification"
      steps:
        - validate_environment
        - check_prerequisites
        - prepare_test_data
    
    - name: "Content Verification"
      steps:
        - verify_content_accuracy
        - check_completeness
        - validate_accuracy
    
    - name: "Reference Verification"
      steps:
        - verify_rule_source
        - verify_test_reference
        - verify_cross_references
    
    - name: "Dependency Verification"
      steps:
        - check_circular_dependencies
        - verify_dependency_resolution
        - validate_dependency_types
    
    - name: "Script Verification"
      steps:
        - validate_script_syntax
        - execute_scripts
        - test_error_handling
    
    - name: "Reporting"
      steps:
        - generate_dimension_reports
        - calculate_overall_score
        - compile_summary_report
    
    - name: "Decision"
      steps:
        - evaluate_results
        - determine_grade
        - recommend_action
```

### Continuous Verification

**Trigger Conditions**
1. Skill file modification
2. Source document update
3. Dependency relationship change
4. Scheduled verification (daily/weekly)

**Notification Settings**
- Pass: Log only
- Conditional Pass: Email notification
- Fail: Immediate alert + Email

---

## Verification Reports

### Report Structure

**Individual Dimension Reports**
- Executive summary
- Detailed findings
- Issue list with severity
- Recommendations

**Overall Verification Report**
- Overall score and grade
- Dimension scores
- Pass/fail status
- Action items

### Report Locations

- Individual reports: `tests/reports/`
- Summary report: `tests/reports/verification-summary.md`
- Score file: `tests/reports/verification-score.json`

---

## Change History

| Version | Date | Changes |
|---------|------|---------|
| 1.0 | 2026-03-14 | Initial creation |
| 1.4 | 2026-03-14 | Added comprehensive verification dimensions |

---

*This configuration is maintained by Prompt 4 execution. Update when verification requirements change.*
