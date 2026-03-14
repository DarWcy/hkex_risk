Feature: VaR Platform Other Margin Add-on Components
  
  @im-calc @add-on
  Scenario: Calculate other margin add-on components
    Given VaR Platform is operational
    And Risk Parameter File is available
    And Add-on component data is loaded
    When user loads Risk Parameter File
    And user inputs add-on component data
    And user calculates other margin add-on components
    Then other margin add-on components are calculated
    And calculation is based on IO-INTRO-001 (v1.4)
  
  Background:
    Given Global Process Node: VaR Platform Overview
  
  # Reference Verification Slot
  # Skill: hkex-intro-overview; Verify: Test_Reference matches
  
  # Relationships
  # Requirement ID: REQ-001 / Skill ID: SKILL-001 / BDD Scenario ID: FT-IM-CALC-004
  
  # Update Marking
  # [RESERVED FOR UPDATES]
