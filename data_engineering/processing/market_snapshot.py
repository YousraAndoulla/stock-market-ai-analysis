def build_market_snapshot(
    symbol,
    latest_price,
    price_change_5m,
    volume_5m,
    bid,
    ask,
    spread,
):
    return {
        "symbol": symbol,
        "latest_price": latest_price,
        "price_change_5m": price_change_5m,
        "volume_5m": volume_5m,
        "bid": bid,
        "ask": ask,
        "spread": spread,
    }