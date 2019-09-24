#/usr/bin/env python3
"""
title: decorators.py
author: exm5840
date(created): 2019-09-20 07:32:59 EDT
date (updated): 2019-09-20 07:32:59 EDT
"""

# In Python, functions are first-class objects. This means that functions can be passed around, and used as arguments, just like any other value (e.g, string, int, float).

def foo(bar):
    return bar + 1

print(foo)
print(foo(2))
print(type(foo))


def call_foo_with_arg(foo, arg):
    return foo(arg)

print(call_foo_with_arg(foo, 3))

# Because of the first-class nature of functions in Python, you can define functions inside other functions. Such functions are called nested functions.

def parent():
    print("Printing from the parent() function.")

    def first_child():
        return f"Printing from the first_child() function. With __name__: '{__name__}'"

    def second_child():
        return f"Printing from the second_child() function. With __name__: '{__name__}'"

    print(first_child())
    print(second_child())
parent()
# Whenever you call parent(), the sibling functions, first_child() and second_child() are also called AND because of scope, both of the sibling functions are not available (e.g., cannot be called) outside of the parent function.

# Returning functions with functions
def parent(num):
    def first_child():
        return "Hi, I am Emma"

    def second_child():
        return "Call me Liam"

    if num == 1:
        return first_child
    else:
        return second_child
# Vars will be functions that can be called...
first = parent(1)
second = parent(2)

## ....
print(first())
print(second())



############################################################
############################################################

# Example 1
def my_decorator(some_function):

    def wrapper():
        print("Something is happening before some_function() is called.")
        some_function()
        print("Something is happening after some_function() is called.")

    return wrapper


def just_some_function():
    print("Wheee!")


just_some_function = my_decorator(just_some_function)
just_some_function()
# Put simply, decorators wrap a function, modifying its behavior.


# Example 2
# This will only run between 7am and 10pm
from datetime import datetime

def not_during_the_night(func):
    def wrapper():
        if 7 <= datetime.now().hour < 22:
            func()
        else:
            pass  # Hush, the neighbors are asleep
    return wrapper

def say_whee():
    print("Whee!")

banana = not_during_the_night(say_whee)


# Syntactic Sugar
# The way you decorated say_whee() above is a little clunky. First of all, you end up typing the name say_whee three times. In addition, the decoration gets a bit hidden away below the definition of the function.

# Instead, Python allows you to use decorators in a simpler way with the @ symbol, sometimes called the “pie” syntax. The following example does the exact same thing as the first decorator example:

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")



## Now don't clutter up our other code by putting that decorator in a module...
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

#/deco-example.py
# from decoratorfile import my_decorator
#
#
# @my_decorator
# def just_some_function():
#     print("Wheee!")
#
# just_some_function()
#/deco-example.py --------------------------------------------------------


#########################################################################
#########################################################################
#########################################################################

#/deco-real-world.py -----------------------------------------------------
# Real world example
# import time
#
#
# def timing_function(some_function):
#
#     """
#     Outputs the time a function takes
#     to execute.
#     """
#
#     def wrapper():
#         t1 = time.time()
#         some_function()
#         t2 = time.time()
#         return "Time it took to run the function: " + str((t2 - t1)) + "n"
#     return wrapper
#
#
# @timing_function
# def my_function():
#     num_list = []
#     for num in (range(0, 10000)):
#         num_list.append(num)
#     print("Sum of all the numbers: " + str((sum(num_list))))
#
#
# print(my_function())
#/deco-real-world.py -----------------------------------------------------

#/deco-rate-limit.py -----------------------------------------------------
# from time import sleep
#
#
# def sleep_decorator(function):
#
#     """
#     Limits how fast the function is
#     called.
#     """
#
#     def wrapper(*args, **kwargs):
#         sleep(2)
#         return function(*args, **kwargs)
#     return wrapper
#
#
# @sleep_decorator
# def print_number(num):
#     return num
#
# print(print_number(222))
#
# for num in range(1, 6):
#     print(print_number(num))
#/deco-rate-limit.py -----------------------------------------------------
