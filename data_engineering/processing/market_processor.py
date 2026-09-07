from data_engineering.processing.market_history import MarketHistory

class MarketDataProcessor:

    def __init__(self):
        self.market_state = {}
        self.history = MarketHistory()

    def process_trade(self, data):
        symbol = data.symbol

        if symbol not in self.market_state:
            self.market_state[symbol] = {}

        self.market_state[symbol]["last_price"] = data.price
        self.market_state[symbol]["last_trade_size"] = data.size
        self.market_state[symbol]["last_trade_time"] = data.timestamp

        self.history.add_trade(data)

    def process_quote(self, data):
        symbol = data.symbol

        if symbol not in self.market_state:
            self.market_state[symbol] = {}

        self.market_state[symbol]["bid"] = data.bid_price
        self.market_state[symbol]["ask"] = data.ask_price
        self.market_state[symbol]["quote_time"] = data.timestamp

        if data.bid_price and data.ask_price:
            self.market_state[symbol]["spread"] = (
                data.ask_price - data.bid_price
            )

    def get_symbol_state(self, symbol):
        return self.market_state.get(symbol)