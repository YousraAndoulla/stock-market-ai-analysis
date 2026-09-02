from alpaca.data.live import StockDataStream

from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY


async def handle_trade(data):
    print(f"Symbol: {data.symbol}")
    print(f"Price: {data.price}")
    print(f"Timestamp: {data.timestamp}")
    print("-" * 40)


stream = StockDataStream(
    ALPACA_API_KEY,
    ALPACA_SECRET_KEY,
)

stream.subscribe_trades(handle_trade, "AAPL")

print("Starting Alpaca WebSocket...")
stream.run()