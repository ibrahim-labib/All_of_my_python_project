import random
dicerolling = True
while dicerolling:
    print(random.randrange(1,6))
    userchoice = input("Do you want to dice again?[y/n]")
    if userchoice == "y":
        continue
    else:
        print("Game over")
        break