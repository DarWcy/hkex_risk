### Instructions
Based on the following [Initial Margin Calculation Guide HKv14] MD files (use only this content), develop **modular, traceable, pre-embedded BDD relationship, automation Script-supporting** Skills for GitHub Copilot, meeting the following requirements:

#### Skill Input Sources

This prompt supports multiple input sources for Skill generation:

**Source 1: Structured MD Files (Primary)**
- Use structured MD files with paragraph IDs as primary input
- Format: MD files with structured paragraph IDs (e.g., DC-IMRPF-001, MRCC-HVaR-001)
- Location: `docs/source-files/` directory
- Processing: Extract rule scenarios from structured IDs and generate Skills

**Source 2: Natural Language Documents (Conversion Required)**
- Accept natural language documents from different user types
- Supported formats: `.md`, `.txt`, `.docx`, `.pdf` (text-extractable)
- User type alignment: Documents are converted based on target user type (A/B/C/D)
- Conversion process:
  1. Analyze document structure and content
  2. Extract rule scenarios and business logic
  3. Convert to standard Skill format with appropriate user type template
  4. Generate structured Reference fields based on document metadata
  5. Apply user type-specific optimizations (BA-Optimized/QA-Optimized/Automation-Optimized/Universal)
- Conversion output: Standard Skill files in `copilot-skills/skill-definitions/` directory

**Source 3: External Repository Skills (Import)**
- Import standard format Skills from external repositories (upstream/downstream systems)
- Supported external sources:
  - Upstream system repos: Core business rules, regulatory requirements
  - Downstream system repos: Implementation guides, test specifications
  - Shared/common repos: General-purpose Skills, utility functions
- Import requirements:
  - External Skills must follow standard Skill format (Skill ID, Description, Trigger Words, Structured Reference)
  - Must include valid Reference fields pointing to source documents
  - Must be compatible with project's user type classification system
- Import process:
  1. Validate external Skill format and completeness
  2. Map Reference fields to local document structure
  3. Assign appropriate user type target based on Skill content
  4. Update Update_History with import source and timestamp
  5. Store in `copilot-skills/skill-definitions/` with import metadata
- Benefits: Reduce maintenance cost by reusing existing Skills

**Source 4: Project-Specific Skills (Local Generation)**
- Generate Skills specific to this project's business requirements
- Based on project's structured MD knowledge base
- Customizable via user type classification and custom templates
- Primary method for project-specific business logic

**Skill Source Selection Logic:**
- If structured MD files are provided, use Source 1 (Primary)
- If natural language documents are provided, use Source 2 (Conversion)
- If external repo Skills are specified, use Source 3 (Import)
- If multiple sources are provided, process in priority order: Source 1 > Source 2 > Source 3
- Combine imported Skills with locally generated Skills as needed

#### User Type Classification System

Before generating Skills, identify the target user type to select appropriate template and customization level:

**User Type Categories:**

1. **Type A: Business Analyst (BA)**
   - **Characteristics**: Focuses on business understanding, requirement analysis, process flow comprehension
   - **Primary Needs**: Business rule explanations, process documentation, requirement clarification
   - **Skill Complexity**: Low to Medium (clear, business-focused explanations)
   - **Example Queries**: "What is the IM calculation process?", "How does margin adjustment work?"
   - **Template Preference**: BA-Optimized Template (simplified technical details, emphasized business logic)

2. **Type B: QA Lead**
   - **Characteristics**: Focuses on rule verification, compliance checking, test strategy design
   - **Primary Needs**: Rule specifications, validation requirements, compliance standards
   - **Skill Complexity**: Medium (balanced technical and business content)
   - **Example Queries**: "What are the validation rules for IMRPF?", "How to verify portfolio margin calculation?"
   - **Template Preference**: QA-Optimized Template (detailed validation steps, compliance references)

3. **Type C: Automation Tester**
   - **Characteristics**: Focuses on implementation details, test case design, boundary condition handling
   - **Primary Needs**: Technical specifications, test data requirements, calculation examples
   - **Skill Complexity**: High (detailed technical content, code examples)
   - **Example Queries**: "How to implement position processing logic?", "What are the boundary conditions for HVaR?"
   - **Template Preference**: Automation-Optimized Template (technical details, code snippets, test scenarios)

4. **Type D: Mixed/General User**
   - **Characteristics**: Needs comprehensive coverage across all aspects (business, QA, automation)
   - **Primary Needs**: Balanced content with multiple perspectives
   - **Skill Complexity**: Medium to High (comprehensive coverage)
   - **Example Queries**: "Explain the complete IM calculation workflow", "How to test and verify margin requirements?"
   - **Template Preference**: Universal Template (comprehensive, multi-perspective)

