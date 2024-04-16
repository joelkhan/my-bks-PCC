# hank
# 我的环境：Windows + PyCharm
#print()
print("Hello Python world!")
# 传统的hello world
print("hello, world! ")
#print("and, good luck~ ")

# 复利计算
init = 2304 # 初始本金
step = 15 # 以多少天为复利计算单位
print(round(365/step))
total = round(365/step)
print(total+1)
rate = 3.5
print(rate/100 + 1)
currDay = init
for i in range(1, total+1):
    # print(i)
    currDay = round(currDay * (rate/100 + 1))
    # print(currDay)
    print(currDay, end=" ")
    if i % 7 == 0:
        print()
print(currDay/init)



