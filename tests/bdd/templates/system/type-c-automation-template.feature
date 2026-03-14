Feature: [Automation-Template] Automated Test Suite

  Background:
    Given the API endpoint is available
    And authentication is configured

  @automated @api @regression
  Scenario Outline: Automated API test
    Given the request payload is prepared
      | field  | value      |
      | param1 | <param1>   |
      | param2 | <param2>   |
    When a <method> request is sent to <endpoint>
    Then the response status should be <status>
    And the response should match expected schema

    Examples:
      | param1 | param2 | method | endpoint    | status |
      | value1 | value2 | POST   | /api/test   | 200    |

  @automated @integration
  Scenario: Integration test flow
    Given component A is running
    And component B is running
    When data flows from A to B
    Then the integration should succeed
    And data integrity should be maintained
