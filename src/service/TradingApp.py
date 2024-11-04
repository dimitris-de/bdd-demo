class TradingPlatform:
    def __init__(self, balance=0.0):
        self.balance = balance
        self.portfolio = {}
        self.error_message = ''
        self.order_status = ''

    def set_account_balance(self, amount):
        self.balance = amount

    def buy_stock(self, symbol, quantity, price):
        total_cost = quantity * price
        if self.balance >= total_cost:
            self.balance -= total_cost
            self.portfolio[symbol] = self.portfolio.get(symbol, 0) + quantity
            self.order_status = 'success'
            return True
        else:
            self.order_status = 'failure'
            self.error_message = 'Insufficient funds'
            return False

    def sell_stock(self, symbol, quantity, price):
        if symbol in self.portfolio and self.portfolio[symbol] >= quantity:
            total_revenue = quantity * price
            print(f"total_revenue: {total_revenue}")
            self.balance += total_revenue
            print(f"balance: {self.balance}")
            self.portfolio[symbol] -= quantity
            if self.portfolio[symbol] == 0:
                del self.portfolio[symbol]
            self.order_status = 'success'
            return True
        else:
            self.order_status = 'failure'
            self.error_message = 'Insufficient shares to sell'
            return False


    def get_account_balance(self):
        return self.balance

    def get_error_message(self):
        return self.error_message

    def get_order_status(self):
        return self.order_status
