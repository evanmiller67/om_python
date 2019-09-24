#/usr/bin/env python3 
"""
title: strings.py
author: exm5840
date(created): 2019-09-16 13:58:47 EDT
date (updated): 2019-09-16 13:58:47 EDT
"""

group_name = 'Monty Python'
statement = "Monty Python's sketches are funny"
message = """This is a string that will span across multiple lines.
Using newline characters and no spaces for the next lines.
The end of lines within this string also count as a newline when printed"""

english_greeting = "Hello"
say_hi_to = "world"
exclamation = "!"
print(english_greeting + say_hi_to + exclamation)
print(english_greeting, say_hi_to, exclamation)
print(english_greeting, say_hi_to + exclamation)

name = "Helga"
last_name = "Susan"
name += last_name
print(name)

print("hello" * 4)
print("alright" * 3)

# Indexing
favorite_things = """Some of my favorite things are bird watching, jogging,
listening to podcasts, and coding in Python."""
print(favorite_things[0])

# Slicing
# string_name[start_index:stop_index]
print(favorite_things[5:10])
# string_name[:stop_index]
print(favorite_things[:10])
# string_name[start_index:]
print(favorite_things[31:])
# string_name[start_index:stop_index:step]
print(favorite_things[::2])

my_name = "Emily"
print("E" in my_name)



################################################
################################################

greeting = "HELLO WORLD!"
print(len(greeting))
greeting = "HELLO WORLD"
print(greeting.lower())
print(greeting.upper())
new_greeting = " ".join(greeting)
print(new_greeting)
new_greeting = ".".join(greeting)
print(new_greeting)


greetings = ["hello", "hola", "salve"]
string_greeting = ",".join(greetings)
print(string_greeting)


greetings = "hello hola salve"
string_greeting = greetings.split()
print(string_greeting)
print(greetings.split("l"))


greetings = "hello, hola, salve"
new_greeting = greetings.replace("salve", "ciao")
print(new_greeting)


################################################
################################################
# Reversing strings

greeting = "Hello"[::-1]
print(greeting)
string = "HELLO"
reversed_string = ''.join(reversed(string))
print(reversed_string)


print("\n\n\n")
## Applying what we've learned

## Describe the sketch comedy group
## Create a variable with their name (Monty Python)
name="Monty Python"
## Create a short description in the form of a string assigned to a variable (Monty Python was a British comedy group)
desc="Monty Python was a British comedy group"
## Create a variable assigned to a number that represents the year they were formed (1969)
year_formed = 1969

## Introduce the group in a sentence
## Assign a variable whose value will be a concatenation of the above variables into a sentence that makes sense.
long_desc="Group Name: '{0}'.\nDesc: '{1}'.\nYear formed: '{2}'".format(name,desc,year_formed)
print(long_desc)
## Using the above variables, write the sentence in two different ways that we have learned to concatenate strings, numbers and variables in a print() statement to avoid a TypeError (Hint: Use + and ,)
print(name, "|",desc + ".","They were formed in",year_formed)

phrase="Don’t count your chickens before they hatch"
slogan="For Everything Else, There's MasterCard"
combined=phrase + ". " + slogan
print(combined)
print(combined * 3)
print(slogan[6])
print(combined[-1])
print(phrase[::2])
print(phrase[16:25])
print(combined[::2])
print("m" in slogan)
print(combined.upper())
print(combined.split(" "))
print(slogan[::-1])
