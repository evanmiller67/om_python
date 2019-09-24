#/usr/bin/env python3 
"""
title: filename.py
author: exm5840
date(created): 2019-09-16 12:11:48 EDT
date (updated): 2019-09-16 12:11:48 EDT
"""

try:
    eval('x === x')
except SyntaxError:
    print("You cannot do that, Dave.")


# Divide by 0
# print(10 + (1 / 0))

try:
    print(10 + (1 / 0))
except ZeroDivisionError:
    print("Oops! We can't divide by zero, please choose a different number and re-evaluate.")

# NameError: name 'spam' is not defined
# print(4 + spam * 3)

try:
    print(4 + spam * 3)
except NameError as error:
    print('You have encountered a NameError because: ', error)

# TypeError: can only concatenate str (not "int") to str
# print("2" + 2)


# Catch multiple Errors with a single `except`
try:
    print("2" +  spam + 15)
except (NameError, TypeError):
    print("Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.")

# Multiple excepts for different errors
try:
    print("2" +  spam + 15)
except TypeError as e:
    print("You gave the wrong type there buddy!", e)
except NameError as e:
    print("That variable name does not exist!", e)

def divide_this(x, y):
    try:
        x / y
        #raise ZeroDivisionError("raised zero division with params: x'{0}' | y'{1}'".format(x,y))
    except ZeroDivisionError as e:
        print(e)
    else: 
        print("in teh elses")
    finally:
        print("Executing finally")


print(divide_this(10, 10))
