#/usr/bin/env python3 
"""
title: conditional_statements.py
author: exm5840
date(created): 2019-09-17 14:20:48 EDT
date (updated): 2019-09-17 14:20:48 EDT
"""

secret_num = 10
guess = int(input("Enter a secret number: "))
if guess == secret_num:
  print("Yay! You won!")

balance = 100
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
balance = -5
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")

balance = 25
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
else:
  print("Balance is positive.")

balance = -33
if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
else:
  print("Balance is positive.")

if balance < 0:
  print("Balance is negative. Put funds in your account or you will be charged a penalty.")
elif balance == 0:
  print("Balance is equal to zero, add funds soon.")
else:
  print("Balance is positive.")

git_skill=127
python_skill=255
if git_skill == 1 and python_skill == 1:
  print("Start off with Git Foundation")
elif git_skill >= 2 and python_skill == 1:
  print("Start off with Python Foundation")
elif git_skill == 2 and python_skill == 2:
  print("Start off with either Python Pillars or Git Pillars")
elif git_skill == 3 and python_skill == 2:
  print("Start off with Python Capstone")
else:
  print("Git Capstone or Python Capstone")
