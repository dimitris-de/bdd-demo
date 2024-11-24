@TradingApp
Feature: Stock Trading
  As a user of the trading platform
  I want to be able to buy and sell stocks
  So that I can manage my investments effectively

    Scenario: Buy a stock successfully
    Given I have an account with balance £10000
    When I buy 100 shares of "AAPL" at £15 per share
    Then the purchase should be successful
    And my account balance should be £8500
    And I should own 100 shares of "AAPL"

  Scenario: Insufficient funds to buy stock
    Given I have an account with balance £5000
    When I buy 100 shares of "GOOG" at £100 per share
    Then the purchase should fail due to insufficient funds
    And my account balance should remain £5000
    And I should own 0 shares of "GOOG"

  Scenario: Sell a stock successfully
    Given I own 50 shares of "MSFT" at an average price of £200
    And I have an account with balance £0
    When I sell 50 shares of "MSFT" at £250 per share
    Then the sale should be successful
    And my account balance should be £12500
    And I should own 0 shares of "MSFT"

  Scenario Outline: Buy stock with varying quantities and prices
    Given I have an account with balance £<balance>
    When I buy <quantity> shares of "<symbol>" at £<price> per share
    Then the purchase should <result>
    Examples:
      | balance | quantity | symbol | price | result                           |
      | 10000   | 50       | AAPL   | 100   | be successful                    |
      | 5000    | 100      | GOOG   | 100   | fail due to insufficient funds   |
