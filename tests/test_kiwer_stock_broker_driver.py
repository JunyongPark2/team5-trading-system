from pytest_mock import MockerFixture

from trading_system.brokers.kiwer_stock_broker_driver import KiwerStockBrokerDriver
from trading_system.brokers.stock_broker_driver import StockBrokerDriver
from trading_system.external.kiwer_api import KiwerAPI


def create_driver(api):
    return KiwerStockBrokerDriver(api)


def test_kiwer_driver_implements_stock_broker_driver(mocker: MockerFixture):
    api = mocker.Mock(spec=KiwerAPI)

    driver = create_driver(api)

    assert isinstance(driver, StockBrokerDriver)


def test_kiwer_driver_login_delegates_to_kiwer_api(mocker: MockerFixture):
    api = mocker.Mock(spec=KiwerAPI)
    driver = create_driver(api)

    driver.login("test-user", "test-password")

    api.login.assert_called_once_with("test-user", "test-password")


def test_kiwer_driver_buy_maps_price_and_count_order(mocker: MockerFixture):
    api = mocker.Mock(spec=KiwerAPI)
    driver = create_driver(api)

    driver.buy("123", 1200, 3)

    api.buy.assert_called_once_with("123", 3, 1200)


def test_kiwer_driver_sell_maps_price_and_count_order(mocker: MockerFixture):
    api = mocker.Mock(spec=KiwerAPI)
    driver = create_driver(api)

    driver.sell("456", 1100, 2)

    api.sell.assert_called_once_with("456", 2, 1100)


def test_kiwer_driver_get_price_returns_current_price(mocker: MockerFixture):
    api = mocker.Mock(spec=KiwerAPI)
    api.current_price.return_value = 5100
    driver = create_driver(api)

    price = driver.get_price("789")

    assert price == 5100
    api.current_price.assert_called_once_with("789")
