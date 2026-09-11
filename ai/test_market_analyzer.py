from ai.market_analyzer import analyze_market


context = """
Stock: NVDA

Current price: $224.62
5-minute price change: -0.0300%
5-minute trading volume: 1668 shares
Best bid: $224.60
Best ask: $224.63
Bid-ask spread: $0.03
"""


analysis = analyze_market(context)

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