#Paul Kummer
#CSIS 153 Fall 2018
#Homework 3 Part1
#Due: 9/10/18

__author__ = "Paul Kummer"
__date__ = "09/09/2018"


#Problem1
myString = "Good Day"
print(myString[2:4])

#Output
"""
od
"""


#Problem2
midInit = input("Enter Your Middle Initial: ")

isInitialUpper = midInit.isupper()
print(isInitialUpper)

#Output
"""
True
"""


#Problem3
sentence = input("Please enter a sentence: ")

ctOfThe = sentence.count("the")
print(ctOfThe)

#Output
"""
Please enter a sentence: the world is the best
2
"""


#Problem4
book = "the grapes of wrath"

book2 = str(book)
print(book2)

#Output
"""
the grapes of wrath
"""


#Problem5
sent = input("Enter a sentence: ")

listOfSent = sent.split()
print(listOfSent)

#Output
"""
Enter a sentence: this is the sentence
['this', 'is', 'the', 'sentence']
"""


#Problem6
emailAdr = input("Email Address: ")

validateEmailEdu = emailAdr.endswith("edu")
print(validateEmailEdu)

#Output
"""
Email Address: pakummer@gmail.com
False

Email Address: pakummer@gmail.edu
True
"""


#Problem7
emailAdr = input("Email Address: ")

locOfLastPeriod = emailAdr.rfind(".")
print(locOfLastPeriod)

#Output
"""
Email Address: pa.kummer@hotmail.com
17
"""


#Problem8
example = "snow world"
example[3] = "s"
print(example)

#Output:  Strings are immuttable, however variable are able to be changed to a different string value
"""
Traceback (most recent call last):
  File "temp.py", line 2, in <module>
    example[3] = "s"
TypeError: 'str' object does not support item assignment
"""


#Problem9
#Citation: https://thehelloworldprogram.com/python/python-variable-assignment-memory-location/
tmp = "Hello"

print(id(tmp))

#Output
"""
3071805984
"""


#Problem10
print("hello"+1+2+3)

#Output
"""
Traceback (most recent call last):
  File "temp.py", line 1, in <module>
    print("hello"+1+2+3)
TypeError: Can't convert 'int' object to str implicitly

"""

print("hello"+"1"+"2"+"3")
print("hello"+str(1+2+3))

#Output
"""
hello123
hello6
"""


#Problem11
print('**{0:.2f}**'.format(1/3))

#Output
"""
**0.33**

"""


#Problem12
result = "#{:10s}#{:4d}#{:6.2f}".format("Hi",111,924.655)
print(result)

#Output
"""
#Hi        # 111#924.65
"""
