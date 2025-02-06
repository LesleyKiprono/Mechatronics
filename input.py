#!/usr/bin/env python
import math
    
print("--------------------------------------------------------------------------")
print("i   | cos(i) |  sin(i)  |  tan(i)  ")


for i in range(-180, 180, 30):

    print(f"| {i} | {math.cos(i)} | {math.sin(i)} | {math.tan(i)}| ")

#print the powers of numbers from 1 to 10 in a tabular form using for loop
print("-----------------------------------------")
print("x^1\tx^2\tx^3\tx^4\tx^5")
for i in range(1,11):
    print(f"{i}")
    print(f"{i}\t{math.pow(i,2)}\t{math.pow(i,3)}\t")

print("---------------------------------------")
#tabs and new lines
print("New York\tSeoul\tBerlin\tNairobi\tAmsterdam")

print("------------------------------------")
print("My name is \n Lesley \n Limo")




