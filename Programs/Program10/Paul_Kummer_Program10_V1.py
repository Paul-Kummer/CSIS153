#Paul Kummer
#CSIS 153
#Program 10
#Due 12/05/18

__author__ = "Paul Kummer"
__date__ = "12/05/18"

from datetime import *
from calendar import *

"""
Description:
V1:
Created functions to retrieve a year, month, and day that occured in the past.
Additionally, another function will calculate the difference between todays
date and the date entered. Error checking still needs to be implemented.
"""

today = datetime.today()

def getYear():
	notValidYear = True
	while notValidYear:
		userInputYear = input("Please Enter a Year (example: 2018): ")
		if userInputYear == "END":
			notValidYear = False
			userInputYear = -1
		elif userInputYear.isdigit() and int(userInputYear) <= today.year\
		and not userInputYear.startswith("0"):
			notValidYear = False
		elif userInputYear[1:].isdigit() and int(userInputYear) <= today.year\
		and not userInputYear.startswith("0"):
			notValidYear = False
		else:
			print("\t-Incorrect Year Entry-\n(Please enter an integer less than todays year)")
	return int(userInputYear)


def getMonth():
	notValidMonth = True
	while notValidMonth:
		userInputMonth = input("Please Enter a Month (example: 12): ")
		if userInputMonth.isdigit() and int(userInputMonth) <= 12 and\
		 int(userInputMonth) > 0 and not userInputMonth.startswith("0"):
			notValidMonth = False
		else:
			print("\t-Incorrect Month Entry-\n(Please enter an integer between 1-12 with no leading zeros)")
	return int(userInputMonth)

#from https://docs.python.org/3/library/calendar.html
#monthcalendar(year, month)
def getDay ():
	
	notValidDay = True
	while notValidDay:
		userInputDay = input("Please Enter a Day (example: 26): ")
		notValidDay = False
	return int(userInputDay)

def calcDiff (newestDate,oldestDate):
	deltaDate = newestDate-oldestDate
	deltaDaysInt = deltaDate.days
	return deltaDaysInt
	
def displayTimePast():
	stayInLoop = True
	while stayInLoop:
		tmpYear = getYear()
		if tmpYear == -1:
			stayInLoop = False
		else:
			tmpMonth = getMonth()
			tmpDay = getDay()
			tmpDate = datetime(tmpYear,tmpMonth,tmpDay)
			daysOfDifference = calcDiff(today,tmpDate)
	
			if daysOfDifference >= 365:
				deltaYears = daysOfDifference//365
				daysOfDifference = daysOfDifference-(deltaYears*365)
				print("{1:^.0f} years and {0:^.0f} days have past between {2:} and today."\
				.format(daysOfDifference,deltaYears,tmpDate.strftime("%d %b, %Y")))
				
			elif daysOfDifference >= 0:
				print("{:3^.0f} days have past between {:} and today."\
				.format(daysOfDifference,tmpDate.strftime("%d %m, %Y")))
				
			else:
				print("The date entered is in the future and has no days past")
				
displayTimePast()	

"""
Program 10– Using Python’s DateTime and Calendar Modules
Documentation: https://docs.python.org/3/library/calendar.html

Part 1: Create the following functions: (10 pts)

    getYear -- accepts a string. If the string doesn’t contain all digits or if the string doesn’t represent a valid year, the function should continue to ask the user to re-enter the year until they’ve provided a valid year. Hint – use an attribute found in the datetime module to determine the validity.
    It should RETURN an integer.


    getMonth – accepts a string. If the string doesn’t contain all digits or if the string doesn’t represent a valid numeric month, the function should continue to ask the user to re-enter the number of the month until they’ve provided a valid month number.
    It should RETURN an integer.


    getDay – accepts a string. If the string doesn’t contain all digits or if the string doesn’t represent a valid numeric day, the function should continue to ask the user to re-enter the number of the day until they’ve provided a valid day number. Hint: use the Calendar module’s monthrange method!
    It should RETURN an integer.


    calcDiff -- accepts 2 parameters of type date and returns the difference of the dates.

Create a loop that does the following:

    Calls the getYear, getMonth, and getDay to obtain valid numeric entries for each component of the date information.

    Calls the calcDiff function with today’s date and the date entered by the user.

    Print the # of days AND the # of years that have passed.
    NOTE – if today’s date is before the user’s date, it should NOT print a negative # -- rather, it should print a message “No days have passed – the date entered is in the future”.

    The loop should end when the user types END for the year.





Part 2: (5 pts)

    Create a function calcLateFee that takes 2 parameters of type dueDate, curDate (both are objects of type date) and dailyFee (a float). It should return the amount to be assessed as the late fee.

    curDate can be any date – do NOT assume it is today’s date!

    dailyFee should be a float that indicates the amount per day to be charged

    if curDate – dueDate yields a negative number or 0, the function should return 0 as the amount.


    Create a loop that does the following:

        Calls the getYear, getMonth, and getDay to obtain valid numeric entries for each component of the date information.

        Calls the calcLateFee function

        Prints the amount of the late fee, formatted as currency.



Part 3: (5 pts)

    Call the getYear function to obtain a year from the user.

    Print the month and the first Friday of every month in that year.
    HINT: use the monthcalendar method to obtain a calendar object that contains the months for that year:
    myFebCal = calendar.monthcalendar(2016, 2)

(monthcalendar returns a matrix representing a month’s calendar).

wk1 = myFebCal[1] # Each row represents a week.


    Example:
    Year: 2016

First Fridays of every month in year 2016:
January 8
February 12
March 11
April 8
May 6
June 10
July 8
August 12
September 9
October 7
November 11
December 9

Scoring Guide:

Part 1

    getYear function with appropriate error checking 1 pt
    getMonth function with appropriate error 1 pt
    getDay function with appropriate error 2 pts

    calcDiff takes 2 parameters, returns difference of the dates (4 pts).
    checks to make sure a negative # isn’t returned -2 if no check

        # of days incorrect -2

        # of years incorrect -2

    Loops continuously until user types END (2 pts)

Part 2

    calcLateFee takes 2 date objects as params and daily fee (float). 2 pts

    Correctly calculates and returns total late fee or 0 if no late fee 3 pts

Part 3

    Correctly determines the day # of the first Friday of the month for the given year 4 pts

    Output includes the MONTH and the day# 1 pt



"""
