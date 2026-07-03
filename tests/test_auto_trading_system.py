from pytest_mock import MockerFixture

from auto_trading_system import AutoTradingSystem
from stock_broker_driver import StockBrokerDriver


def create_system():
    return AutoTradingSystem()


def create_driver(mocker: MockerFixture):
    return mocker.Mock(spec=StockBrokerDriver)


def test_select_stock_broker_changes_current_driver(mocker: MockerFixture):
    first_driver = create_driver(mocker)
    second_driver = create_driver(mocker)
    system = create_system()

    system.select_stock_broker(first_driver)
    system.select_stock_broker(second_driver)
    system.login("test-user", "test-password")

    first_driver.login.assert_not_called()
    second_driver.login.assert_called_once_with("test-user", "test-password")


def test_login_delegates_to_selected_stock_broker(mocker: MockerFixture):
    driver = create_driver(mocker)
    system = create_system()

    system.select_stock_broker(driver)
    system.login("test-user", "test-password")

    driver.login.assert_called_once_with("test-user", "test-password")


def test_buy_delegates_to_selected_stock_broker(mocker: MockerFixture):
    driver = create_driver(mocker)
    system = create_system()

    system.select_stock_broker(driver)
    system.buy("123", 500, 3)

    driver.buy.assert_called_once_with("123", 500, 3)


def test_sell_delegates_to_selected_stock_broker(mocker: MockerFixture):
    driver = create_driver(mocker)
    system = create_system()

    system.select_stock_broker(driver)
    system.sell("456", 600, 2)

    driver.sell.assert_called_once_with("456", 600, 2)


def test_get_price_returns_selected_stock_broker_price(mocker: MockerFixture):
    driver = create_driver(mocker)
    driver.get_price.return_value = 700
    system = create_system()

    system.select_stock_broker(driver)
    price = system.get_price("789")

    assert price == 700
    driver.get_price.assert_called_once_with("789")
