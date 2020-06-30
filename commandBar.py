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
        def null_decorator(ob):
            # global os
            return ob

        if sys.version_info >= (3, 2, 0):
            import functools
            my_cache_decorator = functools.lru_cache( maxsize=4096 )
        else:
            my_cache_decorator = null_decorator

        start_dir = path.normpath(path.abspath( sys.argv[1] ) ) if len( sys.argv ) > 1 else '.'

        @my_cache_decorator
        def get_dir_size(start_path='.'):
            total_size = 0
            if 'scandir' in dir(  ):
                # using fast 'os.scandir' method (new in version 3.5)
                for entry in scandir( start_path ):
                    if entry.is_dir( follow_symlinks=False ):
                        total_size += get_dir_size( entry.path )
                    elif entry.is_file( follow_symlinks=False ):
                        total_size += entry.stat().st_size
            else:
                # using slow, but compatible 'os.listdir' method
                for entry in listdir( start_path ):
                    full_path = path.abspath( path.join( start_path, entry ) )
                    if path.islink( full_path ):
                        continue
                    if path.isdir( full_path ):
                        total_size += get_dir_size( full_path )
                    elif path.isfile( full_path ):
                        total_size += path.getsize( full_path )
            return total_size

        def get_dir_size_walk(start_path='.'):
            total_size = 0
            for dirpath, dirnames, filenames in os.walk( start_path ):
                for f in filenames:
                    fp = path.join( dirpath, f )
                    total_size += os.path.getsize( fp )
            return total_size

        def bytes2human(n, format='%(value).0f%(symbol)s', symbols='customary'):

            SYMBOLS = {
                'customary': ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y'),
                'customary_ext': ('byte', 'kilo', 'mega', 'giga', 'tera', 'peta', 'exa',
                                  'zetta', 'iotta'),
                'iec': ('Bi', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi', 'Yi'),
                'iec_ext': ('byte', 'kibi', 'mebi', 'gibi', 'tebi', 'pebi', 'exbi',
                            'zebi', 'yobi'),
            }
            n = int( n )
            if n < 0:
                raise ValueError( "n < 0" )
            symbols = SYMBOLS[symbols]
            prefix = {}
            for i, s in enumerate( symbols[1:] ):
                prefix[s] = 1 << (i + 1) * 10
            for symbol in reversed( symbols[1:] ):
                if n >= prefix[symbol]:
                    value = float( n ) / prefix[symbol]
                    return format % locals()
            return format % dict( symbol=symbols[0], value=n )

        if __name__ == '__main__':
            dir_tree = {}
            ### version, that uses 'slow' [os.walk method]
            # get_size = get_dir_size_walk
            ### this recursive version can benefit from caching the function calls (functools.lru_cache)
            get_size = get_dir_size

            for root, dirs, files in walk( start_dir ):
                for d in dirs:
                    dir_path = path.join( root, d )
                    if path.isdir( dir_path ):
                        dir_tree[dir_path] = get_size( dir_path )

            for d, size in sorted( dir_tree.items(), key=operator.itemgetter( 1 ), reverse=True ):
                print( '%s\t%s' % (bytes2human( size, format='%(value).2f%(symbol)s' ), d) )

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