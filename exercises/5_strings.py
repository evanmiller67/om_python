#/usr/bin/env python3 
"""
title: strings.py
author: exm5840
date(created): 2019-09-16 14:15:55 EDT
date (updated): 2019-09-16 14:15:55 EDT
"""
import re

#string = input("Enter a character: ")
#if (len(string) > 1):
#    print("You entered more than 1 character. Exiting...")
#    exit()
#
#character = re.search("[a-zA-Z]", string)
#if character:
#    print("That was a character: '{0}'".format(character.group(0)))
#else: 
#    print("Not a character:      '{0}'".format(string))

def short_hand(message):
    """
    replace these four words: "and" with "&", "too" with "2", "you" with "U", and "for" with "4".
    remove all vowels ('a', 'e', 'i', 'o', 'u', whether lowercase or uppercase). Be careful on removing U!
    """
    words = message.split(" ")
    for i in range(len(words)):
        words[i] = words[i].replace("and", "&").replace("too", "2").replace("for", "4")
        words[i] = re.sub("[Yy]ou", "U", words[i])
        words[i] = re.sub("[aeiouAEIO]", "", words[i])
        if ( len(words[i]) > 1 ):
            words[i] = re.sub("U","", words[i])
    print(words)
    return " ".join(words)

print(short_hand("Thank you for that! You are too sweet and kind!"))
