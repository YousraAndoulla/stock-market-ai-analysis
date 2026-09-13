from ai.context import build_market_context


def test_build_market_context():

    snapshot = {
        "symbol": "NVDA",
        "latest_price": 224.62,
        "price_change_5m": -0.03,
        "volume_5m": 1668,
        "bid": 224.60,
        "ask": 224.63,
        "spread": 0.03,
    }

    context = build_market_context(snapshot)

    assert "NVDA" in context
    assert "$224.62" in context
    assert "-0.0300%" in context
    assert "1668 shares" in context
    assert "$224.60" in context
    assert "$224.63" in context
    assert "$0.03" in context