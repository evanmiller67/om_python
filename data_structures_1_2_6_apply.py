#/usr/bin/env python3 
"""
title: data_structures_1_2_6_apply.py
author: exm5840
date(created): 2019-09-17 12:20:51 EDT
date (updated): 2019-09-17 12:20:51 EDT
"""


# Create a tuple called vowels that stores all of the vowels of the alphabet: a, e, i, o, u
vowels = ('a','e','i','o','u')

# Print out the length of the vowels
print(len(vowels))

# Print out the 3rd vowel in vowels
print(vowels[2])

# Print out the 1st - 4th vowel (Use both the start and stop)
print(vowels[0:4])

# Print out the 1st - 4th vowel (Do not use both the start and stop)
print(vowels[:4])

# Print out e and o using slicing
print(vowels[1::3])

# Change the last vowel to y. What happens?
# Tuples are immutable... so: 
tmp_vowel = list(vowels)
tmp_vowel[-1]='y'
vowels=tuple(tmp_vowel)
print(vowels)
# After you are done with the above step, comment it out
