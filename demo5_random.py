import random

roll = random.randint(1,6)

user = int(input("Roll dice :\n"))

if user > 6 or user < 1:
    print("Invalid Entry")
elif roll == user:
    print(roll)
    print("TIE")
elif roll > user:
    print(roll)
    print("COMP wins")
else:
    print(roll)
    print("USER wins")
