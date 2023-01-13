#!/usr/bin/env python3

def main():
    with open("dracula.txt","r") as text_of_dracula:
        vamp_count= 0
        with open("vampytimes.txt","a") as vampfileout:
            for line in text_of_dracula:
                if "vampire" in line:
                    vamp_count+= 1
                    print(line, file=vampfileout)
                elif "Vampire" in line:
                    vamp_count+= 1
                    print(line, file=vampfileout)
    print(f"There are {vamp_count} lines containing the word 'vampire'")
    
if __name__ == "__main__":
    main()
