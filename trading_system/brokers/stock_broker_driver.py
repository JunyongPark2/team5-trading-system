from abc import ABC, abstractmethod


class StockBrokerDriver(ABC):
    @abstractmethod
    def login(self, id, password) -> None:
        pass

    @abstractmethod
    def buy(self, stock_code, price, count) -> None:
        pass

    @abstractmethod
    def sell(self, stock_code, price, count) -> None:
        pass

    @abstractmethod
    def get_price(self, stock_code) -> int:
        pass
