 #!/usr/bin/env

#program that calculates the tax of civil servants

#0 - 50000 = 6% tax
#50001 - 100000 = 15%
#100001 - 500000 = 20%
#above 500001 = 25%

#get your salary
salary = float(input("Enter your salary: "))

new_salary = 0.0
if salary <= 50000: 
    tax = (6 * salary / 100)
    new_salary = salary - tax

elif salary > 50000 and salary < 100000:
    tax = (15 * salary/100)
    new_salary = salary - tax

elif salary > 100000 and salary < 500000:
    tax = (20 * salary/100)
    new_salary = salary - tax

else : 
    tax = (20 * salary / 100)
    new_salary = salary - tax

print(salary)
print(new_salary)


