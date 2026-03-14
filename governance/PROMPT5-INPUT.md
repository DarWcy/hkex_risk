# Prompt 5 Input File
## Skill Automation Script Generation + Git/Verification Linkage

### Input Skill Files List

Based on the generated Copilot Skill files from Prompt 3 and supporting documents from Prompt 4:

**Source Skills (10 total)**:
1. hkex-intro-overview - Introduction Overview Skill (Type A)
2. hkex-risk-parameters - Risk Parameter File Specification (Type B)
3. hkex-input-data - Input Data Specification (Type C)
4. hkex-market-risk - Market Risk Component Calculation (Type A+B)
5. hkex-margin-adjustment - Margin Adjustment Process (Type A)
6. hkex-other-risk - Other Risk Components (Type B)
7. hkex-position-processing - Position Processing Logic (Type C)
8. hkex-collateral-management - Collateral Management (Type A+B)
9. hkex-corporate-action - Corporate Action Processing (Type A)
10. hkex-calculation-examples - Calculation Examples (Type C)

### Input Supporting Documents

**From Prompt 4**:
- tests/index.md - Skill index with dependency graph
- tests/skill-bdd-relation.md - Relationship management
- tests/usage-guidelines.md - Usage guidelines
- tests/config/skill-verify-config.md - Verification configuration
- tests/config/skill-reference-spec.md - Reference specifications

### Required Scripts

**6 Types of Automation Scripts**:

1. **Skill-Reference-Sync Script** (skill-reference-sync.py)
   - Purpose: Synchronize Skill and MD file Reference relationships
   - Target: Update skill-bdd-relation.md
   - Input: Skill files, MD files
   - Output: Updated relationship table

2. **BDD-Relationship-Update Script** (bdd-relationship-update.py)
   - Purpose: Trigger BDD scenario and Skill relationship updates
   - Target: Update tests/bdd-relation-manager.md
   - Input: BDD feature files, Skill files
   - Output: Updated BDD associations

3. **Multi-Model-Verification Script** (multi-model-verify.py)
   - Purpose: Perform multi-model Skill verification
   - Target: Generate verification reports
   - Input: Skill files, verification config
   - Output: Verification reports

4. **Skill-Consistency-Validation Script** (skill-consistency-validate.py)
   - Purpose: Verify Skill consistency across all prompts
   - Checks: Naming conventions, structure, references
   - Input: All Skill files
   - Output: Consistency report

5. **Dependency-Integrity-Validation Script** (dependency-integrity-validate.py)
   - Purpose: Verify Skill dependency relationships integrity
   - Checks: Circular dependencies, missing references
   - Input: Dependency graph, Skill files
   - Output: Dependency integrity report

6. **Execution-Result-Validation Script** (execution-result-validate.py)
   - Purpose: Validate script execution results
   - Checks: Error detection, recovery verification
   - Input: Script execution logs
   - Output: Execution validation report

### Script Requirements

**Technical Requirements**:
- Language: Python 3.8+
- Include comprehensive comments
- Configuration slots for customization
- Exception handling and error recovery
- Directly runnable without modifications

**Documentation Requirements**:
- Environment dependencies
- Configuration modification steps
- Execution steps
- Exception fallback solutions
- Validation script usage instructions

**M365 Integration**:
- Natural language operation guidance
- Step-by-step instructions
- No technical terminology
- Non-technical user friendly

### User Type Distribution

- **Type A (BA)**: 4 Skills - Business-focused validation
- **Type B (QA Lead)**: 2 Skills - Quality-focused validation
- **Type C (Automation Tester)**: 3 Skills - Automation-focused validation
- **Type A+B (Mixed)**: 2 Skills - Combined validation

### Execution Parameters

- **Language**: English ONLY
- **Incremental Update**: Enabled
- **Parallel Execution**: Enabled
- **Error Recovery**: Enabled
- **Performance Metrics**: Enabled

### Expected Outputs

1. **6 Python Scripts** in `copilot-skills/scripts/`:
   - skill-reference-sync.py
   - bdd-relationship-update.py
   - multi-model-verify.py
   - skill-consistency-validate.py
   - dependency-integrity-validate.py
   - execution-result-validate.py

2. **Script Usage Instructions** - Detailed documentation

3. **M365 Operation Guidance** - Natural language guides

4. **Execution Result Verification Table** - Editable table

5. **PROMPT5-OUTPUT.md** - Process output file in governance/

---
Generated: 2026-03-14
Responsible: System
