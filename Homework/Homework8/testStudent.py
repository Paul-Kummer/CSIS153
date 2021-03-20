from modStudent import Student

numStudents = Student.getStuCt()
print("Initial Number of Students: ",numStudents)
s1=Student("Jones","Joe",3.5)
print("Created s1: ",s1)

numStudents=Student.getStuCt()
print("\nNumber of students after s1 created: ",numStudents)

print("\nLast Name of s1: ",s1.getLastName())
print("ID of s1: ",s1.getID())
s1.setLastName("Smith")
s1.setGPA(4.0)
print("s1 after changing last name and gpa: ",s1)

s2=Student("Brown","Rachael",3.6)
print("\nCreated s2: ",s2)
print("Number of students after creating s2: ",Student.getStuCt())
