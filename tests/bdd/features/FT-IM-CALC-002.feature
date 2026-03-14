Feature: VaR Platform Flat Rate Margin Calculation
  
  @im-calc @tier-n
  Scenario: Calculate flat rate margin for Tier N instruments
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Tier N instrument portfolio data is loaded
    When user loads Risk Parameter File
    And user inputs Tier N instrument portfolio
    And user calculates flat rate margin
    Then flat rate margin is calculated for Tier N instruments
    And calculation is based on IO-INTRO-001 (v1.4)
  
  Background:
    Given Global Process Node: VaR Platform Overview
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-001 / Skill ID: SKILL-001 / BDD Scenario ID: FT-IM-CALC-002
  
  # Update Marking
  # [RESERVED FOR UPDATES]
