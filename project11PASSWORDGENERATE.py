import random


def pass_generator():
    print("Welcome to password generator.")
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789@&#"
    pass_amount = int(input("Number of passwords: "))
    pass_length = int(input("Password length:"))

    for pswrd in range(pass_amount):
        password = ""
        for length in range(pass_length):
            password += random.choice(chars)
        print(password)

pass_generator()