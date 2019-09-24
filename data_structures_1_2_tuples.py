#/usr/bin/env python3 
"""
title: data_structures_1_2_tuples.py
author: exm5840
date(created): 2019-09-17 12:08:55 EDT
date (updated): 2019-09-17 12:08:55 EDT
"""

# Tuples are immutable
emp_rank = ("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")
print(emp_rank)

# length
print(len(emp_rank))

# indexing
print(emp_rank[0])
print('The current employee has the position of ' + emp_rank[2])


# slicing
print(emp_rank[1: 3])
print(emp_rank[: 3])
print(emp_rank[3: ])
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(numbers[1: 9: 2])
print(numbers[: : 3])
print(numbers[: : -2])

# concatenating
first_names = ("Noelle", "Tereza", "Raelin", "Linus")
last_names = ("Blossom", "Chrissy", "Grover", "Devin")
print(first_names + last_names)

# Tuples vs Lists
# emp_rank = ("Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal")
# emp_rank[0] = "Newbie Software Engineer"
# TypeError: 'tuple object does not support item assignment'

print(list(emp_rank))
print(emp_rank)
