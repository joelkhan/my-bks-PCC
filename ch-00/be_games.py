# 币圈的合约游戏
# be_games.py means: btc and eth games
# 功能：
# 01. 查看实时行情
# 02. 查看当前持仓
# 03. 查看游戏进度
#-#


import libcoins as coinsLib


def showQuotes(coin='BOTH'):
    '''
    查看实时行情
    :param coin:
    :return: 行情说明字符串
    '''
    if coin == 'BOTH':
        msg = 'BTC: ' + str(coinsLib.avgPrice(coinsLib.spiderBTC())) + ', '
        msg += 'ETH: ' + str(coinsLib.avgPrice(coinsLib.spiderETH()))
        return msg
    elif coin == 'BTC':
        return 'BTC: ' + str(coinsLib.avgPrice(coinsLib.spiderBTC()))
    elif coin == 'ETH':
        return 'ETH: ' + str(coinsLib.avgPrice(coinsLib.spiderETH()))
    else:
        return "Only support: BTC, ETH or BOTH."
#-# showQuotes()


def main():
    while True:
        print("币圈的合约游戏，请选择:")
        print("  1. 查看实时行情")
        print("  2. 查看当前持仓")
        print("  3. 查看游戏进度")
        print("  4. 退出\n")

        choice = input("请输入您的选择 (1/2/3/4): ")

        if choice == '1':
            #print("您选择了选项1，输出选项1的内容。")
            print(showQuotes())
        elif choice == '2':
            print("您选择了选项2，输出选项2的内容。")
        elif choice == '3':
            print("您选择了选项3，输出选项3的内容。")
        elif choice == '4':
            print("退出程序。")
            break  # 退出循环，结束程序
        else:
            print("无效的选择，请输入1、2、3或4。")


if __name__ == '__main__':
    #print("Show Infos: ")
    #print(showQuotes())
    #print(showQuotes('FET'))
    #print(showQuotes('BOTH'))
    #print(showQuotes('BTC'))
    #print(showQuotes('ETH'))

    main()


