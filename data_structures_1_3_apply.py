#/usr/bin/env python3 
"""
title: data_structures_1_3_apply.py
author: exm5840
date(created): 2019-09-17 13:26:18 EDT
date (updated): 2019-09-17 13:26:18 EDT
"""

# Create a set called set1 with a string with a value of aaabcccccdd (Use the set() notation). Print out the values of the set after you create it
set1 = set('aaabccccdd')
print(set1)

# Create a set called set2 with a string with a value of "b", "a", "t", "s", "c", "a", "t", "s" (Use the {value1} notation). Print out the values of the set after you create it
set2 = {"b", "a", "t", "s", "c", "a", "t", "s"}
print(set2)

# Print out the number of elements in set1
print(len(set1))

# Print out what set1 and set2 have in common
print(set1.intersection(set2))

# Print out what values that set1 has that set2 does not have
print(set1.difference(set2))

# Print out the combination of set1 and set2
print(set1.union(set2))

# Add the letter e to set1. Print out the new set
set1.add("e")
print(set1)

# Remove the letter b from set2. Print out the new set
set2.remove("b")
print(set2)
