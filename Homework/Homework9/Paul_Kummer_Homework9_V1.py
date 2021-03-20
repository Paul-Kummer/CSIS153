#Paul Kummer
#CSIS 153
#Homework 10 Version2
#Due: 10/22/18

__author__ = "Paul Kummer"
__date__  = "10/17/18"

#assignment
"""
Design a class called Account with the following methods:
+Constructor (tmpAcctNum, tmpBankName, tmpAcctType, and tmpBalance):void

__str__( ): str
Description:  prints the information for the account one item per line. For example:
Account #:   	100
Bank:		NorWest
Account Type:	Checking
Balance:	$150.98

computeInterest( ):float –should update the balance AND return the amount of interest.

getters/setters for each of these:  accountNum, bankName, accountType, balance

Version 1 of the Account class:  private data is a list that stores the account number, bank name, account type, and balance.

Version2 of the Account class: private data is stored as separate variables.
OPTIONAL Version 3 of the Account class: private data is stored as a tuple that stores the account number, bank name, account type, and balance.
Create a test program that works with all versions of the Account class, regardless of the way the private data was stored in the class.
Suggestion:
Create 3 modules for the 3 different versions of the Account class.  Be sure that the class itself is always called Account in each of the modules – only the module name should change.
Your testing should provide the SAME code for all 3 versions, except that you’ll use a different import statement for each.
"""


class Account:
	def __init__ (self,tmpAcctNum,tmpBankName,tmpAcctType,tmpBalance):
		self._tmpAcctNum = tmpAcctNum
		self._tmpBankName = tmpBankName
		self._tmpAcctType = tmpAcctType
		self._tmpBalance = tmpBalance
		
	def __str__ (self):
		strToReturn = "Account #:	{:<10.0f}\nBank:	{:<10s}\nAccount Type:	{:<10s}\nBalance:	${:<10.2f}"\
.format(self._tmpAcctNum,self._tmpBankName,self._tmpAcctType,self._tmpBalance))
		
		return strToReturn
		
	def getAcctNum(self):
		return self._tmpAcctNum
		
	def getBankName(self):
		return self._tmpBankName
		
	def getAcctType(self):
		return self._tmpAcctType
		
	def getBalance(self):
		return self._balance
		
	def setAcctNum(self,newAcctNum):
		self._tmpAcctNum = newAcctNum
		
	def setBankName(self,newBankName):
		self._tmpBankName = newBankName
		
	def setAcctType(self,newAcctType):
		self._tmpAcctType = newAcctType
		
	def setBalance(self,newBalance):
		self._tmpBalance = newBalance
		
	def computeIntrest(self):
		
		
