# Governance Directory Structure Optimization Proposal

## Current Issues

1. **Flat Structure**: Too many files in root `governance/` directory without clear categorization
2. **Mixed Content**: Analysis files, templates, process outputs, and guides all mixed together
3. **Unclear Reviews Organization**: 30+ files in `reviews/` without sub-categorization
4. **Analysis Files Location**: Root-level analysis files (PROMPT-3-4-5-LOGIC-ANALYSIS.md, etc.) not properly organized

## Proposed Directory Structure

```
governance/
├── README.md                              # Governance directory overview
│
├── analysis/                              # Analysis and research documents
│   ├── prompts/                           # Prompt logic and consistency analysis
│   │   ├── prompt-3-4-5-logic-analysis.md
│   │   ├── prompt-6-7-analysis.md
│   │   ├── prompt-consistency-analysis.md
│   │   └── prompt-dependency-matrix.md
│   ├── outputs/                           # Output analysis and reviews
│   │   ├── prompt1-output-analysis.md
│   │   ├── prompt6-output-analysis.md
│   │   └── prompt7-output-analysis.md
│   └── templates/                         # Template analysis and mapping
│       ├── template-prompt-mapping.md
│       └── prompt-template-creation-guide.md
│
├── reviews/                               # Review system
│   ├── templates/                         # Review templates by artifact type
│   │   ├── skills/
│   │   │   ├── skill-review-template.md
│   │   │   └── skill-validation-review-template.md
│   │   ├── test/
│   │   │   ├── testcase-review-template.md
│   │   │   ├── bdd-review-template.md
│   │   │   └── test-execution-review-template.md
│   │   ├── code/
│   │   │   └── script-review-template.md
│   │   ├── docs/
│   │   │   ├── documentation-review-template.md
│   │   │   ├── md-file-review-template.md
│   │   │   └── supporting-docs-review-template.md
│   │   ├── framework/
│   │   │   ├── framework-review-template.md
│   │   │   └── incremental-update-review-template.md
│   │   └── governance/
│   │       ├── audit-compliance-review-template.md
│   │       └── performance-review-template.md
│   ├── feedback/                          # Feedback and assessment templates
│   │   ├── feedback-template.md
│   │   ├── confidence-assessment.md
│   │   └── failure-analysis-template.md
│   └── executions/                        # Actual review executions by prompt
│       ├── prompt1/
│       │   ├── prompt1-review.md
│       │   └── prompt1-usage-guide.md
│       ├── prompt2/
│       │   └── prompt2-review.md
│       ├── prompt3/
│       │   └── prompt3-review.md
│       ├── prompt4/
│       │   └── prompt4-review.md
│       ├── prompt5/
│       │   ├── prompt5-review.md
│       │   ├── prompt5-input.md
│       │   └── prompt5-output.md
│       ├── prompt6/
│       │   ├── prompt6-review.md
│       │   ├── prompt6-input.md
│       │   └── prompt6-output.md
│       ├── prompt7/
│       │   ├── prompt7-review.md
│       │   ├── prompt7-input.md
│       │   └── prompt7-output.md
│       ├── prompt8-9/
│       │   ├── prompt8-review.md
│       │   ├── prompt9-review.md
│       │   └── prompt8-9-usage-guide.md
│       ├── prompt10-11/
│       │   ├── prompt10-review.md
│       │   ├── prompt11-review.md
│       │   └── prompt10-11-usage-guide.md
│       ├── prompt12-13/
│       │   ├── prompt12-review.md
│       │   ├── prompt13-review.md
│       │   └── prompt12-13-usage-guide.md
│       └── prompt14-15/
│           ├── prompt14-review.md
│           ├── prompt15-review.md
│           └── prompt14-15-usage-guide.md
│
├── checker/                               # LLM Checker System (already well-organized)
│   ├── README.md
│   ├── CHECKER-HOW-TO.md
│   ├── CHECKER-FLOWCHART.md
│   ├── PRESERVATION-GUIDE.md
│   ├── prompts/
│   ├── templates/
│   ├── analysis/
│   ├── outputs/
│   ├── config/
│   └── exit-reports/
│
├── templates/                             # Universal templates and guides
│   ├── prompts/
│   │   └── prompt1-universal-template.md
│   └── guides/
│       └── implementation-summary.md
│
├── validation/                            # Validation and verification
│   ├── prompt-update-validator-guide.md
│   ├── prompt-update-validator.py
│   ├── prompt-update-validator.ps1
│   └── execution-verification-table.md
│
├── process/                               # Process execution files
│   ├── change-history.md
│   ├── audit-trail.md
│   ├── manual-fallback.md
│   └── permission-management.md
│
└── archive/                               # Archived/deprecated files
    └── (for old versions and deprecated documents)
```

## File Migration Plan

### 1. Analysis Files (Root Level → governance/analysis/)

