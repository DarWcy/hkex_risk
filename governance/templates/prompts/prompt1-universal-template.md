# Prompt 1 Universal Template - Rule to MD + Business Standardization Split

## Purpose
This universal template is designed to convert unstructured business rules (PDF/Word) from any document into standardized, modular MD documents that are optimized for BA, QA Lead, and Automation Tester readability and traceability.

## How to Use This Template

### Step 1: Document Configuration
Replace the placeholders in the template with your specific document information:
- `DOCUMENT_NAME`: Your document name (e.g., "Initial Margin Calculation Guide HKv14")
- `DOCUMENT_VERSION`: Your document version (e.g., "1.4")
- `DOCUMENT_DATE`: Your document date (e.g., "Oct 2025")
- `TARGET_ROLES`: Target roles (default: "BA, QA Lead, Automation Tester")
- `MODULE_COUNT`: Number of modules to create (default: "10")

### Step 2: Module Definition Strategy
Choose one of the following approaches:

**Option A: Use Default Module Framework**
- Use the pre-defined 10-module framework suitable for most business rule documents
- Modules cover: Introduction, Data Specification, Calculation Logic, Process Flow, Exception Handling, System Integration, Validation Rules, Testing Considerations, Examples, Reference Tables

**Option B: Define Custom Modules**
- Replace the default framework with your specific module definitions
- Follow the module definition template provided below
- Each module should target specific business logic and role concerns

### Step 3: Custom Requirements (Optional)
Add any document-specific requirements in the `CUSTOM_REQUIREMENTS` section:
- Special formatting requirements
- Industry-specific terminology
- Regulatory compliance notes
- System integration points

### Step 4: Execute the Prompt
Replace the input section with your actual business rule content and execute the prompt.

---

## Universal Prompt Template

```
### Instructions
Based on the following [DOCUMENT_NAME] business rule original text (use only this content), complete the conversion from non-MD files (such as PDF/Word) to standardized MD documents and modular splitting, meeting the following requirements:

1. **Non-MD to MD Conversion Process**: Convert unstructured business rules (PDF/Word) to plain text, maintaining the integrity of the original content, ensuring terminology, formulas, tables, and other information are accurate.

2. **Modular Splitting Strategy**: Split the content into **business-focused modules** designed for [TARGET_ROLES] readability and traceability, with no omission of rule points. Each module should target specific business logic and role concerns.

   **[CUSTOM_MODULE_DEFINITION_START]**
   **Module Definition Template** (Replace with your specific module definitions):
   
   **Module 1: [Module-Name].md**
   - Target Audience: [Target-Role] (BA/QA Lead/Automation Tester)
   - Content: [Brief description of module content]
   - Purpose: [Primary purpose of this module]
   
   **[Repeat for additional modules as needed]**
   **[CUSTOM_MODULE_DEFINITION_END]**

   **Default Module Framework** (Use if no custom modules are defined):
   - **Introduction-Overview.md**: Business background, overview, regulatory context (Target: BA)
   - **Risk-Parameter-File-Specification.md**: IMRPF file layout, field specifications, FieldType definitions (Target: QA Lead)
   - **Input-Data-Specification.md**: Position data requirements, contract values, market values, data sources (Target: Automation Tester)
   - **Market-Risk-Component-Calculation.md**: Portfolio margin, HVaR, SVaR, flat rate margin calculations (Target: BA + QA Lead)
   - **Margin-Adjustment-Process.md**: Margin adjustment process, rounding, favorable MTM, margin credit (Target: BA)
   - **Other-Risk-Components.md**: MTM requirement, position limit add-on, credit risk add-on, ad-hoc add-on (Target: QA Lead)
   - **Position-Processing-Logic.md**: Position adjustment logic, cross-day netting, cross-currency netting (Target: Automation Tester)
   - **Collateral-Management.md**: Data validation, business rule verification, compliance checks, validation logic (Target: QA Lead)
   - **Corporate-Action-Processing.md**: Complete examples, step-by-step calculations, sample data, calculation walkthroughs (Target: Automation Tester + QA Lead)
   - **Calculation-Examples.md**: Lookup tables, parameter definitions, configuration data, reference values (Target: QA Lead)

3. **File Naming and Templates**: Create independent MD files for each module; file names must be in **English**, following the **Module-SubTopic.md** naming convention. All MD files use a unified reusable template with the following structure:
   - Title: # [Topic] - [DOCUMENT_NAME] Version [DOCUMENT_VERSION]
   - Target Audience: Specify primary audience (BA/QA Lead/Automation Tester)
   - Rule Traceability: Document the corresponding original document clause/paragraph number/release version
   - Core Content: Present rule constraints in bullet points/tables with clear logic, organized by business relevance
   - Applicable Scenarios: Clearly define the business scenarios where the rule applies
   - Global Process Nodes: Mark the **core business global process nodes** that the current rule belongs to
   - Testing Considerations: Provide testing guidance for QA Lead and Automation Tester (test data requirements, boundary conditions, expected results)
   - Structured ID: Generate a unique ID for each rule paragraph (format: [Module Abbreviation]-[Paragraph Number]) for precise Skill Reference association

4. **Traceability**: Ensure each rule point can be traced back to the original paragraph, with no subjective information added or deleted.

5. **Language Requirement**: **ALL content must be written in English ONLY**. Chinese can only be used in remarks/notes if absolutely necessary. File names, headings, content, tables, and all text must be in English.

6. **Proofreading Requirements**: Proofread the generated MD files to ensure:
   - Correct grammar and spelling
   - Standardized format, compliant with Markdown syntax
   - Content consistent with the original text, no information loss or errors
   - Complete table structure with accurate data
   - Clear formula expression with correct symbols
   - **All content is in English**
   - **Role-specific clarity**: Content is clear and understandable for the target audience (BA/QA Lead/Automation Tester)
   - **Testing guidance completeness**: Testing considerations provide actionable guidance for test case design and validation
   - **Business logic accuracy**: Calculations and business rules are accurately represented and traceable

7. **Custom Requirements**: [CUSTOM_REQUIREMENTS]
   [Add any document-specific requirements here]

### Input Configuration (Replace with your specific values)
- **DOCUMENT_NAME**: [Your document name, e.g., Initial Margin Calculation Guide HKv14]
- **DOCUMENT_VERSION**: [Your document version, e.g., 1.4]
- **DOCUMENT_DATE**: [Your document date, e.g., Oct 2025]
- **TARGET_ROLES**: [Target roles, default: BA, QA Lead, Automation Tester]
- **MODULE_COUNT**: [Number of modules to create, default: 10]
- **CUSTOM_REQUIREMENTS**: [Any additional specific requirements for your document]

### Custom Module Definition (Optional - Replace default framework)
**[CUSTOM_MODULE_DEFINITION_START]**
[Define your specific modules here following the template above]
**[CUSTOM_MODULE_DEFINITION_END]**

### Input (Replace with actual business rule original text)
[Paste the plain text rule content converted from business PDF/Word]

### Output Requirements
- Output a complete list of **[MODULE_COUNT] MD files** (including file paths/full content/structured paragraph IDs), each targeting specific business logic and role concerns.
- Output the **Core Business Global Process Flowchart** (text version, including process nodes, flow relationships, and rule associations) with clear module mappings.
- **All content must be written in English** (Chinese can be used in remarks only when necessary), compliant with Markdown syntax standards.
- File names must be in English, following the Module-SubTopic.md format for the specified modules.
- Provide proofreading results to ensure all MD files have correct grammar, spelling, formatting, and are consistent with the original text, **and are entirely in English**.
- Ensure each module clearly indicates its target audience and provides role-specific content and testing guidance.
```

