import time


class AutoTradingSystem:
    TREND_CHECK_INTERVAL_SECOND = 0.2
    TREND_CHECK_COUNT = 3
    MAX_PRICE = 9999999999

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

    def get_nice_price(self, stock_code):
        prev_price = AutoTradingSystem.MAX_PRICE
        current_price = 0
        for _ in range(AutoTradingSystem.TREND_CHECK_COUNT):
            current_price = self.get_price(stock_code)
            if current_price >= prev_price:
                return 0
            prev_price = current_price
            time.sleep(AutoTradingSystem.TREND_CHECK_INTERVAL_SECOND)
        return current_price

    def sell_nice_timing(self, stock_code, count):
        if current_price := self.get_nice_price(stock_code):
            self.sell(stock_code, current_price, count)

    def buy_nice_timing(self, stock_code, seed_money):
        price = []
        for _ in range(3):
            price.append(self.get_price(stock_code))
            time.sleep(0.2)

        if price[0] < price[1] < price[2]:
            quantity = seed_money // price[2]
            if quantity > 0:
                self.buy(stock_code, price[2], quantity)
