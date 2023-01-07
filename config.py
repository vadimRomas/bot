import os


class Config:
    binance_key = os.environ.get("binance_key")
    binance_secret_key = os.environ.get("binance_secret_key")
