import pytest

from data_engineering.processing.market_features import calculate_price_change


def test_price_change_increase():
    result = calculate_price_change(231.00, 234.00)

    assert result == pytest.approx(1.2987, rel=1e-4)


def test_price_change_decrease():
    result = calculate_price_change(234.00, 231.00)

    assert result == pytest.approx(-1.2821, rel=1e-4)


def test_price_change_zero_previous_price():
    result = calculate_price_change(0, 234.00)

    assert result == 0.0