import random

def captcha():
    words = ["pizza", "burger", "pasta", "chocolate", "steak"]
    word = random.choice(words)
    print(f"fboywiuefgviuegfpVF{word}iweugfriwy4geufrpw") # random alphabet so that robot can not understand :)
    user_guess = input("Enter that displayed word: ")
    if user_guess == word:
        return True

def display():
    login_user = "spiderman"
    login_pass = "12345"

    count = 0
    lim = 4
    lim_reached = False
    
    while count < lim:
        user = input("Enter your username: ")
        user_pass = input("Enter your password: ")
        
        if user == login_user and user_pass == login_pass:
            print("Please make sure you are not a Robot")
            if captcha():
                print("Welcome to our website")
                return  # Exit the function if login is successful
            else:
                print("Verification failed")
        else:
            count += 1
            print(f"Invalid username or password. Please try again. attempt left {lim - count}")
    
    lim_reached = True

    if lim_reached:
        print("Login Failed!")
    else:
        print("Please make sure you are not a Robot")
        if captcha():
            print("Welcome to our website")
        else:
            print("Verification failed")

    print("Maximum attempt reached!")

display()
