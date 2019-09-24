#/usr/bin/env python3 
"""
title: conditional_statements_main.py
author: exm5840
date(created): 2019-09-17 14:41:51 EDT
date (updated): 2019-09-17 14:41:51 EDT
"""

## Declare global variable name for use in all functions
name = input('Enter your name: ')


## Define function to check if name contains a vowel
def has_vowel():
    if set('aeiou').intersection(name.lower()):
        print('Your name contains a vowel.')
    else:
        print('Your name does not contain a vowel.')


## Iterate over letters in name string
def print_letters():
    for letter in name:
        print(letter)


## Define main method that calls other functions
def main():
    has_vowel()
    print_letters()


## Execute main() function
if __name__ == '__main__':
    main()
