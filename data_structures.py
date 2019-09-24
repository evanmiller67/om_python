#/usr/bin/env python3 
"""
title: data_structures.py
author: exm5840
date(created): 2019-09-17 11:03:27 EDT
date (updated): 2019-09-17 11:03:27 EDT
"""

# 1.1 lists
dogs = ["Collie", "Labrador", "Sheltie", "Dalmatian"]
print(dogs)

# 1.1.1 length
print(len(dogs))

# 1.1.2 indexing
print(dogs[1])

# print(dogs[10])
# IndexError: list index out of range

print(dogs[-2])
print("Charlie is a " + dogs[1])


# 1.1.3 slicing
print(dogs[1: 3])
print(dogs[: 2])
print(dogs[2 :])

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[1: 11: 2])

print(numbers[: : 3])
print(numbers[: : -2])


# 1.1.4 modifying
dogs[1] = "Golden Retriever"
print(dogs)

first_names = ["Noelle", "Tereza", "Raelin", "Linus"]
last_names = ["Blossom", "Chrissy", "Grover", "Devin"]
print(first_names + last_names)

first_names = first_names + ["Sally"]
print(first_names)

first_names += "Sally"
print(first_names)
# Output: ['Noelle', 'Tereza', 'Raelin', 'Linus', 'S', 'a', 'l', 'l', 'y']

dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2]
print(dogs)

dogs = ["Collie", "Golden Retriever", "Sheltie", "Dalmatian"]
del dogs[2: ]
print(dogs)


# 1.1.5 list methods
fish = ["barracuda", "cod", "devil ray", "eel"]
fish.append('flounder')
print(fish)

fish.append(['flounder', 'clown'])
print(fish)

fish = ["barracuda", "cod", "devil ray", "eel"]
fish.extend('flounder')
print(fish)
fish.extend(['seahorse', 'clown'])
print(fish)


fish.insert(0, 'anchovy')
print(fish)

salaries = [20000, 45000, 90000, 70000, 20000, 90000]
print(salaries.count(20000))

fish_ages = [1,2,4,3,2,1,1,2]
fish_ages.sort()
print(fish_ages)

fish_ages = [1,2,4,3,2,1,1,2]
fish_ages.sort(reverse=True)
print(fish_ages)

fish = ["barracuda", "cod", "devil ray", "eel"]
fish.remove("cod")
print(fish)


