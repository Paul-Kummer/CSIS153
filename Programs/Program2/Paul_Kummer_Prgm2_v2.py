#Paul Kummer
#CSIS 153 Fall 2018
#Program 2
#Due September 14

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

#create a function that takes two arguments that will be the menu options and title
def createMenu (menuOptions,menuTitle):

	#The variable that contains what will be returned when the function is called
	strToReturn = str(menuTitle)+"\n"
	
	#Accumulator that is used for labeling the options, which is why it starts at one
	iterationCt = 1
	
	if len(menuOptions) > 0:
		for currentOption in menuOptions:
			if currentOption == menuOptions[(len(menuOptions)-1)]:
				strToReturn += (str(iterationCt) + ". " + currentOption)
				iterationCt += 1
				
			else:	
				strToReturn = strToReturn + (str(iterationCt) + ". " + currentOption + "\n")
				iterationCt += 1
	
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


#returns only a valid integer within the number of choices
def getValidChoice (numberOfChoices, menuStr):

	if int(numberOfChoices) <= 0:
		print(menuStr,"\nThere are no menu options")
		return(int(0))
	else:
		
		notValidSelection = True
		
		while notValidSelection:
			print(menuStr)
			usersChoice = input("\nPlease enter your menu selection: ")
			
			if usersChoice.isdigit() and int(usersChoice) > 0 and int(usersChoice) <= int(numberOfChoices):
				
				notValidSelection = False
			else:
				print("\n\t*Please enter only an integer within the menu list*\n")
		
		return(int(usersChoice))
		
		
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



