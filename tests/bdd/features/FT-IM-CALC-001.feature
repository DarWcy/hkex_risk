Feature: VaR Platform Portfolio Margin Calculation
  
  @im-calc @tier-p
  Scenario: Calculate portfolio margin for Tier P instruments
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Tier P instrument portfolio data is loaded
    When user loads Risk Parameter File
    And user inputs Tier P instrument portfolio
    And user calculates portfolio margin
    Then portfolio margin is calculated for Tier P instruments
    And calculation is based on IO-INTRO-001 (v1.4)
  
  Background:
    Given Global Process Node: VaR Platform Overview
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-001 / Skill ID: SKILL-001 / BDD Scenario ID: FT-IM-CALC-001
  
  # Update Marking
  # [RESERVED FOR UPDATES]
