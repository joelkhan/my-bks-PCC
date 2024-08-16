# 读取google表格的"交易记录"


import gspread
import json
import sys


def getCredFilePath():
    if sys.platform == "darwin":
        credFilePath = "/Users/joel/Downloads/我的/01-炒币/trading-review-432607-fc38cb71b785.json"
    else:
        credFilePath = None
    return credFilePath


def google_online_excel_utils(credFile):
    with open(credFile, 'r', encoding='UTF-8') as f:
        credentials = json.load(f)

    gc = gspread.service_account_from_dict(credentials)
    # 交易计划表
    #targetURL = "https://docs.google.com/spreadsheets/d/1RhzS1CDRC3qDoNcRRDv8VrR5GQ0aUW9lZoc6XVVMcEU/edit?gid=2081659912#gid=2081659912"
    # 交易记录表
    targetURL = "https://docs.google.com/spreadsheets/d/1yMeQIt90HA4fpvK9ZgDx-pyNdnQY2jqemoDhL7RAcKo/edit?gid=0#gid=0"
    sht = gc.open_by_url(targetURL)  # 打开在线excel地址

    worksheet = sht.worksheet("交易记录")  # 选择需要打开的sheet页
    case_data_list = worksheet.get_all_values()  # 获取所有信息
    print(case_data_list)
    #return case_data_list


if __name__ == '__main__':
    # 1. 根据OS类型，确定credentials文件路径
    credFilePath = getCredFilePath()
    #print(credFilePath)

    # 2. 加载credentials文件，执行操作：
    google_online_excel_utils(credFilePath)

    # 3. 操作类型包括：
    #    （1）查看最近的持仓
    #    （2）对比交易计划，查看交易进度

