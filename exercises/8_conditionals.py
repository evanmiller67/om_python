#/usr/bin/env python3 
"""
title: exercises/8_conditionals.py
author: exm5840
date(created): 2019-09-17 14:51:18 EDT
date (updated): 2019-09-17 14:51:18 EDT
"""

print("You enter a dark room with two doors.  Do you go through door #1, #2, or door #3?")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheese cake.  What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off.  Good job!")
    elif bear == "2":
        print("The bear eats your legs off.  Good job!")
    else:
        print("Well, doing {} is probably better.  Bear runs away.".format(bear))

elif door == "2":
    print("You stare into the endless abyss at Cthuhlu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.  Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.  Good job!")
elif door == "3":
    print("A singing mermaid sits on a rock. What do you do?")
    print("1. Summon a harpy to pluck her eyes")
    print("2. Weild a tire iron in tune to her melody")
    print("3. Whip cream pie to the face")

    mermaid = input("> ")

    if mermaid == "3":
      print("You were lulled by the mermaid and drowned. Good job!")
    else:
      print("You scared the mermaid away. Good job!")
else:
    print("You stumble around and fall on a knife and die.  Good job!")
