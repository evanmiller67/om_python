#/usr/bin/env python3 
"""
title: exercises/7_4_dictionaries.py
author: exm5840
date(created): 2019-09-17 13:58:10 EDT
date (updated): 2019-09-17 13:58:10 EDT
"""
# Create a function called polling_friends that does not take in any parameters. In the function, create a dictionary called fav_animals where each key is a person’s name, and each value is that person’s response to the question "What is your favorite animal?". You are going ask your two friends "Miranda" and "Gordo". (Use user input to get their favorite animal). Store two responses in your dictionary. Return the dictionary once you are done!
# Call (invoke) the function like shown below:
#       print(polling_friends())


def polling_friends():
    fav_animals = {'Miranda':"", "Gordo":""}
    for name in fav_animals.keys():
        fav_animals[name] = input(name + ", what is your favorite animal? ")
    return fav_animals

print(polling_friends())


#################################################
def birthday_month(current, birthday):
    months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12}
    diff = months[current] - months[birthday]
    return diff if diff >= 0 else len(months) + diff

print(birthday_month('June', 'December'))
print(birthday_month('May', 'August'))
print(birthday_month('May', 'February'))
print(birthday_month('May', 'May'))
