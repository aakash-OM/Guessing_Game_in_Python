import random

jackpot = random.randint(1,100)
guess = int(input("Chl guess kar number between 1 to 100: \n"))
count = 1

while guess != jackpot:
    if guess < jackpot:
        print("   :guess higher buddy \n")
    else:
        print("   :guess lower \n")

    guess = int(input("Chl guess kar again \n"))
    count+=1


print("You guess correctly! \n")
print(f"You tooks {count} attempts!")



