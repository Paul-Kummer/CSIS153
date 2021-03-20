#Paul Kummer
#CSIS 153 Fall 2018
#Program 4
#Due 10/08/18

__author__ = "Paul Kummer"
__date__= "10-06-18"


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

Version 3:
*made functions return values
*allowed the user to type done or quit at any input dialouge to go back or exit
*annotated code for clarification
"""

#imports
from tkinter import filedialog
from tkinter import *
from os.path import *

#prompts user for a selection from a menu and returns an interger selection if valid
#if user enters "done", "quit", or the last integer from the menu, the program returns "none"
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
			
			#Check if the user entered "quit" or "done", then exit loop if so
			if usersChoice.lower() != "quit" and usersChoice.lower() != "done":
				
				#Check if the user selection is an integer, greater than zero, and within the selectable options
				#If the user input meets all conditions notValidSelection is changed to False
				if usersChoice.isdigit() and int(usersChoice) > 0 and int(usersChoice) <= int(numberOfChoices):
					notValidSelection = False
					return(int(usersChoice))
				
				#If the user input didn't meet the valid criteria, the users is prompted to select a valid integer
				else:
					print("\n\t*Please enter only an integer within the menu list*\n")
		
			else:
				return("none")
		
#create a numbered menu of options with a header and returns it as a displayed string
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

#opens a dialog box that asks for a text file to have it's information converted into a dictionary that is returned
#the dictionary contains {professor name:[[className,[stu1,stu2,stu3]],[className2,[stu1,stu2,stu3]]]}	
def openAndConvertFileToDict():
	
	#the dictionary object to be returned once populated
	fileAsDict = {}
	
	#initialize tk
	root = Tk()
	
	#pop up a dialog box requesting a text file
	root.fileName = filedialog.askopenfilename(initialdir =".",title ="Select file",filetypes =(("text files","*.txt"),("all files","*.*")))

	#check if the specified file is a legitimate file
	if isfile(root.fileName):
		
		#assign the name fileObj to root.fileName and open it as read only
		with open (root.fileName,"r") as fileObj:
			
			#turn the file object into a list of lines
			fileObjList = fileObj.readlines()
			
			#keep a count on which line is being iterated and reset after 3 since the data is in sets of three
			lineCt = 0
			
			#iterate through each line from the file object
			for line in fileObjList:
				
				#increase line count by one
				lineCt += 1
				
				#remove "\n" if it exists at the end of the line
				if line.endswith("\n"):
					cleanLine = line.rstrip("\n")
				else:
					cleanLine = line
				
				#if line count is one the line is a professor name
				if lineCt == 1:
					
					#check if the line starts with professor, then makes the line into a list seperated by " " and only keeps professor's name as a string
					if cleanLine.startswith("Professor"):
						profName = cleanLine.split(" ")[1]
					else:
						profName = cleanLine
				
				#if the line count is 2 it is the class name, which is saved as string className
				elif lineCt == 2:
					className = cleanLine
				
				#if the line count is divisible by 3, line count goes to zero and the current line is the student list	
				elif lineCt%3 == 0:
					lineCt = 0
					
					#create a list of students by seperating based on ","
					stuList = cleanLine.split(",")
					stuList = [tmpStu.strip(" ") for tmpStu in stuList]
					
					#create a list of a class name and student list correlated with each other
					classInfo = [className, stuList]
					
					#if the professors name is in the dictionary being created append the new list of class name and student list
					if profName in fileAsDict:
						tmpValue = fileAsDict[profName]
						tmpValue.append(classInfo)
						fileAsDict[profName] = tmpValue
					
					#if the professors name isn't in the dictionary add the class name and student list as the value to the key of professors name
					else:
						fileAsDict[profName] = [classInfo]
						
			#close the file object
			fileObj.close()
			
		#close any tk windows
		root.destroy()
		
		#return the dictionary of keys of professor names and values of lists class names tied to a list of students
		return(fileAsDict)
		
	#something unexpected happend and tk windows close and user is told file doesn't exist	
	else:
		print("Files Does Not Exist")
		root.destroy()
		quit()
	
#create a display for listed items with a header and returns it as a displayed string
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
#list all professors by last name alphabetically and return a list with list of professors and a header string
def listProfessors(classRoster):
	profList = list(classRoster)
	profList.sort()
	return(profList)
	
#option 2
#list all students in a user entered professor's class and return a list with list of students and a header	 string
def listStuInClass(classRoster):
	
	#force entry into loop
	notValidProf = True
	
	#keep looping until notValidProf changes to False
	while notValidProf:
		
		#ask for professors last name, case sensitive
		enteredProf = input("\nPlease enter the professor's last name: ")
		
		#check if the name is in the dictionary
		if enteredProf in classRoster:
			
			#exit the loop
			notValidProf = False
		
		#check if the user entered "done" or "quit" to exit
		elif enteredProf.lower() == "quit" or enteredProf.lower() == "done":
			notValidProf = False
		
		#tell user they entered bad data
		else:
			print("\t-Incorrect Entry, Please Try Again-")
	
	#ensure the user didn't enter "quit" or "done"		
	if enteredProf.lower() != "quit" and enteredProf.lower() != "done":
		
		#ensure the dictionary has values
		if len(classRoster[enteredProf])>0:
			
			#create list of classes and a dictionary of classes mapped to their students
			profClasses = []
			stuListDict = {}
			
			#assing variable to list of class and student information associated with a professor
			currentProfList = classRoster[enteredProf]
			
			#iterate through the class and student information lists
			for tmpClassList in currentProfList:
				
				#assign meaningful names to the index locations within the list
				tmpClassName = tmpClassList[0]
				tmpStuList = tmpClassList[1]
				
				#create a list of students by their last names
				lastNameStuList = []
				
				#iterate through the string of a student name and create values of last name first name in lastNameStuList
				for stuName in tmpStuList:
					stuName = stuName.split(" ")
					fName = stuName[0]
					lName = stuName[1]
					lastNameStuList.append(lName+" "+fName)
				
				#alphabetize the list
				lastNameStuList.sort()
				
				#store a student list mapped to class name in stuListDict
				stuListDict[tmpClassName] = lastNameStuList
				profClasses.append(tmpClassName)
			
			#alphabetize the professor classes
			profClasses.sort()
			
			#create a menu list for options to select
			listOfClasses = profClasses+["ALL Courses","Main Menu"]
			
			#give the user options to select from
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
						
				#gather and sort information to be returned as a list
				studentListToDisplay.sort()
				listAndHeader = [studentListToDisplay,"Students from all Professor {:}'s Classes".format(enteredProf)]
				return(listAndHeader)
				
			#go back to main
			elif userChoice == (len(listOfClasses)):
				return("main")
			
			#return information from all classes the professor teaches	
			else:
				for option in profClasses:
					if userChoice-1 == listOfClasses.index(option):
						listAndHeader = [stuListDict[option],"Students from all Professor {:}'s Class {:}".format(enteredProf, option)]
						return(listAndHeader)
					
	#the professor has no students, return "none"	
	elif enteredProf.lower() != "done" and enteredProf.lower() != "quit":
		print("\t-No Students Found-")
		return("none")
	
	#user entered "done" or "quit"	
	else:
		return("none")

#option 3
#list all classes a user entered student is enrolled in and return a list with list of classes and a header string
def listClassesEnrolled(classRoster):
	classesEnrolled = []

	#prompt for student first and last name, case sensitve
	enteredStudent = input("\nPlease enter a students First and Last name to view classes enrolled: ")
	
	#if user enters "quit" or "done" return "none"
	if enteredStudent.lower() == "quit" or enteredStudent.lower() == "done":
			return("none")
			
	else:
		
		#iterate through all the professors and information associated with them		
		for tmpProf in classRoster:
			
			#information associated with the professor
			profClassInfo = classRoster[tmpProf]
			
			#iterate through information associated with professor
			for tmpClass in profClassInfo:
				
				#assign meaningful names
				tmpClassName = tmpClass[0]
				tmpClassStudents = tmpClass[1]
				
				#check if the student is enrolled in a professors class, is so add the name of the class to classesEnrolled List
				if enteredStudent in tmpClassStudents:
					classesEnrolled.append(tmpClassName)
		
		#check if the list contains values
		if len(classesEnrolled) >0:
			
			#gather and sort information to be returned as a list
			classesEnrolled.sort()
			listAndHeader = [classesEnrolled, "{:} is enrolled in the following courses".format(enteredStudent)]
			return(listAndHeader)
		
		#student isn't in any classes
		else:
			print("\t-Student Not Enrolled In Classes-")
			return("none")

#option 4
#list all students taking class and sort the list by last name alphabetically and return list with student list with a header string
def totEnrolledStu(classRoster):
	
	#create lists to be populated
	completeStuList = []
	lastNameStuList = []	
		
	#iterate throug informationa associated with each professor	
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		
		#iterate through class and student lists associated with each professor
		for tmpClass in profClassInfo:
			completeStuList += tmpClass[1]
			
	#iterate throught the list of all students
	for stuName in completeStuList:
		
		#sort the students by last name then first name
		stuName = stuName.split(" ")
		fName = stuName[0]
		lName = stuName[1]
		lastNameFirst = lName+" "+fName
		
		#check for duplicate entries
		if lastNameFirst not in lastNameStuList:
			lastNameStuList.append(lastNameFirst)
	
	#ensure that there are elements in the list
	if len(lastNameStuList) >0:
		
		#gather and sore inforamtion to be returned for displaying as a list
		lastNameStuList.sort()
		listAndHeader =[lastNameStuList, "The following {:^.0f} students are enrolled in courses".format(len(completeStuList))]
		return(listAndHeader)
	
	#there are no students enrolled returne "none"
	else:
		print("\t-Students Not Enrolled In Classes-")
		return("none")

#option 5
#list all professors teaching a user entered discipline and return a list with list of professors and a header string
def listProfForClass(classRoster):
	availableClasses = {}
	
	#iterate throug informationa associated with each professor	
	for tmpProf in classRoster:
		profClassInfo = classRoster[tmpProf]
		
		#iterate through class and student lists associated with each professor
		for tmpClass in profClassInfo:
			tmpClassName = tmpClass[0]
			
			#check if the class name is in the availableClasses dictionary, if so add the professor as an additional value to class name key
			if tmpClassName in availableClasses:
				availableClasses[tmpClassName].append(tmpProf)
			
			#if not already in the dictionary add a new key and value	
			else:
				availableClasses[tmpClassName] = [tmpProf]
	
	#enter a loop
	invalidClassName = True
	while invalidClassName:
		
		#prompt for a discipline to veiw available professors
		enteredDiscipline = input("Please enter the course to view available professors: ")
		
		#check if the discipline is one of the classes a professor teaches
		if enteredDiscipline in availableClasses:
			invalidClassName = False
			
			#assign meaningful name to dictionary key, which is a list of professors for each class
			availableProfList = availableClasses[enteredDiscipline] 
			
			#create list of information to be returned and return it
			listAndHeader= [availableProfList, "There are {:} professors available for the {:} course".format(len(availableProfList),enteredDiscipline)]
			return(listAndHeader)
		
		#return "none" if the user enteres "quit" or "none"	
		elif enteredDiscipline.lower() == "quit" or enteredDiscipline.lower() == "done":
			invalidClassName = False
			return("none")
		
		#an invalid course name was entred
		else:
			print("\n\t-Invalid Course Name, example: Chem 101-")
			return("none")
		
#option 6
#list all students enrolled in a user specified number of classes and return a list with a student list and header string
def listStuCourseLoad(classRoster):
	
	#create lists to populate
	completeStuList = []
	stuListToDisplay = []	
	
	#itereate through each professor with their information
	for tmpProf in classRoster:
		
		#assign meaningful name
		profClassInfo = classRoster[tmpProf]
		
		#iterate though the information assocaiate with a professor
		for tmpClass in profClassInfo:
			
			#combine student lists to make a complete student list
			completeStuList += tmpClass[1]

	#enter the loop
	invalidCourseQty = True
	while invalidCourseQty:
		
		#prompt user for input of number of courses
		enteredCourseQty = input("Please enter the courseload quantity you would like to view students for: ")
		
		#check if the entered data is a digit
		if enteredCourseQty.isdigit():
			
			#iterate through the student list
			for tmpStu in completeStuList:
				
				#check if the student is already in the list and if they are enrolled in the number of courses desired
				if tmpStu not in stuListToDisplay and completeStuList.count(tmpStu) == int(enteredCourseQty):
					
					#add the student to list to be displayed
					stuListToDisplay.append(tmpStu)
			invalidCourseQty = False
		
		#if the user enters "quit" or "done" quit the loop so "none" can be returned
		elif enteredCourseQty.lower() == "quit" or enteredCourseQty.lower() == "done":
			invalidCourseQty = False
		
		#the user didn't enter valid information	
		else:
			print("\n\t-Please Enter Only a Digit-")
	
	#verify that there are elements to the list
	if len(stuListToDisplay) >0:
		
		#alphabetize the list and return the list of students and header
		stuListToDisplay.sort()
		listAndHeader = [stuListToDisplay, "There are {:^.0f} students enrolled in {:} courses".format(len(stuListToDisplay),enteredCourseQty)]
		return(listAndHeader)
	
	#return none because the user entered "quit" or "done"
	elif enteredCourseQty.lower() == "quit" or enteredCourseQty.lower() == "done":
		return("none")
	
	#there are no students taking the specified number of courses
	else:
		print("\t-There are no students taking {:} courses-".format(enteredCourseQty))
		return("none")
	
#create a main menu that loops until the user enters 7, "done", "quit"
def main ():
	
	#call the openAndConverFileToDict function and return a value as classRosters
	classRosters = openAndConvertFileToDict()
	
	#enter main menu loop so it will keep repeating until the user stops it
	continueMainMenu = True
	while continueMainMenu:
		
		#list of options to be displayed to the usere and number them
		menuOptions = ["List professors", "List of Students in a professor's class", "List classes student is enrolled", "List of enrolled students", "List of professors teaching a course", "List of students taking \"user selected number\" classes","QUIT"]
		mainMenu = createMenu(menuOptions,"Main Menu")
		
		#check if the user enters a valid option for the menu
		userChoice = getValidChoice(menuOptions, mainMenu)
		
		#if user enters "done" or "none" exit the program
		if userChoice == "none":
			print("\n\t-EXITING-")
			continueMainMenu = False
		
		#check what option the user selected
		else:
			
			#option 1
			if userChoice == 1:
				profList = listProfessors(classRosters)
				displayList(profList, "Professors")
				input("\t-Press <Enter> to continue-")

			#option 2 	
			elif userChoice == 2:
				stuListAndHeader = listStuInClass(classRosters)
				if stuListAndHeader != "main" and stuListAndHeader != "none":
					stuList = stuListAndHeader[0]
					header = stuListAndHeader[1]
					displayList(stuList,header)
				input("\t-Press <Enter> to continue-")
			
			#option 3	
			elif userChoice == 3:
				enrolledListAndHeader = listClassesEnrolled(classRosters)
				if enrolledListAndHeader != "none":
					classList = enrolledListAndHeader[0]
					header = enrolledListAndHeader[1]
					displayList(classList,header)
				input("\t-Press <Enter> to continue-")
			
			#option 4	
			elif userChoice == 4:
				totStuAndHeader = totEnrolledStu(classRosters)
				if totStuAndHeader != "none":
					stuList = totStuAndHeader[0]
					header = totStuAndHeader[1]
					displayList(stuList,header)
				input("\t-Press <Enter> to continue-")
			
			#option 5	
			elif userChoice == 5:
				profAndHeader = listProfForClass(classRosters)
				if profAndHeader != "none":
					profList = profAndHeader[0]
					header = profAndHeader[1]
					displayList(profList,header)
				input("\t-Press <Enter> to continue-")
			
			#option 6	
			elif userChoice == 6:
				stuLoadAndHeader = listStuCourseLoad(classRosters)
				if stuLoadAndHeader != "none":
					stuList = stuLoadAndHeader[0]
					header = stuLoadAndHeader[1]
					displayList(stuList,header)
				input("\t-Press <Enter> to continue-")
			
			#option 7	
			elif userChoice == 7:
				print("\n\t-EXITING-")
				continueMainMenu = False
			
			#unknown option	
			else:
				print("\n\t-Something Went Wrong-")

	quit()

#run the main function unless the file was imported		
if __name__ == "__main__":
	main()
