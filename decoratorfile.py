#/usr/bin/env python3
"""
title: decoratorfile.py
author: exm5840
date(created): 2019-09-20 07:51:26 EDT
date (updated): 2019-09-20 07:51:26 EDT
"""

#/decoratorfile.py
def my_decorator(some_function):
    def wrapper():
        num = 10
        if num == 10:
            print("Yes!")
        else:
            print("No!")
        some_function()
        print("Something is happening after some_function() is called.")
    return wrapper
#/decoratorfile.py -------------------------------------------------------
