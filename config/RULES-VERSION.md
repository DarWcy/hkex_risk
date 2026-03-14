# Rule Version Overview - Initial Margin Calculation Guide HKv14

## Current Version Information

| Attribute | Value |
|-----------|-------|
| **Document Name** | Initial Margin Calculation Guide HKv14 |
| **Source Document Version** | 1.4 |
| **Source Release Date** | October 2025 |
| **Source Publisher** | Hong Kong Securities Clearing Company Limited (HKSCC) |
| **Knowledge Base Version** | 1.0.0 |
| **Knowledge Base Status** | Active |
| **Last Updated** | 2025-03-13 |
| **Last Updated By** | AI Assistant |

---

## Module Version Matrix

| Module | File Name | Version | Last Updated | Status | Primary Owner |
|--------|-----------|---------|--------------|--------|---------------|
| Module 1 | Introduction-Overview.md | 1.0.0 | 2025-03-13 | Active | BA Lead |
| Module 2 | Risk-Parameter-File-Specification.md | 1.0.0 | 2025-03-13 | Active | QA Lead |
| Module 3 | Input-Data-Specification.md | 1.0.0 | 2025-03-13 | Active | Automation Lead |
| Module 4 | Market-Risk-Component-Calculation.md | 1.0.0 | 2025-03-13 | Active | BA Lead |
| Module 5 | Margin-Adjustment-Process.md | 1.0.0 | 2025-03-13 | Active | BA Lead |
| Module 6 | Other-Risk-Components.md | 1.0.0 | 2025-03-13 | Active | QA Lead |
| Module 7 | Position-Processing-Logic.md | 1.0.0 | 2025-03-13 | Active | Automation Lead |
| Module 8 | Collateral-Management.md | 1.0.0 | 2025-03-13 | Active | BA Lead |
| Module 9 | Corporate-Action-Processing.md | 1.0.0 | 2025-03-13 | Active | BA Lead |
| Module 10 | Calculation-Examples.md | 1.0.0 | 2025-03-13 | Active | QA Lead |

---

## Global Process Version

| Process Document | Version | Last Updated | Status |
|-----------------|---------|--------------|--------|
| GLOBAL-PROCESS.md | 1.0.0 | 2025-03-13 | Active |
| Core-Business-Global-Process-Flowchart.md | 1.0.0 | 2025-03-13 | Active |
| process-relationships.md | 1.0.0 | 2025-03-13 | Active |

---

## Source File Version

| Source File | Original Version | Converted Date | Archived |
|-------------|-----------------|----------------|----------|
| Initial-Margin-Calculation-Guide-HKv14.pdf | 1.4 | 2025-03-13 | No |
| Initial-Margin-Calculation-Guide-HKv14.md | 1.4 | 2025-03-13 | No |

---

## Version History

### Knowledge Base Version 1.0.0 (2025-03-13)

**Changes:**
- Initial knowledge base framework creation
- All 10 modules created from source document v1.4
- Global process documentation established
- Git repository structure initialized
- Copilot Skills framework defined
- Test asset structure created
- Governance layer templates generated

**Modules Added:**
- Introduction-Overview.md
- Risk-Parameter-File-Specification.md
- Input-Data-Specification.md
- Market-Risk-Component-Calculation.md
- Margin-Adjustment-Process.md
- Other-Risk-Components.md
- Position-Processing-Logic.md
- Collateral-Management.md
- Corporate-Action-Processing.md
- Calculation-Examples.md

**Configuration Added:**
- RULES-VERSION.md (this file)
- UPDATE-LOG.md template
- NAMING-CONVENTIONS.md
- skill-reference-spec.md
- skill-verify-config.md
- multi-model-verify-config.yaml

**Governance Templates Added:**
- All phase-specific audit templates
- Issue tracking mechanisms
- Permission management framework

---

## Version Update Rules

### Version Numbering Convention

**Format**: `MAJOR.MINOR.PATCH`

- **MAJOR**: Significant structural changes, new module additions, or major framework updates
- **MINOR**: Rule content updates, new features, or significant enhancements
- **PATCH**: Bug fixes, typo corrections, or minor formatting updates

### When to Update Versions

| Change Type | Version Impact | Example |
|-------------|---------------|---------|
| New module added | MAJOR++ | 1.0.0 → 2.0.0 |
| Source document version change | MINOR++ | 1.0.0 → 1.1.0 |
| Rule content update | MINOR++ | 1.0.0 → 1.1.0 |
| Skill structure change | MINOR++ | 1.0.0 → 1.1.0 |
| BDD scenario addition | PATCH++ | 1.0.0 → 1.0.1 |
| Typo/grammar fix | PATCH++ | 1.0.0 → 1.0.1 |
| Reference update | PATCH++ | 1.0.0 → 1.0.1 |

### Update Process

1. **Determine Version Impact**
   - Assess if change is MAJOR, MINOR, or PATCH
   - Review with Knowledge Base Owner

2. **Update This File**
   - Update "Knowledge Base Version"
   - Update "Last Updated" date
   - Update "Last Updated By"
   - Add entry to Version History

3. **Update Module Matrix**
   - Update affected module versions
   - Update "Last Updated" for affected modules

4. **Sync Related Files**
   - Update `config/UPDATE-LOG.md`
   - Update Git tag: `git tag -a v[X.X.X] -m "Version X.X.X"`
   - Update affected Skills' `Update_History`

5. **Verification**
   - Run version consistency check
   - Verify all references updated
   - Obtain approval from Primary Owner

---

## Version Consistency Checklist

Before marking a version as complete, verify:

- [ ] All module versions are consistent with KB version
- [ ] Source document version matches conversion
- [ ] Global process version aligns with modules
- [ ] Git tag created for new version
- [ ] UPDATE-LOG.md reflects all changes
- [ ] Skill references updated to new version
- [ ] BDD relationships reflect current version
- [ ] Governance templates versioned

---

## Git Tags

| Tag | Version | Date | Description |
|-----|---------|------|-------------|
| v1.0.0 | 1.0.0 | 2025-03-13 | Initial knowledge base release |

---

## Related Documents

- [UPDATE-LOG.md](./UPDATE-LOG.md) - Detailed change log
- [NAMING-CONVENTIONS.md](./NAMING-CONVENTIONS.md) - File naming standards
- [README.md](../README.md) - Repository overview
- [GIT-REPOSITORY-FRAMEWORK.md](../GIT-REPOSITORY-FRAMEWORK.md) - Framework structure

---

**Document Owner**: Knowledge Base Owner  
**Review Cycle**: Monthly  
**Next Review Date**: 2025-04-13
