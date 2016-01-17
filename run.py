#!/usr/bin/env python3
import re
from codec import morse
import sys

if "-h" in sys.argv or "--help" in sys.argv or len(sys.argv) < 2:
    print ("Just run this program")
    exit(-1)

def main():

    data_type = input('Input your code type eg:Morse \n')

    if data_type == 'morse' or data_type == 'Morse' or data_type == ‘摩丝’:
        msg = input('Type msg \n')
        r = morse.decode_morse(msg)
        print (r)
    elif data_type == 'budda' or data_type == '佛经' or data_type == 'Budda':
        print ("Please go to http://www.keyfc.net/bbs/tools/tudoucode.aspx")
    else:
        print("We don't support other type yet \n")


main()