**User Type Selection Process:**
- **Default**: If user type is not specified, use **Type D: Mixed/General User** template
- **Explicit Selection**: If user type is specified in input, use corresponding optimized template
- **Hybrid Approach**: For complex scenarios, combine elements from multiple templates as needed

#### Custom Skill Template Entry

**[CUSTOM_SKILL_TEMPLATE_START]**
If you need to customize the Skill template structure, define your custom template below following this format:

**Custom Template Name**: [Your template name]
**Target User Type**: [Type A/B/C/D or custom type]
**Customization Level**: [Low/Medium/High]
**Structure Modifications**:
- [List any sections to add, modify, or remove from standard structure]
- [Specify any custom fields to add to Reference structure]
- [Define any additional Script requirements]

**Example Customization**:
```
Custom Template Name: High-Risk-Complexity Template
Target User Type: Type C (Automation Tester)
Customization Level: High
Structure Modifications:
- Add "Complexity Analysis" section before Description
- Add "Code Examples" section after Example Response
- Add "Performance Considerations" section before Script
- Add custom field "Debug_Reference" to Structured Reference
```
**[CUSTOM_SKILL_TEMPLATE_END]**

**Template Selection Logic:**
- If **[CUSTOM_SKILL_TEMPLATE_START]** to **[CUSTOM_SKILL_TEMPLATE_END]** is provided, use custom template
- If no custom template is provided, use standard template based on user type classification
- For custom templates, ensure all mandatory fields (Skill ID, Description, Trigger Words, Structured Reference) are included

#### Standard Skill Generation Process

1. Each Skill focuses on a single rule scenario; Skill ID follows the **business abbreviation-module-core capability** naming convention (e.g., hkex-im-calculation, hkex-risk-parameters) to facilitate subsequent relationship updates.

2. Each Skill contains a **fixed extensible structure + BDD association pre-embedding + structured Reference + Script pre-embedding**, with no missing information. The structure is as follows:
   - **Skill ID**: Unique identifier
   - **Description**: Core capability of the Skill (AI answer/rule verification/BDD scenario generation)
   - **Trigger Words**: Common user queries (precisely covering core rule questions)
   - **User Type Target**: [Type A/B/C/D] - Indicates which user type this Skill primarily serves
   - **Skill Source**: [Source 1/2/3/4] - Indicates the input source for this Skill
   - **Structured Reference (Required)**:
     + **Rule_Source**: {MD file full path} | {rule paragraph structured ID} | {rule version} | {original document storage path}
     + **Test_Reference**: {BDD test case ID to be associated} | {feature file path to be associated}
     + **Verify_Reference**: {multi-model verification configuration ID} | {manual audit record path (reserved)}
     + **Update_History**: {creation time} | {creator} | {associated Git Commit ID (reserved)} | {import source (if applicable)}
   - **BDD Association Pre-embedding**: Reserve BDD test case ID/feature file path association slots (format: to be associated | after association: TC-XXX-001, tests/xxx/xxx.feature), supporting real-time updates
   - **Script (Pre-embedded by scenario)**:
     + **Automation_Script (GitHub Copilot)**: Reserve lightweight Python script slots (synchronizing relationships/triggering verification/Git linkage), marking input/output specifications
     + **Operation_Guide (M365 Copilot)**: Reserve natural language operation guidance slots, adapted for non-technical personnel
   - **Example Response**: Rule-based precise answer (marking paragraph ID in Rule_Source)

3. Prohibit introducing rule information outside MD files; example responses must 100% align with rule constraints.

4. Skill content reserves **update marking slots** to facilitate subsequent rule modifications and relationship updates.

#### Skill Import/Export and Sharing Mechanism

**Skill Export (Project-Specific Skills Sharing)**
- **Export Format**: Standard Skill format with complete metadata
- **Export Content**:
  - Skill ID, Description, Trigger Words, User Type Target, Skill Source
  - Complete Structured Reference fields
  - BDD Association slots
  - Script pre-embedding slots
  - Example Responses
  - Export metadata: Export timestamp, export version, responsible person
- **Export Location**: `copilot-skills/exports/` directory
- **Export Naming**: `{business}-{module}-{capability}-export-{timestamp}.md`
- **Export Use Cases**:
  - Share project-specific Skills with downstream systems
  - Contribute Skills to shared/common repositories
  - Backup Skills before major updates
  - Archive deprecated Skills for reference

**Skill Import (External Skills Integration)**
- **Import Sources**:
  - Upstream system repositories: Import core business rule Skills
  - Downstream system repositories: Import implementation and test Skills
  - Shared/common repositories: Import utility and general-purpose Skills
  - External partner repositories: Import industry-standard Skills (with validation)
