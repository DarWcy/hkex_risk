# LLM Checker System - Validation Flowchart

## Overview

This flowchart illustrates the complete validation process of the LLM Checker System, from input preparation to final validation results.

## Validation Flow

```mermaid
graph TD
    A[Start Validation] --> B[Prepare Input Files]
    B --> C[Load Marker Output]
    C --> D[Load Original Rules]
    D --> E[Run Checker LLM]
    E --> F[Validate Structure]
    F --> G[Validate Content]
    G --> H[Validate References]
    H --> I[Calculate Confidence Level]
    I --> J{Passed?}
    J -->|Yes| K[Generate Validation Report]
    J -->|No| L[Generate Difference Analysis]
    L --> M[Provide Optimization Suggestions]
    M --> N[Generate Validation Report]
    K --> O[Initial Review Stage]
    N --> O
    O --> P{Initial Review Passed?}
    P -->|Yes| Q[Peer Review Stage]
    P -->|No| R[Request Re-review]
    R --> E
    Q --> S{Peer Review Passed?}
    S -->|Yes| T[Final Approval Stage]
    S -->|No| U[Escalate or Discuss]
    U --> V{Escalation Resolved?}
    V -->|Yes| T
    V -->|No| W[Document Escalation]
    T --> X{Final Approval?}
    X -->|Approved| Y[Update Marker Output]
    X -->|Rejected| Z[Document Rejection Reason]
    X -->|Conditional| AA[Implement with Conditions]
    Y --> AB[End Validation]
    Z --> AB
    AA --> AB
    W --> AB
```

## Detailed Process Steps

### 1. Input Preparation

- **Marker Output**: Load Prompt 6 (test cases) and Prompt 7 (BDD scenarios) outputs
- **Original Rules**: Load relevant MD files with structured paragraph IDs
- **Configuration**: Load checker configuration settings

### 2. Validation Process

- **Structural Validation**: Check format compliance, required fields, and syntax
- **Content Validation**: Verify rule alignment, parameter validity, and completeness
- **Reference Validation**: Validate rule source references, skill IDs, and test references
- **Confidence Calculation**: Compute confidence level based on validation results

### 3. Analysis and Reporting

- **Passed Outputs**: Generate validation report for successful outputs
- **Failed Outputs**: Generate difference analysis and optimization suggestions
- **Report Generation**: Create comprehensive validation reports

### 4. Review and Action

- **Initial Review**: QA Lead or Business Analyst reviews checker outputs
- **Peer Review**: Senior QA or Technical Lead validates findings
- **Final Approval**: Project Manager or System Owner authorizes implementation
- **Implementation**: Update marker outputs with approved changes
- **Documentation**: Record validation results and decisions

## Decision Points

### Confidence Level Assessment

```mermaid
graph TD
    A[Validation Results] --> B{Confidence Level}
    B -->|High (4-5)| C[Pass - No Changes Needed]
    B -->|Medium (2-3)| D[Pass with Minor Suggestions]
    B -->|Low (0-1)| E[Fail - Major Revisions Needed]
    C --> F[Generate Validation Report]
    D --> G[Generate Report with Suggestions]
    E --> H[Generate Detailed Analysis]
    F --> I[End]
    G --> I
    H --> I
```

### Optimization Decision Flow

```mermaid
graph TD
    A[Difference Analysis] --> B{Issue Severity}
    B -->|Critical| C[Reject Marker Output]
    B -->|Major| D[Suggest Major Revisions]
    B -->|Minor| E[Suggest Minor Adjustments]
    B -->|None| F[Accept Marker Output]
    C --> G[Document Rejection Reason]
    D --> H[Generate Revision Plan]
    E --> I[Generate Optimization Suggestions]
    F --> J[Mark as Passed]
    G --> K[End]
    H --> K
    I --> K
    J --> K
```

### Review Process Flow

```mermaid
graph TD
    A[Validation Report] --> B[Initial Review]
    B --> C{Initial Review Passed?}
    C -->|Yes| D[Peer Review]
    C -->|No| E[Request Re-review]
    E --> A
    D --> F{Peer Review Passed?}
    F -->|Yes| G[Final Approval]
    F -->|No| H[Escalate or Discuss]
    H --> I{Escalation Resolved?}
    I -->|Yes| G
    I -->|No| J[Document Escalation]
    G --> K{Final Approval?}
    K -->|Approved| L[Implement Changes]
    K -->|Rejected| M[Document Rejection]
    K -->|Conditional| N[Implement with Conditions]
    L --> O[End]
    M --> O
    N --> O
    J --> O
```

## Data Flow

```mermaid
graph LR
    A[Marker Output] --> B[Checker Input]
    C[Original Rules] --> B
    D[Configuration] --> B
    B --> E[Checker LLM]
    E --> F[Validation Results]
    F --> G[Difference Analysis]
    F --> H[Optimization Suggestions]
    G --> I[Validation Report]
    H --> I
    I --> J[Marker Output Update]
```

## Validation Criteria

### Structural Validation
- [ ] Test case format compliance
- [ ] BDD scenario Gherkin syntax
- [ ] Required fields presence
- [ ] Relationship mapping integrity

### Content Validation
- [ ] Rule alignment
- [ ] Parameter validity
- [ ] Traceability completeness
- [ ] Language consistency

### Reference Validation
- [ ] Rule source references
- [ ] Skill ID references
- [ ] Test reference consistency
- [ ] Cross-reference validity

## Output Files

- **Validation Report**: `governance/checker/outputs/{prompt}-checker-output.md`
- **Difference Analysis**: `governance/checker/analysis/{prompt}-diff-analysis.md`
- **Optimization Suggestions**: `governance/checker/analysis/{prompt}-optimization.md`

## Conclusion

The validation flowchart provides a visual representation of the complete checker process, from input preparation to final validation results. This structured approach ensures consistent and thorough validation of marker outputs, while preserving passed content and providing targeted optimization suggestions.