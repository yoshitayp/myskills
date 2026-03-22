import random
rolls = int(input("How many times do you want to roll the dice? "))
for i in range(rolls):
    print("Roll", i + 1, ":", {random.randint(1, 6)})