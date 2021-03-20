#Paul Kummer
#CSIS 153
#Program 7 tests
#Due: 10/31/18

__author__="Paul Kummer"
__date__="10/27/18"

"""
Description:

This program tests modFraction second version for mathematical opeerations
including +, -, ==, /, //, ~, *. Additonally, it will be able to handle
any valid real numbers. When comparing equalities Fraction objects must
be the first argument.

Note: modFraction.py must be in working directory
"""

from modFraction import *

print("creating Fraction Objects: ")

f1 = Fraction(8,-7)
print("f1 = 8/-7:  ",f1)

f2 = Fraction(1,5)
print("f2 = 1/5:  ", f2)

f3 = Fraction(0,-5)
print("f3 = 0/-5:  ", f3)

f4 = Fraction(5,0)
print("f4 = 5/0:  ", f4)

f5 = Fraction(-4)
print("f5 = -4:  ", f5)

f6 = Fraction(-0)
print("f6 = -0:  ", f6)

f7 = Fraction(2/3)
print("f7 = (2/3)/1:  ", f7)

f8 = Fraction(-25,-100)
print("f8 = -25/-100:  ", f8)

f9 = Fraction(9,-3)
print("f9 = 9/-3:  ", f9)

f10 = Fraction(.5,.333)
print("f10 = .5/.333:  ", f10)

f11 = Fraction(float(1/3),float(5/9))
print("f11 = Fraction(float(1/3)/float(5/9)): ", f11,"\n")




print("(-25/-100) / (9/-3): ", f8/f9)
print(" (-25/-100) // (9/-3): ", f8//f9)
print("(8/-7) * (-4): ", f1*f5)
print("~(1/5) * (-25/-100): ", ~f2*f8)
print("(-25/-100) - (-25/-100): ", f8-f8)
print("(8/-7) - (9/-3): ", f1-f9)
print("(8/-7) + (9/-3): ", f1+f9)
print("(9/-3) + (0/-5): ", f9+f3)
print("8/-7 < 2: ", f1<2)
print("1/5 < 0/-5: ",f2<f3)
print("5/0 <= 2: ",f4<=2)
print("0/-5 <= -0: ", f3<=f6)
print("float(2/3) > 2: ", f7>2)
print("8/-7 > 1/5: ", f1>f2)
print("0/-5 >= 2: ", f3>=2)
print("5/0 >= -4: ", f4>=f5)
print("-0 = 7: ", f6==7)
print("8/-7 = 8/-7: ", f1==f1)
print("8/-7 not equal 2: ", f1!=2)
print("8/-7 not equal 8/-7: ", f1!=f1)
print("inverse 8/-7: ", ~f1)
print("inverse 1/5: ", ~f2)
print("float 0/-5: ", float(f3))
print("float 1/5: ", float(f2))
print("integer -4: ", int(f5))
print("integer 8/-7: ", int(f1))


print("\n\nTests from assignment:")
print("Creating Fraction Objects f1=(1/-3) f2=(2/8) f3=() f4=(2/-4): \n")
f1 = Fraction(1,-3); f2=Fraction(2,8); f3=Fraction( ); f4 = Fraction(2,-4)


print("Testing ADD")

print("f1+f2: ",f1 + f2)

print("f1+f4: ",f1 + f4)
print("f1+f3: ",f1 + f3)

print("Bonus Fraction(1/-3)+int(5): ", f1 + 5)


print("\nBONUS: Testing EQ")

print("Fraction(4,3)=Fraction(3,9): ",Fraction(4,3) == Fraction(3,9))

print("Fraction(6,18)=Fraction(3,9): ",Fraction(6,18) == Fraction(3,9))


print("\nBONUS -- Testing float")

print("float(Fraction(4,3)): ", float(Fraction(4,3)))

print("\nnew tests:")

t1 = Fraction(4,8)
print("creating t1 as Fraction(4,8)\n",t1)

t2 = Fraction(1,3)
print("creating t2 as Fraction(1,3)\n",t2)
print("t1-t2: ",t1-t2)
print("t1//t2: ",t1//t2)






"""
Output:

creating Fraction Objects: 
f1 = 8/-7:   -8/7
f2 = 1/5:   1/5
f3 = 0/-5:   0/1
f4 = 5/0:   0/1
f5 = -4:   -4/1
f6 = -0:   0/1
f7 = (2/3)/1:   6004799503160661/9007199254740992
f8 = -25/-100:   1/4
f9 = 9/-3:   -3/1
f10 = .5/.333:   9007199254740992/5998794703657501
f11 = Fraction(float(1/3)/float(5/9)):  6004799503160661/10007999171934436 

(-25/-100) / (9/-3):  -1/12
 (-25/-100) // (9/-3):  -1/12
(8/-7) * (-4):  32/7
~(1/5) * (-25/-100):  5/4
(-25/-100) - (-25/-100):  0/1
(8/-7) - (9/-3):  13/7
(8/-7) + (9/-3):  -29/7
(9/-3) + (0/-5):  -3/1
8/-7 < 2:  True
1/5 < 0/-5:  False
5/0 <= 2:  True
0/-5 <= -0:  True
float(2/3) > 2:  False
8/-7 > 1/5:  False
0/-5 >= 2:  False
5/0 >= -4:  True
-0 = 7:  False
8/-7 = 8/-7:  True
8/-7 not equal 2:  True
8/-7 not equal 8/-7:  False
inverse 8/-7:  -7/8
inverse 1/5:  5/1
float 0/-5:  0.0
float 1/5:  0.2
integer -4:  -4
integer 8/-7:  -1


Tests from assignment:
Creating Fraction Objects f1=(1/-3) f2=(2/8) f3=() f4=(2/-4): 

Testing ADD
f1+f2:  -1/12
f1+f4:  -5/6
f1+f3:  -1/3
Bonus Fraction(1/-3)+int(5):  14/3

BONUS: Testing EQ
Fraction(4,3)=Fraction(3,9):  False
Fraction(6,18)=Fraction(3,9):  True

BONUS -- Testing float
float(Fraction(4,3)):  1.3333333333333333

new tests:
t1-t2:  1/6
t1//t2:  3/2

"""
