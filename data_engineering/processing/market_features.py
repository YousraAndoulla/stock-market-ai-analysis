def calculate_price_change(previous_price, current_price):
    if previous_price == 0:
        return 0.0

    return ((current_price - previous_price) / previous_price) * 100