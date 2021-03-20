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

V2:
Allowed users to pass arguments into functions, and reverted to using datetime
calander limitations. Also, added getDailyFee and displayAmount Due functions

V3:
"""

#global var
today = date.today()
print("\t### Today is {:} ###\n".format(today.strftime("%d %b, %Y")))


def getYear(tmpUserYearStr=-1):
	notValidYear = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserYearStr == -1:
		tmpUserYearStr = input("Please Enter a Year (example: 2018): ")
	
	while notValidYear:
		
		if tmpUserYearStr == "END":
			notValidYear = False
			tmpUserYearStr = -1
			
		#handles positive integers less than todays year, currently excludes zero
		elif tmpUserYearStr.isdigit() and int(tmpUserYearStr) <= today.year\
			and int(tmpUserYearStr) > 0:
			notValidYear = False
			
		#handles negative integers, Does Not Work With BC Dates
		#elif tmpUserYearStr[1:].isdigit() and int(tmpUserYearStr) <= today.year\
		#and not tmpUserYearStr[0] == "-":
		#	notValidYear = False
		
		else:
			print("\t-Invalid Year Entry-\n(Please enter an integer less than or equal to todays year)")
			tmpUserYearStr = input("Please Enter a Year (example: 2018): ")
			
	return int(tmpUserYearStr)


def getMonth(tmpUserMonthStr=-1):
	notValidMonth = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserMonthStr == -1:
		tmpUserMonthStr = input("Please Enter a Month (example: 12): ")
	
	while notValidMonth:
		
		if tmpUserMonthStr.isdigit() and int(tmpUserMonthStr) <= 12 and\
			int(tmpUserMonthStr) > 0 and not tmpUserMonthStr.startswith("0"):
			notValidMonth = False
			
		else:
			print("\t-Invalid Month Entry-\n(Please enter an integer between 1-12 with no leading zeros)")
			tmpUserMonthStr = input("Please Enter a Month (example: 12): ")
			
	return int(tmpUserMonthStr)
	
	
def getDailyFee(tmpDailyFee="None"):
	notVaildFee = True
	
	if tmpDailyFee == "None":
		tmpDailyFee = input("What is the daily fee? (example 0.25): ")
	
	while notVaildFee:
		if tmpDailyFee.count(".") <= 1:
			if tmpDailyFee[0] == "-":
				for char in tmpDailyFee[1:]:
					validChars = True
					if not char.isdigit() or char == ".":
						validChars = False
						
			else:
				for char in tmpDailyFee[1:]:
					validChars = True
					if not char.isdigit() or char == ".":
						validChars = False
				
		if validChars == True:
			notVaildFee = False	
			
		else:
			print("\t-Invalid Entry-\n(Please Enter a Floating Number)")
			tmpDailyFee = input("What is the daily fee? (example 0.25): ")
			
	return float(tmpDailyFee)
				


#from https://docs.python.org/3/library/calendar.html
#monthcalendar(year, month)
def getDay (tmpYear,tmpMonth,tmpUserDayStr=-1):
	monthObj = monthcalendar(tmpYear,tmpMonth)
	maxMonthRange = max(monthObj[len(monthObj)-1])
	notValidDay = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserDayStr == -1:
		tmpUserDayStr = input("Please Enter a Day (between 1 and {:}): "\
			.format(maxMonthRange))
	
	while notValidDay:

		if tmpUserDayStr.isdigit() and int(tmpUserDayStr) <= maxMonthRange\
		and int(tmpUserDayStr) > 0:
			notValidDay = False
			
		else:
			print("\t-Invalid Day Entry-\n(Please enter an integer between 1 and {:})"\
				.format(maxMonthRange))
			tmpUserDayStr = input("Please Enter a Day (between 1 and {:}): "\
				.format(maxMonthRange))
			
	return int(tmpUserDayStr)


def calcDiff (newestDate,oldestDate):
	deltaDate = newestDate-oldestDate
	deltaDaysInt = deltaDate.days
	
	return deltaDaysInt

	
def calcLateFee(tmpDueDate,tmpCurDate,tmpDailyFee=0):
	daysOverDue = calcDiff(tmpCurDate,tmpDueDate)
	balanceIncurred = daysOverDue * tmpDailyFee
	
	if balanceIncurred < 0 or daysOverDue < 0:
		balanceIncurred = 0
		
	return float(balanceIncurred)


def displayTimePast():
	print("\n\t:::: Calculate Time Past ::::\n")
	stayInLoop = True
	
	while stayInLoop:
		tmpYear = getYear()
		
		if tmpYear == -1:
			stayInLoop = False
			
		else:
			tmpMonth = getMonth()
			tmpDay = getDay(tmpYear,tmpMonth)
			tmpDate = date(tmpYear,tmpMonth,tmpDay)
			daysOfDifference = calcDiff(today,tmpDate)
	
			if daysOfDifference >= 365:
				deltaYears = daysOfDifference//365
				daysOfDifference = daysOfDifference-(deltaYears*365)
				
				print("\n\t### Time Difference ###\n{1:^.0f} years and {0:^.0f} days have past between {2:} and today.\n"\
					.format(daysOfDifference,deltaYears,tmpDate.strftime("%d %b, %Y")))
				
			elif daysOfDifference >= 0:
				print("\n\t### Time Difference ###\n{:3^.0f} days have past between {:} and today.\n"\
					.format(daysOfDifference,tmpDate.strftime("%d %m, %Y")))
				
			else:
				print("\n\t### Time Difference ###\nThe date entered is in the future and has no days past\n")
	
	
def displayAmountDue():
	print("\n\t:::: Calculate Amount Due ::::")
	stayInLoop = True

	while stayInLoop:
		print("\n\t### Enter Due Date ###")
		tmpYearDue = getYear()
		if tmpYearDue == -1:
			stayInLoop = False
			
		else:
			tmpMonthDue = getMonth()
			tmpDayDue = getDay(tmpYearDue,tmpMonthDue)
			tmpDateDue = date(tmpYearDue,tmpMonthDue,tmpDayDue)
		
		
		if stayInLoop == True:
			print("\n\t### Enter Borrowed Date ###")
			tmpYearBorrowed = getYear()
			if tmpYearBorrowed == -1:
				stayInLoop = False
				
			else:
				tmpMonthBorrowed = getMonth()
				tmpDayBorrowed = getDay(tmpYearBorrowed,tmpMonthBorrowed)
				tmpDateBorrowed = date(tmpYearBorrowed,tmpMonthBorrowed,tmpDayBorrowed)
			
			print("\n\t### Enter Daily Fee ###")
			tmpFee = getDailyFee()
			balanceDue = calcLateFee(tmpDateBorrowed,tmpDateDue,tmpFee)	
			print("\n\tThe total amount due is ${:<.2f}\n".format(balanceDue))
 

displayTimePast()
displayAmountDue()

"""

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
