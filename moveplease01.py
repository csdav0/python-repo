#!/usr/bin/env python3

#module imports needed for this exercise
import shutil
import os

def main():
    #force python to start from home directory
    os.chdir('/home/student/mycode/')

    #move file to folder
    shutil.move('raynor.obj', 'ceph_storage/')

    #prompt for new name to rename a file
    xname= input("what is the new name for kerrigan.obj?")
    #rename file w provided name
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

if __name__ == "__main__":
    main()
