# -*- coding: UTF-8 -*-
# 爬取静态网页工具
import requests
import time
import re
from bs4 import BeautifulSoup
import random


def get_html_text(url):
    '''
    @方法名称: 获取网页的html信息
    @中文注释: 获取网页的html信息,转换成字符串格式数据
    @入参:
        @param url str 网址
    @出参:
        @返回状态:
            @return 0 失败或异常
            @return 1 成功
        @返回错误码
        @返回错误信息
        @param rsp_text str 网页html信息
    @作    者: PandaCode辉
    @创建时间: 2023-09-05
    @使用范例: get_html_text('https://www.baidu.com/')
    '''
    try:
        if (not type(url) is str):
            return [0, "111111", "网址参数类型错误,不为字符串", [None]]

        # 浏览器用户信息列表
        user_agents = [
            'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
            'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:43.0) Gecko/20100101 Firefox/43.0',
            'Opera/9.25 (Windows NT 5.1; U; en)',
            'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
            'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
            'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
            'Lynx/2.8.5rel.1 libwww-FM/2.14 SSL-MM/1.4.1 GNUTLS/1.2.9',
            'Mozilla/5.0 (X11; Linux i686) AppleWebKit/535.7 (KHTML, like Gecko) Ubuntu/11.04 Chromium/16.0.912.77 Chrome/16.0.912.77 Safari/535.7',
            'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:10.0) Gecko/20100101 Firefox/10.0',
        ]
        # 随机获取一个浏览器用户信息
        agent = random.choice(user_agents)
        # header头信息
        headers = {
            'User-Agent': agent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
        }
        # 代理IP地址，需要找到可用的代理ip，不然无法使用
        # proxy = {'HTTP': 'xx.xx.xx.xx:8000', 'HTTPS': 'xx.xx.xx.xx:80'}
        # response = requests.get(url, headers=headers, proxies=proxy, timeout=30)
        # 增加随机模拟浏览器访问header头信息，提高反爬网站成功率
        response = requests.get(url, headers=headers, timeout=30)
        # print(response.status_code)
        response.raise_for_status()
        response.encoding = 'utf-8'
        rsp_text = response.text
        # 返回容器
        return [1, '000000', '获取网页的html信息成功', [rsp_text]]

    except Exception as e:
        print("获取网页的html信息异常," + str(e))
        return [0, '999999', "获取网页的html信息异常," + str(e), [None]]


