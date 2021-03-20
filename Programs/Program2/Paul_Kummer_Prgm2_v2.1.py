#Paul Kummer
#CSIS 153 Fall 2018
#Program 2
#Due September 14

__author__ = "Paul Kummer"
__date__= "9-12-18"


#Program Description:
"""
Create a function that uses a list of menu choices and menu title to return a 
string of menu options with a header along with numbered choices. Also, another
function will ask for the user to input an integer selection of one of the menu
options. Upon entering a valid menu option the function will output the valid
integer
"""

#Lists that contain menu options
choiceList = ["Add", "Subtract", "Multiply", "Divide", "Quit"]
optionsList = ["Deposit", "Withdrawl", "Quit"]

#Create a function that takes two arguments that will be the menu options and title
def createMenu (menuOptions,menuTitle):

	#The variable that contains what will be returned when the function is called
	strToReturn = str(menuTitle)+"\n"
	
	#Accumulator that is used for labeling the options, which is why it starts at one
	iterationCt = 0
	
	#Check if menu options are within the presumed list menuOptions
	if len(menuOptions) > 0:
		
		#iterate through all the options in the list menuOptions
		for currentOption in menuOptions:
			
			#Check if the current option is the last item in the list, 
			#if it is the last item in the list there will be no newline added
			if currentOption == menuOptions[(len(menuOptions)-1)]:
				
				#Increase the count of accumulator
				iterationCt += 1
				
				#Concatenate strToReturn with the iteration count, a period, and the current option
				strToReturn += (str(iterationCt) + ". " + currentOption)
			
			#increase the counter and concatenate strToReturn with iteration count, a period, curent option, and a newline	
			else:
				iterationCt += 1
				strToReturn += (str(iterationCt) + ". " + currentOption + "\n")
				
	#Return a concatenated string to whatever called the function
	return(strToReturn)



menuStr = createMenu(choiceList,"Main Menu")#; print(menuStr)

#Output
"""
Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit
"""


menuStr = createMenu(optionsList,"Banking Menu")#; print(menuStr)

#Output
"""
Banking Menu
1. Deposit
2. Withdrawl
3. Quit
"""


#Create a function that returns only a valid integer within the number of choices
#from menuStr. Reaquires two arguments which are and integer of the number of choices
#and the string that contains the menu.
def getValidChoice (numberOfChoices, menuStr):

	#Checks if there are menu options, if there are none, zero is returned and the user is notified
	if int(numberOfChoices) <= 0:
		print(menuStr,"\nThere are no menu options")
		return(int(0))
	
	else:
		
		#Sentinel that triggers the while loop. When a valid selection is entered the value changes to False
		notValidSelection = True
		
		#Loop that continues to ask the user for input until a valid integer is chosen
		while notValidSelection:
			
			#Display to users the menu options with a header
			print(menuStr)
			
			#Ask the user to choose a menu selection
			usersChoice = input("\nPlease enter your menu selection: ")
			
			#Check if the user selection is an integer, greater than zero, and within the selectable options
			#If the user input meets all conditions notValidSelection is changed to False
			if usersChoice.isdigit() and int(usersChoice) > 0 and int(usersChoice) <= int(numberOfChoices):
				notValidSelection = False
			
			#If the user input didn't meet the valid criteria, the users is prompted to select a valid integer
			else:
				print("\n\t*Please enter only an integer within the menu list*\n")
		
		#Return an integer, which the user entered that has been proven valid
		return(int(usersChoice))
		
		
		
#New choice list and menuStr		
choiceList = ["Add", "Subtract", "Multiply", "Divide", "Quit"]			
menuStr = createMenu(choiceList,"Main Menu")

ch = getValidChoice(len(choiceList), menuStr); print(ch)

#Output
"""
Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: 0

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: !

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: a

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: 1.1

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: -4

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: 1a

	*Please enter only an integer within the menu list*

Main Menu
1. Add
2. Subtract
3. Multiply
4. Divide
5. Quit

Please enter your menu selection: 2
2
"""