| Current Location | New Location | File Type |
|-----------------|--------------|-----------|
| `/PROMPT-3-4-5-LOGIC-ANALYSIS.md` | `governance/analysis/prompts/prompt-3-4-5-logic-analysis.md` | Prompt Logic Analysis |
| `/PROMPT-6-7-ANALYSIS.md` | `governance/analysis/prompts/prompt-6-7-analysis.md` | Prompt Logic Analysis |
| `/PROMPT-CONSISTENCY-ANALYSIS.md` | `governance/analysis/prompts/prompt-consistency-analysis.md` | Prompt Logic Analysis |
| `/PROMPT1-Universal-Template.md` | `governance/templates/prompts/prompt1-universal-template.md` | Universal Template |
| `/governance/TEMPLATE-PROMPT-MAPPING.md` | `governance/analysis/templates/template-prompt-mapping.md` | Template Analysis |
| `/governance/PROMPT-TEMPLATE-CREATION-GUIDE.md` | `governance/analysis/templates/prompt-template-creation-guide.md` | Template Analysis |

### 2. Review Templates (governance/reviews/ → governance/reviews/templates/)

| Current Location | New Location | Category |
|-----------------|--------------|----------|
| `skill-review-template.md` | `reviews/templates/skills/` | Skills |
| `skill-validation-review-template.md` | `reviews/templates/skills/` | Skills |
| `testcase-review-template.md` | `reviews/templates/test/` | Test |
| `bdd-review-template.md` | `reviews/templates/test/` | Test |
| `test-execution-review-template.md` | `reviews/templates/test/` | Test |
| `script-review-template.md` | `reviews/templates/code/` | Code |
| `documentation-review-template.md` | `reviews/templates/docs/` | Docs |
| `md-file-review-template.md` | `reviews/templates/docs/` | Docs |
| `supporting-docs-review-template.md` | `reviews/templates/docs/` | Docs |
| `framework-review-template.md` | `reviews/templates/framework/` | Framework |
| `incremental-update-review-template.md` | `reviews/templates/framework/` | Framework |
| `audit-compliance-review-template.md` | `reviews/templates/governance/` | Governance |
| `performance-review-template.md` | `reviews/templates/governance/` | Governance |
| `feedback-template.md` | `reviews/feedback/` | Feedback |
| `confidence-assessment.md` | `reviews/feedback/` | Feedback |
| `failure-analysis-template.md` | `reviews/feedback/` | Feedback |

### 3. Review Executions (governance/reviews/ → governance/reviews/executions/)

| Current Location | New Location | Prompt Group |
|-----------------|--------------|--------------|
| `prompt1-review.md` | `reviews/executions/prompt1/` | Prompt 1 |
| `prompt2-review.md` | `reviews/executions/prompt2/` | Prompt 2 |
| `prompt3-review.md` | `reviews/executions/prompt3/` | Prompt 3 |
| `prompt4-review.md` | `reviews/executions/prompt4/` | Prompt 4 |
| `prompt5-review.md` | `reviews/executions/prompt5/` | Prompt 5 |
| `prompt5-input.md` | `reviews/executions/prompt5/` | Prompt 5 |
| `prompt5-output.md` | `reviews/executions/prompt5/` | Prompt 5 |
| `prompt6-review.md` | `reviews/executions/prompt6/` | Prompt 6 |
| `prompt6-input.md` | `reviews/executions/prompt6/` | Prompt 6 |
| `prompt6-output.md` | `reviews/executions/prompt6/` | Prompt 6 |
| `prompt7-review.md` | `reviews/executions/prompt7/` | Prompt 7 |
| `prompt7-input.md` | `reviews/executions/prompt7/` | Prompt 7 |
| `prompt7-output.md` | `reviews/executions/prompt7/` | Prompt 7 |
| `prompt8-review.md` | `reviews/executions/prompt8-9/` | Prompt 8-9 |
| `prompt9-review.md` | `reviews/executions/prompt8-9/` | Prompt 8-9 |
| `prompt8-9-usage-guide.md` | `reviews/executions/prompt8-9/` | Prompt 8-9 |
| `prompt10-review.md` | `reviews/executions/prompt10-11/` | Prompt 10-11 |
| `prompt11-review.md` | `reviews/executions/prompt10-11/` | Prompt 10-11 |
| `prompt10-11-usage-guide.md` | `reviews/executions/prompt10-11/` | Prompt 10-11 |
| `prompt12-review.md` | `reviews/executions/prompt12-13/` | Prompt 12-13 |
| `prompt13-review.md` | `reviews/executions/prompt12-13/` | Prompt 12-13 |
| `prompt12-13-usage-guide.md` | `reviews/executions/prompt12-13/` | Prompt 12-13 |
| `prompt14-review.md` | `reviews/executions/prompt14-15/` | Prompt 14-15 |
| `prompt15-review.md` | `reviews/executions/prompt14-15/` | Prompt 14-15 |
| `prompt14-15-usage-guide.md` | `reviews/executions/prompt14-15/` | Prompt 14-15 |

### 4. Validation Files (governance/ → governance/validation/)

