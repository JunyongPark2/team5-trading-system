from trading_system.brokers.nemo_stock_broker_driver import NemoStockBrokerDriver
from trading_system.external.nemo_api import NemoAPI


def test_nemo_driver_login(capsys):
    api = NemoAPI()
    driver = NemoStockBrokerDriver(api)

    driver.login("test-user", "test-password")
    capture = capsys.readouterr()

    assert capture.out == "[NEMO]test-user login GOOD\n"


def test_nemo_driver_buy(capsys):
    api = NemoAPI()
    driver = NemoStockBrokerDriver(api)

    driver.buy("123", 1200, 3)
    capture = capsys.readouterr()

    assert capture.out == "[NEMO]123 buy stock ( price : 1200 ) * ( count : 3)\n"


def test_nemo_driver_sell(capsys):
    api = NemoAPI()
    driver = NemoStockBrokerDriver(api)

    driver.sell("456", 1100, 2)
    capture = capsys.readouterr()

    assert capture.out == "[NEMO]456 sell stock ( price : 1100 ) * ( count : 2)\n"


def test_nemo_driver_get_price_returns_market_price():
    api = NemoAPI()
    driver = NemoStockBrokerDriver(api)

    price = driver.get_price("789")

    assert 5000 <= price <= 5900
