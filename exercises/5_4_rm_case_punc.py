#/usr/bin/env python3 
"""
title: 5_4_rm_case_punc.py
author: exm5840
date(created): 2019-09-17 09:08:10 EDT
date (updated): 2019-09-17 09:08:10 EDT
"""
import re

str_inp = input("Enter any string: ")
formatted = re.sub(r'[^a-z]','',str_inp.lower())

print("Formatted string: '{0}'".format(formatted))
