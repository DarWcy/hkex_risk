Feature: Risk Parameter File Daily Dissemination
  
  @risk-param @dissemination
  Scenario: Verify Risk Parameter File is disseminated to all CPs on a daily basis
    Given VaR Platform is operational
    And Risk Parameter File generation is configured
    And CP list is available
    When user triggers Risk Parameter File generation
    Then file is generated
    And dissemination to all CPs is verified
    And daily dissemination schedule is confirmed
    And process is based on IO-INTRO-005 (v1.4)
  
  Background:
    Given Global Process Node: Risk Parameter Dissemination Process
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-002 / Skill ID: SKILL-001 / BDD Scenario ID: FT-RISK-PARAM-001
  
  # Update Marking
  # [RESERVED FOR UPDATES]