- **Import Validation**:
  - Format validation: Ensure Skill follows standard structure
  - Completeness check: Verify all mandatory fields are present
  - Reference integrity: Validate Reference fields point to valid sources
  - User type compatibility: Confirm Skill content aligns with user type classification
  - Duplicate detection: Check for duplicate Skill IDs or content
- **Import Process**:
  1. Validate imported Skill format and completeness
  2. Map external Reference fields to local document structure
  3. Assign appropriate User Type Target based on Skill content
  4. Update Update_History with import source, timestamp, and original repo
  5. Store in `copilot-skills/skill-definitions/` with import metadata
  6. Update Skill index table with import information
  7. Generate import log in `copilot-skills/imports/` directory
- **Import Metadata**:
  - Import source repository URL
  - Original Skill version
  - Import timestamp
  - Import validation results
  - Mapping of external to local Reference fields

**Skill Sharing and Collaboration**
- **Internal Sharing**:
  - Share Skills between teams within the organization
  - Maintain version control for shared Skills
  - Track usage and dependencies of shared Skills
- **External Sharing**:
  - Export Skills for sharing with external partners
  - Follow data governance and security policies
  - Anonymize sensitive information before sharing
  - Document sharing agreements and restrictions
- **Skill Versioning**:
  - Maintain version history for imported/exported Skills
  - Track changes between versions
  - Support rollback to previous versions if needed
  - Document breaking changes in version notes

**Skill Maintenance Cost Reduction**
- **Reuse Strategy**:
  - Prioritize importing Skills from external repos over creating new ones
  - Customize imported Skills for project-specific needs
  - Maintain mapping between original and customized Skills
- **Standardization**:
  - Follow standard Skill format across all repositories
  - Use consistent naming conventions
  - Maintain common Reference field structure
- **Documentation**:
  - Document import/export procedures
  - Maintain Skill dependency graph
  - Track Skill usage statistics

#### Integration Test Guidance (MANDATORY)
- **Integration Test Scenarios**:
  - Verify Prompt 1-2-3 integration: MD files → Framework → Skills
  - Verify multi-source input functionality: structured MD, natural language docs, external Skills
  - Verify user type classification: BA, QA Lead, Automation Tester, Mixed/General User
  - Verify Skill import/export functionality: external repo import, project-specific export
  - Verify structured ID referencing in Skills
  - Verify BDD relationship pre-embedding
  - Verify Script pre-embedding slots
- **Test Steps**:
  1. Execute Prompt 1 to generate MD modules with structured IDs
  2. Execute Prompt 2 to create framework structure
  3. Verify MD files are properly placed in docs/ directory
  4. Prepare test inputs for all sources:
     - Source 1: MD files with structured IDs
     - Source 2: Natural language documents (various formats)
     - Source 3: External repository Skills
     - Source 4: Project-specific Skills
  5. Execute Prompt 3 with each input source separately
  6. Execute Prompt 3 with mixed input sources
  7. Verify Skills are created in copilot-skills/skill-definitions/ directory
  8. Verify Skills correctly reference MD file structured IDs
  9. Verify user type classification in Skills
  10. Test Skill import from external repository
  11. Test Skill export for sharing
  12. Verify all process output files are created in correct locations
- **Expected Results**:
  - All Skills are generated with correct structure and content
  - Multi-source input works correctly for all source types
  - User type classification is properly applied
  - Import/export functionality works as expected
  - Skills correctly reference MD file structured IDs
  - BDD relationship and Script pre-embedding slots are properly created
  - No missing dependencies or broken references
  - All prompts execute successfully in sequence

**Skill Conflict Resolution**
- **Conflict Detection**:
  - Detect duplicate Skill IDs from different sources
  - Identify conflicting Reference field mappings
  - Flag incompatible user type classifications
  - Detect overlapping functionality between Skills
- **Resolution Strategies**:
  - **Duplicate Skill IDs**: Append source identifier or version number
  - **Reference conflicts**: Prioritize local references while maintaining external links
  - **User type conflicts**: Use hybrid template approach
  - **Functionality overlap**: Consolidate Skills or clarify scope boundaries
- **Conflict Documentation**:
  - Log all detected conflicts and resolution actions
  - Maintain audit trail of conflict resolution decisions
  - Document rationale for resolution strategies
  - Update Skill metadata to reflect conflict resolution

**Skill Quality Assurance**
- **Content Validation**:
  - Verify all Skill content aligns with rule constraints
  - Ensure no extraneous information is introduced
  - Validate all Reference fields point to valid sources
  - Check for consistency across related Skills
