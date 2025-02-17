#write a program to print your name, weight and age using command line
#python print_details Lesley 87 18

#I am Lesley and I weigh 66 and also 18 yrs
import sys

name = sys.argv[1]
weight = sys.argv[2]
age = sys.argv[3]
print(f"I am {name} and I weigh {weight}kgs and also {age } years old ")
