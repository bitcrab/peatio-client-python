import time
import urllib.request
import urllib.error
import urllib
import pickle


from lib.client import Client, get_api_path

client = Client(access_key='fwrWjuHe6sKJnOdnkvLGHruMXhoKOtE6sI59V49G', secret_key='DVKqRFxxChj2QPq4pKnIQc6ufAKxclt98qteKNNC')

#demo of GET APIs



#get member info
#print (client.get(get_api_path('members'),None, True))

#get markets
#markets =  client.get(get_api_path('markets'))
#print ("markets:", markets)

#get tickers of each market
#market should be specified in url
#print ("tickers in markets")

#print (client.get(get_api_path('tickers') % 'btscny'))

#for market in markets:
    #print(market)
    #print(str(market["id"]))
#    print (client.get(get_api_path('tickers') % market["id"]))


#print (client.get(get_api_path('orders'), {'market':'btscny'}, True))
#get orders of each market
#market should be specified in params

#print ("orders in markets")
#for market in markets:
#    print (client.get(get_api_path('orders'), {'market': market['id']}, True))

#get order book
#print (client.get(get_api_path('order_book'), {'market': 'btscny'}, True))

#get tardes
#print (client.get(get_api_path('trades'), {'market': 'btccny'}, True))

#print('get my trades')
#print (client.get(get_api_path('my_trades'), {'market': 'btccny'},True))

#get k line
#print (client.get(get_api_path('k'), {'market': 'btccny'}, True))


#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs



markets =  client.get(get_api_path('markets'))
print (markets)


#sell 1 BTS at price 0.031
params = {'market': 'btscny', 'side': 'sell', 'volume': 1, 'price': 0.031}
res = client.post(get_api_path('orders'), params)
#print (pickle.load(res))

"""
#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print res

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print res
"""
