from collections import defaultdict, deque


class MarketHistory:

    def __init__(self, max_events=1000):
        self.trade_history = defaultdict(
            lambda: deque(maxlen=max_events)
        )

    def add_trade(self, data):
        self.trade_history[data.symbol].append(
            {
                "price": float(data.price),
                "size": float(data.size),
                "timestamp": data.timestamp,
            }
        )

    def get_trades(self, symbol):
        return list(self.trade_history[symbol])