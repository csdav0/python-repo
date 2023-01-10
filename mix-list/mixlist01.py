#!/usr/bin/env python3
#create a list
my_list = [ "192.168.0.5", 5060, "UP" ]

#print the item at each index
print("The first item in the list (IP):", my_list[0])
print("The second item in the list (port):", my_list[1].__str__())
print("The third item in the list (state):", my_list[2])

#list of ips
iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]
onlyip = [iplist[3], iplist[4]]
print(onlyip)
