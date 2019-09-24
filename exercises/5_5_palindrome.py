#/usr/bin/env python3 
"""
title: 5_5_palindrome.py
author: exm5840
date(created): 2019-09-17 09:40:43 EDT
date (updated): 2019-09-17 09:40:43 EDT
"""

import re

def is_palindrome(message):
    for i in range(len(message)):
        if (message[i] != message[len(message) - 1 + i*-1]):
            return False
    return True

def lower_and_strip(message):
    return re.sub(r'[^a-z]', '', message.lower())

str_input = input("Enter any string: ")

print("Formatted string: '{0}'".format(lower_and_strip(str_input)))
print("Is a palindrome?  '{0}'".format(is_palindrome(lower_and_strip(str_input))))
