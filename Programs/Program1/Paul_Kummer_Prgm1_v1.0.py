#Paul Kummer
#CSIS 153 Fall 2018
#Program 1
#Due September 5

__author__ = "Paul Kummer"
__date__ = "9/03/2018"

myEmployees = []

def phoneValidation (phoneNumber):
	
	if len(phoneNumber) == int(14):
		
		phoneLong = isValidLong(phoneNumber)
		while phoneLong == False:

	
	elif len(empPhone) == int(13):
		
		phoneMed == False
		while phoneMed == False:
			if empPhone[0] != "(" and empPhone[4] != ")":
				print("\nPhone number contains incorrect values, please try again")
				empPhone = input()

			elif empPhone[0:3].isdigit() == False or empPhone[4:7].isdigit() == False or empPhone[8:].isdigit()== False:
				print("\nPhone number must consist of integers, please try again")
				empPhone = input()
				
			elif empPhone[8] != "-":
				print("\nPhone number contains incorrect values, please try again")
				empPhone = input()
			
			else:
				phoneMed ==True
							
	elif len(empPhone) == int(12):
		
		phoneShort == False
		while phoneShort == False:
			if empPhone[3] != "-" and empPhone[7] != "-":
				print(empPhone[3], empPhone[7])
				print("\nPhone number contains incorrect values, please try again")
				empPhone = input()
				
			elif empPhone[1:4].isdigit() == False or empPhone[5:8].isdigit() == False or empPhone[9:].isdigit()== False:
				print("\nPhone number must consist of integers, please try again")
				empPhone = input()
			
			else:
				phoneShort == True
	
	else:
		return(True)
		tmp.append(empPhone, lastName, firstName)
	
	
def isValidLongPhone (phoneNumber):
	if empPhone[5].isspace() == False:
		print("\nIncorrect phone length, please try again")
		Return(False)
		
	elif empPhone[0] != "(" and empPhone[4] != ")":
		print("\nPhone number contains incorrect values, please try again")
		Return(False)

	elif empPhone[1:4].isdigit() == False or empPhone[6:9].isdigit() == False or empPhone[10:].isdigit()== False:
		print("\nPhone number must consist of integers, please try again")
		Return(False)
		
	elif empPhone[9] != "-":
		print("\nPhone number contains incorrect values, please try again")
		Return(False)
	else:
		Return(True)
				
def isValidMedPhone (phoneNumber):
def isValidShortPhone(phoneNumber):

def isValidPhone (tmp):
	print("Please enter employee\'s last name or \"done\" to exit: ")
	lastName = input()
	
	isDone = False
	while isDone == False:
		empInfo = []
		if str(lastName.upper()) == str("DONE"):
			print("\nEntry Complete")
			isDone = True
		
		else:
			print("\nPlease enter employee\'s first name")
			firstName = input()
			
			print("\nPlease enter employee\'s phone number")
			empPhone = input()
			
			validPhone = False
			while validPhone == False:
				if int(12) > len(empPhone) or len(empPhone) > int(14):
					print("\nIncorrect phone length, please try again")
					empPhone = input()
				
				else:
					validPhone = phoneValidation(empPhone)
			tmp.append(empPhone, lastName, firstName)
					
				
					

#use while loop with sentinel to wait for correct input.
#"Done" is exit to sentinel as input of last name
"""
lastName = input()
while lastName != "DONE":
	#use while loop for 
	#phone, firstname
	lastName = input()
"""   
if __name__ == "__main__":
	isValidPhone(myEmployees)
    
