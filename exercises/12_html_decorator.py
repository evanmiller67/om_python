#/usr/bin/env python3
"""
title: 12_html_decorator.py
author: exm5840
date(created): 2019-09-24 12:37:29 EDT
date (updated): 2019-09-24 12:37:29 EDT
"""
from functools import wraps
import random


choices = ['make_uppercase', 'make_lowercase', 'make_bold', 'make_italic', 'make_underline', 'make_emphasis', 'make_strong']
def add_markup(decisions, *args):
  def deco(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
      print("in teh wrapper")
      print("decisions: " + str(decisions))
      ptag = ""
      etag = ""
      for d in decisions:
        if d in choices:
          tag = d[5:]
          ptag = "<" + tag + ">" + ptag
          etag = "</" + tag + ">" + etag
      return ptag + func(*args, **kwargs) + etag
    return wrapper
  return deco

#def make_strong(fn):
#    def wrapped():
#        return "<strong>" + fn() + "</strong>"
#    return wrapped


# TODO: add the functions for the other 6 decorator functions

picked = [] # This will hold the users choices


# TODO: ask the user to choose 3 of the options and store their choices in picked
picked.append(random.choice(choices))
picked.append("not_real_choice")
picked.append(random.choice(choices))
picked.append(random.choice(choices))


altered_text = 'hello'

#if 'make_strong' in picked:
#    @make_strong
#    def greeting():
#        return altered_text
#    altered_text = greeting()

@add_markup(picked)
def greeting():
  return altered_text

print(greeting())


# TODO: create other if statements to handle if the other 6 decorator functions are chosen
#print(altered_text)
