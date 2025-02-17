#!/usr/bin/env python

#<less than 
#>greater than
#>=greater than or equal to
#<=less than or equal to
#==equal to
#!=not equal to

number = 20
guess = int(input('Enter a number between 1 to 25'))

if guess == 20 :
    print("Hurray, you are correct")

age = int(input("Enter your age:"))
if age < 18:
    print("You are not allowed to drink/ drive")
elif age <= 50:
    print("You can drink")
else :
    print("You are too old to drink")