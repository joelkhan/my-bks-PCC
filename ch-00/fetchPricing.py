# 获取实时币价数据
# BTC、ETH

import requests

# coingecko
response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd')
data = response.json()
print(f"比特币当前价格: {data['bitcoin']['usd']} USD")

response = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd')
data = response.json()
print(f"以太坊当前价格: {data['ethereum']['usd']} USD")


# binance
response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT')
data = response.json()
print(f"比特币当前价格: {data['price']} USDT")

response = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT')
data = response.json()
print(f"以太坊当前价格: {data['price']} USDT")

