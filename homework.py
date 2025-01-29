#!/usr/bin/env python

#calculate the speed of a vehicle
distance = 3600
time = 30
speed = distance / time

print("The speed of a vehicle travelling for {0}km in {1}hrs is {2}km/h".format(distance,time,speed))

#calculate the volume and surface area of a closed cylinder
pie = 3.142
radius = 50 
height = 30
variable = 2
volume = pie * radius * radius * height
circumference = pie * radius * variable
surface_area1 = variable * pie * radius * radius 
surface_area2 = circumference * height 
surface_area3 = surface_area1 + surface_area2

print("The volume of the closed cylinder is {0}cm3 and the surface area is {1}cm2".format(volume,surface_area3))

# calculate the pressure applied to a surface when a force of 120N acts on a square surface of 200cm
force = 120 
area = 2
pressure = force / area

print("The pressure which acts on the surace is {0}N/m2".format(pressure))

