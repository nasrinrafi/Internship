# Created by ross at 5/16/23
Feature: Test Scenarios for Search functionality

  Scenario: User can search for a product
    Given Open Cure website
    Then  click on search icon
    When Input CureSkin gel in the  search field
    Then  Click on search product
    Then  Verify products are returned