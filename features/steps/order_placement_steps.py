import re
from behave import given, when, then
from src.service.TradingApp import TradingPlatform

@given('I am logged in')
def step_given_logged_in(context):
    context.platform = TradingPlatform()
    context.platform.is_logged_in = True

@given('I have sufficient funds in my account')
def step_given_sufficient_funds(context):
    context.platform.set_account_balance(5000)
    context.starting_balance = 5000

@given('I load my account with {balance}')
def step_given_account_balance(context, balance):
    match = re.search(r'[\d.]+', balance)
    amount = float(match.group())
    context.platform.set_account_balance(amount)
    context.starting_balance = amount

@when('I place a buy order for 10 shares of "AAPL" at £150 per share')
def step_when_place_buy_order(context):
    context.order_successful = context.platform.buy_stock('AAPL', 10, 150)

@then('the order should be placed successfully')
def step_then_order_successful(context):
    assert context.order_successful, "Order was not placed successfully"

@then('my account balance should decrease by £1500')
def step_then_account_balance_decreased(context):
    expected_balance = context.starting_balance - 1500  # Starting balance minus order cost
    actual_balance = context.platform.get_account_balance()
    assert actual_balance == expected_balance, f"Expected balance £{expected_balance}, but got £{actual_balance}"

@then('I should see an error message "Insufficient funds"')
def step_then_insufficient_funds_error(context):
    assert not context.order_successful, "Order was placed when it should have failed"
    assert context.platform.get_error_message() == 'Insufficient funds', "Incorrect error message displayed"

@then('"{outcome}"')
def step_then_outcome(context, outcome):
    if outcome == 'the order should be placed successfully':
        assert context.platform.get_order_status() == 'success', "Order was not placed successfully"
    elif outcome == 'I should see an error message "Insufficient funds"':
        assert context.platform.get_order_status() == 'failure', "Order was placed when it should have failed"
        assert context.platform.get_error_message() == 'Insufficient funds', "Incorrect error message displayed"
    else:
        assert False, f"Unknown outcome: {outcome}"