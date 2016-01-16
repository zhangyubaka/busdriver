#!/usr/bin/env python3

letter_to_morse = {
    "a" : ".-",     "b" : "-...",     "c" : "-.-.",
    "d" : "-..",    "e" : ".",        "f" : "..-.",
    "g" : "--.",    "h" : "....",     "i" : "..",
    "j" : ".---",   "k" : "-.-",      "l" : ".-..",
    "m" : "--",     "n" : "-.",       "o" : "---",
    "p" : ".--.",   "q" : "--.-",     "r" : ".-.",
    "s" : "...",    "t" : "-",        "u" : "..-",
    "v" : "...-",   "w" : ".--",      "x" : "-..-",
    "y" : "-.--",   "z" : "--..",     " " : "/"
}

morse_to_letter = {morse: letter for letter, morse in letter_to_morse.items()}

def decode_morse(morse_code):
    return ''.join(morse_to_letter[code] for code in morse_code.split())

def encode_morse(text):
    return ' '.join(letter_to_morse[letter] for letter in text)
