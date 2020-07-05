# This program works as a simple command bar using python
from __future__ import print_function

import sys
import operator
from os import *
from pathlib import *

userInput = "none"
originalUserInput="none"
def display():
    global userInput
    global originalUserInput
    print("--------------This is a python command bar--------------\n")
    print("To show the current directory enter 'pwd'\n")
    print("To go to a subdirectory type 'cd+a space + the directory's name'ex:cd New folder\n")
    print("To go back to the parent directory type 'cd+..'\n")
    print("To see the content of a folder type 'ls'\n")
    print("To see the size of all files and folders under the current directory type 'du'\n")
    print("To remove the current directory type'rm'\n")
    print("To see the tree from of file and folders of this directory type ''tree\n")
    print("To exit this command bar type 'x'\n")

stillGoOn=True
while stillGoOn:
    def parentDir():
        global userInput
        myDir = getcwd()
        parentDir=Path(myDir).parent
        chdir(parentDir)
        print(parentDir)
        main()


    def pwd():
        global userInput
        currentDir=getcwd()
        print(currentDir)
        main()


    def subDir():
        global userInput
        global originalUserInput
        myDir = getcwd()
        content=walk(myDir).__next__()[1]
        userInput = originalUserInput[3:]
        myDir = getcwd()
        if userInput in content:
            chdir( myDir + "\\" + userInput )
            print( getcwd() )
            main()
        else:
            print("There is no folder by that name please try again")
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
                            return userInput
                elif mylist[0] == 2:
                    userInput = "cdSub"
                    checkTrue = False

            elif userInput !="pwd" and userInput !="ls" and userInput !="du" and userInput !="x":
                print( "Unknown entry\nPlease try again" )
                userInput = input( ":>" )
            else:
                checkTrue = False
        return userInput


    def listOfContent():
        mydir = getcwd()
        entries = listdir( mydir )
        print( entries )
        for entry in entries:
            print( entry )
        main()

    def du():
        global size
        size = 0
        # this function finds the name of the current folder and extracts it from the path of the directory
        def getFolderNmae():
            global size
            global foldername
            dir = getcwd()
            mylist = []
            for i in range( len( dir ) ):
                if dir[i] == "\\":
                    mylist.append( i )
            foldername = dir[mylist[-1] + 1:]
            printFolder( foldername )
            return foldername

        def printFolder(foldername):
            global size
            myDir = getcwd()
            allFiles = walk( myDir ).__next__()[2]
            allFolderds = walk( myDir ).__next__()[1]
            if len( allFolderds ) == 0:
                return
            else:
                for folder in allFolderds:
                    # currentDir = getcwd()
                    chdir( myDir + "\\" + folder )
                    currentDir = getcwd()

                    allFiles = walk( currentDir ).__next__()[2]
                    for files in allFiles:
                        size += path.getsize( files )
                    allFolderds = walk( currentDir ).__next__()[1]
                    # print( "the current directory is :" )
                    # print( currentDir )
                    # print( "the list of all files inside this folder is:" )
                    # print( allFiles )
                    # print( "the list of all folders inside the current folder is:" )
                    # print( allFolderds )
                    getFolderNmae()
            return size

        getFolderNmae()
        sizeInMb=size/1024
        print("The size of this directory is equal to %s bytes or %.2f MB "%(size,sizeInMb))
        main()



    def main():
        global userInput
        global originalUserInput
        global stillGoOn
        userInput = input( ":>" )
        originalUserInput = userInput
        checkUserInput()
        if userInput=="pwd":
            pwd()
        elif userInput=="cdSub":
            subDir()
        elif userInput=="cdParent":
            parentDir()
        elif userInput=="ls":
            listOfContent()
        elif userInput=="du":
            du()

        elif userInput=="x":
            stillGoOn=False


    display()
    main()