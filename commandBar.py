# This program works as a simple command bar using python

from os import *
from pathlib import *
# print(getcwd())
# chdir("D:\MEHRZAD\Programing\python\python-command-bar01\sahand")
# print(getcwd())
# chdir("D:\MEHRZAD\Programing\python\python-command-bar01\zad")
# print(getcwd())
#
# userInput="sahand"
# chdir("D:\MEHRZAD\Programing\python\python-command-bar01\\"+userInput)
# print(getcwd())
# myDir=getcwd()
#
# print(myDir)
# reza=Path(myDir).parent
# print("_------------")
# print(reza)
def display():
    print("--------------This is a python command bar--------------\n")
    print("To show the current directory enter 'pwd'\n")
    print("To go to a subdirectory type 'cd+the directory's name'\n")
    print("To go back to the parent directory type 'cd+..'\n")
    print("To see the content of a folder type 'ls'\n")
    print("To see the size of all files and folders under the current directory type 'du'\n")
    print("To exit this command bar type 'x'\n")


display()
userInput=input(":>")
a=userInput[0]+userInput[1]
# print(a)
# print(type(a))
checkTrue=True
while checkTrue:
    if userInput!="pwd" or userInput!="ls" or userInput!="du" or userInput!="x" or a!="cd":
        print("UNKNOWN COMMAND\n please try again")
        userInput = input( ":>" )



