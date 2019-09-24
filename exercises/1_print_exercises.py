#/usr/bin/env python3 
import random
import re

"""
title: 1_print_exercies.py
author: exm5840
date(created): 2019-09-16 10:20:42 EDT
date (updated): 2019-09-16 10:20:42 EDT
"""

print("1.1\n\n")
print("Elizabeth,", end=" ")
print("Emily,", end=" ")
print("Bob,", end=" ")
print("Antonio.")

print("=====================================================================================")
print("=====================================================================================")
print("=====================================================================================")
print("1.2\n\n")

ascii_art="""
FFFFFFFFFFFFFFFFFFFFFF                                 hhhhhhh                                                                    
F::::::::::::::::::::F                                 h:::::h                                                                    
F::::::::::::::::::::F                                 h:::::h                                                                    
FF::::::FFFFFFFFF::::F                                 h:::::h                                                                    
  F:::::F       FFFFFFooooooooooo      ggggggggg   gggggh::::h hhhhh          ooooooooooo   rrrrr   rrrrrrrrr   nnnn  nnnnnnnn    
  F:::::F           oo:::::::::::oo   g:::::::::ggg::::gh::::hh:::::hhh     oo:::::::::::oo r::::rrr:::::::::r  n:::nn::::::::nn  
  F::::::FFFFFFFFFFo:::::::::::::::o g:::::::::::::::::gh::::::::::::::hh  o:::::::::::::::or:::::::::::::::::r n::::::::::::::nn 
  F:::::::::::::::Fo:::::ooooo:::::og::::::ggggg::::::ggh:::::::hhh::::::h o:::::ooooo:::::orr::::::rrrrr::::::rnn:::::::::::::::n
  F:::::::::::::::Fo::::o     o::::og:::::g     g:::::g h::::::h   h::::::ho::::o     o::::o r:::::r     r:::::r  n:::::nnnn:::::n
  F::::::FFFFFFFFFFo::::o     o::::og:::::g     g:::::g h:::::h     h:::::ho::::o     o::::o r:::::r     rrrrrrr  n::::n    n::::n
  F:::::F          o::::o     o::::og:::::g     g:::::g h:::::h     h:::::ho::::o     o::::o r:::::r              n::::n    n::::n
  F:::::F          o::::o     o::::og::::::g    g:::::g h:::::h     h:::::ho::::o     o::::o r:::::r              n::::n    n::::n
FF:::::::FF        o:::::ooooo:::::og:::::::ggggg:::::g h:::::h     h:::::ho:::::ooooo:::::o r:::::r              n::::n    n::::n
F::::::::FF        o:::::::::::::::o g::::::::::::::::g h:::::h     h:::::ho:::::::::::::::o r:::::r              n::::n    n::::n
F::::::::FF         oo:::::::::::oo   gg::::::::::::::g h:::::h     h:::::h oo:::::::::::oo  r:::::r              n::::n    n::::n
FFFFFFFFFFF           ooooooooooo       gggggggg::::::g hhhhhhh     hhhhhhh   ooooooooooo    rrrrrrr              nnnnnn    nnnnnn
                                                g:::::g                                                                           
                                    gggggg      g:::::g                                                                           
                                    g:::::gg   gg:::::g                                                                           
                                     g::::::ggg:::::::g                                                                           
                                      gg:::::::::::::g                                                                            
                                        ggg::::::ggg                                                                              
                                           gggggg                                                                                 
"""
# print(ascii_art)


print("=====================================================================================")
print("=====================================================================================")
print("=====================================================================================")
print("1.3\n\n")

name=input("What is your name? ")
salary_raw=input("Hello, %s. What is your salary? " %(name))
salary = int(re.sub("\D", "", salary_raw))
raise_per = random.randint(0,100)
raise_amount = salary + salary * raise_per / 100.0
print("%s, you said your current salary is: %0.2f.\nYour random percentage incraese is: %d \nThis makes your new salary: $%0.2f" %(name,salary,raise_per, raise_amount))
