from types import SimpleNamespace

from data_engineering.processing.market_history import MarketHistory


def test_add_trade():
    history = MarketHistory()

    trade = SimpleNamespace(
        symbol="NVDA",
        price=234.50,
        size=100,
        timestamp="2026-09-06T15:00:00"
    )

    history.add_trade(trade)

    trades = history.get_trades("NVDA")

    assert len(trades) == 1
    assert trades[0]["price"] == 234.50
    assert trades[0]["size"] == 100
    assert trades[0]["timestamp"] == "2026-09-06T15:00:00"

def test_store_multiple_trades():
    history = MarketHistory()

    trade_1 = SimpleNamespace(
        symbol="NVDA",
        price=231.00,
        size=100,
        timestamp="2026-09-06T15:00:00"
    )

    trade_2 = SimpleNamespace(
        symbol="NVDA",
        price=232.00,
        size=200,
        timestamp="2026-09-06T15:01:00"
    )

    trade_3 = SimpleNamespace(
        symbol="NVDA",
        price=234.00,
        size=150,
        timestamp="2026-09-06T15:02:00"
    )

    history.add_trade(trade_1)
    history.add_trade(trade_2)
    history.add_trade(trade_3)

    trades = history.get_trades("NVDA")

    assert len(trades) == 3
    assert trades[0]["price"] == 231.00
    assert trades[1]["price"] == 232.00
    assert trades[2]["price"] == 234.00