#!/usr/bin/env python

name = input("Enter your name") 
print(name)

favourite_team = "Man U"
 #format specifiers
 #  # %d -integers - positive and negative whole numbers 
# %f float - fractions / decimal points
# %s string and characters
name = input ("Enter your name: ")
city = input("Where are you from?:")
print("My name is {0} and I am from {1}".format(name,city))

t = 8
club = "Arsenal"
w = 140.9
print("I support %s and I weigh %f" %(club,w))

#f string print(f"I am {name}")

age = 17
fav_food = "pizza"
hobby = "playing_guitar"
print(f"I am {age} yrs old and my fav food is {fav_food} and I love {hobby}")


