import time, json
import hmac, hashlib, base64
import requests, urllib.parse


def sendMsg(token, secret, msg='我是美股在线の机器人哟'):
    # 钉钉机器人Webhook地址
    webhook = 'https://oapi.dingtalk.com/robot/send?access_token=' + token
    # 钉钉机器人秘钥
    #secret = 'SEC4b38510f2a1f778dc640bf754b6fbc024ef65261baf92214aa9ff71f79203314'

    # 计算加签
    timestamp = str(round(time.time() * 1000))
    secret_enc = secret.encode('utf-8')
    string_to_sign = '{}\n{}'.format(timestamp, secret)
    string_to_sign_enc = string_to_sign.encode('utf-8')
    hmac_code = hmac.new(secret_enc, string_to_sign_enc, digestmod=hashlib.sha256).digest()
    sign = urllib.parse.quote_plus(base64.b64encode(hmac_code))

    # 完整的Webhook URL
    webhook_with_sign = f"{webhook}&timestamp={timestamp}&sign={sign}"

    # 定义要发送的数据
    headers = {'Content-Type': 'application/json'}
    #data = {
    #    "msgtype": "text",
    #    "text": {
    #        "content": "最近行情不好，以观望为主~"
    #    },
    #    "isAtAll": False  # 是否@所有人
    #}
    textDict = {}
    textDict['content'] = msg
    data = {}
    data['msgtype'] = 'text'
    data['text'] = textDict
    data['isAtAll'] = False # 是否@所有人

    # 发送POST请求
    response = requests.post(webhook_with_sign, data=json.dumps(data), headers=headers)
    print(response.text)
# ~:~


def loadToken():
    tokenFilepath = '/Users/joel/Downloads/my-mine/04-其它/data/钉钉机器人/美股在线/access_token.txt'

    # 使用with open打开文件并读取内容
    with open(tokenFilepath, 'r', encoding='utf-8') as file:
        content = file.read()  # 读取文件的全部内容

    # 输出读取的内容
    #print(content)
    return content
#~:~


def loadSecret():
    secretFilepath = '/Users/joel/Downloads/my-mine/04-其它/data/钉钉机器人/美股在线/secret.txt'

    # 使用with open打开文件并读取内容
    with open(secretFilepath, 'r', encoding='utf-8') as file:
        content = file.read()  # 读取文件的全部内容

    # 输出读取的内容
    #print(content)
    return content
#~:~


def main():
    #print('In the main():')
    #allprices = loadURLs()
    #pprint(allprices)
    token = loadToken()
    print(token)
    secret = loadSecret()
    print(secret)

    msg = '我是天天盯，很高兴为您盯盘~'
    sendMsg(token, secret, msg)
#~:~


if __name__ == '__main__':
    main()


