#/usr/bin/env python3 
import math

"""
title: 2_math_variables.py
author: exm5840
date(created): 2019-09-16 11:26:18 EDT
date (updated): 2019-09-16 11:26:18 EDT
"""

print("Carrying capacity of a swallow: %d" %(60/3))
print("How many swallows would it take to carry a 1450g coconut? : %f" %(1450/(60/3)))

swallow_weight = 60.0
swallow_capacity = swallow_weight / 3

coconut_weight = 1450

print("Coconut weight: %s | Swallows/coconut: %f" %(coconut_weight, coconut_weight/swallow_capacity))


### =============================================

macaw_capacity = 1/3
macaw_weight = 900
macaws_required = coconut_weight / (macaw_weight * macaw_capacity)

print("Coconut weight: %s | Macaws/coconut: %f" %(coconut_weight, math.ceil(macaws_required)))
