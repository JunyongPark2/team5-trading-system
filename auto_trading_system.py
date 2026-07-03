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

    def buy_nice_timing(self, param, param1):
        price1 = self.get_price(param)
        price2 = self.get_price(param)
        price3 = self.get_price(param)
        if price1 < price2 and price2 < price3:
            self.buy(param, price3, param1 // price3)