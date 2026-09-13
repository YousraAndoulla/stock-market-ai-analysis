def build_market_context(snapshot):
    return f"""
Stock: {snapshot['symbol']}

Current price: ${snapshot['latest_price']:.2f}
5-minute price change: {snapshot['price_change_5m']:.4f}%
5-minute trading volume: {snapshot['volume_5m']:.0f} shares
Best bid: ${snapshot['bid']:.2f}
Best ask: ${snapshot['ask']:.2f}
Bid-ask spread: ${snapshot['spread']:.2f}
""".strip()