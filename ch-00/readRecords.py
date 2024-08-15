# 读取google表格的"交易记录"


import gspread


def google_online_excel_utils():
    credentials = {
    }


    gc = gspread.service_account_from_dict(credentials)
    # 交易计划表
    #targetURL = "https://docs.google.com/spreadsheets/d/1RhzS1CDRC3qDoNcRRDv8VrR5GQ0aUW9lZoc6XVVMcEU/edit?gid=2081659912#gid=2081659912"
    # 交易记录表
    targetURL = "https://docs.google.com/spreadsheets/d/1yMeQIt90HA4fpvK9ZgDx-pyNdnQY2jqemoDhL7RAcKo/edit?gid=0#gid=0"
    sh = gc.open_by_url(targetURL)  # 打开在线excel地址

    worksheet = sh.worksheet("交易记录")  # 选择需要打开的sheet页
    case_data_list = worksheet.get_all_values()  # 获取所有信息
    print(case_data_list)
    #return case_data_list


if __name__ == '__main__':
    google_online_excel_utils()


