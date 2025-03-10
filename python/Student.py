#!/usr/bin/env python

#creating a class

class Student:

    #attributes of the student
    hobby = "Swimming"


    #behaviour of the student
    def __init__(self, name, id, age, grade):
        self.name = name
        self.id = id
        self.age = age
        self.grade = grade

    def print_name(self,name):
        print(f"My name is {name}")

    def print_id(self,id):
        print(f"My ID is {id}")

    def print_age(self,age):
        print(f"My age is {age}")

    def print_grade(self,grade):
        print(f"My grade is {grade}")

#an instance of the student
student1 = Student("Lesley", 1100, 18, "A")
student2 = Student("James", 2632, 19, "B")   
student3 = Student("Mike", 1415, 14, "A")



print(student1.age)
print(student2.grade)
print(student3.id)

student2.print_id(789)


class Teacher:
    def __init__(self, name, salary, subject): 
        self.name = name
        self.salary = salary
        self.subject = subject
    
    def increase_salary(self, salary):
        new_salary = salary + (0.2 * salary)
        return new_salary
    
    def print_salary(self, salary):
        print(f"The teacher earns {salary} in ksh")

teacher1 = Teacher("Jada", 20000, "Biology")
teacher2 = Teacher("Emmanuel", 70000, "Physics")

print(teacher2.salary)

new_sal = teacher2.increase_salary(70000)
print(new_sal)

