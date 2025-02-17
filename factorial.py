#!/usr/bin/env python

#program to calculate the factorial of a number using while loop

number = int(input("Enter the number :"))

fact_n = 1
while number >= 1: 
    fact_n = number * fact_n
    number = number - 1
print(fact_n)

