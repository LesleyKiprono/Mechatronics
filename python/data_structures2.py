#!/usr/bin/env python

#arrays



#lists ---> uses the square brackets




#tuples -----> uses normal brackets
friends = ("Jada","Lesley", "Moses", "Emmanuel" )
print(friends)

numbers = tuple(range(10))
print(numbers)

print(len(friends))
print(friends[0])

for friend in friends:
    print(friend)

print(type(friends))
friends_list = list(friends)
print(type(friends_list))
print(friends_list)

#sets----.> are immutable ------>uses curly brackets

cities = {"Seoul", "Nairobi", "Dodoma", "Rabat"}
for city in cities:
    print(city)

print(cities)
 
stuff = {"Bob", 24, 45.6, True }
print(stuff)

stuff.remove("Bob")
print(stuff)

#dictionaries ----->special type of set which stores data in key:value pairs

car = {"Brand" : "Toyota", "Model" : "Land cruiser", "Year" : 2024 , "Fuel_cc" : 2000}

print(car["Brand"])
print(car["Fuel_cc"])

for key in car:
    print(key)
for val in car.values():
    print(val)

del(car["Brand"])
print(car)
