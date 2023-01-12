#!/usr/bin/env python3
#create failed login attempts counter
loginfail= 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as log_file:
    for line in log_file:
        if "- - - - -] Authorization failed" in line:
            loginfail += 1
    print("The number of failed login attempts is: ", loginfail)
