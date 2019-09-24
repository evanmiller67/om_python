#/usr/bin/env python3 
"""
title: data_structures_1_3_sets.py
author: exm5840
date(created): 2019-09-17 12:41:13 EDT
date (updated): 2019-09-17 12:41:13 EDT
"""

# Sets are mutable, unique, unordered. Used for removing duplicates and performing set operations like intersection, union and difference
myset1 = set()
print(myset1)

myset = set('aabbcc')
priint(myset)

positions = set(["Software Engineer", "Sr. Software Engineer", "Staff Software Engineer", "Software Engineer Principal", "Software Engineer"])
print(positions)

languages={'python','java','c#','php'}
print(languages)

# Length
print(len(positions))

# set methods
# set1.intersection(set2)
jos_favs = {'python', 'c++', 'javascript'}
als_favs = {'c#', 'python'}
print(jos_favs.intersection(als_favs))
print(jos_favs.difference(als_favs))
print(jos_favs.union(als_favs))


# Modifying sets
jos_favs.add('java')
print(jos_favs)

jos_favs.remove('java')
print(jos_favs)
