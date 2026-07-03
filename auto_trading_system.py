class AutoTradingSystem:
    TREND_CHECK_INTERVAL_MS = 200
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

    def sell_nice_timing(self, stock_code, count):
        prev_price = self.MAX_PRICE
        current_price = 0
        for _ in range(self.TREND_CHECK_COUNT):
            current_price = self.get_price(stock_code)
            if current_price >= prev_price:
                return
            prev_price = current_price
        self.sell(stock_code, current_price, count)

