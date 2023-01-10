#!/usr/bin/env python3

def main():
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n")
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n")
    marvelchars= {
    "Starlord": {"real name": "peter quill", "powers": "dance moves", "archenemy": "Thanos"},
    "Mystique": {"real name": "raven darkholme", "powers": "shape shifter", "archenemy": "Professor X"},
    "Hulk": {"real name": "bruce banner", "powers": "super strength", "archenemy": "adrenaline"}
    }
    print(char_name.title() + "'s " + char_stat.lower() + " is: " + marvelchars[char_name.title()][char_stat.lower()].title())

main()
