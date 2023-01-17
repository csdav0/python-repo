#!/usr/bin/env python3

import requests

def main():
    pokenum= input("Pick a number between 1 and 151!\n>")
    pokeapi= requests.get("https://pokeapi.co/api/v2/pokemon/" + pokenum).json()

    print(pokeapi)
    
    sprite= pokeapi["sprites"]["front_default"]
    print(sprite)

    moves= pokeapi["moves"]
    for move in moves:
        print(f"{move['move']['name']}")
    
    my_count= 0
    for game in pokeapi["game_indices"]:
        my_count += 1

    print(str(my_count))

    print(len(pokeapi["game_indices"]))


    with open("dragonite.png", "wb") as dragonite:
        pic= requests.get(sprite, stream=True)
        ##may want to come back and digest the code below. look up documentation on Requests library and the .iter_content command
        for chunk in pic.iter_content(chunk_size=128):
            dragonite.write(chunk)
main()
