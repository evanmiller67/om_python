#/usr/bin/env python3 
"""
title: data_structures_1_1_7_apply.py
author: exm5840
date(created): 2019-09-17 11:27:44 EDT
date (updated): 2019-09-17 11:27:44 EDT
"""

my_friends = ["Rizzo", "French", "Danny", "Kenickie", "Marty", "Sandy", "Cha-Cha", "Patty", "Sonny", "Calhoun"]

# print out the length of the list
print(len(my_friends))
# print out the 4th friend’s name
print(my_friends[3])
# print out the 11th friend’s name (What happens?)
# print(my_friends[10])
# IndexError
# once you have run this once, comment out the above line

# print out the last friend’s name (Use negative indexing)
print(my_friends[-1])
# print out the 5th - 8th friend’s names
print(my_friends[4:8])
# print out the last 5 names (Do not place a number in both start and stop)
print(my_friends[-5:])
# print out the first 3 names (Do not place a number in both start and stop)
print(my_friends[:3])
# print out every other name, starting at the first name
print(my_friends[::2])
# print out every third name, starting at the last name going backwards to the front of the list.
print(my_friends[::-3])
# change the 8th friend’s name to "Elizabeth". Print out the changed list.
my_friends[7] = "Elizabeth"
print(my_friends)
# add a new friend, Danny, to the end of the list. Print out the changed list.
my_friends.extend(["Danny"])
# remove the 7th friend’s name (They ate the last cookie in the jar). Print out the changed list.
del(my_friends[6])
print(my_friends)
# insert a new friend, Sandy, in the 3rd spot of the list. Print out the changed list.
my_friends.insert(2, "Sandy")
print(my_friends)
# print out the number of times the name Sandy appears in the list.
print(my_friends.count("Sandy"))
# sort the list to be in alphabetical order. Print out the sorted list.
my_friends.sort()
print(my_friends)
