from pytest_mock import MockerFixture

from nemo_api import NemoAPI
from nemo_stock_broker_driver import NemoStockBrokerDriver
from stock_broker_driver import StockBrokerDriver


def create_driver(api):
    return NemoStockBrokerDriver(api)


def test_nemo_driver_implements_stock_broker_driver(mocker: MockerFixture):
    api = mocker.Mock(spec=NemoAPI)

    driver = create_driver(api)

    assert isinstance(driver, StockBrokerDriver)


def test_nemo_driver_login_delegates_to_nemo_api(mocker: MockerFixture):
    api = mocker.Mock(spec=NemoAPI)
    driver = create_driver(api)

    driver.login("test-user", "test-password")

    api.cerification.assert_called_once_with("test-user", "test-password")


def test_nemo_driver_buy_delegates_to_nemo_api(mocker: MockerFixture):
    api = mocker.Mock(spec=NemoAPI)
    driver = create_driver(api)

    driver.buy("123", 1200, 3)

    api.purchasing_stock.assert_called_once_with("123", 1200, 3)


def test_nemo_driver_sell_delegates_to_nemo_api(mocker: MockerFixture):
    api = mocker.Mock(spec=NemoAPI)
    driver = create_driver(api)

    driver.sell("789", 1100, 2)

    api.selling_stock.assert_called_once_with("456", 1100, 2)


def test_nemo_driver_get_price_returns_market_price(mocker: MockerFixture):
    api = mocker.Mock(spec=NemoAPI)
    api.get_market_price.return_value = 5200
    driver = create_driver(api)

    price = driver.get_price("789")

    assert price == 5200
    api.get_market_price.assert_called_once_with("789", 0)
