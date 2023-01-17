#!/usr/bin/env python3

while True:
    userinput= input("How many bottles of beer are we starting with?")
    if userinput.isdigit():
        userinput= int(userinput)
        break

for eachbottle in range(userinput, 0, -1):
    if eachbottle == userinput:
        print(f"{eachbottle} bottles of beer on the wall! {eachbottle} bottles of beer! You take one down, pass it around!")
    else:
        print(f"{eachbottle} bottles of beer on the wall!")
        print(f"{eachbottle} bottles of beer on the wall! {eachbottle} bottles of beer! You take one down, pass it around!")

print("No more bottle-sh of beer on the wall!")
