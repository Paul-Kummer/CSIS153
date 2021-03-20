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
Added first Fridays function, and made display layouts look nicer. Furthermore,
changed getYear function to allow dates within the datetime modules range.
"""

#global var
today = date.today()


def getYear(tmpUserYearStr=-1):
	notValidYear = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserYearStr == -1:
		tmpUserYearStr = input("Please Enter a Year (example: 2018): ")
	
	while notValidYear:
		
		if tmpUserYearStr == "END":
			notValidYear = False
			tmpUserYearStr = -1
			
		#handles integers between datetime's resolution
		elif tmpUserYearStr.isdigit() and int(tmpUserYearStr) <= MAXYEAR\
			and int(tmpUserYearStr) >= MINYEAR:
			notValidYear = False
		
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
		
		if (tmpUserMonthStr.isdigit() 
			and int(tmpUserMonthStr) <= 12 
			and int(tmpUserMonthStr) > 0 
			and not tmpUserMonthStr.startswith("0")):
				
			notValidMonth = False
			
		else:
			print("\t-Invalid Month Entry-\n(Please enter an integer between 1-12 with no leading zeros)")
			tmpUserMonthStr = input("Please Enter a Month (example: 12): ")
			
	return int(tmpUserMonthStr)			


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
	
	
def getDailyFee(tmpDailyFee="None"):
	notVaildFee = True
	
	if tmpDailyFee == "None":
		tmpDailyFee = input("What is the daily fee? (example 0.25): ")
	
	#allows negative numbers, which could be used in pro-rating.
	while notVaildFee:
		validChars = True
		if tmpDailyFee == "":
			tmpDailyFee = "0"
			
		if tmpDailyFee.count(".") <= 1:
			if tmpDailyFee[0] == "-" and len(tmpDailyFee) > 1:
				for char in tmpDailyFee[1:]:
					validChars = True
					if not char.isdigit() or char == ".":
						validChars = False
						
			else:
				for char in tmpDailyFee:
					validChars = True
					if not char.isdigit() or char == ".":
						validChars = False
				
		if validChars == True:
			notVaildFee = False	
			
		else:
			print("\t-Invalid Entry-\n(Please Enter a Floating Number)")
			tmpDailyFee = input("What is the daily fee? (example 0.25): ")
			
	return float(tmpDailyFee)


def calcDiff (newestDate,oldestDate):
	deltaDate = newestDate-oldestDate
	deltaDaysInt = deltaDate.days
	
	if deltaDaysInt < 0:
		deltaDaysInt = 0
	
	return deltaDaysInt


def calcLateFee(tmpDueDate,tmpCurDate,tmpDailyFee=0):
	if tmpDueDate <= tmpCurDate:
		balanceIncurred = 0
		
	else:
		daysOverDue = calcDiff(tmpDueDate,tmpCurDate)
		balanceIncurred = daysOverDue * tmpDailyFee
		if balanceIncurred < 0:
			balancedIncurred = 0
	
	if balanceIncurred < 0:
		balanceIncurred = 0
		
	return float(balanceIncurred)


def displayTimePast():
	print("\n--------------------------------------------------------")
	print("|\t{:^40s}\t|".format("Calculate Time Past"))
	print("--------------------------------------------------------")
	stayInLoop = True
	
	while stayInLoop:
		print("\n\t### Enter Past Date ###")
		tmpYear = getYear()
		
		if tmpYear == -1:
			stayInLoop = False
			
		elif int(tmpYear) > today.year:
			print("\n\t### Time Difference ###\nThe date entered is in the future and has no days past\n")
			
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


def displayToday():
	print("\t----------------------------------")
	print("\t| Today is: {:^20s} |".format(today.strftime("%d %b, %Y")))
	print("\t----------------------------------")
	print("Enter \"END\" at any year input to exit that part of the scrip\n")				
	
	
def displayAmountDue():
	print("\n--------------------------------------------------------")
	print("|\t{:^40s}\t|".format("Calculate Amount Due"))
	print("--------------------------------------------------------")
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
			print("\n\t### Enter Return Date ###")
			tmpYearReturn = getYear()
			if tmpYearReturn == -1:
				stayInLoop = False
				
			else:
				tmpMonthReturn = getMonth()
				tmpDayReturn = getDay(tmpYearReturn,tmpMonthReturn)
				tmpDateReturn = date(tmpYearReturn,tmpMonthReturn,tmpDayReturn)
			
			print("\n\t### Enter Daily Fee ###")
			tmpFee = getDailyFee()
			balanceDue = calcLateFee(tmpDateReturn,tmpDateDue,tmpFee)	
			print("\n\tThe total amount due is ${:<.2f}\n".format(balanceDue))


def displayFirstFridays():
	print("\n--------------------------------------------------------")
	print("|\t{:^40s}\t|".format("First Fridays Of Every Month From A Year"))
	print("--------------------------------------------------------")
	
	stayInLoop = True

	while stayInLoop:
		print("\n\t### Enter Year Too Find First Fridays ###")
		tmpYear = getYear()
		
		if tmpYear == -1:
			stayInLoop = False
			
		else:
			print("\n\t### The First Fridays that Occur in year {:} ###".format(tmpYear))
			
			for month in range(1,13):
				monthDays = monthcalendar(tmpYear,month)
				firstWeek = monthDays[0]
				friday = firstWeek[4]
				
				if friday == 0:
					secondWeek = monthDays[1]
					friday = secondWeek[4]

				tmpDate = date(tmpYear,month,friday)
				print(tmpDate.strftime("%B %d"))
			
	



def main():
	displayToday()
	displayTimePast()
	displayAmountDue()
	displayFirstFridays()

if __name__ == "__main__":
	main()

