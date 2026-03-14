Feature: [General-Template] Universal Test Template

  @general
  Scenario: General test scenario
    Given a test condition exists
    When an action is performed
    Then the expected result should occur

  @general @flexible
  Scenario Outline: Flexible test with parameters
    Given input parameter is <input>
    When processing is performed
    Then output should be <output>

    Examples:
      | input  | output  |
      | value1 | result1 |
      | value2 | result2 |
