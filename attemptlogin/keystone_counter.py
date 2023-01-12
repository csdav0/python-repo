#!/usr/bin/env python3
#create failed logins counter
loginfail= 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as keystone_file:
    keystone_file_lines = keystone_file.readlines()
    #now iterate over lines
    for line in keystone_file_lines:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
    print("The number of failed login attempts is: ", loginfail)
