import random
randomnums = random.randint(1,200)
print(randomnums)
usermsg = int(input("Enter a number: "))
#well guessed one time :)
if usermsg > randomnums:
    print("Number is too Big")
elif usermsg < randomnums:
    print("Number is too small")
else:
    print("correct!")