- **Structure Validation**:
  - Verify all mandatory fields are present
  - Ensure consistent formatting across Skills
  - Validate Script pre-embedding slots are properly formatted
  - Check BDD association slots are correctly structured
- **Performance Optimization**:
  - Optimize Skill content for prompt response time
  - Ensure Script pre-embedding slots are lightweight
  - Minimize redundant information across Skills
  - Optimize Reference field structure for quick access

### Input (Replace with actual MD files list)

**MD Files List from Prompt 1:**

1. **Introduction-Overview.md**
   - **File Path**: `docs/Introduction-Overview.md`
   - **Structured IDs**: INTRO-001 to INTRO-015
   - **Target Audience**: Business Analysts (BA)

2. **Risk-Parameter-File-Specification.md**
   - **File Path**: `docs/Risk-Parameter-File-Specification.md`
   - **Structured IDs**: DATA-001 to DATA-028
   - **Target Audience**: QA Lead

3. **Input-Data-Specification.md**
   - **File Path**: `docs/Input-Data-Specification.md`
   - **Structured IDs**: CALC-001 to CALC-045
   - **Target Audience**: Automation Tester

4. **Market-Risk-Component-Calculation.md**
   - **File Path**: `docs/Market-Risk-Component-Calculation.md`
   - **Structured IDs**: PROC-001 to PROC-022
   - **Target Audience**: BA + QA Lead

5. **Margin-Adjustment-Process.md**
   - **File Path**: `docs/Margin-Adjustment-Process.md`
   - **Structured IDs**: ADJ-001 to ADJ-018
   - **Target Audience**: BA

6. **Other-Risk-Components.md**
   - **File Path**: `docs/Other-Risk-Components.md`
   - **Structured IDs**: OTHER-001 to OTHER-015
   - **Target Audience**: QA Lead

7. **Position-Processing-Logic.md**
   - **File Path**: `docs/Position-Processing-Logic.md`
   - **Structured IDs**: POS-001 to POS-030
   - **Target Audience**: Automation Tester

8. **Collateral-Management.md**
   - **File Path**: `docs/Collateral-Management.md`
   - **Structured IDs**: COLL-001 to COLL-012
   - **Target Audience**: BA + QA Lead

9. **Corporate-Action-Processing.md**
   - **File Path**: `docs/Corporate-Action-Processing.md`
   - **Structured IDs**: CORP-001 to CORP-010
   - **Target Audience**: BA

10. **Calculation-Examples.md**
    - **File Path**: `docs/Calculation-Examples.md`
    - **Structured IDs**: EX-001 to EX-020
    - **Target Audience**: Automation Tester

**User Type Selection:**
- Default: Type D (Mixed/General User)
- For specific modules, use corresponding user type template

**Skill Source Selection:**
- Primary: Source 1 (Structured MD Files)
- No external Skills to import
- No natural language documents to convert

### Output Requirements
- **Language Requirements**: ALL generated content MUST be in English ONLY. Chinese or other languages are NOT allowed in any generated files, including Skill files, index tables, and documentation.
- **Process File Naming**: Generate a process output file named `PROMPT3-OUTPUT.md` containing execution logs and results.
- **Process File Storage**: Store `PROMPT3-OUTPUT.md` in `copilot-skills/` directory.
- **Skill File Generation**: Output complete Skill MD files to `copilot-skills/skill-definitions/` directory, following the naming convention: `{business}-{module}-{capability}.md`.
- **Skill Index Table**: Output Skill index table (including Skill ID/description/trigger words/structured Reference/BDD association pre-embedding slots/Script pre-embedding slots/user type target/skill source).
- **User Type Classification Output**: Include user type classification in each Skill file and index table, indicating which user type (A/B/C/D) each Skill primarily serves.
- **Skill Source Tracking**: Include Skill source (Source 1/2/3/4) in each Skill file and index table to track input origin.
- **Natural Language Document Conversion**: If Source 2 is used, document:
  - Original document path and format
  - Conversion process and transformations applied
  - Validation results and quality assessment
- **External Skill Import**: If Source 3 is used, document:
  - Imported Skill IDs and sources
  - Validation results and mapping details
  - Any conflicts detected and resolved
- **Proofreading Requirements**: Proofread all generated content to ensure correct grammar, spelling, formatting, and consistency.
- **README.md Synchronization**: If this update affects directory structure or file locations, update `README.md` accordingly.
- **Execution Instructions**: This prompt MUST include instructions to ACTUALLY CREATE Skill files and directories if they don't exist, not just output plans.