| Current Location | New Location | Purpose |
|-----------------|--------------|---------|
| `PROMPT-UPDATE-VALIDATOR-GUIDE.md` | `validation/prompt-update-validator-guide.md` | Validation Guide |
| `prompt-update-validator.py` | `validation/prompt-update-validator.py` | Validation Script |
| `prompt-update-validator.ps1` | `validation/prompt-update-validator.ps1` | Validation Script |
| `EXECUTION-VERIFICATION-TABLE.md` | `validation/execution-verification-table.md` | Verification Table |

### 5. Process Files (governance/ → governance/process/)

| Current Location | New Location | Purpose |
|-----------------|--------------|---------|
| `change-history.md` | `process/change-history.md` | Change Tracking |
| `audit-trail.md` | `process/audit-trail.md` | Audit Trail |
| `manual-fallback.md` | `process/manual-fallback.md` | Fallback Procedures |
| `permission-management.md` | `process/permission-management.md` | Permission Management |

### 6. Templates and Guides (governance/ → governance/templates/)

| Current Location | New Location | Purpose |
|-----------------|--------------|---------|
| `IMPLEMENTATION-SUMMARY.md` | `templates/guides/implementation-summary.md` | Implementation Guide |

## Benefits of New Structure

### 1. Clear Categorization
- **Analysis**: All analytical documents in one place
- **Reviews**: Templates separated from execution files
- **Checker**: Self-contained system (already good)
- **Validation**: All validation tools together
- **Process**: Operational documents organized

### 2. Scalability
- Easy to add new prompt analyses
- Easy to add new review templates
- Easy to add new validation tools
- Clear location for new file types

### 3. Maintainability
- Clear file locations reduce confusion
- Logical grouping makes files easier to find
- Consistent structure across directories
- Easy to identify orphaned files

### 4. Navigation
- README files at each level guide users
- Clear naming conventions
- Logical hierarchy
- Reduced cognitive load

## Implementation Steps

### Phase 1: Create New Directory Structure
1. Create all new directories
2. Ensure directory permissions are correct
3. Add README.md files to key directories

### Phase 2: Move Files
1. Move analysis files to `analysis/`
2. Move review templates to `reviews/templates/`
3. Move review executions to `reviews/executions/`
4. Move validation files to `validation/`
5. Move process files to `process/`
6. Move templates to `templates/`

### Phase 3: Update References
1. Update all internal links in moved files
2. Update `README.md` files
3. Update `chat-prompt-en.md` references
4. Update any scripts that reference old paths

### Phase 4: Validation
1. Verify all files are in correct locations
2. Verify all links work
3. Verify no broken references
4. Test validation scripts

### Phase 5: Cleanup
1. Remove empty old directories
2. Update `.gitignore` if needed
3. Document the changes
4. Commit all changes

## Prompt Updates Required

The following prompts need to be updated to reflect the new directory structure:

### Prompt 1 (MD Generation)
Update references to:
- `governance/reviews/md-file-review-template.md` → `governance/reviews/templates/docs/md-file-review-template.md`
- `governance/reviews/prompt1-review.md` → `governance/reviews/executions/prompt1/prompt1-review.md`

### Prompt 2 (Framework Creation)
Update references to:
- `governance/reviews/framework-review-template.md` → `governance/reviews/templates/framework/framework-review-template.md`

### Prompt 3 (Skill Generation)
Update references to:
- `governance/reviews/skill-review-template.md` → `governance/reviews/templates/skills/skill-review-template.md`

### Prompt 5 (Script Generation)
Update references to:
- `governance/reviews/script-review-template.md` → `governance/reviews/templates/code/script-review-template.md`
- `governance/PROMPT5-INPUT.md` → `governance/reviews/executions/prompt5/prompt5-input.md`
- `governance/PROMPT5-OUTPUT.md` → `governance/reviews/executions/prompt5/prompt5-output.md`

### Prompt 6 (Test Case Generation)
Update references to:
- `governance/reviews/testcase-review-template.md` → `governance/reviews/templates/test/testcase-review-template.md`
- `governance/reviews/feedback-template.md` → `governance/reviews/feedback/feedback-template.md`
- `governance/PROMPT6-INPUT.md` → `governance/reviews/executions/prompt6/prompt6-input.md`
- `governance/PROMPT6-OUTPUT.md` → `governance/reviews/executions/prompt6/prompt6-output.md`

### Prompt 7 (BDD Generation)
Update references to:
- `governance/reviews/bdd-review-template.md` → `governance/reviews/templates/test/bdd-review-template.md`
- `governance/PROMPT7-INPUT.md` → `governance/reviews/executions/prompt7/prompt7-input.md`
- `governance/PROMPT7-OUTPUT.md` → `governance/reviews/executions/prompt7/prompt7-output.md`

### Generic Checker Prompt Generator
Update references to:
- All template paths in `governance/checker/` remain unchanged (already well-organized)
- Update any references to review templates to use new paths

## Conclusion

This optimized directory structure provides:
- **Clear organization**: Files grouped by purpose and type
- **Better scalability**: Easy to add new files without clutter
- **Improved navigation**: Logical hierarchy with README guidance
- **Consistent patterns**: Similar structure across directories
- **Reduced confusion**: Clear separation of templates vs executions

The migration should be done in phases to ensure no files are lost and all references are updated correctly.
