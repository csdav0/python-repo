#!/usr/bin/env python3
## create file object in "r"ead mode
userfilename = input("What is the name of the file you'd like to load?")

with open(userfilename,"r") as vlanconfig:
    configlist= vlanconfig.readlines()

print(configlist)
print("Total number of lines in configlist= ", str(len(configlist)))
