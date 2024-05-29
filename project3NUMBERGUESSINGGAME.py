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

#If you want to computer play against for you :)
import random

def computer_guess(x):
    guess = int(input(f"Enter a number between 1 to {x} : "))
    computerguess = 0

    while computerguess != guess:
        computerguess = random.randint(1,x)
        if computerguess < guess:
            print(f"Compter guessed the wrong number which is very low , {computerguess}")
        elif computerguess > guess:
                print(f"Computer guessed the wrong number which is very big , {computerguess}")
        guess = int(input("Enter your next guess: ")   ) 
    
    print(f"Compter guessed your word correctly which is {computerguess}")

computer_guess(5)