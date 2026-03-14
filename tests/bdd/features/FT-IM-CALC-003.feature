Feature: VaR Platform Corporate Action Position Margin Calculation
  
  @im-calc @corporate-action
  Scenario: Calculate corporate action position margin
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Corporate action position data is loaded
    When user loads Risk Parameter File
    And user inputs corporate action position data
    And user calculates corporate action position margin
    Then corporate action position margin is calculated
    And calculation is based on IO-INTRO-001 (v1.4)
  
  Background:
    Given Global Process Node: VaR Platform Overview
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-001 / Skill ID: SKILL-001 / BDD Scenario ID: FT-IM-CALC-003
  
  # Update Marking
  # [RESERVED FOR UPDATES]
