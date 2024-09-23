temperature = 5
if temperature >= 35:
    print("It's too Hot")
    print("Stay Indoor")
print("Let's go for a walk")

if temperature >= 35:
    print("It's too Hot")
    print("Stay Indoor")
elif temperature <= 15:
    print("It's too Cold")
    print("Stay Indoor")
else:
    print("Let's go for a walk")

if temperature >= 35 or temperature <=15:
    print("Stay Indoor")
else:
    print("Let's go fora walk")
