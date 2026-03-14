Feature: Risk Parameter File Usage for Margin Calculation
  
  @risk-param @usage
  Scenario: Verify Risk Parameter File is used to calculate total MTM and margin requirement
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Portfolio data is loaded
    When user loads Risk Parameter File
    And user inputs portfolio data
    And user calculates total MTM
    And user calculates margin requirement
    Then calculations use Risk Parameter File
    And process is based on IO-INTRO-004 (v1.4)
  
  Background:
    Given Global Process Node: Margin Calculation Framework Definition
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-003 / Skill ID: SKILL-001 / BDD Scenario ID: FT-RISK-PARAM-003
  
  # Update Marking
  # [RESERVED FOR UPDATES]
