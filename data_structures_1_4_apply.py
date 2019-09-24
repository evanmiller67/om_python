#/usr/bin/env python3 
"""
title: data_structures_1_4_apply.py
author: exm5840
date(created): 2019-09-17 13:52:12 EDT
date (updated): 2019-09-17 13:52:12 EDT
"""
# Create a dictionary called cool_ranking. Set the corresponding keys equal to their values: "Chandler" = 1, "Monica" = 10, "Ross" = 5, "Phoebe" = 2, "Joey" = 3, "Rachel" = 4.
cool_ranking = {"Chandler":1, "Monica":10, "Ross":5, "Phoebe":2, "Joey":3, "Rachel":4}

# print out the ranking of 'Monica'
print(cool_ranking['Monica'])

# add the following key-value pair to the dictionary: 'Janice' = 6. Print out the new dictionary
cool_ranking['Janice'] = 6
print(cool_ranking)

# print out all of the keys of the dictionary
print(cool_ranking.keys())

# print out all of the values of the dictionary
print(cool_ranking.values())

# print out all of the key, value pairs of the dictionary in a list format.
print(cool_ranking.items())

# change 'Monica' to have a ranking of 7. Print out the new dictionary.
cool_ranking['Monica'] = 7
print(cool_ranking)

# remove 'Janice' from the dictionary. Print out the new dictionary.
del cool_ranking['Janice']
print(cool_ranking)
