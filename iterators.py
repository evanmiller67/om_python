#/usr/bin/env python3
"""
title: iterators.py
author: exm5840
date(created): 2019-09-20 07:17:44 EDT
date (updated): 2019-09-20 07:17:44 EDT
"""

## Iteration is the repetition of some kind of process over and over again. Python’s for loop gives us an easy way to iterate over various objects. Often, you’ll iterate over a list, but we can also iterate over other Python objects such as strings and dictionaries.

# Iterating over a list
ez_list = [1, 2, 3]
for i in ez_list:
    print(i)

# Iterating over a string
ez_string = "Generators"
for s in ez_string:
    print(s)

# Iterating over a dictionary
ez_dict = {1 : "First", 2 : "Second"}
for key, value in ez_dict.items():
    print(key, value)

# Only objects that implement the Iterator Protocol may be interated over
# number = 12345
# for n in number:
#     print(n)
# ----output----
# >>> TypeError: 'int' object is not iterable

# The Iterator Protocol mentioned previously looks for two methods within the class: __iter__ and __next__
def check_prime(number):
  for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
        return False
  return True

class Primes:
    def __init__(self, max):
        self.max = max
        self.number = 1
    def __iter__(self):
        return self
    def __next__(self):
        self.number += 1
        if self.number >= self.max:
            raise StopIteration
        elif check_prime(self.number):
            return self.number
        else:
            return self.__next__()

primes = Primes(100000000000)
print(primes)

for x in primes:
    print(x)
