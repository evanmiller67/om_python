#/usr/bin/env python3 
"""
title: exercises/9_while_loops.py
author: exm5840
date(created): 2019-09-18 12:55:51 EDT
date (updated): 2019-09-18 12:55:51 EDT
"""
import matplotlib.pyplot as plt
import random

## 2.1 Modify the for-loop from the `apply` section and stop when you find a '4'
# a = []  ## create an empty list
# choices = [1,2,3,4,5,6]
# x = random.choice(choices)  ## choose a random choice of either 1, 3 or 10 to a (the list)
# a += [x]
# while a[-1] != 4:
#     x = random.choice(choices)  ## choose a random choice of either 1, 3 or 10 to a (the list)
#     a += [x]
# plt.hist(a, range=(1, 6), align='mid')  ## options for aligning are 'mid', 'left', and 'right'
# plt.show()
# print('\n----------------')

## 2.2 Guessing game
## Create a program that will ask the user to guess a random number between 1 - 20. Keep asking the user until they guess it correctly.
# inp = 0
# winrar = random.choice(range(1,21))
# while inp != winrar:
#     inp = int(input("Guess a number between 1 and 20: "))
# print("That was it!")
# print('\n----------------')

## 2.3. Credit Limit
## Create a program that has the user first set a value for their bank account balance. Then ask the user to enter a new amount that they just spent and subtract this value from the total. Once they reach a zero balance, print out "All out of money!". If they reach a negative balance, raise a RuntimeError.
# balance = int(input(">>> Enter beginning balance: "))
# while balance > 0:
#     debit = int(input(">>> Enter debit amount: "))
#     balance -= debit
#     print("Current balance: {}".format(balance))
# if balance < 0:
#     raise RuntimeError('You spent too much')

## 2.4. Pig Latin
## Create a function called pig_latin that receives a String called pig and return pig in pig latin.
## Here’s how to translate the English word into the Pig Latin word:
## If there are no vowels in englishWord, then pigLatinWord is just englishWord + "ay". (There are ten vowels: 'a', 'e', 'i', 'o', and 'u', and their uppercase counterparts. y is not considered to be a vowel for the purposes of this assignment, i.e. my becomes myay, why becomes whyay, etc.)
## Else, if englishWord begins with a vowel, then pigLatinWord is just englishWord + "yay"
## Otherwise (if englishWord has a vowel in it and yet doesn’t start with a vowel), then pigLatinWord is end + start + "ay", where end and start are defined as follows:
##     Let start be all of englishWord up to (but not including) its first vowel.
##     Let end be all of englishWord from its first vowel on.
def pig_latin(englishWord):
    vowels = ['a','e','i','o','u']
    pigLatinWord = ''
    if len(set(list(englishWord)).intersection(set(vowels))) == 0:
        pigLatinWord = englishWord + "ay"
    elif len(set(vowels).intersection(set(list(englishWord[0])))) == 1:
        pigLatinWord = englishWord + "yay"
    else:
        idx = 0
        start = ''
        end = ''
        found_vowel = False
        while idx < len(englishWord):
            if not found_vowel:
                if len(set(vowels).intersection(set(list(englishWord[idx])))) == 1:
                    found_vowel = True
                    idx -=1
                else:
                    start += englishWord[idx]
            else:
                end = end + englishWord[idx]
            idx +=1
        pigLatinWord = end + start + "ay"
    return pigLatinWord

def main():
    words = ["my", "why", "foobar", "apple", "banana"]
    for word in words:
        print(pig_latin(word))

if __name__ == '__main__':
    main();
