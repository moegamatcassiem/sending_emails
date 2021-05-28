import random

guess = int(input("Try to guess the number between 1-100:"))
randNum = random.randint(1, 100)
count = 1

while guess <=100 and guess >=1:
    count += 1
    if guess > randNum:
        print("You guess too high")
        guess = int(input("Try to guess the number:"))

    elif guess < randNum:
        print("You guessed too low")
        guess = int(input("Try to guess the number:"))
    else:
        print("Nommer Ja")
        break