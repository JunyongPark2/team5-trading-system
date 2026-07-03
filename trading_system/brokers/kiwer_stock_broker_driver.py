from trading_system.brokers.stock_broker_driver import StockBrokerDriver
from trading_system.external.kiwer_api import KiwerAPI


class KiwerStockBrokerDriver(StockBrokerDriver):
    def __init__(self, kiwer_api: KiwerAPI) -> None:
        self._kiwer_api = kiwer_api

    def login(self, id, password) -> None:
        self._kiwer_api.login(id, password)

    def buy(self, stock_code, price, count) -> None:
        self._kiwer_api.buy(stock_code, count, price)

    def sell(self, stock_code, price, count) -> None:
        self._kiwer_api.sell(stock_code, count, price)

    def get_price(self, stock_code) -> int:
        return self._kiwer_api.current_price(stock_code)
