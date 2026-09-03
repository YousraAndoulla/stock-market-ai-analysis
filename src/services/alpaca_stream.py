from alpaca.data.live import StockDataStream

from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY
from src.universe import NASDAQ_100_SYMBOLS 


async def handle_trade(data):
    print(
        f"TRADE | "
        f"Symbol: {data.symbol} | "
        f"Price: {data.price} | "
        f"Size: {data.size} | "
        f"Time: {data.timestamp}"
    )


async def handle_quote(data):
    print(
        f"QUOTE | "
        f"Symbol: {data.symbol} | "
        f"Bid: {data.bid_price} | "
        f"Ask: {data.ask_price} | "
        f"Time: {data.timestamp}"
    )


stream = StockDataStream(
    ALPACA_API_KEY,
    ALPACA_SECRET_KEY,
)


stream.subscribe_trades(handle_trade, *NASDAQ_100_SYMBOLS)
stream.subscribe_quotes(handle_quote, *NASDAQ_100_SYMBOLS)  

print("Starting Alpaca WebSocket...")
stream.run()