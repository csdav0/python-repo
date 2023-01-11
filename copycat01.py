#!/usr/bin/env python3

#import additional modules for this exercise
import shutil
import os

def main():
    #starts from working directory
    os.chdir("/home/student/mycode/")

    #copy the fileA to fileB (or rename the file if not providing paths)
    shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

    #copys the entire directory A and creates a new one with second string provided
    os.system("rm -rf /home/student/mycode/5g_research_backup/")
    shutil.copytree("5g_research/", "5g_research_backup/")

if __name__ == "__main__":
    main()
