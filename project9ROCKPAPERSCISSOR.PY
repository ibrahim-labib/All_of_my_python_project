import random

def play():
    while True:
        computer_choice = random.choice(["r","p","s"])
        user_input = input("'r' for Rock \n 'p' for Paper \n 's' for Scissor \n Enter your choice: ")

        if user_input == "q":
            print("Thanks for playing")
            break

        if user_input == computer_choice:
            print("It's a Tie!")
        elif win(user_input, computer_choice):
            print("You Won!")
        else:
            print("You Lost!")
#concept: r > s, p > r, s > r

def win(player , opponent):
    if (player == "r" and opponent == "s") or (player == "p" and opponent == "r") or (player == "s" and opponent == "p"):
        return True

play()