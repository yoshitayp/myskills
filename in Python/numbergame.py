import random
number=random.randint(1,100)
guess=None
while guess !=number:
    guess=int(input("guess a number(1-100):"))
    if guess<number:
        print("too low")
    elif guess>number:
        print("too high")
    else:
        print("congratulations! you guessed the number")