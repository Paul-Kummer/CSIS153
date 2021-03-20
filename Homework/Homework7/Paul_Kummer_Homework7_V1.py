#Paul Kummer
#CSIS 153 Fall 2018
#Homework 7
#Due: 10-05-18

#Program Description
"""
This program asks the user to input a date in the past or present. Then the program displays the days and years away that date is frome the current date.
"""

__author__="Paul Kummer"
__date__="10-01-18"

from datetime import *


def validMonth():
	months = ("january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december")
	isNotValidMonth=True
	while isNotValidMonth:
		
		enteredMonth = input("Please enter a month: ")
		
		if enteredMonth.lower() in months:
			enteredMonth = months.index(enteredMonth.lower()) + 1
			isNotValidMonth = False
			
		elif enteredMonth.isdigit() and int(enteredMonth) > 0 and int(enteredMonth) <= 12:
			isNotValidMonth = False
			
		else:
			print("\t-Invalid Month, Please type the full month-")
	return(enteredMonth)
	
	
def validDay(enteredMonth):
	isNotValidDay=True
	while isNotValidDay:
		
		enteredDay = input("Please enter a day: ")
		
		#potential error from months not having 31 days, could use try/except statement with datetime
		if enteredDay.isdigit() and int(enteredDay) >= 0 and int(enteredDay) <= 31:
				isNotValidDay = False
			
		else:
			print("\t-Invalid Day, Please type a day between 0 and 31-")
	return(enteredDay)
	
def displayDaysExpired(userDateObject):
	timeExpired = abs(userDateObject - date.today())
	timeExpiredYears = timeExpired.days/365

	#timeExpired.days: https://docs.python.org/3/library/datetime.html
	print("\nThere is a {:.0f} day difference or {:.0f} year difference since year {:.0f}, month {:.0f}, day {:.0f}\n".format(timeExpired.days,timeExpiredYears,userDateObject.year,userDateObject.month,userDateObject.day))
	
	
def main():
	isNotValidYear = True
	while isNotValidYear:
		
		enteredYear = input("Please enter a year, or END to quit: ")
		
		if enteredYear == "END":
			print("\t-Exiting-")
			isNotValidYear = False
			
		elif len(enteredYear) > 0 and enteredYear.isdigit():
			enteredMonth = validMonth()
			enteredDay = validDay(enteredMonth)
			
			userDate = date(int(enteredYear), int(enteredMonth), int(enteredDay))
			
			displayDaysExpired(userDate)
			
			
		else:
			print("\t-Invalid Entry, Please enter a year-")


if __name__ == "__main__":
	main()
	
#Program Output
"""
Please enter a year, or END to quit: 1986
Please enter a month: 7
Please enter a day: 31

There is a 11750 day difference or 32 year difference since year 1986, month 7, day 31

Please enter a year, or END to quit: END
	-Exiting-
"""



#Homework 7: Using DateTime Module

##Problem 1.
#from datetime import *

##print(date.today())
##print(datetime.today())

#d1=datetime(2032,4,5,23,35,45)
#print(d1.month, d1.day, d1.year)
#print(d1.hour, d1.minute, d1.second)


##Output
#"""
#2018-10-01
#2018-10-01 20:15:03.426082
#4 5 2032
#23 35 45
#"""


##Problem 2.
#d2=date(2018,10,1)
#print(d2)
#print(d2.month,d2.day,d2.year)
#print(d2.weekday())


##Output
#"""
#2018-10-01
#10 1 2018
#0
#"""


##Problem 3.
#d1Str="October 2, 2018"
#print(d1Str, end = "")
#print(datetime.strptime(d1Str, "%B %d, %Y"))

##Output
#"""
#October 2, 20182018-10-02 00:00:00
#"""


##Problem 4.
#print(datetime.strftime(d2, "%B %d, %y"))
#print(datetime.strftime(d2, "%A %B %d, %Y"))

##Output
#"""
#October 01, 18
#Monday October 01, 2018
#"""
