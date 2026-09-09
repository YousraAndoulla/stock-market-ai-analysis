from datetime import timedelta

def calculate_price_change(previous_price, current_price):
    if previous_price == 0:
        return 0.0

    return ((current_price - previous_price) / previous_price) * 100





def calculate_price_change_over_window(trades, window_minutes=5):
    if len(trades) < 2:
        return None

    current_trade = trades[-1]
    current_price = current_trade["price"]
    current_time = current_trade["timestamp"]

    cutoff_time = current_time - timedelta(minutes=window_minutes)

    previous_trade = None

    for trade in trades:
        if trade["timestamp"] >= cutoff_time:
            previous_trade = trade
            break

    if previous_trade is None:
        return None

    return calculate_price_change(
        previous_trade["price"],
        current_price
    )