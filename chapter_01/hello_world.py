# hank
# 我的环境：Windows + PyCharm
#print()
print("Hello Python world!")
# 传统的hello world
print("hello, world! ")
#print("and, good luck~ ")

# 一个币市的复利计算模型
print()
init = 2304     # 初始本金
step = 15       # 以多少天为复利计算单位， 如：15天，大约2周
#print(round(365/step))
total = round(365/step)
#print(total+1)
rate = 7.5      # 做到比银行的定期高一点点
#print(rate/100 + 1)
print('初始本金：\t' + str(init))
print('目标是：\t每' + str(step) + '天找到一次' + str(rate) + '%的增长机会。')
currDay = init
for i in range(1, total+1):
    # print(i)
    currDay = round(currDay * (rate/100 + 1))
    # print(currDay)
    print(currDay, end=" ")
    if i % 7 == 0:
        print()
print('\n365天后，本金：\t' + str(currDay))
print('本金增长约：\t' + str(round(currDay/init, 2)) + '倍')



