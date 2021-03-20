#Paul Kummer
#CSIS 153 Fall 2018
#Homework 2
#Due September 5

__author__ = "Paul Kummer"
__date__ = "9/04/2018"


#Problem 1:
 
def calcAvg(listOfNums):
		
		#can't use built in names like "sum"
        runningTotal=0
		
		#need to check if the list is empty before calcualting average to avoid divide by zero
        if len(listOfNums) > 0:
                count=len(listOfNums)

                for num in listOfNums:
                        runningTotal+=num

                averageOfList= int(runningTotal)/int(count)
                print("The average of the List is: ",averageOfList)
                
        else:
                print("There is nothing in the list")

numberList=[4,2,6,7,8,0]               
calcAvg(numberList)


#Problem 2:

#if user enters a non integer the program will error
score = input("Enter a score: ")

if score.isdigit():
	
	#convert user input to a integer only after input is validated as
	#and integer
	score = int(score)
	
	#"elif" follows "if" statments
	#when using "and" the variable being compared needs to be 
	#specified which is "score" being compared to 90 and 100
	if score >=90 and score <=100:print("A")
	elif score >=80:print("B")
	elif score >=70:print("C")
	elif score >=60:print("D")	
	elif score <60 and score >=0:print("F")	
	else:print("Score Out of Range")
	
else:print("Score must be an integer")
	

#Problem 3:

#if user enters a non integer the program will error if "int()" is used
#around input()
score = input("Enter a score: ")

if score.isdigit():
	
	score = int(score)

	#the largest value needs to come first, otherwise the program will
	#assign "D" first. Also, this programs allows for impossible scores
	if score >=90:print("A")
	elif score >=80:print("B")
	elif score >=70:print("C")
	elif score >=60:print("D")
	else:print("F")	
else:print("Score must be an integer")


#Problem 4:

phone = input("Phone: ###-###-#### or (###)###-#####: ")
print(len(phone))
if len(phone)!=int(12) and len(phone)!=int(13):
	print("invalid number-try again: ")
	
	#loop that ensures users enter a valid phone number length		
	validPhone = False
	while validPhone == False:
		phone = input()
		if len(phone)!=12 or len(phone)!=13:
			print("invalid number-try again: ")
		else:
			validPhone=True
else:
	print("valid entry")
		

#Problem 5:

"""count # of words with more than 5 characters"""

sentence = input("Enter a sentence: ")

#looked up from https://stackoverflow.com "list" splits the words into
#letters
wordList = sentence.split()

ct=0
for word in wordList:
	if len(word) >5:
		ct+=1
print(ct)


#Problem 6:

"""Print the # of vowels in a sentence entered by the user. NOTE: case
shouldn't matter. Hint-use the "in" operator if sentence is "HELLO There
Andy" the output is 5"""

sentence=input("enter a sentence: ")
ct=0
letterList = list(sentence)
for letter in letterList:
	letter = letter.upper()
	if letter=="A" or letter=="E" or letter=="I" or letter=="O" or\
	letter == "U":
		ct+=1
	
print("there are ", ct, " vowels in the sentence")


#Problem 7:

"""Ask the user to continue entering #'s until they type DONE. Print the
AVERAGE of the number entered by the user that were EVEN."""
numList=[]

stopLoop = False
while stopLoop == False:
	num=input("Please enter a number: ")
	if num.isdigit():
		numList.append(num)
		
	elif num.isalpha():
		num=num.upper()
		if num == "DONE":
			stopLoop=True
ct = 0
if len(numList) > 0:
	for num in numList:
		ct+=int(num)
	avg=int(ct)/len(numList)
	print("Average is: ",int(avg))
else:
	print("No Values Entered")


#Problem 8:

#Information on datetime found from: https://stackoverflow.com
import datetime
currentDate = datetime.datetime.now()
currentYear = currentDate.year

def getCommissionRate(yearHired):
	yearHired = str(yearHired)
	if yearHired.isdigit():
		if int(yearHired) < 0:
			print("Cannot be hired negative years")
		else:
			yearsWorked = int(currentYear)-int(yearHired)
			if yearsWorked > 20:
				return (float(.10))
			elif yearsWorked > 10:
				return(float(.05))
			else:
				return(float(.02))

	else:
		print("yearHired is not an integer")
		
currentCommisssion = getCommissionRate(1990)		
		
		
#Problem 9:

positiveNumList = []
negativeNumList = []
isNumber=False
while isNumber == False:
	enteredNum = input("Enter a Number: ")
	if enteredNum.isdigit():
		positiveNumList.append(enteredNum)

	elif enteredNum[0] == "-" and (enteredNum[1:]).isdigit():
		if int(enteredNum[1:])==999:
			isNumber=True
		else:
			negativeNumList.append(enteredNum[1:])
			
positiveCt=0
for pos in positiveNumList:
	positiveCt+=int(pos)

negativeCt=0
for neg in negativeNumList:
	negativeCt+=int(neg)

print(int(positiveCt)-int(negativeCt))


#Problem 10:

total=0
numFound=0

for ct in range(2,21,3):
	print("ct: ",ct)
	
	total+=ct
	if(ct%2==0)or(ct%5==0):
		print("numFound: ",numFound)
		numFound += 1
	print("sum: ",total)
	
#Program Execution
"""
ct:  2
numFound:  0
sum:  2
ct:  5
numFound:  1
sum:  7
ct:  8
numFound:  2
sum:  15
ct:  11
sum:  26
ct:  14
numFound:  3
sum:  40
ct:  17
sum:  57
ct:  20
numFound:  4
sum:  77


------------------
(program exited with code: 0)
Press return to continue
"""
