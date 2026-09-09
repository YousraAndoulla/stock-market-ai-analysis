import pytest
from datetime import datetime

from data_engineering.processing.market_features import (
    calculate_price_change,
    calculate_volume_over_window,
)


def test_price_change_increase():
    result = calculate_price_change(231.00, 234.00)

    assert result == pytest.approx(1.2987, rel=1e-4)


def test_price_change_decrease():
    result = calculate_price_change(234.00, 231.00)

    assert result == pytest.approx(-1.2821, rel=1e-4)


def test_price_change_zero_previous_price():
    result = calculate_price_change(0, 234.00)

    assert result == 0.0

def test_volume_over_window():
    trades = [
        {
            "price": 224.50,
            "size": 100.0,
            "timestamp": datetime.fromisoformat(
                "2026-09-09T14:25:00"
            ),
        },
        {
            "price": 224.60,
            "size": 50.0,
            "timestamp": datetime.fromisoformat(
                "2026-09-09T14:27:00"
            ),
        },
        {
            "price": 224.80,
            "size": 200.0,
            "timestamp": datetime.fromisoformat(
                "2026-09-09T14:29:00"
            ),
        },
    ]

    result = calculate_volume_over_window(trades, window_minutes=5)

    assert result == 350.0  