#### Verification Requirements (MANDATORY)
- **Pre-Execution Verification**: Before generating Skills, verify:
  - All required input files exist and are in correct locations (MD files, natural language docs, or external Skills)
  - Input data is complete and follows required format
  - For Source 1: MD files have structured paragraph IDs
  - For Source 2: Natural language documents are readable and parseable
  - For Source 3: External Skills follow standard format
  - User type classification is specified or default to Type D
  - Import/Export directories exist or can be created
- **Post-Execution Verification**: After generating Skills, verify:
  - All Skill files are created in `copilot-skills/skill-definitions/` directory
  - Skill file names follow naming convention `{business}-{module}-{capability}.md`
  - Each Skill contains all mandatory fields (Skill ID, Description, Trigger Words, Structured Reference, User Type Target, Skill Source)
  - User Type Target field is populated correctly
  - Skill Source field indicates correct input source
  - For Source 2: Conversion is documented and validated
  - For Source 3: Import metadata is complete and validation passed
  - Process output file `PROMPT3-OUTPUT.md` is created in `copilot-skills/` directory
  - All references and links in Structured Reference are valid
  - Import/Export directories are created with appropriate files
  - README.md is updated if required by README.md Synchronization Rule

#### Change Management Requirements (MANDATORY)
- **Impact Analysis**: Before generating Skills, document:
  - Which modules and rules will be covered by the Skills
  - How these Skills relate to existing Skills (if any)
  - Potential impact on downstream prompts (Prompt 4, 5, etc.)
  - For Source 3: Impact of imported Skills on existing Skills
  - For Source 2: Impact of document conversion on knowledge base
- **Change Documentation**: In process output file, document:
  - List of all Skills generated with their user type targets and skill sources
  - Template used for each Skill (standard or custom)
  - Any customizations applied to standard template
  - For Source 2: Conversion details and validation results
  - For Source 3: Import details, source repository, and validation results
  - Creation timestamp and responsible person
- **Rollback Procedures**: Include instructions for:
  - Removing generated Skills if needed
  - Restoring previous state if generation fails
  - Reverting imported Skills to previous versions
  - Reverting converted Skills to original documents
  - Reverting README.md changes if applicable
- **Import/Export Management**:
  - Maintain import logs for audit trail
  - Track exported Skills and their destinations
  - Document Skill dependencies across repositories
  - Establish approval process for external Skill imports

#### Prompt Dependencies (MANDATORY)
- **Input Sources**:
  - MD files generated by Prompt 1
  - Framework structure created by Prompt 2
  - No other dependencies
- **Output Usage**:
  - Skill files used by Prompt 4 for index and relationship management
  - Skill files used by Prompt 5 for script generation
  - Skill files used by subsequent prompts
- **Execution Order**:
  - Prompt 1 → Prompt 2 → Prompt 3 → Prompt 4 → Prompt 5
  - Must be executed after Prompt 2 and before Prompt 4
  - Provides Skills for the entire knowledge base

#### Integration Test Guidance (MANDATORY)
- **Integration Test Scenarios**:
  - Verify Prompt 1-2-3 integration: MD files → Framework → Skills
  - Verify multi-source input functionality: structured MD, natural language docs, external Skills
  - Verify user type classification: BA, QA Lead, Automation Tester, Mixed/General User
  - Verify Skill import/export functionality: external repo import, project-specific export
  - Verify structured ID referencing in Skills
  - Verify BDD relationship pre-embedding
  - Verify Script pre-embedding slots
- **Test Steps**:
  1. Execute Prompt 1 to generate MD modules with structured IDs
  2. Execute Prompt 2 to create framework structure
  3. Verify MD files are properly placed in docs/ directory
  4. Prepare test inputs for all sources:
     - Source 1: MD files with structured IDs
     - Source 2: Natural language documents (various formats)
     - Source 3: External repository Skills
     - Source 4: Project-specific Skills
  5. Execute Prompt 3 with each input source separately
  6. Execute Prompt 3 with mixed input sources
  7. Verify Skills are created in copilot-skills/skill-definitions/ directory
  8. Verify Skills correctly reference MD file structured IDs
  9. Verify user type classification in Skills
  10. Test Skill import from external repository
  11. Test Skill export for sharing
  12. Verify all process output files are created in correct locations
- **Expected Results**:
  - All Skills are generated with correct structure and content
  - Multi-source input works correctly for all source types
  - User type classification is properly applied
  - Import/export functionality works as expected
  - Skills correctly reference MD file structured IDs
  - BDD relationship and Script pre-embedding slots are properly created
  - No missing dependencies or broken references
  - All prompts execute successfully in sequence