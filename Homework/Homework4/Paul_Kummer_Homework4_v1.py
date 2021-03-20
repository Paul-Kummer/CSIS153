#Paul Kummer
#CSIS 153 Fall 2018
#Homework 4
#Due: 9/10/18

__author__ = "Paul Kummer"
__date__ = "09/09/2018"


#Problem1
tmp = "John Doe";print(tmp[5:])

#Output
"""
Doe
"""

#Problem2
sentence = "Hi Bye"
tmp = list(sentence)
print(tmp)

#Output
"""
['H', 'i', ' ', 'B', 'y', 'e']
"""

#Problem3
print(sentence.count("e"))

#Output
"""
1
"""

#Problem4
nameList=["Doe","John"]
name=','.join(nameList)
print(name)

#Output
"""
Doe,John
"""

areaCode = "701"; prefix = "477"; last="2339"
myTuple = (areaCode,prefix,last)

phoneNumber = "-".join(myTuple)
print(phoneNumber)

#Output
"""
701-477-2339
"""

#Problem5
def myLen(tmpStr):
	return(len(tmpStr))
	
print(myLen("Paul"))

#Output
"""
4
"""

#Problem6
def maleOrFemale(tmpName):
	if tmpName.startswith("Mr."):
		return("Male")
	else:
		return("Female")
		
print(maleOrFemale("Mr. Paul Kummer"))

#Output
"""
Male
"""

#Problem7
tmp = "$5,234"
#tmp is stripped of "$" then put in a list sepperated by ",", next the list is concatenated, followed by conversion to integer, finally it is multiplied by two.
num = (int("".join(tmp.strip("$").split(",")))*2)

print(num)

#Output
"""
10468
"""

#Problem8
def myIsDigit(tmpStr):
	validDigit = True
	for char in tmpStr:
		if char.isalpha():
			validDigit = False
	return(validDigit)
			
print(myIsDigit(input("Enter something: ")))

#Output
"""
Enter something: 1234
True
"""

def myIsDigitTwo(tmpStr):
	numTuple = ("1","2","3","4","5","6","7","8","9","0")
	tmpLen = len(tmpStr)
	numCt = 0
	for char in tmpStr:
		if char in numTuple:
			numCt += 1
	if tmpLen == numCt:
		return(True)
	else:
		return(False)
			
print(myIsDigitTwo(input("Enter something: ")))
			
#Output
"""
Enter something: 12ab
False
"""	

#Problem9
str1 = "aeiou"; str2 = "12345"
myTable = str.maketrans(str1,str2)
sentence = "This is not all one unit"
sentence = sentence.translate(myTable)
print(sentence)

#Output
"""
Th3s 3s n4t 1ll 4n2 5n3t
"""

#Problem10
intab = "!?,"; outtab=".."
#Create translation table
table = str.maketrans(intab,outtab)
sentence="This is funny! This, is not?"
result=sentence.translate(table)
print(result)

#Output
"""
Traceback (most recent call last):
  File "temp.py", line 3, in <module>
    table = str.maketrans(intab,outtab)
ValueError: the first two maketrans arguments must have equal length
"""

#added one more "." to outtab to make lenght the same as intab
intab = "!?,"; outtab="..."
#Create translation table
table = str.maketrans(intab,outtab)
sentence="This is funny! This, is not?"
result=sentence.translate(table)
print(result)
			
#Output
"""
This is funny. This. is not.
"""
