# Prompt 8 and 9 Usage Guide

## Overview
This guide provides detailed instructions for using Prompt 8 (New Business Document Addition) and Prompt 9 (Existing Document Update) to maintain knowledge base synchronization and ensure consistency across all artifacts.

## Prompt 8: New Business Document Addition

### Purpose
Generate incremental update processes for adding new business documents to the knowledge base while maintaining synchronization with existing MD rules, Copilot Skills, test cases, BDD scenarios, and Reference/Script.

### When to Use
- New business documents need to be added to the knowledge base
- New rules need to be integrated with existing framework
- Global process nodes need to be matched
- Reference and Script synchronization is required

### Input Requirements
1. **New Document Content**: Paste the complete content of the new business document
2. **Existing Knowledge Base Structure**: Provide current structure including:
   - MD file list with structured IDs
   - Skill list with Skill IDs
   - Test case list with TC IDs
   - BDD scenario list with FT IDs

### Output Expectations
1. **Incremental Update Process**: Step-by-step process including:
   - Step name
   - Operation requirements
   - Reference/Script update standards
   - Verification standards

2. **Global Process Node Matching**: Requirements for matching new documents with existing process nodes

3. **Reference/Script Synchronization**: Requirements for updating Skills and Scripts

4. **Incremental Update Templates**: Ready-to-use templates for relationship and Reference/Script files

### Usage Steps
1. **Preparation**:
   - Gather new business document content
   - Collect existing knowledge base structure
   - Identify target global process nodes

2. **Execution**:
   - Run Prompt 8 with prepared inputs
   - Review generated incremental update process
   - Validate global process node matching
   - Verify Reference/Script synchronization requirements

3. **Review**:
   - Use `governance/reviews/prompt8-review.md` for review tracking
   - Apply `governance/reviews/incremental-update-review-template.md` for structured feedback
   - Calculate confidence levels using `governance/reviews/confidence-assessment.md`
   - Perform failure analysis if needed using `governance/reviews/failure-analysis-template.md`

4. **Implementation**:
   - Follow the generated incremental update process
   - Update MD files with new content
   - Update Skills with new References
   - Update Scripts for synchronization
   - Update relationship management files

5. **Verification**:
   - Verify all updates are correctly applied
   - Validate Reference integrity
   - Test Script functionality
   - Confirm no broken references

### User Type Templates
- **Type A (BA)**: Business-focused templates with business rule verification
- **Type B (QA Lead)**: Quality-focused templates with impact analysis
- **Type C (Automation Tester)**: Automation-focused templates with CI/CD integration
- **Type D (Mixed/General)**: Universal templates with balanced coverage

## Prompt 9: Existing Document Update

### Purpose
Generate synchronization update processes for updating existing business documents while maintaining consistency across all affected artifacts and providing rollback capabilities.

### When to Use
- Existing business documents need to be updated
- Rules are revised, optimized, or corrected
- Changes affect multiple related artifacts
- Rollback and version control are required

### Input Requirements
1. **Updated Document Content**: Paste the complete content of the updated business document
2. **Original Document Content**: Paste the original content for comparison
3. **Existing Knowledge Base Structure**: Provide current structure including:
   - MD file list with structured IDs
   - Skill list with Skill IDs
   - Test case list with TC IDs
   - BDD scenario list with FT IDs

### Output Expectations
1. **Synchronization Update Process**: Step-by-step process including:
   - Step name
   - Operation requirements
   - Modification specifications
   - Reference/Script update requirements

2. **Rule Update Impact Scope List**: Comprehensive list of affected artifacts including:
   - File path
   - Change type
   - Reference impact
   - Script impact
   - Global process node impact

3. **Update Marking Specifications**: Requirements for marking updates
4. **Rollback Plans**: Detailed rollback procedures
5. **Git Version Tagging**: Requirements for version control

### Usage Steps
1. **Preparation**:
   - Gather updated and original document content
   - Collect existing knowledge base structure
   - Identify all potentially affected artifacts
   - Prepare rollback strategy

