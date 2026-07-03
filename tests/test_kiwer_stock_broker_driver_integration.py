import pytest

from trading_system.brokers.kiwer_stock_broker_driver import KiwerStockBrokerDriver
from trading_system.external.kiwer_api import KiwerAPI


@pytest.fixture
def real_driver():
    # test_kiwer_stock_broker_driver.py 는 KiwerAPI 를 mocking 하지만,
    # 여기서는 실제 KiwerAPI 를 그대로 사용해 콘솔 출력을 검증한다.
    return KiwerStockBrokerDriver(KiwerAPI())


def test_login_prints_success_message(real_driver, capsys):
    real_driver.login("test-user", "test-password")

    captured = capsys.readouterr()
    assert captured.out == "test-user login success\n"


def test_buy_prints_order_with_price_and_count(real_driver, capsys):
    real_driver.buy("123", 1200, 3)

    captured = capsys.readouterr()
    assert captured.out == "123 : Buy stock ( 1200 * 3\n"


def test_sell_prints_order_with_price_and_count(real_driver, capsys):
    real_driver.sell("456", 1100, 2)

    captured = capsys.readouterr()
    assert captured.out == "456 : Sell stock ( 1100 * 2\n"


def test_get_price_returns_value_in_expected_range(real_driver):
    price = real_driver.get_price("789")

    assert 5000 <= price < 5900