def spider_weather(region_code, tqyb_type):
    '''
    @方法名称: 爬取天气预报信息
    @中文注释: 根据地区代码，天气预报类型，爬取天气预报信息
    @入参:
        @param region_code str 地区代码
        @param tqyb_type str 类型(1-今天，2-近7天)
    @出参:
        @返回状态:
            @return 0 失败或异常
            @return 1 成功
        @返回错误码
        @返回错误信息
        @param rsp_dict dict 响应容器
    @作    者: PandaCode辉
    @创建时间: 2023-09-05
    @使用范例: spider_weather('101010100','1')

    天气预报网址
    http://www.weather.com.cn/weather/101010100.shtml   --北京市，近7日天气
    http://www.weather.com.cn/weather1d/101010100.shtml --北京市，今天天气
    '''

    try:
        if (not type(region_code) is str):
            return [0, "111111", "地区代码参数类型错误,不为字符串", [None]]
        if (not type(tqyb_type) is str):
            return [0, "111112", "类型参数类型错误,不为字符串", [None]]

        url = ""
        # 类型(1-今天，2-近7天)
        if tqyb_type == '1':
            url = 'http://www.weather.com.cn/weather1d/' + region_code + '.shtml'
        elif tqyb_type == '2':
            url = 'http://www.weather.com.cn/weather/' + region_code + '.shtml'

        # UTC格式当前时区时间
        t = time.localtime()
        work_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
        print('当前日期时间:' + str(work_time))
        now_day = str(work_time)[:7]
        # 根据url地址获取网页信息
        rst = get_html_text(url)
        if rst[0] != 1:
            return rst
        html_str = rst[3][0]
        # 使用BeautifulSoup解析网页数据
        soup = BeautifulSoup(html_str, "html.parser")

        # 返回容器初始化
        rsp_dict = {}
        # 类型(1-今天，2-近7天)
        if tqyb_type == '1':
            # 获取今天天气信息
            # 白天,天气情况
            tq_day_info = soup.select("div.t >ul.clearfix > li > p.wea")[0].text
            rsp_dict["tq_day_info"] = '白天,天气情况:' + tq_day_info
            print(rsp_dict["tq_day_info"])

            # 最高温度
            temperatrue_high = soup.select("div.t >ul.clearfix > li > p.tem")[0].text
            # 去除换行符
            temperatrue_high = ''.join(re.findall(r'\S', temperatrue_high))
            rsp_dict["temperatrue_high"] = '白天,最高温度:' + temperatrue_high
            print(rsp_dict["temperatrue_high"])

            # 夜间,天气情况
            tq_night_info = soup.select("div.t >ul.clearfix > li > p.wea")[1].text
            rsp_dict["tq_night_info"] = '夜间,天气情况:' + tq_night_info
            print(rsp_dict["tq_night_info"])
            # 夜间,最低温度
            temperatrue_low = soup.select("div.t >ul.clearfix > li > p.tem")[1].text
            # 去除换行符
            temperatrue_low = ''.join(re.findall(r'\S', temperatrue_low))
            rsp_dict["temperatrue_low"] = '夜间,最低温度:' + temperatrue_low
            print(rsp_dict["temperatrue_low"])
            print('===============================')
        elif tqyb_type == '2':
            # 获取近7日天气
            rsp_dict["c7day_list"] = []
            # 日期
            day_info = soup.select(
                "div.c7d > input > input > input > ul.t.clearfix > li > h1")
            # print('日期:' + str(day_info))
            # 天气
            tq_info = soup.select(
                "div.c7d > input > input > input > ul.t.clearfix > li > p.wea")
            # print('天气:' + str(tq_info))
            # 温度
            tem_info = soup.select(
                "div.c7d > input > input > input > ul.t.clearfix > li > p.tem")
            # print('温度:' + str(tem_info))
            # 风力
            win_info = soup.select(
                "div.c7d > input > input > input > ul.t.clearfix > li > p.win > i")
            # print('风力:' + str(win_info))
            # 列表存储
            for i in range(7):
                temp_dict = {}
                # 日期
                temp_dict["day_info"] = '日期:' + now_day + '-' + str(day_info[i].text)
                print(temp_dict["day_info"])
                # 天气
                temp_dict["tq_info"] = '天气:' + str(tq_info[i].text)
                print(temp_dict["tq_info"])
                # 温度
                # 去除换行符
                temperatrue = ''.join(re.findall(r'\S', str(tem_info[i].text)))
                temp_dict["tem_info"] = '温度:' + temperatrue
                print(temp_dict["tem_info"])
                # 风力
                temp_dict["win_info"] = '风力:' + str(win_info[i].text)
                print(temp_dict["win_info"])
                # 添加到列表
                rsp_dict["c7day_list"].append(temp_dict)
                print('===============================')
        # 返回容器
        return [1, '000000', '爬取天气预报信息成功', [rsp_dict]]

    except Exception as e:
        print("爬取天气预报信息异常," + str(e))
        return [0, '999999', "爬取天气预报信息异常," + str(e), [None]]


# 主方法
if __name__ == '__main__':
    # 101010100 - 北京市
    # 爬取天气预报-今天
    rst1 = spider_weather('101010100', '1')
    rsp_dict1 = rst1[3][0]
    print(rsp_dict1)
    # 爬取天气预报-近7天
    #rst2 = spider_weather('101010100', '2')
    #rsp_dict2 = rst2[3][0]
    #print(rsp_dict2)