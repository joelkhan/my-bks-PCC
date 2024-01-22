# 演示了一个逻辑上的缩进错误，同时，展示了for循环变量的一些特性
magicians = ['alice', 'david', 'carolina']
for magician in magicians: 
    print(f"{magician.title()}, that was a great trick!")
print(f"I can't wait to see your next trick, {magician.title()}.\n")

# 即使跳出了for循环，仍然可以引用到变量“magician”
print(f"{magician}")
