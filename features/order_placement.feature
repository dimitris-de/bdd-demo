@TradingApp
Feature: Order Placement
  As a user of the trading platform
  I want to place buy orders
  So that I can invest in stocks

  Scenario: Place a buy order successfully
    Given I am logged in
    And I have sufficient funds in my account
    When I place a buy order for 10 shares of "AAPL" at £150 per share
    Then the order should be placed successfully
    And my account balance should decrease by £1500

  Scenario: Fail to place a buy order due to insufficient funds
    Given I am logged in
    And I load my account with £500
    When I place a buy order for 10 shares of "AAPL" at £150 per share
    Then I should see an error message "Insufficient funds"

  Scenario Outline: Order placement with varying account balances
    Given I am logged in
    And I load my account with "<balance>"
    When I place a buy order for 10 shares of "AAPL" at £150 per share
    Then "<outcome>"

    Examples:
      | balance | outcome                                            |
      | £2000   | the order should be placed successfully            |
      | £500    | I should see an error message "Insufficient funds" |
