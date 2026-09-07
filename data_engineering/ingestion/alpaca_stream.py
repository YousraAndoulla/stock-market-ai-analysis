from alpaca.data.live import StockDataStream

from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY
from src.universe import NASDAQ_100_SYMBOLS 
from data_engineering.processing.market_processor import MarketDataProcessor


processor = MarketDataProcessor()

async def handle_trade(data):
    processor.process_trade(data)

    trades = processor.history.get_trades(data.symbol)
    print(
        f"TRADE | "
        f"Symbol: {data.symbol} | "
        f"Price: {data.price} | "
        f"Size: {data.size} | "
        f"Time: {data.timestamp}"
    )
    print(
        f"{data.symbol} | "
        f"Current Price: {data.price} | "
        f"Recent Trades Stored: {len(trades)}"
    ) 


async def handle_quote(data):
    processor.process_quote(data)
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