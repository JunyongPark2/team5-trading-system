from stock_broker_driver import StockBrokerDriver


class NemoStockBrokerDriver(StockBrokerDriver):
    def __init__(self, api):
        self._api = api

    def login(self, id, password) -> None:
        self._api.cerification(id, password)

    def buy(self, stock_code, price, count) -> None:
        self._api.purchasing_stock(stock_code, price, count)

    def sell(self, stock_code, price, count) -> None:
        self._api.selling_stock(stock_code, price, count)

    def get_price(self, stock_code) -> int:
        return self._api.get_market_price(stock_code, 0)
