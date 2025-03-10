#!/usr/bin/env python
from array import *

#arrays

ages = array('i',[23,45,67,78,89,29])# i = integers

print(ages)

ages.append(73)
ages.append(88)
ages.append(56)
print(ages)

ages.pop()
print(ages)

ages.reverse()
print(ages)
