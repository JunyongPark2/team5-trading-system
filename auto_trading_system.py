import time

class AutoTradingSystem:
    def __init__(self):
        self._driver = None

    def select_stock_broker(self, driver):
        self._driver = driver

    def login(self, id, password):
        self._driver.login(id, password)

    def buy(self, stock_code, price, count):
        self._driver.buy(stock_code, price, count)

    def sell(self, stock_code, price, count):
        self._driver.sell(stock_code, price, count)

    def get_price(self, stock_code):
        return self._driver.get_price(stock_code)

    def buy_nice_timing(self, stock_code, seed_money):
        price = []
        for _ in range(3):
            price.append(self.get_price(stock_code))
            time.sleep(0.2)

        if price[0] < price[1] and price[1] < price[2]:
            quantity = seed_money // price[2]
            if quantity > 0:
                self.buy(stock_code, price[2], seed_money // price[2])