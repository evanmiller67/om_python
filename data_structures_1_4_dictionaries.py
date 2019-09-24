#/usr/bin/env python3 
"""
title: data_structures_1_4_dictionaries.py
author: exm5840
date(created): 2019-09-17 13:44:16 EDT
date (updated): 2019-09-17 13:44:16 EDT
"""

# Dictonaries are key/val pairs
salaries = {'Pam': 12000, 'Jim': 10000, 'Dwight': 50000}
print(salaries)
print(salaries['Jim'])

# Methods to access elements:
# dict.keys()
# dict.values()
# dict.items() => tuple of (key, value) pairs

results_10k = {'Elizabeth': '56: 09', 'Emily': '56: 23', 'Alison': '57: 36'}
print(results_10k.keys())
print(results_10k.values())
print(results_10k.items())
# Add new
results_10k['Laurel'] = '59: 40'
print(results_10k)
# Edit existing
results_10k['Alison'] = '55: 36'
print(results_10k)
# Delete key
del results_10k['Laurel']
print(results_10k)
