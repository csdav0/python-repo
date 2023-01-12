#!/usr/bin/env python3
#explore read
configfile = open("vlanconfig.cfg","r")
print(configfile.read())
configfile.close()

#explore readlines
configfile = open("vlanconfig.cfg","r")
configlist= configfile.readlines()
print(configlist)

for line in configlist:
    line = line.strip()
    print(line)

configfile.close()
