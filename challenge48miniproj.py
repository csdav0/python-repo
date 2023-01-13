#!/usr/bin/env python3
import pyfiglet
import curses
import random
import sys, time
import os

def main():
    #using curses module, set up title text windows that can handle Figlet objects
    stdscr= curses.initscr()
    win2 = curses.newwin(9, 44, 9, 16)
    win3 = curses.newwin(9, 122, 18, 0)


    welcome_title = pyfiglet.figlet_format("WELCOME", font= "doom")
    stdscr.addstr(1,0,welcome_title)
    stdscr.refresh()
    to_title = pyfiglet.figlet_format("TO", font= "doom")
    win2.addstr(0,0,to_title)
    win2.refresh()
    title = pyfiglet.figlet_format("DEATH ROLL", font= "doom")
    win3.addstr(0,0,title)
    win3.refresh()
    
    #press any key to continue is a built-in behavior to curses .getch() and .endwin()
    win4 = curses.newwin(2,30,27,0)
    win4.addstr(0,0,"Press any key to continue")
    win4.refresh()

    stdscr.getch()
    curses.endwin()

    #intro preamble, uses system flush to display text one character at a time in 0.02s increments
    for char in "In DEATH ROLL, you will face off against GAMBLER_BOT_5000 in rolls to the DEATH!!!":
        print(char, end="")
        sys.stdout.flush()
        time.sleep(0.02)
    print("\n")

    #QoL feature so you don't have to sit through rules every time game starts
    while True:
        see_rules_query= input("Would you like to read the rules? (y/n)\n")
        if see_rules_query.lower() == "y":
            for char in "Select a number to start, this will be the initial upper bound for a random number generator.\n\nThen 'roll' to generate a random integer in that range.\n\nNow it\'s GAMBLER_BOT_5000's turn -\nit will roll between 1 and the number that was generated (decreasing the roll range).\n\nIt is then your turn again to roll between 1 and the number GAMBLER_BOT_5000 just rolled.\n\nTurns continue in this way until someone rolls the number '1'.\n\nWhoever rolls a '1' first has rolled a DEATH ROLL and loses the game!":
                print(char, end="")
                sys.stdout.flush()
                time.sleep(0.02)
            print("\n")
            break
        elif see_rules_query.lower() == "n":
            print("")
            break
        else:
            print("y or n response required.")

    while True:
        user_input= input("When you are ready to begin press 'Enter'.\n")
        if user_input == "":
            os.system('clear')
            break
        else:
            print("")
    
    #prompt user for starting number range, has logic to prevent any input but a number in specified range
    while True: 
        start_number= input("Enter a whole number between 100 and 10000.\n")
        if start_number.isdigit() is True:
            if int(start_number) >= 100 and int(start_number) <= 10000:
                current_roll= int(start_number)
                player_roll(current_roll)
                break
        else:
            print("I saaaiiiiddd....")

#player_roll class to handle when it is player's turn to roll. Also controls flow of logic at user's press of 'enter'. Passes to computer if roll is not 1.
def player_roll(current_roll):
    gen_num= random.randint(1, int(current_roll))
    gen_num= str(gen_num)
    print(f"You rolled {gen_num}.")
    if int(gen_num) == 1:
        print("YOU ROLLED THE DEATH ROLL. GAMBLER_BOT_5000 WINS! BETTER LUCK NEXT TIME.")
    else:
        current_roll= int(gen_num)
        change_turn_check= input("Press 'enter' to pass the roll to GAMBLER_BOT_5000.\n")
        while True:
            if change_turn_check == "":
                gambler_bot_5000_roll(current_roll)
                break
            else:
                change_turn_check= input("Press 'enter' when you are ready to pass the roll to GAMBLER_BOT_5000.\n")

#computer_roll class to handle computer's rolls and pass back to player if roll is not 1
def gambler_bot_5000_roll(current_roll):
    gen_num= random.randint(1, int(current_roll))
    gen_num= str(gen_num)
    print(f"GAMBLER_BOT_5000 rolled {gen_num}.")
    if int(gen_num) == 1:
        print("GAMBLER_BOT_5000 HAS ROLLED THE DEATH ROLL. YOU WIN - THANK YOU FOR PLAYING.")
        time.sleep(2)
        print("GAMBLER_BOT_5000 WILL SELF-DESTRUCT IN 5...")
        time.sleep(1)
        print("4...")
        time.sleep(1)
        print("3...")
        time.sleep(2)
        print("Just kidding. Please come back and let me win.")
    else:
        current_roll= int(gen_num)
        player_roll(current_roll)

if __name__ == "__main__":
    main()


