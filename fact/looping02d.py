#!/usr/bin/env python3

with open("dnsservers.txt", "r") as dnsfile:
    #loop thru lines of file and sort them to .com or .org
    for server in dnsfile:
        #strip carriage returns
        server= server.rstrip("\n")
        if server.endswith(".org"):
            with open("org-domain.txt", "a") as orgdomains:
                orgdomains.write(server + "\n")

        elif server.endswith(".com"):
            with open("com-domain.txt", "a") as comdomains:
                comdomains.write(server + "\n")

            
