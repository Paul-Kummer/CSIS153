#Paul Kummer
#CSIS 153
#Program 9
#Due 11/14/18

__author__="Paul Kummer"
__date__="11/14/18"

"""
Description:

V1:
This program allows the user to open a text file containing potential credit
card strings seperated by new lines to determine the following;
*type of credit card
*from right to left, sum of all doubled even location numbers or if the 
	resulting doubled number is greater than 9, the sum of the two numbers 
	composing the two digit number.
*from right to left, sum of all odd location numbers
*validity of the combination of card numbers
*validity of all aspects of the card number

After running tests on all the credit card numbers, the program will
display a table of all the information about the card analysis.


V2:
Added error checking for non-integers to each function to allow for better
unit testing without causing program failure.

V3:
Made evaluation functions only evaluate the indexes used for alpha characters
instead of the whole string. This allows better unit testing.
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
		return "N/A"

#Eval One
def reversedOddIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	oddIndexNumList = []
	alphaPresent = False
	
	for indexLocation in range (cardLen-2,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		if tmpNumStr.isdigit() is False:
			alphaPresent = True
			return -1
			
	if alphaPresent is False:
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
				oddIndexNumList.append(tmpNumInt*2)
		return sum(oddIndexNumList)


#Eval Two	
def reversedEvenIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	evenIndexNumList = []
	alphaPresent = False
	
	for indexLocation in range (cardLen-1,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		if tmpNumStr.isdigit() is False:
			alphaPresent = True
			return -1
		
	if alphaPresent is False:		
		for indexLocation in range (cardLen-1,-1,-2):
			tmpNumStr = cardNumStr[indexLocation]
			tmpNumInt = int(tmpNumStr)
			evenIndexNumList.append(tmpNumInt)
		return sum(evenIndexNumList)

		
def cardNumEvaluator (cardNumStr):
	returnValue = True
	
	for tmpChar in cardNumStr:
		if tmpChar.isdigit() is False:
			returnValue = False
	if returnValue is True:
		listOneEvalSum = reversedEvenIndexCardNumEvaluator(cardNumStr)
		listTwoEvalSum = reversedOddIndexCardNumEvaluator(cardNumStr)
		totalListSum = listOneEvalSum + listTwoEvalSum
		
		if totalListSum > 0:
			if totalListSum % 10 != 0:
				returnValue = False	
	
	return returnValue
			

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

	if root.fileName == ():
		print("User Canceled")
		root.destroy()
		quit()
		
	#check if the specified file is a legitimate file
	if isfile(root.fileName):
		
		#assign the name fileObj to root.fileName and open it as read only
		with open (root.fileName,"r") as fileObj:
			
			#turn the file object into a list of lines
			fileObjList = fileObj.readlines()
			fileObj.close()
			
			fileAsCardNumStrList = [tmpCardNumStr.replace("\n","") \
			for tmpCardNumStr in fileObjList if tmpCardNumStr != "\n"]
					
			
		#close any tk windows
		root.destroy()
		
		#return list of credit card numbers as strings
		return fileAsCardNumStrList
		
	#something unexpected happend and tk windows close and user is told file doesn't exist
	else:
		print("Files Does Not Exist")
		fileObj.close()
		root.destroy()
		quit()
		
	root.destroy()

def main():
	creditCardListFromFile = openAndConvertFileToList()
	validCreditCards = []
	invalidCreditCards = []
	
	#didn't use list comprehension to avoid iterating multiple times
	for tmpCreditCard in creditCardListFromFile:
		if isValidCreditCard(tmpCreditCard):
			validCreditCards.append(tmpCreditCard)
		else:
			invalidCreditCards.append(tmpCreditCard)
	
	print("\t#########################################")
	print("\t### Summary of Credit Cards from File ###")
	print("\t#########################################\n")
	print("*there are {:^.0f} valid Credit Cards and {:^.0f} invalid Credit Cards\n"\
	.format(len(validCreditCards),len(invalidCreditCards)))
	print("-----------------------------------------------------------------------------------------------")
	print("|{:^22s}|{:^12s}|{:^18s}|{:^12s}|{:^12s}|{:^12s}|".format\
	("Card Number","Card Length","Card Type","Eval Sum 1","Eval Sum 2","Validity"))
	print("-----------------------------------------------------------------------------------------------")
	
	#cannot use justification or type with boolean values in str.format
	#
	for tmpValidCard in validCreditCards:
		evenIndexValue = str(reversedEvenIndexCardNumEvaluator(tmpValidCard))
		oddIndexValue = str(reversedOddIndexCardNumEvaluator(tmpValidCard))
			
		print("|{:^22s}|{:^12.0f}|{:^18s}|{:^12s}|{:^12s}|{:^12}|".format\
	(tmpValidCard,len(tmpValidCard),getCardType(tmpValidCard),\
	evenIndexValue,oddIndexValue,"True"))
	
	for tmpInvalidCard in invalidCreditCards:
		
		#convert 
		if reversedEvenIndexCardNumEvaluator(tmpInvalidCard) < 0:
			evenIndexValue = "N/A"
		else:
			evenIndexValue = str(reversedEvenIndexCardNumEvaluator(tmpInvalidCard))
		
		#convert 	
		if reversedOddIndexCardNumEvaluator(tmpInvalidCard) < 0:
			oddIndexValue = "N/A"
		else:
			oddIndexValue = str(reversedOddIndexCardNumEvaluator(tmpInvalidCard))
			
		print("|{:^22s}|{:^12.0f}|{:^18s}|{:^12s}|{:^12s}|{:^12}|".format\
		(tmpInvalidCard,len(tmpInvalidCard),getCardType(tmpInvalidCard),\
		evenIndexValue,oddIndexValue,"False"))



if __name__ == "__main__":
	main()
