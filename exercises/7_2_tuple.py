#/usr/bin/env python3 
"""
title: exercises/7_2_tuple.py
author: exm5840
date(created): 2019-09-17 12:33:45 EDT
date (updated): 2019-09-17 12:33:45 EDT
"""
import random
# Create a function called gymnast_scores that does not have any parameters or return anything. A gymnast can earn a score between 1 and 5 from each judge; nothing lower, nothing higher. All scores are integer values; there are no decimal scores from a single judge. Store the possible scores a gymnast can earn from one judge in a tuple.

# Print out the sentence, "The lowest possible score is _ _ _, and the highest possible score is _ _ _." Use the values from your tuple. (Do not hard code the values)

# Print out "A judge can give a gymnast _ points.". Filling in the blank with a random value from the tuple. (Do not hard code the value)

possible_scores = (1, 2, 3, 4, 5)
# def gymnast_scores():

print("The lowest possible score is '{0}', and the highest possible score is '{1}'".format(min(possible_scores), max(possible_scores)))
print("A judge can give a gymnast '{0}' points.".format(random.choice(possible_scores)))
