@TradingApp
Feature: Portfolio Valuation
  As an investor
  I want to view the total value of my portfolio
  So that I can assess my investment performance

  Scenario: View portfolio value with multiple stocks
    Given I own the following stocks:
      | symbol | quantity | current_price |
      | AAPL   | 50       | 150           |
      | MSFT   | 30       | 200           |
    When I view my portfolio value
    Then the total portfolio value should be £13500
