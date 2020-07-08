import sys
import threading
import requests
from time import sleep
from decimal import Decimal
from .ib_api import IBApi, Contracts
from configuration import Config as config


class Trader:
    def __init__(self):
        self.ibapi = IBApi()
        self.contracts = Contracts()

    def run_loop(self):
        self.ibapi.run()

    def perform(self):
        try:
            """
            Connection process and setup of thread to force loop
            """
            print("Connecting...")
            self.ibapi.connect("127.0.0.1", 7497, clientId=0)
            self.api_thread = threading.Thread(target=self.run_loop, daemon=True)
            self.api_thread.start()
            sleep(1) # Allow for the connection to the server

            """
            Trading logic goes in here, this will be performed during every loop
            """
            await self.ibapi.reqAccountSummary(9001, "All", "$LEDGER")
            print("After waiting")
            self.ibapi.reqHistoricalData(1, self.contracts.apple_stocks(), '', '5 M', '1 day', 'BID', 0, 2, False, [])
            self.ibapi.reqMarketDataType(3) # Has to be delayed data for Free Account
            self.ibapi.reqMktData(1, self.contracts.btc_futures(), '', False, False, [])

            sleep(10) # Set this to wait for all

            """
            Driver code to setup interval and disconnect from the server after each iteration
            """
            self.ibapi.disconnect()
        except:
            raise ConnectionError("Unable to create bound connection to TWS")
        # portfolio_value = self.alpaca.portfolio_value()
        # cash_balance = self.alpaca.get_cash_balance()
    #     investable_cash = Decimal(config.ALLOCATION) * cash_balance
    #     cash_to_invest_this_round = Decimal(
    #         config.PERCENTAGE_TO_BUY) * investable_cash
    #     number_of_stocks = len(config.BASKET_OF_STOCKS)
    #     dollar_per_stock = cash_to_invest_this_round / number_of_stocks

    #     print("-" * 100)
    #     print(f"Portfolio Value: {portfolio_value}")
    #     print(f"Cash Balance: {cash_balance}")
    #     print(f"Investable Cash: {investable_cash}")
    #     print(f"Cash to Invest this Round: {cash_to_invest_this_round}")
    #     print(f"Dollar per Stock: {dollar_per_stock}")
    #     print(f"# of Stocks in Basket: {number_of_stocks}")
    #     print(f"Basket of Stocks: {config.BASKET_OF_STOCKS}")

    #     if self.alpaca.is_open():
    #         self.alpaca.time_to_market_close()
    #         for symbol in config.BASKET_OF_STOCKS:
    #             last_trade = self.alpaca.get_last_trade(symbol)
    #             last_traded_price = Decimal(str(last_trade.price))

    #             try:
    #                 item = self.dynamodb.read(
    #                     table=config.DYNAMO_PRICE_HISTORY_TABLE,
    #                     key={'symbol': symbol})
    #             except KeyError as err:
    #                 breakpoint()
    #                 print(f"{symbol} " + str(self.dynamodb.write(
    #                     table=config.DYNAMO_PRICE_HISTORY_TABLE,
    #                     key={'symbol': symbol},
    #                     data={'price': last_traded_price})))
    #                 item = self.dynamodb.read(
    #                     table=config.DYNAMO_PRICE_HISTORY_TABLE,
    #                     key={'symbol': symbol})

    #             if last_traded_price > item['price']:
    #                 print(f"{symbol} " + str(self.dynamodb.write(
    #                     table=config.DYNAMO_PRICE_HISTORY_TABLE,
    #                     key={'symbol': symbol},
    #                     data={'price': last_traded_price})))

    #             elif abs((last_traded_price - item['price']) / item['price']) > config.BUY_WHEN_DROPPED_PERCENTAGE and cash_balance > Decimal("10"):
    #                 if config.PLACE_TRADES:
    #                     print(self.alpaca.market_buy(symbol, dollar_per_stock))
    #                     print(f"{symbol} " + str(self.dynamodb.write(
    #                         table=config.DYNAMO_PRICE_HISTORY_TABLE,
    #                         key={'symbol': symbol},
    #                         data={'price': last_traded_price})))
    #                 else:
    #                     print(f"Simulate market buy {dollar_per_stock} worth of {symbol}")
    #             else:

    #                 print(f"{symbol} Nothing to do")
    #     else:
    #         self.alpaca.time_to_market_open()

    #     self.print_positions()

    #     obj = {
    #         "data": {
    #             'strategy_access_token': config.PROJECT_ALGO_STRATEGY_TOKEN,
    #             'last_price': 0, # ?
    #             'margin_balance': float(portfolio_value),
    #             'wallet_balance': float(cash_balance),
    #             'realised_pnl': 0, # ?
    #             'positions': 0, # ?
    #             'symbol': config.BASKET_OF_STOCKS,
    #             'average_entry_price': # ?
    #         }
    #     }

    #     self.track_data(obj)

    # def print_positions(self):
    #     print("Positions:")
    #     print(self.alpaca.list_positions())

    # def track_data(self, data):
    #     result = requests.post(config.PROJECT_ALGO_DATA_ENDPOINT, json=data)
