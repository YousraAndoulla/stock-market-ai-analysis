from alpaca.data.live import StockDataStream

from src.config import ALPACA_API_KEY, ALPACA_SECRET_KEY
from src.universe import NASDAQ_100_SYMBOLS
from data_engineering.processing.market_processor import MarketDataProcessor
from data_engineering.processing.market_features import (
    calculate_price_change_over_window,
    calculate_volume_over_window,
)
from data_engineering.processing.market_snapshot import (
    build_market_snapshot,
)


processor = MarketDataProcessor()


async def handle_trade(data):
    processor.process_trade(data)

    trades = processor.history.get_trades(data.symbol)

    price_change_5m = calculate_price_change_over_window(
        trades,
        window_minutes=5
    )

    volume_5m = calculate_volume_over_window(
        trades,
        window_minutes=5
    )

    state = processor.get_symbol_state(data.symbol)

    if price_change_5m is not None and state is not None:

        snapshot = build_market_snapshot(
            symbol=data.symbol,
            latest_price=state.get("last_price"),
            price_change_5m=price_change_5m,
            volume_5m=volume_5m,
            bid=state.get("bid"),
            ask=state.get("ask"),
            spread=state.get("spread"),
        )

        print("MARKET SNAPSHOT:", snapshot)

    print(
        f"TRADE | "
        f"Symbol: {data.symbol} | "
        f"Price: {data.price} | "
        f"Size: {data.size} | "
        f"Time: {data.timestamp}"
    )

    print(
        f"{data.symbol} | "
        f"Latest Price: {data.price} | "
        f"Recent Trades Stored: {len(trades)}"
    )

    if price_change_5m is not None:
        print(
            f"{data.symbol} | "
            f"Price Change 5m: {price_change_5m:.2f}% | "
            f"Volume 5m: {volume_5m:.0f} shares"
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