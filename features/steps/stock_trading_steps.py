from behave import given, when, then # type: ignore
from src.service.TradingApp import TradingPlatform

@given('I have an account with balance £{balance}')
def step_given_account_balance(context, balance):
    if not hasattr(context, 'platform'):
        context.platform = TradingPlatform(float(balance))
    else:
        context.platform.set_account_balance(float(balance))

@given('I own {quantity} shares of "{symbol}" at an average price of £{avg_price}')
def step_given_own_shares(context, quantity, symbol, avg_price):
    if not hasattr(context, 'platform'):
        context.platform = TradingPlatform()
    context.platform.portfolio[symbol] = int(quantity)

@when('I buy {quantity} shares of "{symbol}" at £{price} per share')
def step_when_buy_shares(context, quantity, symbol, price):
    quantity = int(quantity)
    price = float(price)
    context.purchase_successful = context.platform.buy_stock(symbol, quantity, price)

@when('I sell {quantity} shares of "{symbol}" at £{price} per share')
def step_when_sell_shares(context, quantity, symbol, price):
    quantity = int(quantity)
    price = float(price)
    context.sale_successful = context.platform.sell_stock(symbol, quantity, price)

@then('the purchase should be successful')
def step_then_purchase_successful(context):
    assert context.purchase_successful, "Purchase was not successful"

@then('the purchase should fail due to insufficient funds')
def step_then_purchase_failed(context):
    assert not context.purchase_successful, "Purchase was successful but should have failed"

@then('my account balance should be £{expected_balance}')
def step_then_account_balance(context, expected_balance):
    expected_balance = float(expected_balance)
    actual_balance = context.platform.balance
    assert actual_balance == expected_balance, f"Expected balance £{expected_balance}, but got £{actual_balance}"

@then('my account balance should remain £{expected_balance}')
def step_then_account_balance_remain(context, expected_balance):
    expected_balance = float(expected_balance)
    actual_balance = context.platform.balance
    assert actual_balance == expected_balance, f"Expected balance to remain £{expected_balance}, but got £{actual_balance}"

@then('I should own {quantity} shares of "{symbol}"')
def step_then_own_shares(context, quantity, symbol):
    expected_quantity = int(quantity)
    actual_quantity = context.platform.portfolio.get(symbol, 0)
    assert actual_quantity == expected_quantity, f"Expected to own {expected_quantity} shares of {symbol}, but own {actual_quantity}"

@then('the sale should be successful')
def step_then_sale_successful(context):
    assert context.sale_successful, "Sale was not successful"

@then('the purchase should {result}')
def step_then_purchase_result(context, result):
    if result == "be successful":
        assert context.purchase_successful, "Purchase was not successful"
    elif result == "fail due to insufficient funds":
        assert not context.purchase_successful, "Purchase was successful but should have failed due to insufficient funds"
    else:
        assert False, f"Unknown result specified: {result}"
