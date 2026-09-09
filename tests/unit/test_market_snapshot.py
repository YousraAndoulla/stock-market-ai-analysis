from data_engineering.processing.market_snapshot import (
    build_market_snapshot,
)


def test_build_market_snapshot():

    snapshot = build_market_snapshot(
        symbol="NVDA",
        latest_price=224.615,
        price_change_5m=-0.03,
        volume_5m=1668,
        bid=224.60,
        ask=224.63,
        spread=0.03,
    )

    assert snapshot["symbol"] == "NVDA"
    assert snapshot["latest_price"] == 224.615
    assert snapshot["price_change_5m"] == -0.03
    assert snapshot["volume_5m"] == 1668
    assert snapshot["bid"] == 224.60
    assert snapshot["ask"] == 224.63
    assert snapshot["spread"] == 0.03