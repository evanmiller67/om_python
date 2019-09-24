#/usr/bin/env python3 
"""
title: filename.py
author: exm5840
date(created): 2019-09-16 13:35:40 EDT
date (updated): 2019-09-16 13:35:40 EDT
"""

x = 5
y = 8

print("x == y :", x == y)
print("x != y :", x != y)
print("x < y  :", x < y)
print("x > y  :", x > y)
print("x <= y :", x <= y)
print("x >= y :", x >= y)

name1 = "Sally"
name2 = "sally"
print("Sally == sally: ", name1 == name2)

print((9 > 7) and (2 < 4))  ## Both expressions are True
print((8 == 8) or (6 != 6)) ## One expression is True
print(not(3 <= 1))          ## The expression is True
