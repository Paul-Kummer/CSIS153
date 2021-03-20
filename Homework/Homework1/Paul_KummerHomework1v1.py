#Paul Kummer
#CSIS 153 Fall 2018
#Homework 1
__author__ = "Paul Kummer"
__date__ = "8/28/2018"


#Problem 1: take a list and sort it from largest to smallest in a
#printout to the user

#create a list with valid integers
myList = [15,30,20,18,45,40,20,15,20]

#sort myList in descending order
myList.sort()

#reverse the order of list myList
myList.reverse()

#print to user the values of myList
print (myList)

#code execution
"""
[45, 40, 30, 20, 20, 20, 18, 15, 15]


------------------
(program exited with code: 0)
"""


#Problem 2: remove all the values less than 30 in the list myList

#create a list with valid integers
myList = [15,30,20,18,45,40,20,15,20]

#list of values to remove from myList at end of program
numToRemove = []

#iterate through every object in myList and assign it the value num
for num in myList:
	
	#check if num is less than 30
	if num < 30:
		
		#adds value to list numToRemove, which will later be removed
		numToRemove.append(num)
		
	#do nothing if value is greater than 30
	else:
		pass

#removes numbers from list myList
for num in numToRemove:
	
	#removes values under 30 from myList
	myList.remove(num)

#print to user the values of myList
print (myList)

#code execution
"""
[30, 45, 40]


------------------
(program exited with code: 0)
Press return to continue
"""


#Problem 3: print the average of sales from salesList

#create sales list as salesList
salesList = [["Qtr1",400],["Qtr2",150],["Qtr3",200]]

#number of sales entries
numberOfSales = len(salesList)

#tally of total sales from every quater
totalSales = 0

#iterate through lists within salesList
for currentList in salesList:
	
	#accumulator for totalSales
	totalSales += int(currentList[1])

#set the value of averageSales as total sales over number of sales	
averageSales = int(totalSales/numberOfSales)

#print to user the value of averageSales
print("The average sales for all quarters is: ",averageSales)

#code execution
"""
The average sales for all quarters is:  250


------------------
(program exited with code: 0)
Press return to continue
"""


#Problem 4: print out to user the number of occurrenes of whatever
#value they input are in the list myList

#create main line of logic
def main():
	
	
	#create a list with valid integers
	myList = [15,30,20,18,45,40,20,15,20]

	#prompts user for an integer
	print("Please enter a valid integer: ")
	num = input()
	
	#attempts to convert num into an integer
	try:
		num = int(num)
	
	#if num cannot be converted to an integer the program executes again
	#after notifying the user of invalid input
	except:
		print("Invalid input, Please input a valid integer")
		main()

	#variable to keep cout of the number of occurrences of inputed value
	numCount = 0
	
	#iterate through myList and determine if user input is equal to value
	#in myList. If user input matches value in myList the value numCount
	#is increased by one	
	for integer in myList:
		if integer == num:
			numCount +=1
		else:
			pass
			
	#print out to user the number of occurrences of their inputed value
	print("The value ",num, " occurs ",numCount," times.")

#execute the main function unless the file was imported, which __name__
#will take on another value	
if __name__ == "__main__":
	main()

#code execution	
"""
Please enter a valid integer: 
15
The value  15  occurs  2  times.


------------------
(program exited with code: 0)
Press return to continue
"""


#Problem 5: prompt for a student name, and then display their score

#list of students with corresponding scores
studentList = [["Joe", 100],["Mary",90],["Sam",95]]

#prompt user to input a student name
print("What students score would you like to view? ")
studentName = input()

#iterate through every list within studentList
for list in studentList:
	
	#use the value at index 0 as student's name
	student = list[0]
	
	#use the value at index 1 as student's score
	score = list[1]
	
	#if the user inputed name matches a name in studentList a score
	#will be displayed
	if str(studentName) == str(student):
		print("\n student: ",student,"\t score: ",score)
	
	#if students name is not found nothing will happen
	else:
		pass

#code execution
"""
What students score would you like to view? 
Sam

 student:  Sam 	 score:  95


------------------
(program exited with code: 0)
Press return to continue
"""
