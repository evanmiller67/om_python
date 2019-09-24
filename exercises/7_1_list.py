#/usr/bin/env python3 
"""
title: 7_1_list.py
author: exm5840
date(created): 2019-09-17 12:29:10 EDT
date (updated): 2019-09-17 12:29:10 EDT
"""
import random

# Create a function called shake_ball that has no parameters. Inside the function, ask the user to ask a question about their future. Have your program return a random response of either: Yes definitely, As I see it, yes, Ask again later, Cannot predict now, Don’t count on it, Very doubtful, and 4 other responses.

responses = ["Yes definitely", "As I see it, yes", "As again later", "Cannot predict now", "Don't count on it", "Very doubtful", "yeet", "yolo", "nah", "goway"]

def shake_ball():
    return random.choice(responses)

input("What is your question? ")
print(shake_ball())
