import ollama


# Define the functions
def get_current_weather(location):
    # Simulate API call to get current weather
    weather_data = {
        "New York, NY": {"weather": "sunny", "temperature": 75},
        "Los Angeles, CA": {"weather": "cloudy", "temperature": 65}
    }
    return weather_data.get(location, {"weather": "unknown", "temperature": "unknown"})


def get_stock_price(ticker):
    # Simulate API call to get stock price
    stock_data = {
        "AAPL": {"price": 150.0},
        "GOOG": {"price": 2500.0}
    }
    return stock_data.get(ticker, {"price": "unknown"})
