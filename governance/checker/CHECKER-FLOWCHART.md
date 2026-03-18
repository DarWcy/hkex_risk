# LLM Checker System - Validation Flowchart

**Version**: 2.0.0
**Last Updated**: 2026-03-18
**Author**: System Administrator

## Overview

This flowchart illustrates the complete validation process of the LLM Checker System, from input preparation to final validation results. This version includes enhanced monitoring, security features, and parameterized configuration capabilities.

## Enhanced System Architecture

The checker system now includes:
- **Real-time Monitoring**: Track execution metrics, performance, and errors
- **Security Layer**: Access control, input validation, and audit logging
- **Parameterized Configuration**: Flexible configuration management
- **Alerting System**: Threshold-based alerts for critical events

## Validation Flow

```mermaid
graph TD
    A[Start Validation] --> B[Security Check<br/>Access Control]
    B --> C[Input Validation<br/>Security Layer]
    C --> D[Prepare Input Files]
    D --> E[Load Configuration<br/>Parameterized Settings]
    E --> F[Start Monitoring<br/>Real-time Tracking]
    F --> G[Load Marker Output]
    G --> H[Load Original Rules]
    H --> I[Run Checker LLM]
    I --> J[Validate Structure]
    J --> K[Validate Content]
    K --> L[Validate References]
    L --> M[Calculate Confidence Level]
    M --> N[Monitor Performance<br/>Execution Time & Resources]
    N --> O{Passed?}
    O -->|Yes| P[Generate Validation Report]
    O -->|No| Q[Generate Difference Analysis]
    Q --> R[Provide Optimization Suggestions]
    R --> S[Generate Validation Report]
    P --> T[Initial Review Stage]
    S --> T
    T --> U{Initial Review Passed?}
    U -->|Yes| V[Peer Review Stage]
    U -->|No| W[Request Re-review]
    W --> I
    V --> X{Peer Review Passed?}
    X -->|Yes| Y[Final Approval Stage]
    X -->|No| Z[Escalate or Discuss]
    Z --> AA{Escalation Resolved?}
    AA -->|Yes| Y
    AA -->|No| AB[Document Escalation]
    Y --> AC{Final Approval?}
    AC -->|Approved| AD[Update Marker Output]
    AC -->|Rejected| AE[Document Rejection Reason]
    AC -->|Conditional| AF[Implement with Conditions]
    AD --> AG[End Validation]
    AE --> AG
    AF --> AG
    AB --> AG
    
    F -.->|Monitor| AH[Monitoring Dashboard]
    I -.->|Monitor| AH
    J -.->|Monitor| AH
    K -.->|Monitor| AH
    L -.->|Monitor| AH
    M -.->|Monitor| AH
    N -.->|Monitor| AH
    
    AH --> AI{Alert Thresholds?}
    AI -->|Performance Alert| AJ[Generate Alert]
    AI -->|Error Alert| AJ
    AI -->|Resource Alert| AJ
    AI -->|Normal| AK[Continue Monitoring]
    
    AJ --> AL[Notify Security Team]
    AL --> AK
    AK --> I
    
    style B fill:#ffe6e6
    style C fill:#ffe6e6
    style F fill:#fff4e6
    style AH fill:#fff4e6
    style AJ fill:#ffcccc
    style AL fill:#ffcccc
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