#Paul Kummer
#CSIS 153
#Homework 10 Version1
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
	def __init__ (self,tmpAcctNum=000000,tmpBankName="Default",tmpAcctType="Default",tmpBalance=0.00,tmpIntrest=0.00):
		self._tmpAcctList = [tmpAcctNum,tmpBankName,tmpAcctType,tmpBalance,tmpIntrest]
		
	def __str__ (self):
		strToReturn = "Account #:	{:<10.0f}\nBank:		{:<10s}\nAccount Type:	{:<10s}\nBalance:	${:<10.2f}"\
.format(self._tmpAcctList[0],self._tmpAcctList[1],self._tmpAcctList[2],self._tmpAcctList[3])
		
		return strToReturn
		
	def getAcctNum(self):
		return self._tmpAcctList[0]
		
	def getBankName(self):
		return self._tmpAcctList[1]
		
	def getAcctType(self):
		return self._tmpAcctList[2]
		
	def getBalance(self):
		return self._tmpAcctList[3]
		
	def setAcctNum(self,newAcctNum):
		self._tmpAcctList[0] = newAcctNum
		
	def setBankName(self,newBankName):
		self._tmpAcctList[1] = newBankName
		
	def setAcctType(self,newAcctType):
		self._tmpAcctList[2] = newAcctType
		
	def setBalance(self,newBalance):
		if self._tmpAcctList[3]!=0:
			intrestRate = (newBalance-self._tmpAcctList[3])/self._tmpAcctList[3]
		else:
			intrestRate = 1
		self._tmpAcctList[4] = intrestRate*self._tmpAcctList[3]
		self._tmpAcctList[3] = newBalance
		
	def computeIntrest(self,intrestRate):
		self._tmpAcctList[4] = intrestRate*self._tmpAcctList[3]
		newBalance = self._tmpAcctList[3]*(1+intrestRate)
		self.setBalance(newBalance)
		return "${:<.2f}".format(self._tmpAcctList[4])
		
