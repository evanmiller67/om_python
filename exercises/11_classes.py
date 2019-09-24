#/usr/bin/env python3 
"""
title: exercises/11_classes.py
author: exm5840
date(created): 2019-09-19 19:31:37 EDT
date (updated): 2019-09-19 19:31:37 EDT
"""
import re

class StringManipulation:
    vowels=set('aeiou')

    def __init__(self, altering_string):
        self.altering_string = altering_string

    def string_reversal(self, reverse=None):
        return self.altering_string if reverse is None else reverse[::-1]

    def remove_case(self, removed=None):
        return self.altering_string if removed is None else re.sub(r'[^a-z]', '', removed.lower())

    def is_vowel(self, searching=None):
        if searching is None:
            return len(StringManipulation.vowels.intersection(self.altering_string.lower())) > 0
        else:
            return len(StringManipulation.vowels.intersection(searching.lower())) > 0

    def palindrome(self, searching=None):
        is_palindrome = self.altering_string if searching is None else searching
        is_palindrome = self.remove_case(is_palindrome)
        for i in range(len(is_palindrome)):
            if (is_palindrome[i] != is_palindrome[len(is_palindrome) -1 + i*-1]):
                return False
        return True

    def short_hand(self, short=None):
        shorten = self.altering_string if short is None else short
        words = shorten.split(" ")
        for i in range(len(words)):
            words[i] = words[i].replace("and", "&").replace("too", "2").replace("for", "4")
            words[i] = re.sub("[Yy]ou", "U", words[i])
            words[i] = re.sub("[aeiouAEIO]", "", words[i])
            if ( len(words[i]) > 1 ):
                words[i] = re.sub("U","", words[i])
        return " ".join(words)

    def pig_latin(self, pig=None):
        if pig is None:
            pig = self.altering_string
        pigLatinWord = ''
        if len(set(list(pig)).intersection(StringManipulation.vowels)) == 0:
            pigLatinWord = pig + "ay"
        elif len(StringManipulation.vowels.intersection(set(list(pig[0])))) == 1:
            pigLatinWord = pig + "yay"
        else:
            idx = 0
            start = ''
            end = ''
            found_vowel = False
#            while idx < len(pig):
#                if not found_vowel:
#                    if len(set(vowels).intersection(set(list(pig[idx])))) == 1:
#                        found_vowel = True
#                        idx -=1
#                    else:
#                        start += pig[idx]
#                else:
#                    end = end + pig[idx]
#                idx +=1
#            pigLatinWord = end + start + "ay"
            for i,char in enumerate(pig):
                if (len(StringManipulation.vowels.intersection(set(list(pig[i])))) > 0):
                    idx = i
                    break
            pigLatinWord = pig[idx:] + pig[:idx] + "ay"
        return pigLatinWord


if __name__ == '__main__':
    stringy = StringManipulation("My =Fun= String!!!")
    print(stringy.string_reversal())
    print(stringy.string_reversal(reverse="the quick brown fox"))
    print(stringy.string_reversal("bubba"))
    print(stringy.remove_case())
    print(stringy.remove_case(removed="This Is My Bat!!!"))
    print(stringy.remove_case("Will you --PLEASE-- take out the trash?"))
    print(stringy.is_vowel())
    print(stringy.is_vowel("my butterknife"))
    print(stringy.is_vowel(searching="a"))
    print(stringy.is_vowel("qwrtyplkjhg"))
    print(stringy.is_vowel(searching="t"))
    print(stringy.palindrome())
    print(stringy.palindrome(searching="taco cat"))
    print(stringy.palindrome("Madam, I'm Adam!"))
    print(stringy.palindrome("this is not a palindrome"))
    print(stringy.short_hand("Thank you for that! You are too sweet and kind!"))
    words = ["my", "why", "foobar", "apple", "banana"]
    for word in words:
        print(word,end=': ')
        print(stringy.pig_latin(word))
