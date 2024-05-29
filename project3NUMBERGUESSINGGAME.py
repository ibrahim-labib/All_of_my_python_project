import random

def guess(x):
    random_num = random.randint(1,x)
    guess = ""
    while guess != random_num:
        guess = int(input(f"Guess the number between 1 to {x} : "))
        if guess < random_num:
            print("Your number is too small")
        elif guess > random_num:
            print("Your number is too big")
    print(f"Yay , you successfully guessed the number which is {guess}")
guess(10)