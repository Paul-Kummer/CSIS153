#Paul Kummer
#CSIS 153
#Program 9
#Due 11/14/18

__author__="Paul Kummer"
__date__="11/14/18"

"""
Description:

"""

from tkinter import filedialog
from tkinter import *
from os.path import *

def getCardType (cardNumStr):
	if cardNumStr[0] == "4":
		return "Visa"
	
	elif cardNumStr[0] == "5":
		return "Mastercard"
		
	elif cardNumStr[0] == "6":
		return "Discover"
		
	elif cardNumStr[:2] == "37":
		return "American Express"
		
	else:
		return "Unknown"

def reversedOddIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	oddIndexNumList = []
	for indexLocation in range (cardLen-2,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		tmpNumInt = int(tmpNumStr)
		
		if tmpNumInt*2 > 9:
			doubledTmpNumInt = tmpNumInt*2
			
			firstTmpNumStr = str(doubledTmpNumInt)[0]
			secondTmpNumStr = str(doubledTmpNumInt)[1]
			
			firstTmpNumInt = int(firstTmpNumStr)
			secondTmpNumInt = int(secondTmpNumStr)
			
			newNumInt = firstTmpNumInt + secondTmpNumInt
			
			oddIndexNumList.append(newNumInt)
			
		else:
			oddIndexNumList.append(tmpNumInt)
			
		return sum(oddIndexList)
	
def reversedEvenIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	evenIndexNumList = []		
	for indexLocation in range (cardLen-1,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		tmpNumInt = int(tmpNumStr)
		evenIndexNumList.append(tmpNumInt)
		
	return sum(evenIndexNumList)
		
def cardNumEvaluator (cardNumStr):
	cardLen = len(cardNumStr)
	if cardNumStr.isdigit() == "False":
		return False
	else:
		listOneEvalSum = reversedEvenIndexCardNumEvaluator(cardNumStr)
		listTwoEvalSum = reversedOddIndexCardNumEvaluator(cardNumStr)
		totalListSum = listOneEvalSum + listTwoEvalSum
		
		if totalListSum % 10 == 0:
			return True
			
		else:
			return False
			

def isValidCreditCard (cardNumStr):
	availableCardTypes = ("Visa","Mastercard","Discover","American Express")
	cardLen = len(cardNumStr)
	cardType = getCardType(cardNumStr)
	
	if cardLen < 13 or cardLen > 16:
		return False
	
	elif cardType not in availableCardTypes:
		return False
		
	else:
		return cardNumEvaluator(cardNumStr)
		

def openAndConvertFileToList():

	#initialize tk
	root = Tk()
	
	#pop up a dialog box requesting a text file
	root.fileName = filedialog.askopenfilename(initialdir =".",title =\
	"Select file",filetypes =(("text files","*.txt"),("all files","*.*")))
	if root.fileName == "genericpath.py":
		print("User Canceled")
		root.destroy()
		quit()
	#check if the specified file is a legitimate file
	if isfile(root.fileName):
		
		#assign the name fileObj to root.fileName and open it as read only
		with open (root.fileName,"r") as fileObj:
			
			#turn the file object into a list of lines
			fileObjList = fileObj.readlines()
			
			fileAsCardNumStrList = [tmpCardNumStr.replace("\n","") \
			for tmpCardNumStr in fileObjList if tmpCardNumStr != "\n"]
					
			#close the file object
			fileObj.close()
			
		#close any tk windows
		root.destroy()
		
		#return the dictionary of keys of professor names and values of lists class names tied to a list of students
		return fileAsCardNumStrList
		
	#something unexpected happend and tk windows close and user is told file doesn't exist
	#or user selects cancel	
	else:
		print("Files Does Not Exist")
		root.destroy()
		quit()
		
	root.destroy()

def main():
	listFromFile = openAndConvertFileToList()
	print(listFromFile)
	
	print("MasterCard")
	testCardOne = "512345678912345"
	print("testCard 1: ",testCardOne,getCardType(testCardOne))
	
	print("\nVisa")
	testCardTwo = "412345678912345"
	print("testCard 1: ",testCardTwo,getCardType(testCardTwo))
	
	print("\nAmericanExpress")
	testCardThree ="3712345678912345"
	print("testCard 1: ",testCardThree,getCardType(testCardThree))
	
	print("\nDiscover")
	testCardFour = "612345678912345"
	print("testCard 1: ",testCardFour,getCardType(testCardFour))
	
	#testCardFive = input("\nEnter Card Num: ")



if __name__ == "__main__":
	main()






"""
Assignment:
Program 9 (30 pts) Fall 2018 Unit Testing and Credit Card Number Validation: The Luhn check or the Mod 10 check

In 1954, Hans Luhn of IBM proposed an algorithm for validating credit card numbers. The algorithm is useful to determine whether a card number is entered or scanned correctly.

To ensure that credit card numbers are valid:

    Check to see that the number has 13-16 digits

    For certain companies, must start with a particular number:

        Visa cards: must begin with 4

        Mastercard: must begin with 5

        American Express: must begin with 37

        Discover: must begin with 6


    Going from RIGHT to LEFT, double every second digit. If doubling a digit results in a two-digit number, add up the two digits to get a single-digit number.

    Then ADD all of these single-digit numbers together  sumSecondDigits.

    Next, going from RIGHT to LEFT, add all digits in the ODD places  sumOddPlaces.

    Add the sumSecondDigits to the sumOddPlaces.
    If the result is divisible by 10, the card number is valid. Otherwise, it is invalid.


Step 1: Write a function called isValidCreditCard that accepts a string and returns True if the string represents a valid credit card number and False if it is invalid. NOTE – the function should not print anything – it simply returns a boolean (True or False)


NOTE: the function MUST call other functions to complete its work. You should create at LEAST the following functions:

    A function that accepts a string and returns the sum of the digits in the even places doubled

    A function that accepts a string and returns the sum of the digits in odd places

    A function that accepts a string and returns the Prefix as a string (Visa, MC, Discover, AmEx).

    Others as you see fit


Step 2: Create a unit test for the isValidCreditCard function to thoroughly test the function and run it.

Some tests to consider:

- valid Discover
- valid Visa
- valid Mastercard
- valid American Express

- invalid: incorrect length – too short or too long

- invalid: incorrect opening digit(s) – must begin with 4,5,6 or 37

- invalid: totals of the sumSecondDigits and sumOddPlaces not divisible by 10




Step 3: Read credit card numbers from a textfile – use a tkinter File Open dialog and allow the user to select the file. BE SURE to check that the user actually selected a file instead of clicking Cancel.
If the user clicked cancel , simply end the program.
Example file:

123

12345678901234567

1234567890123a

91234567890123

412345678901234

612345678901234

512345678901234

371234567890123

4388576018402626

4388576018410707

6312345678901

6312345678902


Step 3: Create the following report – you are REQUIRED to use the format method!

Display the following for EACH credit card entered, print a report in tabular form:

CardNumber Length Prefix SumEvDbl SumOdd Valid?

4388576018410707 16 Visa 29 41 Yes

4388576018402626 16 Visa 37 38 No

4865 3 N/A N/A N/A No

12345678901234567 17 N/A N/A N/A N

Etc. – PLEASE PROVIDE THOROUGH TESTING!


Explanation of the terms and algorithm:

    CardNumber: the card number that was read from the text file

    Length: the number of characters in the cardnumber

    Prefix: Visa or Discover or AmEx or MasterCard or N/A if prefix wasn’t valid

    SumDblEvenPlace: the sum or N/A if not applicable

    sumOddPlace: the sum or N/A if not applicable

    Valid? yes if the entry is a valid credit card number, no if not.

NOTE: be sure to format the report it so that it is neatly presented in columns!

Example1:

CardNumber: 4388576018402626
Length: 16
Prefix: Visa
sumDblEvenPlace: 37

2*2 = 4, 2*2=4, 4*2 = 8, 1*2 = 2, 6*2 = 12 two digits, so add them and get 1+2 =3, 5*2 = 10 two digits, so add them and get 1+ 0 =1, 8*2 = 16 two digits, so add them and get 1+6 =7, 4*2 = 8
Sum: (4 + 4 + 8 + 2 + 3 + 1 + 7 +8)  37

sumOddPlace: 38 ( 6+6+0+8+0+7+8+3)
Valid?: No

Example2:

CardNumber: 4388576018410707
Length: 16
Prefix: Visa
sumDblEvenPlace: 29 ( 0 + 0+ 8 + 2 + 3 + 1 + 7 + 8 = 29)
sumOddPlace: 41
7 + 7 + 1 + 8 + 0 + 7 + 8 + 3 = 41
Valid: Yes (29 + 41 = 70 which is evenly divisible by 10)



Tentative Scoring Guide: 30 pts

10 pts Unit test – must provide THOROUGH TESTS OF ALL POSSIBILITIES
10 pts Format method used to create report with column headings and proper alignment, correct data for each card #
10 pts File Dialog, checks for CANCEL instead of selection of a file, closes the file when finished reading, properly reads the information from the file. 
"""
