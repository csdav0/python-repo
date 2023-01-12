#!/usr/bin/env python3
#create counter for successful logins
loginsuccess= 0

with open("/home/student/mycode/attemptlogin/keystone.common.wsgi","r") as log_file:
    for line in log_file:
        if "-] Authorization failed" in line:
            loginsuccess += 1
    print("The number of successful login attempts is: ", loginsuccess)
