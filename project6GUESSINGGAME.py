secret_word = "pizza"
guess = ""
guess_count = 0
guess_lim = 5
lim_reached = False

while guess != secret_word and not lim_reached:
    if guess_count < guess_lim:
        guess = input(f"Your guess limit is {guess_lim - guess_count} and Enter that secret word: ")
        guess_count+=1
    else:
        lim_reached = True
if lim_reached:
    print("You Lost!!!!!")
else:
    print("You Win!!!!!")