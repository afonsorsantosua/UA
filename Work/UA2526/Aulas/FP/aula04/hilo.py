# Complete the code to make the HiLo game.

import random

def playHiLo():
    # Pick a random number between 1 and 100, inclusive
    secret = random.randrange(1, 101)

    print("I picked a number between 1 and 100. Can you guess it?")
    # put your code here
    guess = int(input("Enter your guess: "))
    tentativas = 1
    while guess != secret:
        if guess > secret:
            print("Too high")
            guess = int(input("Try again: "))
        elif guess < secret:
            print("Too low")
            guess = int(input("Try again: "))
        tentativas = tentativas + 1
    print("Congrats!!\nYour number of tries: " , tentativas)

playHiLo()

