#!/usr/bin/env python3
import re
from codec import morse
import sys

def main():

    data_type = input('Input your code type eg:Morse \n')

    msg = input('Type msg \n')

    if data_type == 'morse':
        r = morse.decode_morse(msg)
        print (r)
    elif data_type == 'Morse':
        r = morse.decode_morse(msg)
        print (r)
    else:
        print("We don't support other type yet \n")


main()
