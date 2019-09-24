#/usr/bin/env python3 
"""
title: loops_apply.py
author: exm5840
date(created): 2019-09-17 15:26:16 EDT
date (updated): 2019-09-17 15:26:16 EDT
"""

# Create a for loop that prints off the numbers 89, 41, 73, and 90 - each on their own line
for x in [89,41,73,90]:
    print(x)
print('----------------')
# Create a for loop that prints off the numbers 5 up-to but not including 15
for x in range(5,15):
    print(x)
print('----------------')
# Create a for loop that prints off the numbers 100 to 200 by 10’s
for x in range(100,201,10):
    print(x)
print('----------------')
# Create a for loop that prints off the numbers from 80 to 32 by 8’s
for x in range(80,32,-8):
    print(x)
print('----------------')
# Create a for loop that prints off the word Alright three times.
for x in range(3):
    print("Alright", end = " ")
print('\n----------------')
# Create a for loop that creates the following image:
# *
# **
# ***
# ****
# *****
for x in range(1,6):
    print("*"* x)
print('\n----------------')

# Using range, create a for loop that prints off the numbers 1, 4, 9, 16.
for x in range(1,5):
    print(x**2)
print('\n----------------')

# 8. Create a for loop that goes through a list and counts the number of even and odd numbers. Use the following list as an example to work with: numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Output:
#   Even numbers: 4
#   Odd numbers: 5
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even=0
odd=0
for x in numbers:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1
print("Even numbers: {}".format(even))
print("Odd numbers:  {}".format(odd))
print('\n----------------')

# 9. Change the following starter code to choose a random number between 1 and 6 100 times and display it on the histogram:
import matplotlib.pyplot as plt
import random

a = []  ## create an empty list
choices = [1,2,3,4,5,6]
for roll in range(100):
    x = random.choice(choices)  ## choose a random choice of either 1, 3 or 10 to a (the list)
    a += [x]
plt.hist(a, range=(1, 10), align='right')  ## options for aligning are 'mid', 'left', and 'right'
plt.show()
