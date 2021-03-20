#Paul Kummer
#CSIS 153 Fall 2018
#Program 1
#Due September 5

#Program Description:
"""
This program will prompt the user to input an employees first name, last name, and phone number. The program also validates
phone number entry to ensure it is a valid United States phone number format. Once the user is done and enters a not case-sensitive
form of "done", the program will display all the information collected in myEmployees list in a labeled visual table
"""


#list to store user entry of employee first name, last name, and phone number
myEmployees = []

#checks if user inputed correct phone number
def isValidPhone (phoneNumber):
	
	#checks if phone number is long and if true calls isValidLongPhone() function and returns True or False
	if len(phoneNumber) == int(14):
		
		phoneLong = isValidLongPhone(phoneNumber)
		return(phoneLong)

	#checks if phone number is medium and if true calls isValidMedPhone() function and returns True or False	
	elif len(phoneNumber) == int(13):
		
		phoneMed = isValidMedPhone(phoneNumber)
		return(phoneMed)

	#checks if phone number is short and if true calls isValidShortPhone() function and returns True or False						
	elif len(phoneNumber) == int(12):
		
		phoneShort = isValidShortPhone(phoneNumber)
		return(phoneShort)
	
	#if the user entered phone length isn't between 12 and 14 characters
	#the function returns False
	else:
		print("Phone number length is out of Range, please try again\n")
		return(False)

#checks validity of only long phone numbers 14 characters long
def isValidLongPhone (phoneNumber):
	
	#checks for whitespace at index 5 and returns false if not
	if phoneNumber[5].isspace() == False:
		print("\nPhone number contains incorrect characters, please leave space after parenthesis")
		return(False)
	
	#checks for parenthesis at index 0 and 4 and returns false if not	
	elif phoneNumber[0] != "(" or phoneNumber[4] != ")":
		print("\nPhone number contains incorrect characters, please try using parenthesis")
		return(False)

	#checks index (1-3), (6-8), and (10-13) to ensure they are all integers and  returns false if not
	elif phoneNumber[1:4].isdigit() == False or phoneNumber[6:9].isdigit() == False or phoneNumber[10:].isdigit()== False:
		print("\nPhone number must consist of integers, please try again")
		return(False)
	
	#checks for hypen at index 9 and return false if not
	elif phoneNumber[9] != "-":
		print("\nPhone number contains incorrect characters, please try using hypens")
		return(False)
		
	#if the long phone number makes it through all checks the function returns true	
	else:
		return(True)

#checks validity of only medium phone numbers 13 characters long			
def isValidMedPhone (phoneNumber):
	
	#checks for parenthesis at index 0 and 4 and returns false if not
	if phoneNumber[0] != "(" or phoneNumber[4] != ")":
		print("\nPhone number contains incorrect characters, please try using parenthesis")
		return(False)

	#checks index (1-3), (5-7), and (9-12) to ensure they are all integers and  returns false if not
	elif phoneNumber[1:4].isdigit() == False or phoneNumber[5:8].isdigit() == False or phoneNumber[9:].isdigit()== False:
		print("\nPhone number must consist of integers, please try again")
		return(False)
		
	#checks for hypen at index 8 and return false if not		
	elif phoneNumber[8] != "-":
		print("\nPhone number contains incorrect characters, please try using hypens")
		return(False)
	
	#if the long phone number makes it through all checks the function returns true		
	else:
		return(True)

#checks validity of only short phone numbers 12 characters long	
def isValidShortPhone(phoneNumber):
	
	#checks for hypen at index 3 and 7 and return false if not	
	if phoneNumber[3] != "-" or phoneNumber[7] != "-":
		print("\nPhone number contains incorrect characters, please try using hypens")
		return(False)
	
	#checks index (1-3), (4-6), and (8-11) to ensure they are all integers and  returns false if not		
	elif phoneNumber[0:3].isdigit() == False or phoneNumber[4:7].isdigit() == False or phoneNumber[8:].isdigit() == False:
		print("\nPhone number must consist of integers, please try again")
		return(False)
	
	#if the long phone number makes it through all checks the function returns true		
	else:
		return(True)

#main line of logic for program
def main ():
	
	#ask for user to input the employee's last name first, allowing them to exit right away if desired
	print("Please enter employee\'s last name or \"done\" to exit: ")
	lastName = input()
	
	#sentinel for while loop, when isDone == True the loop will stop
	isDone = False
	
	#creates a loop that asks for employee last name, first name, and phone number. Exists only when last name is done
	while isDone == False:
		
		#checks if the user inputed done for a last name, which will exit the program and print out data accumulated
		if str(lastName.upper()) == str("DONE"):
			
			#create a visual table displaying user inputed data
			print(myEmployees)
			print("\n\tEntry Complete\n\n")
			print("First\t\tLast\t\t\tPhone\n")
			print("Name\t\tName\t\t\tNumber\n")
			print("===================================================================\n")
			
			#iterate through every user entry in myEmployees, which is a list within a list
			for person in myEmployees:
				
				#easily identifiable variables for index locations of the current list
				personFirstName = person[2]
				personLastName = person[1]
				personPhone = person[0]
				
				#visually display the user data in the current list
				print(personFirstName,"\t\t", personLastName,"\t\t", personPhone,"\n")
			isDone = True
		
		#if the last name isn't done, the user is asked to enter first name and phone number
		else:
			print("\nPlease enter employee\'s first name")
			firstName = input()
			
			print("\nPlease enter employee\'s phone number")
			empPhone = input()
			
			#sentinel for phone validation loop, the initial value of true or false is determined by the function isValidPhone()
			validPhone = isValidPhone(empPhone)
			
			#loop that ensures users enter a valid phone number. Only exits once user has correctly entered a phone number
			while validPhone == False:
				empPhone = input()
				validPhone = isValidPhone(empPhone)
				
			#erases any previous entries in newEmpEntry then appends the empty list with the most current information entered	
			newEmpEntry = []	
			newEmpEntry.append(empPhone)			
			newEmpEntry.append(lastName)
			newEmpEntry.append(firstName)
			
			#adds the current newEmpEntry list to the myEmployees list
			myEmployees.append(newEmpEntry)	
			
			#allows the users to exit the user entry loop			
			print("\nPlease enter employee\'s last name or \"done\" to exit: ")
			lastName = input()			
 
#prevents the main function from executing if it was imported
if __name__ == "__main__":
	main()
    
__author__ = "Paul Kummer"
__date__ = "9/03/2018"



#program execution
"""
Please enter employee's last name or "done" to exit: 
kummer

Please enter employee's first name
paul

Please enter employee's phone number
*123)123-1234

Phone number contains incorrect characters, please try using parenthesis
(123)123-1234

Please enter employee's last name or "done" to exit: 
done
[['(123)123-1234', 'kummer', 'paul']]

	Entry Complete


First		Last			Phone

Name		Name			Number

===================================================================

paul 		 kummer 		 (123)123-1234 



------------------
(program exited with code: 0)
Press return to continue

"""
