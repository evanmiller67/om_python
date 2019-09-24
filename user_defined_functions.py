#/usr/bin/env python3 
"""
title: user_defined_functions.py
author: exm5840
date(created): 2019-09-17 09:56:01 EDT
date (updated): 2019-09-17 09:56:01 EDT
"""

# 1.1 intro to functions
def subtract_total():
    total = 10000
    my_share = 20000
    print(my_share - total)

# 1.1.1 calling functions
def while_loop():
    x = True
    count = 0
    while x and count < 10:
        print("x exists")
        count++
while_loop()

# 1.2 Parameters
def hello(name):
    print("Hello " + name)
hello("Emily")

def has_vowel(word):
    ## Check whether name has a vowel
    if set('aeiou').intersection(word.lower()):
        print(word, 'contains a vowel.')
    else:
        print(word, 'does not contain a vowel.')

has_vowel("supercalifragilisticexpialidocious")
has_vowel("why")
has_vowel("hey")

# 1.2.1 Keyword args
def profile_info(username, followers):
    print("Username: " + username)
    print("Followers: " + str(followers))

## Call function with parameters assigned as above
profile_info("sammyshark", 945)

## Call function with keyword arguments
profile_info(username="AlexAnglerfish", followers=342)

## Change order of parameters
profile_info(followers=820, username="cameron-catfish")

# 1.2.2 Default args
def profile_info(username, followers=1):
    print("Username: " + username)
    print("Followers: " + str(followers))

profile_info(username="JOctopus")
profile_info(username="sammyshark", followers=945)

# 1.3 `return`
def square(x):
    y = x ** 2
    return y

result = square(3)
print(result)

result = square(3) * 2
print(result)
