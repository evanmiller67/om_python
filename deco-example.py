#/usr/bin/env python3
"""
title: deco-example.py
author: exm5840
date(created): 2019-09-20 07:51:26 EDT
date (updated): 2019-09-20 07:51:26 EDT
"""

from decoratorfile import my_decorator


@my_decorator
def just_some_function():
    print("Wheee!")

just_some_function()
