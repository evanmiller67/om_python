#/usr/bin/env python3 
"""
title: filename.py
author: exm5840
date(created): 2019-09-16 13:40:53 EDT
date (updated): 2019-09-16 13:40:53 EDT
"""

True and True                                                   # TRUE
False and True                                                  # FALSE
1 == 1 and 2 == 1                                               # FALSE
"test" == "test"                                                # true
1 == 1 or 2 != 1                                                # true
True and 1 == 1                                                 # true
False and 0 != 0                                                # false
True or 1 == 1                                                  # true
"test" == "testing"                                             # false
1 != 0 and 2 == 1                                               # false
"test" != "testing"                                             # true
"test" == 1                                                     # false
not (True and False)                                            # true
not (1 == 1 and 0 != 1)                                         # false
not (10 == 1 or 1000 == 1000)                                   # false
not (1 != 1 or 3 == 4)                                          # true
not ("testing" == "testing" and "Ronny" == "Gool Guy")          # true
1 == 1 and not ("testing" == 1 or 1 == 0)                       # true
"chunky" == "bacon" and not (3 == 4 or 3 == 3)                  # false
3 == 3 and not ("testing" == "testing" or "Python" == "Fun")    # false
