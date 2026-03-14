Feature: [BA-Template] Business Rule Verification
  As a business user
  I want to verify business rules
  So that I can ensure compliance

  @business @rule
  Scenario: Verify basic business rule
    Given the business rule is defined
    When the rule is applied
    Then the result should comply with the rule

  @business @validation
  Scenario: Validate business process
    Given a business process is initiated
    When the process completes
    Then the outcome should meet business requirements
