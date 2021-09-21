#!/usr/bin/python

# -*- coding: utf-8 -*-

import sys
import os

def wc(filename):
    """Function prints number of lines, words and characters in given file

        Args:
            filename: the name of the file that shoud be read

        Rasies:
            OSError: An error occured trying to read file
    """
    try:
        file=open(filename, "r")
    except OSError as e:
        print("Error: cant open file")
        print(e)
        return
    data=file.read()
    lines=data.split("\n")
    words=[]
    for line in lines:
        for word in line.split(" "):
            words.append(word)
    numLines=len(lines)
    numWords=len(words)
    numChars=sum(len(word) for word in words)
    print(str(numLines)+"\n"+str(numWords)+"\n"+str(numChars)+"\n"+str(filename)+"\n")

if __name__=="__main__":
    """Main

        Checks if the right number of arguments i s given
        If argument is *: wc for all files in current dir
        If argument is *.py: wc for all python files in directory
        Else: try to wc for the given argument (filename)
    """
    arguments=sys.argv
    if (len(arguments) < 2):
        print("Wrong number of arguments.")
        sys.exit()
    arguments.pop(0)
    for arg in arguments:
        wc(arg)