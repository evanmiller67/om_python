#/usr/bin/env python3 
"""
title: deco-functools-wraps.py
author: exm5840
date(created): 2019-09-24 11:29:36 EDT
date (updated): 2019-09-24 11:29:36 EDT
"""

# When you use a decorator, you’re replacing one function with another. In this example f() is replaced with the function with_logging().
'''from my_decorator import my_decorator

@my_decorator
def the_decorated_func():
  print("Hi from the decorated function!")

print(the_decorated_func)
the_decorated_func()
'''

# Wrapping our decorator this way allows docstring and naming from the main func to flow to the caller
from functools import wraps
def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging

@logged
def f(x):
   """does some math"""
   return x + x * x

print(f(10))  # prints 'f'
print(f.__name__)  # prints 'f'
print(f.__doc__ ) # prints 'does some math'
