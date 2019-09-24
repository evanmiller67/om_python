#/usr/bin/env python3 
"""
title: classes.py
author: exm5840
date(created): 2019-09-19 19:02:54 EDT
date (updated): 2019-09-19 19:02:54 EDT
"""

class Player:
    """
    Creates a game Player template.
    """
    def __init__(self, user_name, points=0):
        self.user_name = user_name
        self.points = points

    def gain_point(self, points):
        """Prints that the user has gained a certain number of points."""
        self.points += points
        print(f"Yay {self.user_name}! You have gained {points} point(s)! That means you now have {self.points} points!")

    def lose_point(self, points):
        """Prints that the user has lost a certain number of points."""
        self.points -= points
        print(f"Oh no, {self.user_name}! You have lost {points} point(s)! That means you now have {self.points} points!")

def main():
  ralph = Player("R@!ph123", 100)
  ralph.gain_point(10)
  ralph.lose_point(5)
  sally = Player("iS@llee", 1245)
  sally.lose_point(5)

if __name__ == "__main__":
  main()
