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
userInput = "none"
originalUserInput="none"
def display():
    global userInput
    global originalUserInput
    print("--------------This is a python command bar--------------\n")
    print("To show the current directory enter 'pwd'\n")
    print("To go to a subdirectory type 'cd+the directory's name'\n")
    print("To go back to the parent directory type 'cd+..'\n")
    print("To see the content of a folder type 'ls'\n")
    print("To see the size of all files and folders under the current directory type 'du'\n")
    print("To exit this command bar type 'x'\n")
    userInput = input( ":>" )
    originalUserInput=userInput

def parentDir():
    global userInput
    myDir = getcwd()
    parentDir=Path(myDir).parent
    print(parentDir)
    main()


def pwd():
    global userInput
    currentDir=getcwd()
    print(currentDir)
    userInput = input(":>")

def subDir():
    global userInput
    global originalUserInput
    userInput = originalUserInput[3:]

    myDir = getcwd()
    chdir( myDir + "\\" + userInput )
    print( getcwd() )
    main()

def checkUserInput():
    global userInput
    mylist = []
    for i in range( len( userInput ) ):
        if userInput[i] == " ":
            mylist.append( i )
    if len( mylist ) == 0:
        mylist.append( 0 )

    checkTrue = True
    while checkTrue:
        if userInput[0] == "c" and userInput[1] == "d":
            if mylist[0] != 2:
                if len( userInput ) != 4:
                    print( "Unknown entry\nPlease try again" )
                    userInput = input( ":>" )
                else:
                    if userInput[2] != "." and userInput[3] != ".":
                        print( "Unknown entry\nPlease try again" )
                        userInput = input( ":>" )
                    else:
                        userInput = "cdParent"
                        checkTrue = False
                        print( userInput )
            elif mylist[0] == 2:
                userInput = "cdSub"
                checkTrue = False

        elif userInput !="pwd" or userInput !="ls" or userInput !="du" or userInput !="x":
            print( "Unknown entry\nPlease try again" )
            userInput = input( ":>" )
        else:
            checkTrue = False
    return userInput


def main():
    display()
    checkUserInput()
    if userInput=="pwd":
        pwd()
    elif userInput=="cdSub":
        subDir()
    elif userInput=="cdParent":
        parentDir()

main()