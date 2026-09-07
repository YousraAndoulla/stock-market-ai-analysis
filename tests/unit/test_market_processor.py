import pytest
from types import SimpleNamespace

from data_engineering.processing.market_processor import MarketDataProcessor


def test_process_trade():
    processor = MarketDataProcessor()

    trade = SimpleNamespace(
        symbol="NVDA",
        price=234.50,
        size=100,
        timestamp="2026-09-06T15:00:00"
    )

    processor.process_trade(trade)

    state = processor.get_symbol_state("NVDA")

    assert state["last_price"] == 234.50
    assert state["last_trade_size"] == 100
    assert state["last_trade_time"] == "2026-09-06T15:00:00"


def test_process_quote():
    processor = MarketDataProcessor()

    quote = SimpleNamespace(
        symbol="NVDA",
        bid_price=234.46,
        ask_price=234.49,
        timestamp="2026-09-06T15:00:00"
    )

    processor.process_quote(quote)

    state = processor.get_symbol_state("NVDA")

    assert state["bid"] == 234.46
    assert state["ask"] == 234.49
    assert state["spread"] == pytest.approx(0.03)