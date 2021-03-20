#Paul Kummer
#CSIS 153 4:15-4:45PM
#Homework 9
#Due: 10/19/18

__author__="Paul Kummer"
__date__="10/18/18"

#description
"""
This program will test two classes from modStudent to ensure that the 
class objects are created correctly. The class Student is a subclass of
person
"""

from modStudent_V2 import *

numStudents = Student.getStuCt()
print("Initial Number of Students: ",numStudents)
s1=Student("Jones","Joe",3.5)
print("\nCreated s1: ",s1)
print("Number of students after s1 created: ",Student.getStuCt())
print("s1 Person ID: ",s1.getPersonID())

print("\nLast Name of s1: ",s1.getLastName())
print("ID of s1: ",s1.getStudentID())
s1.setLastName("Smith")
s1.setGPA(4.0)
print("s1 after changing last name and gpa: ",s1)


s2=Student("Brown","Rachael",3.6)
print("\nCreated s2: ",s2)
print("Number of students after creating s2: ",Student.getStuCt())
print("s2 Person ID: ",s2.getPersonID())

p1=Person("Kummer","Paul")
print("\nCreated p1: ")
print(p1)
print("Numer of people after creating p1: ",Person.getPopulation())

print("\nFinal number of students: ",Student.getStuCt())

#output
"""
Initial Number of Students:  0

Created s1:  0    Jones     Joe       3.5
Number of students after s1 created:  1
s1 Person ID:  0

Last Name of s1:  Jones
ID of s1:  0
s1 after changing last name and gpa:  0    Smith     Joe       4.0

Created s2:  1    Brown     Rachael   3.6
Number of students after creating s2:  2
s2 Person ID:  1

Created p1: 
Person ID: 2    
Name: Paul      Kummer    
Numer of people after creating p1:  3

Final number of students:  2
"""
