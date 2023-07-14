# Created by ross at 5/16/23
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open cure skin website
    When Input cure in the  search field
    And Click on search icon
    And click on product
    And add to card
 #   Then  Verify that 23 products are returned