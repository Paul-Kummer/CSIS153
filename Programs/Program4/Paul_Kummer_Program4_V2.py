#Paul Kummer
#CSIS 153 Fall 2018
#Program 4
#Due 10/08/18

__author__ = "Paul Kummer"
__date__= "10-05-18"


#Program Description:
"""
This Program will prompt the user for a text file containing lines that contain;
1.Professor Name
2.Course Name
3.Students enrolled in that course
Then the program will covert the text file into a dictionary with professors as keys and a list of course name and student list.

Next the user will be displayed a main menu with options;
1.sorted professor list
2.list of students in a professor's class
3.list of classes taken by a student
4.sorted list of students classes
5.list of professors teaching specified discipline
6.list of students taking n courseload
7.quit

The program will then allow the user to navigate through the menus, and provide input to have results returned to them.
Once they are done viewing and entering information, while being at the main menu, the user can enter 7 to stop the program.
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
	strToReturn = "\n\t["+menuTitle+"]\n"
	
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
						tmpValue.append(classInfo)
						fileAsDict[profName] = tmpValue
						
					else:
						fileAsDict[profName] = [classInfo]
			fileObj.close()
		root.destroy()
		return(fileAsDict)
	else:
		print("Files Does Not Exist")
		root.destroy()
	
def displayList(listObj, header):
	#The variable that contains what will be returned when the function is called
	print("\n\t### ",header+" ###")
	
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

#option 1	
def listProfessors(classRoster):
	profList = list(classRoster)
	profList.sort()
	displayList(profList, "Professors")

#option 2	
def listStuInClass(classRoster):
	notValidProf = True
	while notValidProf:
		enteredProf = input("\nPlease enter the professor's last name: ")
		if enteredProf in classRoster:
			notValidProf = False
		else:
			print("\t-Incorrect Entry, Please Try Again-")
	
	if len(classRoster[enteredProf])>0:
		profClasses = []
		stuListDict = {}
		
		currentProfList = classRoster[enteredProf]
		for tmpClassList in currentProfList:
			tmpClassName = tmpClassList[0]
			tmpStuList = tmpClassList[1]
			lastNameStuList = []
			for stuName in tmpStuList:
				stuName = stuName.split(" ")
				fName = stuName[0]
				lName = stuName[1]
				lastNameStuList.append(lName+" "+fName)
			lastNameStuList.sort()
			
			#store a student list mapped to class name in stuListDict
			stuListDict[tmpClassName] = lastNameStuList
			profClasses.append(tmpClassName)
			
		profClasses.sort()
		listOfClasses = profClasses+["ALL Courses","Main Menu"]
			
		profClassMenu = createMenu(listOfClasses,"Select Class to View Students")
		userChoice = getValidChoice(listOfClasses, profClassMenu)
		
		#all options
		if userChoice == len(listOfClasses)-1:
			lastNameStuList = []
			studentListToDisplay = []
			
			#combine class lists
			for tmpClassList in classRoster[enteredProf]:
				nClassStuList = []
				for stuName in tmpClassList[1]:
					stuName = stuName.split(" ")
					fName = stuName[0]
					lName = stuName[1]
					nClassStuList.append(lName+" "+fName)
				
				lastNameStuList += nClassStuList
			
			#check for duplicate students
			for student in lastNameStuList:
				if student not in studentListToDisplay:
					studentListToDisplay.append(student)
			studentListToDisplay.sort()
			
			displayList(studentListToDisplay, "Students from all Professor {:}'s Classes".format(enteredProf))
			
		#go back to main
		elif userChoice == (len(listOfClasses)):
			print()
			
		else:
			for option in profClasses:
				if userChoice-1 == listOfClasses.index(option):
					displayList(stuListDict[option], "Students from all Professor {:}'s Class {:}".format(enteredProf, option))
					
		
	else:
		print("\t-No Students Found-")

#option 3	
def listClassesEnrolled(classRoster):
	classesEnrolled = []

	enteredStudent = input("\nPlease enter a students First and Last name to view classes enrolled: ")
		
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		for tmpClass in profClassInfo:
			tmpClassName = tmpClass[0]
			tmpClassStudents = tmpClass[1]
			
			if enteredStudent in tmpClassStudents:
				classesEnrolled.append(tmpClassName)
	
	if len(classesEnrolled) >0:
		classesEnrolled.sort()
		displayList(classesEnrolled, "{:} is enrolled in the following courses".format(enteredStudent))
		
	else:
		print("\t-Student Not Enrolled In Classes-")	

#option 4	
def totEnrolledStu(classRoster):
	completeStuList = []
	lastNameStuList = []	
		
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		for tmpClass in profClassInfo:
			completeStuList += tmpClass[1]
			
		
	for stuName in completeStuList:
		stuName = stuName.split(" ")
		fName = stuName[0]
		lName = stuName[1]
		lastNameFirst = lName+" "+fName
		if lastNameFirst not in lastNameStuList:
			lastNameStuList.append(lastNameFirst)
	
	if len(lastNameStuList) >0:
		lastNameStuList.sort()
		displayList(lastNameStuList, "The following {:^.0f} students are enrolled in courses".format(len(completeStuList)))
		
	else:
		print("\t-Students Not Enrolled In Classes-")

#option 5	
def listProfForClass(classRoster):
	availableClasses = {}
	
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		for tmpClass in profClassInfo:
			tmpClassName = tmpClass[0]
			
			if tmpClassName in availableClasses:
				availableClasses[tmpClassName].append(tmpProf)
				
			else:
				availableClasses[tmpClassName] = [tmpProf]
	
	invalidClassName = True
	while invalidClassName:
		enteredDiscipline = input("Please enter the course to view available professors: ")
		
		if enteredDiscipline in availableClasses:
			availableProfList = availableClasses[enteredDiscipline]
			displayList(availableProfList, "There are {:} professors available for the {:} course".format(len(availableProfList),enteredDiscipline))
			invalidClassName = False
			
		else:
			print("\n\t-Invalid Course Name, example: Chem 101-")
		
#option 6	
def listStuCourseLoad(classRoster):
	completeStuList = []
	stuListToDisplay = []	
	
		
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		for tmpClass in profClassInfo:
			completeStuList += tmpClass[1]

	invalidCourseQty = True
	while invalidCourseQty:
		enteredCourseQty = input("Please enter the courseload quantity you would like to view students for: ")
		if enteredCourseQty.isdigit():
			for tmpStu in completeStuList:
				if tmpStu not in stuListToDisplay and completeStuList.count(tmpStu) == int(enteredCourseQty):
					stuListToDisplay.append(tmpStu)
			invalidCourseQty = False
			
		else:
			print("\n\t-Please Enter Only a Digit-")
	
	if len(stuListToDisplay) >0:
		stuListToDisplay.sort()
		displayList(stuListToDisplay, "There are {:^.0f} students enrolled in {:} courses".format(len(stuListToDisplay),enteredCourseQty))
		
	else:
		print("\t-There are no students taking {:} courses-".format(enteredCourseQty))
	

def main ():
	classRosters = openAndConvertFileToDict()
	
	continueMainMenu = True
	while continueMainMenu:
		menuOptions = ["List professors", "List of Students in a professor's class", "List classes student is enrolled", "List of enrolled students", "List of professors teaching a course", "List of students taking \"user selected number\" classes","QUIT"]
		mainMenu = createMenu(menuOptions,"Main Menu")
		
		userChoice = getValidChoice(menuOptions, mainMenu)
		
		if userChoice == 1:
			listProfessors(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 2:
			listStuInClass(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 3:
			listClassesEnrolled(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 4:
			totEnrolledStu(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 5:
			listProfForClass(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 6:
			listStuCourseLoad(classRosters)
			input("\t-Press <Enter> to continue-")
			
		elif userChoice == 7:
			print("\n\t-EXITING-")
			continueMainMenu = False
	quit()
		
if __name__ == "__main__":
	main()
