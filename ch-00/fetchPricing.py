# 获取实时币价数据
# BTC、ETH

import requests
from pprint import pprint
import liblogr as logr
from requests.exceptions import RequestException, HTTPError,\
    ConnectionError, Timeout, SSLError


def fetchResponse(url):
    resp = {}
    try:
        #response = requests.get(url, timeout=10)  # 设置超时时间
        response = requests.get(url, verify=False)
        #response.raise_for_status()  # 检查响应状态码
        resp = response.json()  # 返回JSON数据
    except HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")  # 处理HTTP错误
    except ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")  # 处理连接错误
    except Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")  # 处理超时错误
    except SSLError as ssl_err:
        print(f"SSL error occurred: {ssl_err}")  # 处理SSL错误
    except RequestException as req_err:
        print(f"An error occurred: {req_err}")  # 处理其他请求错误
    except Exception as e:
        print(f"An unknown error occurred: {e}")  # 处理未知错误
    return resp


def doVerify(webName, webInfos):
    #logr.debug(webName)
    #logr.debug(webInfos)
    data = fetchResponse(webInfos['url'])
    #logr.debug(data)
    return data



def loadURLsETH():
    ethURLs = {}

    # 1. coingecko
    ethCoingecko = {}
    ethCoingecko['url'] = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    ethURLs['coingecko'] = ethCoingecko
    # 2. binance
    ethBinance = {}
    ethBinance['url'] = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    ethURLs['binance'] = ethBinance
    # 3. CryptoCompare
    ethCryptoCompare = {}
    ethCryptoCompare['url'] = 'https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD'
    ethURLs['cryptocompare'] = ethCryptoCompare
    # 4. CoinMarketCap
    ethCoinMarketCap = {}
    ethCoinMarketCap['url'] = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    ethURLs['coinmarketcap'] = ethCoinMarketCap
    # 5. Bitfinex
    ethBitfinex = {}
    ethBitfinex['url'] = 'https://api.bitfinex.com/v1/pubticker/ethusd'
    ethURLs['bitfinex'] = ethBitfinex
    # 6. CoinAPI
    ethCoinAPI = {}
    ethCoinAPI['url'] = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    ethURLs['coinapi'] = ethCoinAPI
    return ethURLs
#~:~


def loadURLsBTC():
    btcURLs = {}

    # 1. coingecko
    btcCoingecko = {}
    btcCoingecko['url'] = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    btcURLs['coingecko'] = btcCoingecko
    # 2. binance
    btcBinance = {}
    btcBinance['url'] = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    btcURLs['binance'] = btcBinance
    # 3. CryptoCompare
    btcCryptoCompare = {}
    btcCryptoCompare['url'] = 'https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD'
    btcURLs['cryptocompare'] = btcCryptoCompare
    # 4. Blockchain
    btcBlockchain = {}
    btcBlockchain['url'] = 'https://api.blockchain.info/stats'
    btcURLs['blockchain'] = btcBlockchain
    # 5. Bitfinex
    btcBitfinex = {}
    btcBitfinex['url'] = 'https://api.bitfinex.com/v2/ticker/tBTCUSD'
    btcURLs['bitfinex'] = btcBitfinex
    # 6. CoinMarketCap
    btcCoinMarketCap = {}
    btcCoinMarketCap['url'] = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    btcURLs['coinMarketCap'] = btcCoinMarketCap
    # 7. CoinAPI
    btcCoinAPI = {}
    btcCoinAPI['url'] = 'https://rest.coinapi.io/v1/exchangerate/BTC/USD'
    btcURLs['coinapi'] = btcCoinAPI

    #pprint(btcURLs)
    return btcURLs
#~:~


def loadURLs():
    allPrices = {}
    # BTC
    btcURLs = loadURLsBTC()
    #pprint(btcURLs)
    btcResult = verifyURLs('BTC', btcURLs)
    allPrices['BTC'] = btcResult['BTC']
    # ETH
    ethURLs = loadURLsETH()
    #pprint(ethURLs)
    ethResult = verifyURLs('ETH', ethURLs)
    allPrices['ETH'] = ethResult['ETH']

    #pprint(allPrices)
    return allPrices
#~:~


def verifyURLs(coinName, urls):
    #pprint(urls)
    coinPrices = {}
    coinPrices[coinName] = {}
    for website, url in urls.items():
        #logr.debug(website)
        #logr.debug(url)
        respData = doVerify(website, url)
        if respData:
            parsingPrice(website, respData, coinName, coinPrices[coinName])
    #pprint(coinPrices)
    return coinPrices
#~:~


def parsingPrice(website, data, coinName, recordsCurrPrice):
    #pprint(website)
    #pprint(data)
    if website == 'coingecko':
        if coinName == 'BTC':
            recordsCurrPrice[website] = data['bitcoin']['usd']
        elif coinName == 'ETH':
            recordsCurrPrice[website] = data['ethereum']['usd']
    elif website == 'binance':
        recordsCurrPrice[website] = float(data['price'])
    elif website == 'cryptocompare':
        recordsCurrPrice[website] = data['USD']
    elif website == 'bitfinex':
        if coinName == 'BTC':
            recordsCurrPrice[website] = data[0]
        elif coinName == 'ETH':
            recordsCurrPrice[website] = float(data['ask'])
#~:~


def main():
    #print('In the main():')
    allprices = loadURLs()
    pprint(allprices)


if __name__ == '__main__':
    main()


