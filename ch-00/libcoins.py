# 和币有关的函数库
import requests
from requests.exceptions import RequestException, HTTPError,\
    ConnectionError, Timeout, SSLError

#import sys
#from loguru import logger
import liblogr as logr

def fetchResponse(url):
    resp = {}
    try:
        #response = requests.get(url, timeout=10)  # 设置超时时间
        response = requests.get(url, verify=False)
        response.raise_for_status()  # 检查响应状态码
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
    #print("resp:\n\t")
    #print(resp)
    #logger.trace("resp:\n\t")
    #logger.trace(str(resp))
    logr.debug("resp:\n\t")
    logr.debug(str(resp))
    return resp


def spiderBTC():
    priceBTC = {}

    # coingecko BTC
    geckoBTCURL = 'https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd'
    data = fetchResponse(geckoBTCURL)
    #pprint(data)
    if data:
        #print(f"比特币当前价格: {data['bitcoin']['usd']} USD")
        priceBTC['coingecko'] = data['bitcoin']['usd']

    # binance BTC
    binanceBTCURL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'
    data = fetchResponse(binanceBTCURL)
    #pprint(data)
    if data:
        #print(f"比特币当前价格: {data['price']} USDT")
        priceBTC['binance'] = float(data['price'])

    return priceBTC


def avgPrice(pricingAll):
    cntr = 0
    sum = 0
    for v in pricingAll.values():
        #print(v)
        if v:
            cntr += 1
            sum += v
    #print(cntr)
    #print(sum)
    #print(sum / cntr)
    #print(round(sum / cntr, 2))
    if cntr:
        return int(round(sum / cntr, 2))


def spiderETH():
    priceETH = {}

    # coingecko ETH
    geckoETHURL = 'https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd'
    data = fetchResponse(geckoETHURL)
    if data:
        #print(f"以太坊当前价格: {data['ethereum']['usd']} USD")
        priceETH['coingecko'] = data['ethereum']['usd']

    # binance ETH
    binanceETHURL = 'https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT'
    data = fetchResponse(binanceETHURL)
    if data:
        #print(f"以太坊当前价格: {data['price']} USDT")
        priceETH['binance'] = float(data['price'])

    return priceETH




if __name__ == '__main__':
    logr.debug("this is a debug.")
    #main()

    # 移除默认的日志处理器
    #logger.remove()

    # 添加新的日志处理器，输出到标准输出
    #logger.add(sys.stdout, level="TRACE", format="{time} {level} {message}")
    #logger.add(sys.stdout, level="DEBUG", format="{time} {level} {message}")
    #logger.add(sys.stdout, level="INFO", format="{time} {level} {message}")
    #logger.add(sys.stdout, level="SUCCESS", format="{time} {level} {message}")

    # 不同级别的日志记录示例
    #logger.trace("This is a trace message.")
    #logger.debug("This is a debug message.")
    #logger.info("This is an info message.")
    #logger.success("This is a success message.")
    #logger.warning("This is a warning message.")
    #logger.error("This is an error message.")
    #logger.critical("This is a critical message.")

