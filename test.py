from binance.client import Client
from lamda import *

client = Client(AK, AS)

# get market depth
depth = client.get_order_book(symbol='BNBBTC')

# place market buy order
from binance.enums import *
order = client.create_order(
    symbol='BNBBTC',
    side=SIDE_BUY,
    type=ORDER_TYPE_MARKET,
    quantity=100)

# get all symbol prices
prices = client.get_all_tickers()

# withdraw 100 ETH
# check docs for assumptions around withdrawals
from binance.exceptions import BinanceApiException, BinanceWithdrawException
try:
    result = client.withdraw(
        asset='ETH',
        address='<eth_address>',
        amount=100)
except BinanceApiException as e:
    print(e)
except BinanceWithdrawException as e:
    print(e)
else:
    print("Success")

# fetch list of withdrawals
withdraws = client.get_withdraw_history()

# get a deposit address
address = client.get_deposit_address('BTC')
# start trade websocket
def process_message(msg):
    print("message type:" + msg[e])
    print(msg)
    # do something

from binance.websockets import BinanceSocketManager
bm = BinanceSocketManager(client)
bm.start_trade_socket(symbol='BNBBTC')
bm.start()
