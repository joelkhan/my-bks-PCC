# 切片的示例
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players on my team:")
for player in players[:3]:
    print(f"\t{player.title()}")

# 最后三名队员的名字
print("And, here are the last three:")
print(players[-3:])
