#/usr/bin/env python3
"""
title: text_manipulation.py
author: exm5840
date(created): 2019-09-19 09:50:31 EDT
date (updated): 2019-09-19 09:50:31 EDT
"""

def main():
  file_name="days.txt"
#    with open(file_name, 'r') as days_file:
## This will print the entire file
##        print(days_file.read())
## This will read a single line (including newline), could be done with a loop. BUT...
##        print(days_file.readline())
## This function returns a list of all the lines
##        print(days_file.readlines())
## This allows us to read the lines and modify them in-memory
##    with open(file_name, 'r') as days_file:
##        days = days_file.readlines()
##
##    num_lines = len(days)
##    for i in range(num_lines):
##        days[i] = "Yay! It's " + days[i]

## Modifying
  with open('days.txt', 'r') as days_file:
    days = days_file.readlines()

  num_lines = len(days)
  for i in range(num_lines):
    days[i] = "Yay! It's " + days[i]

  title = "Days of the Week\n"

  with open('days.txt', 'w') as new_days:
    new_days.write(title)
    new_days.writelines(days)

if __name__ == '__main__':
    main()
