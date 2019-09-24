#/usr/bin/env python3 
"""
title: loops_while.py
author: exm5840
date(created): 2019-09-18 11:33:56 EDT
date (updated): 2019-09-18 11:33:56 EDT
"""

temperature = 115
while (temperature > 112):
  print(temperature, end = "-")
  temperature -= 1
print('The tea is cool enough')

x_input = input("Enter the x key: ")
while (x_input != "x"):
  print("Waiting")
  x_input = input("Enter the x key: ")
print("Thank you for typing x!")

# Infinite loops
# while True:
#   print("Ah!")
# while 5 == 5:
#   print("Forever looping!")

# Create a while loop that will count down from 10 to 1.
count=10
while count >= 1:
    print(count,end="-")
    count-=1
print('\n-----------------')

# Asks the user to enter an integer that is greater than 0. The function will keep on asking the user for the number until it is valid.
inp_x = 0
while int(inp_x) <= 0:
    try:
        inp_x = int(input("Enter an integer greater than 0: "))
    except ValueError as e:
        print("That's not an integer... Try again.")

# Ask the user to enter two separate integers (The first number must be smaller than the second). Create a while loop that will count from the first number to the second.
print("Please input 2 numbers. The frist must be smaller than the second.")
x = int(input("num 1: "))
y = int(input("num 2: "))
while x < y:
    print(x)
    x += 1

# Ask the user to respond by 'Y', 'y', 'yes', 'YES' or 'N', 'n', 'no', 'NO'. The function keeps on asking until the user enters the correct information.
print("plesae respond yes or no")
inp = input("> ")
beginning_char = inp[0].lower()
while not (beginning_char == 'y' or beginning_char == 'n'):
    print("not yes or no")
    inp = input("> ")
    beginning_char = inp[0].lower()

# Given this while loop, write a try/except statement. The input of the users guess can only be a whole number. Make sure the except throws an error (One exception total) for both floating point numbers and letters.

count = 0
while count < 5:
    try:
	guess = int(input("Take a guess "))
    except Exception as e:
	raise ValueError("That was not a goog number")
    count = count + 1
