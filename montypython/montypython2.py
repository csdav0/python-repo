#!/usr/bin/env python3

my_counter = 0

while True:
    my_counter = my_counter + 1
    print("Finish the movie title, 'Monty Python\'s The Life of ______'")
    answer = input("Your guess --> ")
    if answer == "Brian":
        print("Correct")
        break
    elif my_counter == 3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")
