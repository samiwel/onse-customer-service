Feature: Update a customer
  As a recently married customer
  I want to change my surname
  In order to ensure my information is current

  Scenario: A customer changes their surname
    Given customer "Gene Kim" with ID "5" exists
    When I update customer with ID "5" with name "Gene Jones"
    And I fetch customer "5"
    Then I should see customer "Gene Jones"
