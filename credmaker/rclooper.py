#!/usr/bin/env python3
#import standard library
import csv
with open("csv_users.txt","r") as csvfile:
    #counter for unique file names
    my_counter= 0
    for line in csv.reader(csvfile):
        my_counter += 1
        filename= f"admin.rc{my_counter}"

        #open each new filename and write the appropriate data
        with open(filename, "w") as rcfile:
            print("export OS_AUTH_URL=" + line[0], file=rcfile)
            print("export OS_IDENTITY_API_VERSION=3", file=rcfile)
            print("export OS_PROJECT_NAME=" + line[1], file=rcfile)
            print("export OS_PROJECT_DOMAIN_NAME=" + line[2], file=rcfile)
            print("export OS_USERNAME=" + line[3], file=rcfile)
            print("export OS_USER_DOMAIN_NAME=" + line[4], file=rcfile)
            print("export OS_PASSWORD=" + line[5], file=rcfile)

print("admin.rc files created!")
