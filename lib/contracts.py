from ibapi.contract import Contract

class Contracts:
    def apple_stocks(self):
        contract = Contract()
        contract.symbol = 'AAPL'
        contract.secType = 'STK'
        contract.exchange = 'SMART'
        contract.currency = 'USD'

        return contract

    def spy_stocks(self):
        contract = Contract()
        contract.symbol = "SPY"
        contract.secType = "STK"
        contract.exchange = "SMART"
        contract.currency = "USD"

        return contract

    def btc_futures(self):
        contract = Contract()
        contract.symbol = 'BRR'
        contract.secType = 'FUT'
        contract.exchange = 'CMECRYPTO'
        contract.lastTradeDateOrContractMonth  = '202007'

        return contract