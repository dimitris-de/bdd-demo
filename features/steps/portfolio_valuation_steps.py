from behave import given, when, then

@given('I own the following stocks')
def step_given_own_stocks(context):
    context.portfolio = {}
    for row in context.table:
        symbol = row['symbol']
        quantity = int(row['quantity'])
        current_price = float(row['current_price'])

        context.portfolio[symbol] = {
            'quantity': quantity,
            'current_price': current_price
        }

@when('I view my portfolio value')
def step_when_view_portfolio_value(context):
    context.total_value = sum(
        stock['quantity'] * stock['current_price']
        for stock in context.portfolio.values()
    )

@then('the total portfolio value should be £{expected_value}')
def step_then_verify_portfolio_value(context, expected_value):
    expected_value = float(expected_value)
    assert context.total_value == expected_value, f"Expected portfolio value £{expected_value}, but got ${context.total_value}"
