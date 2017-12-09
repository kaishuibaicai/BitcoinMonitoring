from binance.client import Client
from lamda import *
import json
import urllib

client = Client(AK, AS)

depth = client.get_order_book(symbol='IOTAETH')
#print depth

prices = client.get_all_tickers()
subscriberList = ['EOSBTC', 'EOSETH', 'IOTABTC', 'IOTAETH', 'CDTBTC', 'CDTETH', 'BTCUSDT', 'ETHUSDT']
#print prices
for item in prices:
	if item['symbol'] in subscriberList :
		print 'coinType: {}   pirce: {}'.format(item['symbol'],  float(item['price']))
#print json.loads(client.get_exchange_info()) 
rate = urllib.urlopen('http://op.juhe.cn/onebox/exchange/query')
print json.loads(rate)