#!/usr/bin/env python3
"""Number guessing game! User has 5 chances to guess a number between 1 and 100!"""

import random

def main():
    num= random.randint(1,100)

    rounds= 0
    guess= ""

    while rounds < 5 and guess != num:
        guess= input("Guess a number between 1 and 100\n>")

        # COOL CODE ALERT: what is the purpose of the next four lines?
        if guess.isdigit() and int(guess) >= 1 and int(guess) <= 100:
            guess= int(guess)
            
            if guess > num:
                print("Too high!")
                rounds= rounds + 1
            elif guess < num:
                print("Too low!")
                rounds= rounds + 1
            else:
                print("Correct!")
                break
        else:
            print("You must enter an integer between 1 and 100!")
            continue

main()
