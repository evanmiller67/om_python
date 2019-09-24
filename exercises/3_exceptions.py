#/usr/bin/env python3 
"""
title: 3_exceptions.py
author: exm5840
date(created): 2019-09-16 13:22:09 EDT
date (updated): 2019-09-16 13:22:09 EDT
"""

try:
    eval('x === x')
except SyntaxError as e:
    print("Yo bruh. You got a syntax error: ", e)

try:
    print(10 / 0)
except ZeroDivisionError as e:
    print("This has no meaning.", e)


try:
    print(4 + spam)
except NameError as e:
    print("you've not defined something.", e)

try:
    print(2 + "2")
except TypeError as e:
    print("one of these things is not like the other: ", e)


try:
    raise FizzleError("all your fizz are belong to us")
except FizzleError as e:
    print("All out of Buzz", e)
