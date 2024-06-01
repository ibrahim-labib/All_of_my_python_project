import random

def password_generator(num_password, password_lenght):
    passwords = []
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@&#"
    for i in range(num_password):
        password = ""
        for i in range(password_lenght):
            password += random.choice(char)
        passwords.append(password)
    
    return passwords


def valid_int(promt):
    while True:
        try:
            value = int(input(promt))
            if value < 0:
                print("Please enter a positive integer value.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")


def main_screen():
    while True:
        print("Welcome to the password generator.")
        num_password = valid_int("Number of password: ")
        password_lenght = valid_int("Password lenght: ")
        passwords = password_generator(num_password,password_lenght)

        
        for password in passwords:
            print(password)

        user_quit = input("Do you want to quit? [y/n]: ")
        if user_quit.lower() == "y":
            break 

if __name__ == "__main__":
    main_screen()