---

## Module Definition Best Practices

### 1. Module Granularity
- **Too Granular**: Creates too many small files, difficult to maintain
- **Too Broad**: Creates large files, hard to navigate and understand
- **Optimal**: Each module covers a cohesive business concept or calculation area

### 2. Role Targeting
- **BA Focus**: Business understanding, requirements, process flows, exception scenarios
- **QA Lead Focus**: Data validation, specifications, compliance, verification rules
- **Automation Tester Focus**: Test data, system integration, boundary conditions, examples

### 3. Content Organization
- **Logical Flow**: Organize modules in business logic sequence
- **Dependency Management**: Ensure modules reference each other appropriately
- **Cross-Reference**: Include links between related modules

### 4. Naming Conventions
- **Descriptive**: Module names should clearly indicate content
- **Consistent**: Use similar naming patterns across modules
- **English Only**: All module names must be in English

---

## Example Configurations

### Example 1: Financial Risk Calculation Document
```
DOCUMENT_NAME: "Initial Margin Calculation Guide HKv14"
DOCUMENT_VERSION: "1.4"
DOCUMENT_DATE: "Oct 2025"
TARGET_ROLES: "BA, QA Lead, Automation Tester"
MODULE_COUNT: "10"
CUSTOM_REQUIREMENTS: "Include detailed calculation examples with step-by-step breakdown"
```

### Example 2: Insurance Policy Document
```
DOCUMENT_NAME: "Insurance Policy Claims Processing Guide"
DOCUMENT_VERSION: "2.1"
DOCUMENT_DATE: "Jan 2026"
TARGET_ROLES: "BA, QA Lead, Automation Tester"
MODULE_COUNT: "8"
CUSTOM_REQUIREMENTS: "Focus on claim validation rules and exception handling"
```

### Example 3: Banking Operations Manual
```
DOCUMENT_NAME: "Banking Operations Standard Procedures"
DOCUMENT_VERSION: "3.0"
DOCUMENT_DATE: "Dec 2025"
TARGET_ROLES: "BA, QA Lead, Automation Tester"
MODULE_COUNT: "12"
CUSTOM_REQUIREMENTS: "Emphasize regulatory compliance and audit trail requirements"
```

---

## Troubleshooting

### Issue: Module Definition Not Clear
**Solution**: Review the original document structure and identify natural breakpoints (chapters, sections, logical groupings)

### Issue: Too Many Modules
**Solution**: Combine related modules that cover similar business logic or target the same audience

### Issue: Too Few Modules
**Solution**: Split large modules into smaller, more focused sub-modules

### Issue: Content Overlap Between Modules
**Solution**: Define clear boundaries and include cross-references where appropriate

---

## Integration with Other Prompts

This optimized Prompt 1 is designed to work seamlessly with:
- **Prompt 2**: Git Knowledge Base Framework Generation
- **Prompt 3**: Copilot Skill Modular Generation
- **Prompt 5**: Structured Test Case Generation

The modular structure and role-specific content ensure smooth integration with downstream prompts in the prompt set.