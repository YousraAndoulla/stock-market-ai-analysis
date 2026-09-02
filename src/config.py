import os
from dotenv import load_dotenv

load_dotenv()

ALPACA_API_KEY = os.getenv("ALPACA_API_KEY")
ALPACA_SECRET_KEY = os.getenv("ALPACA_SECRET_KEY")

print("API key loaded:", bool(ALPACA_API_KEY))
print("Secret key loaded:", bool(ALPACA_SECRET_KEY))