#/usr/bin/env python3 
"""
title: exercises/6_2_average.py
author: exm5840
date(created): 2019-09-17 10:38:40 EDT
date (updated): 2019-09-17 10:38:40 EDT
"""

# Define another function, avg_numbers that takes three parameters, that returns the average of three numbers.
def avg_numbers(*args):
    return sum(args) / len(args)

# Place the following at the bottom of your code, outside of the function:
print(avg_numbers(4, 7, 8))
