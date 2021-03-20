#Paul Kummer
#CSIS 153
#Homework 10
#Due: 10/22/18

__author__="Paul Kummer"
__date__="10/18/18"

#Program Description
"""
test both versions of modAcct to demonstrate how the class
methods operate the same to the end user despite changing how the 
information is stored

Information for account class:
(tmpAcctNum=000000,tmpBankName="Default",tmpAcctType="Default",tmpBalance=0.00,tmpIntrest=0.00)
"""


from modAcctV1 import Account
#from modAcctV2 import Account



accountOne = Account(123456,"US Bank","Savings",22436.24)
print("account one info:")
print(accountOne)

intrest=accountOne.computeIntrest(.10)
print("\nadded 10% intrest:",intrest)
print(accountOne)

accountTwo = Account()
print("\naccount two info:")
print(accountTwo)

print("\nsetting account 2 num to: 6543210")
accountTwo.setAcctNum(6543210)
print("setting account 2 bank to: Gate City Bank")
accountTwo.setBankName("Gate City Bank")
print("setting account 2 type to: Checking")
accountTwo.setAcctType("Checking")
print("setting account 2 balance to: $200.10")
accountTwo.setBalance(200.10)
print("\nadding 25% intrest to account 2")
print(accountTwo.computeIntrest(.25))
print("\naccount two information:\n")
print(accountTwo)

#Output from both versions
"""
account one info:
Account #:	123456    
Bank:		US Bank   
Account Type:	Savings   
Balance:	$22,436.24 

added 10% intrest: $2243.62
Account #:	123456    
Bank:		US Bank   
Account Type:	Savings   
Balance:	$24,679.86 

account two info:
Account #:	0         
Bank:		Default   
Account Type:	Default   
Balance:	$0.00      

setting account 2 num to: 6543210
setting account 2 bank to: Gate City Bank
setting account 2 type to: Checking
setting account 2 balance to: $200.10

adding 25% intrest to account 2
$50.03

account two information:

Account #:	6543210   
Bank:		Gate City Bank
Account Type:	Checking  
Balance:	$250.12 
"""





