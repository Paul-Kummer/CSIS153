#Paul Kummer
#CSIS 153 Fall 2018
#Program 4
#Due 10/08/18

__author__ = "Paul Kummer"
__date__= "10-04-18"


#Program Description:
"""

"""

from tkinter import filedialog
from tkinter import *
from os.path import *


def getValidChoice (choiceList, menuStr):
	numberOfChoices = len(choiceList)
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

def createMenu (menuOptions,menuTitle):

	#The variable that contains what will be returned when the function is called
	strToReturn = "\t["+menuTitle+"]\n"
	
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
	
def openAndConvertFileToDict():
	fileAsDict = {}
	root = Tk()
	root.fileName = filedialog.askopenfilename(initialdir =".",title ="Select file",filetypes =(("text files","*.txt"),("all files","*.*")))

	if isfile(root.fileName):
		with open (root.fileName,"r") as fileObj:
			
			fileObjList = fileObj.readlines()
			lineCt = 0
			for line in fileObjList:
				lineCt += 1
				if line.endswith("\n"):
					cleanLine = line.rstrip("\n")
				else:
					cleanLine = line
				
				if lineCt == 1:
					if cleanLine.startswith("Professor"):
						profName = cleanLine.split(" ")[1]
					else:
						profName = cleanLine
					
				elif lineCt == 2:
					className = cleanLine
				
					
				elif lineCt%3 == 0:
					lineCt = 0
					stuList = cleanLine.split(",")
					classInfo = [className, stuList]
					
					
					if profName in fileAsDict:
						tmpValue = fileAsDict[profName]
						fileAsDict[profName] = tmpValue, [classInfo]
						
					else:
						fileAsDict[profName] = [classInfo]
			fileObj.close()
		
		return(fileAsDict)
	else:
		print("Files Does Not Exist")
	root.destroy()
	
def displayList(listObj, header):
	#The variable that contains what will be returned when the function is called
	print("\n\t[",header+"]")
	
	#Check if menu options are within the presumed list menuOptions
	if len(listObj) > 0:
		
		iterationCt = 0
		#iterate through all the options in the list menuOptions
		for element in listObj:
			iterationCt += 1
			#Check if the current option is the last item in the list, 
			#if it is the last item in the list there will be no newline added
			if iterationCt <= (len(listObj)-1):
				
				#Concatenate strToReturn with the iteration count, a period, and the current option
				print("-",element)
			
			#increase the counter and concatenate strToReturn with iteration count, a period, curent option, and a newline	
			else:
				print("-", element,"\n")
	
def listProfessors(classRoster):
	profList = list(classRoster)
	profList.sort()
	displayList(profList, "Professors")
	
def listStuInClass(classRoster):
	notValidProf = True
	while notValidProf:
		enteredProf = input("\nPlease enter the professor's last name: ")
		if enteredProf in classRoster:
			notValidProf = False
		else:
			print("\t-Incorrect Entry, Please Try Again-")
	
	if len(classRoster[enteredProf])>0:
		profClasses = ["ALL"]
		for tmpClassInfo in classRoster[enteredProf]:
			tmpClassName = tmpClassInfo[0]
			profClasses.append(tmpClassName[0])
		profClasses.append("QUIT")	
		profClassMenu = createMenu(profClasses,"Select Class to View Students")
		userChoice = getValidChoice(profClasses, profClassMenu)
		
		
			if userChoice == 1:
				#all options
			elif userChoic == (len(profClasses)+1)
				#quit
			else:
				for option in profClasses:
					if userChoice == (profClasses.index(option)+1)
		
	else:
		print("\t-No Students Found-")
	
def listClassesEnrolled(classRoster):
	pass
	
def totEnrolledStu(classRoster):
	pass
	
def listProfForClass(classRoster):
	pass
	
def listStuCourseLoad(classRoster):
	pass
	

def main ():
	classRosters = openAndConvertFileToDict()
	print(classRosters)
	
	menuOptions = ["List professors", "List of Students in a professor's class", "List classes student is in", "List of enrolled students", "List of professors teaching a course", "List of students taking \"user selected number\" classes","QUIT"]
	mainMenu = createMenu(menuOptions,"Main Menu")
	
	userChoice = getValidChoice(menuOptions, mainMenu)
	
	if userChoice == 1:
		listProfessors(classRosters)
		
	elif userChoice == 2:
		listStuInClass(classRosters)
		
	elif userChoice == 3:
		listClassesEnrolled(classRosters)
		
	elif userChoice == 4:
		totEnrolledStu(classRosters)
		
	elif userChoice == 5:
		listProfForClass(classRosters)
		
	elif userChoice == 6:
		listStuCourseLoad(classRosters)
		
	elif userChoice == 7:
		print("\t-EXITING-")
		quit()
		
if __name__ == "__main__":
	main()
