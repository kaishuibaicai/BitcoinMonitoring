from binance.client import Client
from lamda import *


client = Client(AK, AS)

depth = client.get_order_book(symbol='IOTAETH')
print depth
