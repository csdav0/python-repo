#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

my_counter = 0
answer = " "

while my_counter < 3 and answer != "Brian":
    my_counter += 1     # increase the my_counter counter by 1
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer = answer.capitalize()
    if answer == "Brian": # logic to check if user gave correct answer
        print("Correct!")
    elif my_counter == 3:    # logic to ensure my_counter has not yet reached 3
        print("Sorry, the answer was Brian.")
    elif answer == "Shrubbery":
        print("You provided the super secret answer!")
        break
    else:                 # if answer was wrong
        print("Sorry. Try again!")
        

