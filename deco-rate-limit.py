#/usr/bin/env python3
"""
title: deco-rate-limit.py
author: exm5840
date(created): 2019-09-20 08:01:22 EDT
date (updated): 2019-09-20 08:01:22 EDT
"""

from time import sleep


def sleep_decorator(function):

    """
    Limits how fast the function is
    called.
    """

    def wrapper(*args, **kwargs):
        sleep(2)
        return function(*args, **kwargs)
    return wrapper


@sleep_decorator
def print_number(num):
    return num

print(print_number(222))

for num in range(1, 6):
    print(print_number(num))
