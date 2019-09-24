#/usr/bin/env python3
"""
title: deco-real-world.py
author: exm5840
date(created): 2019-09-20 07:57:47 EDT
date (updated): 2019-09-20 07:57:47 EDT
"""

# Real world example
import time


def timing_function(some_function):

    """
    Outputs the time a function takes
    to execute.
    """

    def wrapper():
        t1 = time.time()
        some_function()
        t2 = time.time()
        return "Time it took to run the function: " + str((t2 - t1)) + "n"
    return wrapper


@timing_function
def my_function():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print("Sum of all the numbers: " + str((sum(num_list))))


print(my_function())
