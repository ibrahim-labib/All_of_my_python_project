userans = input("Do you want to play this game?[y/n]")
if userans == "y":
    print("Welcome to the game! Now we shall begin.....")
    userchoice = input("You want to play as [traveller/gamer]")
    if userchoice == "traveller":
        print("Suppose you are walking through a map and completely lost in a new country. And suddently you saw a cave and a jungle.")
        ans = input("Where should you go then?[cave/jungle]")
        if ans == "cave":
            print("There is a hungry Tiger waiting for food")
            ans = input("Now you should [run/cook food for him]")
            if ans == "run":
                print("You are too slow..You lost the game!")
            else:
                print("You are right. The tiger was VEGAN")
        else:
            print("Suddenly you saw a girl fishing near a pond")
            ans = input("What should you do now?[do some flirt/marry her and be a farmer]")
            if ans == "do some flirt":
                print("I see you are a big simp!")
            else:
                print("Good now you should apply for the PR")
    else:
        print("Suppose you are playing valorant with your teammates and suddently someone called you")
        ans = input("Now you should[pick up the phone/break the phone]")
        if ans == "pick up the phone":
            print("This is why you are still in Silver rank!")
        else:
            print("This is why you dont have a GF!!")
else:
    print("You lost the game!!")
