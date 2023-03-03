Feature: game
""" 
Confirm that we can browse the customer related pages on our site
"""

Scenario: success for visiting customer and customer details pages
    Given I navigate to the game pages
    When I click on the link to developer
    Then I should see the developer for that game

