import datetime
from time import sleep
from ibapi.wrapper import EWrapper
from ibapi.client import EClient
from .contracts import Contracts
from .utils import overwrite

class IBApi(EWrapper, EClient):
    def __init__(self):
        EClient.__init__(self, self)

        self.contracts = Contracts()
        self.done = False
        self.started = False
        self.nextValidOrderId = None

    @overwrite
    def nextValidId(self, orderId: int):
        super().nextValidId(orderId)

        self.nextValidOrderId = orderId
        print("Order Phase: ", orderId)

        self.start()

    @overwrite
    def historicalData(self, reqId: int, bar):
        print(f'Time: {bar.date} Close: {bar.close}')

    @overwrite
    def accountSummary(self, reqId: int, account: str, tag: str, value: str, currency: str):
        super().accountSummary(reqId, account, tag, value, currency)
        print(f"Account: {account}  Tag: {tag}  Value: {value}")
            # if tag ==
    @overwrite
    def tickPrice(self, reqId: int, tickType, price, attrib):
        print('The current ask price is: ', price)

    def setSubscriptions(self):
        self.reqAccountSummary(9001, "All", "$LEDGER")
        self.reqMarketDataType(3)
        self.reqMktData(1, self.contracts.btc_futures(), '', False, False, [])

    def start(self):
        self.setSubscriptions()
        # while True:
        #     print("Requested!")
        #     sleep(30)