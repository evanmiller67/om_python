#/usr/bin/env python3 
"""
title: exercises/7_3_sets.py
author: exm5840
date(created): 2019-09-17 13:36:01 EDT
date (updated): 2019-09-17 13:36:01 EDT
"""

# Create a function called remove_duplicates that takes in an iterable as a parameter and returns a set without any duplicates.
# Call (invoke) the function like the example shown below:
#    print(remove_duplicates('MISSISSIPPI'))

def remove_duplicates(i):
    return set(i)


print(remove_duplicates('MISSISSIPPI'))


# Create a function called finding_vowels that takes in a string and returns True if there are any vowels in the word and False if there are not any vowels.
# Call (invoke) the function like the example shown below:
#         print(finding_vowels('mississippi'))
def finding_vowels(i):
    return len({'a','e','i','o','u'}.intersection(i.lower())) > 0

print(finding_vowels('mississippi'))
print(finding_vowels('qwrtplkjhgfds'))
