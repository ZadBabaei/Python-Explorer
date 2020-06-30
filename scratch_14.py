from os import *
userInput = "none"
originalUserInput="none"
def subDir():
    global userInput
    global originalUserInput
    userInput=originalUserInput[3:]

    myDir = getcwd()
    chdir(myDir+"\\"+userInput)
    print(getcwd())

    userInput = input( ":>" )

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

        elif userInput!="pwd" or userInput!="ls" or userInput!="du" or userInput!="x" :
            print( "Unknown entry\nPlease try again" )
            userInput = input( ":>" )
        else:
            checkTrue = False
    return userInput

def main():
    global userInput
    global originalUserInput
    userInput = input( ":>" )
    originalUserInput=userInput
    checkUserInput()
    subDir()

main()