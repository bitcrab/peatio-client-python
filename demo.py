import time
import urllib.request
import urllib.error
import urllib

from lib.client import Client, get_api_path

client = Client(access_key='ACCESS_KEY', secret_key='SECRET_KEY')

#demo of GET APIs

#get member info
print ("memo")
print (client.get(get_api_path('members'),None, True))

#get markets
markets =  client.get(get_api_path('markets'))
print ("markets:", markets)

#get tickers of each market
print ("tickers in markets")
print (client.get(get_api_path('tickers') % 'btscny'))

for market in markets:
    print(str(market["id"]))
    print (client.get(get_api_path('tickers') % market["id"]))

print (client.get(get_api_path('orders'), {'market':'daocny'}, True))

#get orders of each market
#market should be specified in params

print ("orders in markets")
for market in markets:
    print (client.get(get_api_path('orders'), {'market': market['id']}, True))

#get order book
print (client.get(get_api_path('order_book'), {'market': 'btscny'}, True))

#get tardes
print (client.get(get_api_path('trades'), {'market': 'btccny'}, True))

#print('get my trades')
print (client.get(get_api_path('my_trades'), {'market': 'btccny'},True))

#get k line
print (client.get(get_api_path('k'), {'market': 'btccny'}, True))

#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

"""
#create an order
params = {'market': 'btscny', 'side': 'sell', 'volume': 1.0, 'price': 0.031}
res = client.post(get_api_path('orders'), params)
print (res)

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print (res)

#delete a specific order by order_id
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
#this is not tested yet
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print (res)
"""
