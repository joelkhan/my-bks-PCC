# 读取google表格的"交易记录"


import gspread


def google_online_excel_utils():
    credentials = {
    "type": "service_account",
    "project_id": "trading-review-432607",
    "private_key_id": "fc38cb71b785194a34887a158a72490320c3b1d8",
    "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDI0HyhSsid7LjN\nCa9PEriVkuIJYBypu9gmmt9zO00edwK+553qwFEvM+D1VgKeSZA0QRnoy56KfQNU\ny3lgiS4j5rjxHBw7SslOfpFfWPKNebaehoDwMmDF//K39gpp01iBaYDaCbEHxVsq\n1KIWwsSMkrt2NcG7cXMxDC+n30Rc8BaK20OgkJ9VgbabohzQJacNf7E0hRjGnUK2\n77aV4efouXMRwJA1Y3utw37LmMM6LsYJl60hh3vRatyzwOshTakSsjlVAI4cPeW4\n+gTIVIRO4jQ1hR9oNx8CBP4FMuSTh1hVYPg9Sdf62RYVWnxcSrneGiWjqDoJO0s8\n2Qw6sFnvAgMBAAECggEABLW0act6azFBDvz0wtPftbv0tXjqiIPGzPZSyXEVR41e\nvchIWb535LWnC7OXpsuIOX5Rpthbc9DayHrfWJABOUuqqsFDW3G1lecKkLuEQZwe\ngsHV5FTSrhZpEU//sKiBGMOmB1T5QfIzR5VZXkJ90zjdyGsraaF+eZol9y9M0H8G\nV4KL3iWNVCc+8NufoEtgt/ISy+5WfSNa3pNMzfhBB6Ap1WxpMouBVGeTF6E6IY3j\nCFLZYq4W3xQHiUCNjo/c/Bc1EY76VsbHJrQvRLSbtMc/WxYqvqu5j1DUP1tigZJp\nnafn91G27xw38FdFkBsyCH/8nWKim3YXsE+MC6zKAQKBgQD7BhdE1bXHa8RYXT79\nU57XuVaJFJikQTGyduM8poLD+ahK71K8fQfnMdWzt9eSwoKVRf4muWPHybmbN4pB\nw/4m76GFIz/iP9Ko15Bf4mz1rJUZiQOmgZirfMYurPCIVL44dFGNVXp7u/0ZrmFd\nvceSjiI/5jsfEFloYOrnfbvpUQKBgQDMy5cyX9kcHWLIMoBa+Euo71IurMrUrNGf\n6ubfV4Xbpges+k4UNHcuhoa/qYIvHbALqnWIJpVo/6ixU8hFIx1DY2N5tRNuUoz7\nY+CQ8PvrOjyauq/B0lrQug4Sd5ZvlV9VV3rZtpYXWx1BMc7rpat657Q/XDJNkL/I\n68eqmNc/PwKBgCQ4DMNx0nijpADb82q51gFqTIIa5qtMfM8zODZYECYWr6GgRl/L\n6ogBOMRlkkUqq4y+PJ15wlvhT1aF/PzgOpuDl9qN63nJm6ug7sPm97G65Qh6LHyp\n1k1oA3BYo5wIHionHl02KCYSScKa1pGgAFu1BlwR7BXfVgcpdLtR+PsBAoGBAKaD\n91j/NAG3JwWOgmz1LFec156Z4oXQStWTYstAV9eDhQQxtWCaVDmhKlkWk4KJygWC\nQPRGIv/vuBMPA2yro3SSkGR6ReVS+8y/pe1T9BGMFZDdsGCREERcs2pykAAEXTJ/\n4aS54An3jK7gt9VErExPr3BBH6mPw1Cz3XIpugJzAoGBALd7RUOAl4f/IubUk8CU\nh38Hu+wuB0o5HsGbYMEWahFuTen1zrP6tV1MDFPkXhbnZLmBUnRN0SeB1vlsuhgp\nfklzM3IHyeyYywGICxQQb08ikie+sm7nHtKVmVhMaXVtGJRgutc9VzRRkj8Y9Sh/\nTVU2oeEEw3bwE3lgtPj546pB\n-----END PRIVATE KEY-----\n",
    "client_email": "trading-review@trading-review-432607.iam.gserviceaccount.com",
    "client_id": "110322283860114852467",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/trading-review%40trading-review-432607.iam.gserviceaccount.com",
    "universe_domain": "googleapis.com"
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


