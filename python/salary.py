#!/usr/bin/env python 

salary = int(input("Enter your salary :"))

if salary < 50000 :
    new_salary = salary *1.1
elif salary >= 50000 or salary <= 100000:
    new_salary = salary * 1.05
elif salary > 100000:
    new_salary = salary * 0.98
else :
    print("You are not affected")
    
print(new_salary)


