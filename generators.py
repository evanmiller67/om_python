#/usr/bin/env python3
"""
title: generators.py
author: exm5840
date(created): 2019-09-20 06:56:12 EDT
date (updated): 2019-09-20 06:56:12 EDT
"""

# Generators generate a value one at a time making them useful for `for` loops
# There are two ways to create a generator. They differ in their syntax, but the end result is still a generator. We’ll teach these concepts by covering their syntax and comparing them to a similar, but non-generator equivalent.
# A generator function versus a regular function
# A generator expression versus a list comprehension

# Generators allow us to create iterators in a more simple fashion
# Generators introduce the yield statement to Python. It works a bit like return because it returns a value
# The difference is that it saves the state of the function. The next time the function is called, execution continues from where it left off, with the same variable values it had before yielding.
# If we transform our Primes() iterator into a generator, it’ll look like this:

def check_prime(number):
  for divisor in range(2, int(number ** 0.5) + 1):
    if number % divisor == 0:
        return False
  return True


def Primes(max):
    number = 1
    while number < max:
        number += 1
        if check_prime(number):
            yield number
primes = Primes(100000000000)
print(primes)

for x in primes:
    print(x)


# Can we do better?
# Yes: generator expressions
primes = (i for i in range(2, 100000000000) if check_prime(i))
print(primes)
for x in primes:
    print(x)
