from ai.pipeline import run_market_analysis


snapshot = {
    "symbol": "NVDA",
    "latest_price": 224.62,
    "price_change_5m": -0.03,
    "volume_5m": 1668,
    "bid": 224.60,
    "ask": 224.63,
    "spread": 0.03,
}


analysis = run_market_analysis(snapshot)

print("\nAI MARKET ANALYSIS:\n")

print("Market state:")
print(analysis.market_state)

print("\nPrice observation:")
print(analysis.price_observation)

print("\nVolume observation:")
print(analysis.volume_observation)

print("\nLiquidity observation:")
print(analysis.liquidity_observation)

print("\nRisk notes:")
print(analysis.risk_notes)