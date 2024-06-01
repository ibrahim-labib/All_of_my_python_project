import random

def password_generator(num_password, password_length):
    passwords = []
    char = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@&#"
    for i in range(num_password):
        password = ""
        for j in range(password_length):
            password += random.choice(char)
        passwords.append(password)
    
    return passwords

def valid_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a positive integer value.")
            else:
                return value
        except ValueError:
            print("Please enter a valid integer.")

def main_screen():
    print("Welcome to the password generator.")
    while True:
        num_password = valid_int("Number of passwords: ")
        password_length = valid_int("Password length: ")
        passwords = password_generator(num_password, password_length)
    
        for password in passwords:
            print(password)
        
        user_quit = input("Do you want to quit? [y/n]: ")
        if user_quit == "y":
            break 

if __name__ == "__main__":
    main_screen()
