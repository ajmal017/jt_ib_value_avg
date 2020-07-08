import os
from dotenv import load_dotenv
load_dotenv()


class Config:
    ALLOCATION = 1
    BASKET_OF_STOCKS = ["AAPL",
                        "MSFT",
                        "JPM",
                        "FB",
                        "TMUS",
                        "NVDA"]
    PERCENTAGE_TO_BUY = 1  # 20%
    BUY_WHEN_DROPPED_PERCENTAGE = 0.1  # 5%
    # REBALANCE_MONTHS = 6

    PROJECT_ALGO_DATA_ENDPOINT = "https://projectalgo.herokuapp.com/api/v1/strategy/"
    PROJECT_ALGO_STRATEGY_TOKEN = os.getenv("PROJECT_ALGO_STRATEGY_TOKEN")

    if os.getenv("PLACE_TRADES", False) == 't':
        PLACE_TRADES = True
    else:
        PLACE_TRADES = False
