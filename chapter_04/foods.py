my_foods = ['pizza', 'falafel', 'carrot cake'] 
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)
for myFood in my_foods:
    print(f"\t{myFood}")

print("\nMy friend's favorite foods are:")
print(friend_foods)
for friFood in friend_foods:
    print(f"\t{friFood}")