2. **Execution**:
   - Run Prompt 9 with prepared inputs
   - Review generated synchronization update process
   - Analyze rule update impact scope
   - Validate Reference/Script update requirements
   - Review rollback plans and version tagging

3. **Review**:
   - Use `governance/reviews/prompt9-review.md` for review tracking
   - Apply `governance/reviews/incremental-update-review-template.md` for structured feedback
   - Calculate confidence levels using `governance/reviews/confidence-assessment.md`
   - Perform failure analysis if needed using `governance/reviews/failure-analysis-template.md`

4. **Implementation**:
   - Follow the generated synchronization update process
   - Update affected MD files
   - Update affected Skills
   - Update affected test cases
   - Update affected BDD scenarios
   - Update Scripts for synchronization
   - Apply Git version tags
   - Document rollback points

5. **Verification**:
   - Verify all updates are correctly applied
   - Validate Reference integrity across all affected artifacts
   - Test Script functionality
   - Confirm no broken references
   - Test rollback procedures

### User Type Templates
- **Type A (BA)**: Business-focused templates with business rule verification
- **Type B (QA Lead)**: Quality-focused templates with impact analysis
- **Type C (Automation Tester)**: Automation-focused templates with CI/CD integration
- **Type D (Mixed/General)**: Universal templates with balanced coverage

## Review and Feedback Process

### Review Workflow
1. **Initial Review**: First review of generated update process
2. **Peer Review**: Second review by another team member
3. **Final Approval**: Final approval and confidence level determination

### Review Templates
- **Incremental Update Review Template**: `governance/reviews/incremental-update-review-template.md`
- **Confidence Assessment Guide**: `governance/reviews/confidence-assessment.md`
- **Failure Analysis Template**: `governance/reviews/failure-analysis-template.md`

### Confidence Level Calculation
Based on:
- Update process quality (40%)
- Synchronization accuracy (30%)
- Completeness (20%)
- Impact assessment (10%)

### Failure Analysis
- Identify failure types
- Analyze root causes
- Provide recommended fixes
- Document lessons learned

## Integration with Other Prompts

### Upstream Dependencies
- Prompt 1: MD files generation
- Prompt 2: Framework structure
- Prompt 3: Skills generation
- Prompt 4: Supporting documents
- Prompt 5: Scripts generation
- Prompt 6: Test cases generation
- Prompt 7: BDD scenarios generation

### Downstream Impact
- Prompt 8 and 9 updates affect all previously generated artifacts
- Changes propagate through the entire knowledge base
- Requires comprehensive impact analysis

## Best Practices

### For Prompt 8
1. Always verify global process node matching
2. Ensure new rules don't conflict with existing rules
3. Test incremental update process before full implementation
4. Maintain complete audit trail

### For Prompt 9
1. Always analyze impact scope before implementation
2. Test rollback procedures in isolation
3. Apply Git version tags before making changes
4. Document all modifications thoroughly

### Common to Both
1. Use appropriate user type templates
2. Follow review workflow strictly
3. Calculate confidence levels objectively
4. Perform failure analysis when needed
5. Maintain complete revision history

## Troubleshooting

### Common Issues
1. **Global Process Node Mismatch**: Verify node definitions and mapping
2. **Reference Integrity Issues**: Check Reference field formats and validity
3. **Synchronization Failures**: Review update process steps and dependencies
4. **Rollback Failures**: Verify Git version tags and backup procedures

### Support Resources
- Review templates in `governance/reviews/`
- Confidence assessment guide in `governance/reviews/confidence-assessment.md`
- Failure analysis template in `governance/reviews/failure-analysis-template.md`
- Change tracking in `governance/change-history.md`

## Conclusion
Prompt 8 and 9 provide comprehensive capabilities for maintaining knowledge base synchronization. By following this guide and using the provided review templates, you can ensure high-quality updates with proper confidence levels and minimal risk.