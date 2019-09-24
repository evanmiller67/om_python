#/usr/bin/env python3 
"""
title: 5_3_password.py
author: exm5840
date(created): 2019-09-16 15:52:34 EDT
date (updated): 2019-09-16 15:52:34 EDT

A random credential using a combination of string skills, random numbers and concatenation. All input to the algorithm must be at least three characters long. Your program should first ask the user for:

their first name
last name
city they were born
university they graduated from
a name of a relative
a name of a friend
"""
import random

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
city = input("Enter your birth city: ")
uni = input("Enter the university you attended (or 'None'): ")
relative = input("Enter the name of a relative: ")
friend = input("Enter the naem of a friend: ")

emp_id = first_name[0:3] + last_name[-2:]
username = city[:2] + uni[-3:]
password = relative[random.randint(0,len(relative)):] + friend[:random.randint(0,len(friend))]


print("""
Employee id: {0}
Username:    {1}
Password:    {2}
""".format(emp_id, username, password))
