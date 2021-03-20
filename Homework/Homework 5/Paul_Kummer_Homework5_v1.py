#Paul Kummer
#CSIS 153 Fall 2018
#Due Sept 17

__author__ = "Paul Kummer"
__date__="9-16-18"

#Globals
empDict = {}
empList = []


#Dictionary
#Problem1
moreEntries = True

while moreEntries:
	userName = input("Please Enter User Name or Done to exit: ")

	if userName.upper() == "DONE":
		moreEntries = False

	else:
		empDict[input("Please Enter User ID: ")]=userName

print("Finished adding Users and ID's")

#Problem2
selectedUser = input("What user would you like to see their ID: ")
userExists = False

for userID in empDict:
	currentUser = empDict[userID]
	if currentUser == selectedUser:
		print("User: ",selectedUser,"\tID: ",userID)
		userExists = True
		
if userExists != True:
	print("Name Not Found")

	
#Problem3
selectedID = input("What ID would you like to delete? ")

if selectedID in empDict:
	del empDict[selectedID]
	print("ID ",selectedID," Deleted")
		
else:
	print("No delete - ID not found")	

	
#Problem4
selectedID = input("What ID would you like to revise the user's name? ")

if selectedID in empDict:
	currentUser = empDict.pop(selectedID)
	newName = input("What would you like the new name to be? ")
	print("User ",currentUser," revised to ",newName)
	empDict[selectedID]=(newName)
		
else:
	print("No revision - ID not found")	


#Problem5
print("{:14s}\t\t{:14s}".format("ID","User"))
for tmpKey in empDict:
	print("{:14s}\t\t{:14s}".format(tmpKey,empDict[tmpKey]))


#Output from Dictionaries
"""
Please Enter User Name or Done to exit: Paul
Please Enter User ID: 1234
Please Enter User Name or Done to exit: 
Please Enter User ID: 
Please Enter User Name or Done to exit: Doug     
Please Enter User ID: 4321
Please Enter User Name or Done to exit: donE
Finished adding Users and ID's
What user would you like to see their ID: Doug
User:  Doug 	ID:  4321
What ID would you like to delete? none
No delete - ID not found
What ID would you like to revise the user's name? 4321
What would you like the new name to be? bob
User  Doug  revised to  bob
ID            		User          
              		              
4321          		bob           
1234          		Paul  
"""




#List
#Problem1
moreEntries = True

while moreEntries:
	userName = input("Please Enter User Name or Done to quit: ")
	
	tmpList = []
	
	if userName.upper() == "DONE":
		moreEntries = False
		
	else:
		tmpList.append(userName)
		tmpList.append(input("Please Enter User ID: "))
		empList.append(tmpList)

print("Finished Adding Entries")

#Problem2
selectedUser = input("Please Enter User Name to View ID: ")

userExists = False
for tmpList in empList:
	if selectedUser == tmpList[0]:
		userExists = True
		print("User: ",tmpList[0],"\tID: ",tmpList[1])

if userExists != True:
	print("Name Not Found")
	
#Problem3
selectedID = input("Please enter an ID to delete: ")

idExists = False
listToRemove = []

for tmpList in empList:
	tmpName = tmpList[0]
	tmpID = tmpList[1]
	
	if tmpID == selectedID:
		idExists = True
		listToRemove = tmpList
	
if idExists:
	empList.remove(listToRemove)
	print(selectedID," removed from list")
	
else:
	print("No delete - name not found")
	
#Problem4
selectedID = input("Please enter an ID to revise the user's name: ")

idExists = False
listToAppend = []
newName = ""

for tmpList in empList:
	tmpName = tmpList[0]
	tmpID = tmpList[1]
	
	if tmpID == selectedID:
		idExists = True
		listToAppend = tmpList
		newName = input("Please Enter New User Name: ")
	
if idExists:
	listToChange = empList[empList.index(listToAppend)]
	listToChange[0] = newName
	
else:
	print("ID Not Found")
	
#Problem5
print("{:14s}\t\t{:14s}".format("User","ID"))
for tmp in empList:
	currentUser = tmp[0]
	currentID = tmp[1]
	print("{:14s}\t\t{:14s}".format(currentUser,currentID))
	
	
	
#Output for Lists
"""
Please Enter User Name or Done to quit: Paul
Please Enter User ID: 1234
Please Enter User Name or Done to quit: Doug
Please Enter User ID: 4321
Please Enter User Name or Done to quit: 
Please Enter User ID: 12121
Please Enter User Name or Done to quit: DoNE
Finished Adding Entries
Please Enter User Name to View ID: 121212
Name Not Found
Please enter an ID to delete: 
No delete - name not found
Please enter an ID to revise the user's name: 
ID Not Found
User          		ID            
Paul          		1234          
Doug          		4321          
              		12121  
"""
