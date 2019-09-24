#/usr/bin/env python3 
"""
title: exercises/9_for_loops.py
author: exm5840
date(created): 2019-09-17 16:52:54 EDT
date (updated): 2019-09-17 16:52:54 EDT
"""

# 1.1 create string
letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']
def create_string():
    stringy=''
    for l in letters:
        stringy = stringy + l
    return stringy

print(create_string())


# 1.2 filling tickets
# Define a function fill_ticket() that will ask a user five times to insert a number. (Use a loop to do this). After every time they answer, their newest answer is placed at the end of a list. This list is then returned.

def fill_ticket():
   nums = []
   for x in range(5):
      nums.append(int(input("Gimme a number: ")))
   return nums
# print(fill_ticket())

# 1.3 Finding matches
# The winning combination of this lottery is chosen by picking five numbers. 
# Define a function matches(ticket, winners) that takes two lists and returns an integer that says how many numbers the two lists are in the exact same position.
# Copy and paste the code below at the bottom of your main function to test out your matches(ticket, winners) functions.
def matches(ticket, winners, *args, **kvargs):
    matches = 0
    for i in range(len(ticket)):
        if ticket[i] == winners[i]:
            matches+=1
    return matches

# 1.4 Caesar Cipher
cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}
def caesar_cipher(cipher_text):
    decoded = ""
    for l in range(len(cipher_text)):
        try:
            decoded = decoded + cipher_key[cipher_text[l]]
        except KeyError:
            decoded = decoded + cipher_text[l]
    return decoded

def main():
    guesses = fill_ticket()

    winners = [1, 2, 3, 4, 5]
    print(matches(guesses, winners))
    print(caesar_cipher("pnrfne pvcure? v zhpu cersre pnrfne fnynq!"))

if __name__ == '__main__':
    main()
