#/usr/bin/env python3 
"""
title: loops.py
author: exm5840
date(created): 2019-09-17 15:13:06 EDT
date (updated): 2019-09-17 15:13:06 EDT
"""

numbers = [10, 5, 2, 7]
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])

for i in [10, 5, 2, 7]:
  print(i, end = " ")
print("")

for x in [1, 2, 3, 4]:
  print(x, end = " ")
print("")

numbers = [20, 30, 40, 50]
for k in numbers:
  print(k, end = " ")
print("")

name = "Betty"
for w in name:
  print(w, end = " ")
print("")

# Just stop
print(range(4))

# start and stop
print(range(1, 4))

# start, stop, step
print(range(1, 10, 2))

for i in range(2, 10, 3):
  print(i, end = " ")
print("")

## Say you wanted to repeat the word "OM" 5 times
for i in range(5):
  print("OM", end = " ")
print("")


# for loop using operators
prices = [12, 7, 9, 10]
for i in prices:
  print(i ** 2, end = " ")
print("")

prices = [12, 7, 9, 10]
total = 0
for i in prices:
  total += i
  print(total)
print("")

# enumerate
grocery = ['bread', 'milk', 'butter']

for item in enumerate(grocery):
  print(item)

print('\n')
for count, item in enumerate(grocery):
  print(count, item)

# start counting from given number
for count, item in enumerate(grocery, 100):
  print(count, item)

