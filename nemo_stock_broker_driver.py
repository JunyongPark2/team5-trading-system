from stock_broker_driver import StockBrokerDriver


class NemoStockBrokerDriver(StockBrokerDriver):
    def __init__(self, api):
        pass

    def login(self, id, password) -> None:
        pass

    def buy(self, stock_code, price, count) -> None:
        pass

    def sell(self, stock_code, price, count) -> None:
        pass

    def get_price(self, stock_code) -> int:
        pass
