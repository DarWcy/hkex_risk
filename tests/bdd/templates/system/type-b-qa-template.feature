Feature: [QA-Template] Quality Assurance Test
  Background:
    Given the test environment is configured
    And test data is prepared

  @smoke @critical
  Scenario: Validate critical functionality
    Given the system is in initial state
    When critical operation is performed
    Then the system should respond correctly
    And results should be logged

  @regression
  Scenario: Regression test for existing feature
    Given a feature exists in the system
    When the feature is tested
    Then it should behave as expected
    And no regressions should be detected
