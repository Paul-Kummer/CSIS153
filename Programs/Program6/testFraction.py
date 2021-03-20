#Paul Kummer
#CSIS 153
#Program 6, testFile
#Due: 10/26/18

__author__="Paul Kummer"
__date__="10/22/18"

#description
"""
This program will test modFraction's ability to create class objects
of fractions. modFraction is reliant on modUsefulFuncs' 
greatestCommonDivisor function. greatestCommonDivisor function is also
tested as a result of testing modFraction's Fraction class
"""

from modFraction import *

f1 = Fraction(1,3)
print("Creating fraction of 1 over 3")
print(f1)

f2 = Fraction(2,8)
print("\nCreating fraction of 2 over 8")
print(f2)

f3 = Fraction(2,0)
print("\nCreating fraction of 2 over 0")
print(f3)

f4 = Fraction(3)
print("\nCreating fraction of 3")
print(f4)

f5 = Fraction()
print("\nCreating fraction of no value")
print(f5)

f6 = Fraction(-1,3)
print("\nCreating fraction of -1 over 3")
print(f6)

f7 = Fraction(1,-3)
print("\nCreating fraction of 1 over -3")
print(f7)

f8 = Fraction(0,3)
print("\nCreating fraction of 0 over 3")
print(f8)

f9 = Fraction(-10,-7)
print("\nCreating fraction of -10 over -7")
print(f9)

#Output
"""
Creating fraction of 1 over 3
1/3

Creating fraction of 2 over 8
1/4

Creating fraction of 2 over 0
0/1

Creating fraction of 3
3/1

Creating fraction of no value
0/1

Creating fraction of -1 over 3
-1/3

Creating fraction of 1 over -3
-1/3

Creating fraction of 0 over 3
0/1

Creating fraction of -10 over -7
10/7
"""

