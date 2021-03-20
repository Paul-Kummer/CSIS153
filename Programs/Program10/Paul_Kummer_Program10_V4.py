#Paul Kummer
#CSIS 153
#Program 10
#Due 12/05/18

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

V4:
Cleaned up some code for readability using PEP 8 Style Guidelines and added
Doc-Strings. Also, fixed an issue when the user supplied "" as an arg.
"""

__author__ = "Paul Kummer"
__date__ = "12/05/18"
__version__ = "version 4"

from datetime import *
from calendar import *

#global var
today = date.today()


def getYear(tmpUserYearStr=-1):
	"""
	Precondition:
	tmpUserYearStr must be a string or integer -1
	
	Postcondition:
	Returns an integer within datetime's years
	
	Description:
	tmpUserYearStr is checked against the module datetime's min and max
	resolution to determine if it is within range. Then it is checked for
	only string representation of digits, indicating acceptable characters. 
	If the user doesn't supply an argument the default value of 
	tmpUserYearStr is negative one or if the argument is "", indicating 
	that the user is to be prompted for input. The user will continue to
	be prompted until they enter END or enter a valid month.
	"""
	
	notValidYear = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserYearStr == -1 or tmpUserYearStr == "":
		tmpUserYearStr = input("Please Enter a Year (example: 2018): ")
	
	while notValidYear:
		
		#user chooses to exit function and -1 is returned specifying exit
		if tmpUserYearStr == "END":
			notValidYear = False
			tmpUserYearStr = -1
			
		#handles integers between datetime's resolution
		elif (tmpUserYearStr.isdigit() 
			and int(tmpUserYearStr) <= MAXYEAR
			and int(tmpUserYearStr) >= MINYEAR):
				
			notValidYear = False
		
		else:
			print("\t-Invalid Year Entry-\n(Please enter an integer less than or equal to todays year)")
			tmpUserYearStr = input("Please Enter a Year (example: 2018): ")
			
	return int(tmpUserYearStr)


def getMonth(tmpUserMonthStr=-1):
	"""
	Precondition:
	tmpUserMonthStr must be a string or integer -1
	
	Postcondition:
	Returns an integer within the range of months
	
	Description:
	tmpUserMonthStr is checked against the integers 1-12 to determine if
	the user input is within the range of months. Also, it is checked for
	only string representation of digits, indicating acceptable characters. 
	If the user doesn't supply an argument the default value of tmpUserMonthStr
	is negative one or if the argument is "", indicating that the user 
	is to be prompted for input. The user will continue to be prompted 
	until they enter a valid month.	
	"""
	
	notValidMonth = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserMonthStr == -1 or tmpUserMonthStr == "":
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
def getDay (tmpYear, tmpMonth, tmpUserDayStr=-1):
	"""
	Precondition:
	*tmpUserDayStr must be a string or integer -1
	*tmpMonth must be an integer of a vaild month
	*tmpYear must be an integer of a vailid datetime year
	
	Postcondition:
	Returns an integer within the range of a month from a specific year.
	
	Description:
	tmpUserDayStr is checked against the valid integers for a specific
	month from a specific year. Also, it is checked for only string 
	representation of digits, indicating acceptable characters. 
	If the user doesn't supply an argument the default value of tmpUserDayStr
	is negative one or if the argument is "", indicating that the user 
	is to be prompted for input. The user will continue to be prompted 
	until they enter a valid day.
	"""
	
	monthObj = monthcalendar(tmpYear,tmpMonth)
	
	#selects the maximum value from the last list, which is the the last
	#day of the last week of that specific month.
	maxMonthRange = max(monthObj[len(monthObj)-1])
	notValidDay = True
	
	#checks if user supplied an argument. Then prompts for input if no arg
	if tmpUserDayStr == -1 or tmpUserDayStr == "":
		tmpUserDayStr = input("Please Enter a Day (between 1 and {:}): "\
			.format(maxMonthRange))
	
	while notValidDay:

		if (tmpUserDayStr.isdigit() 
			and int(tmpUserDayStr) <= maxMonthRange
			and int(tmpUserDayStr) > 0):
				
			notValidDay = False
			
		else:
			print("\t-Invalid Day Entry-\n(Please enter an integer between 1 and {:})"\
				.format(maxMonthRange))
				
			tmpUserDayStr = input("Please Enter a Day (between 1 and {:}): "\
				.format(maxMonthRange))
			
	return int(tmpUserDayStr)
	
	
def getDailyFee(tmpDailyFee="None"):
	"""
	Precondition:
	tmpDailyFee must be a string
	
	Postcondition:
	tmpDailyFee is returned as a float
	
	Description:
	tmpDailyFee string is analyzed to determine that the string can be
	converted to a float without errors. If the user does not supply an
	argument or the argument is "", they will be prompted to enter a 
	string value for tmpDailyFee that meets the criteria of a float.
	"""
	
	notVaildFee = True
	
	#user didn't specify a valu
	if tmpDailyFee == "None" or tmpDailyFee == "":
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


def calcDiff (newestDate, oldestDate):
	"""
	Precondition:
	Two datetime.date objects supplied as arguments
	
	Postcondition:
	deltaDaysInt is returned as an integer
	
	Description:
	Two date objects are compared to determine the number of days between
	the two dates. If the dates have a negative value of days between them,
	the days of difference is zero. This indicates that the dates are
	entered in the wrong order for the purpose of this program, where the
	newest date cannot occur before the oldest date.
	"""
	
	deltaDate = newestDate - oldestDate
	deltaDaysInt = deltaDate.days
	
	#Occurs if oldest date was entered before newest date
	if deltaDaysInt < 0:
		deltaDaysInt = 0
	
	return deltaDaysInt


def calcLateFee(tmpDueDate, tmpCurDate, tmpDailyFee=0):
	"""
	Precondition:
	*tmpDueDate and tmpCurDate must be date objects.
	*tmpDailyFee must be an integer or float
	
	Postcondition:
	returns balanceIncurred as a float
	
	Description:
	Checks the dueDate agains the curDate to determine if the dueDate is
	after the curDate. If true, the balace will be zero. Otherwise, the 
	due date has been passed and the daily fee is multiplied by the days
	passed. The code could be modified slightly to allow negative values,
	which could be used for pro-rating.
	"""
	
	#checks if the due date is in the future of the supplied current date
	if tmpDueDate <= tmpCurDate:
		balanceIncurred = 0
		
	else:
		daysOverDue = calcDiff(tmpDueDate,tmpCurDate)
		balanceIncurred = daysOverDue * tmpDailyFee
	
	if balanceIncurred < 0:
		balanceIncurred = 0
		
	return float(balanceIncurred)


def displayTimePast():
	"""
	Precondition:
	None
	
	Postcondition:
	Displays to User
	
	Description:
	Calls functions to gather a date to determine how many days and/or years
	have past since that date and today. The user has this information
	displayed to them in the terminal.
	"""
	
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
			tmpDay = getDay(tmpYear, tmpMonth)
			tmpDate = date(tmpYear, tmpMonth, tmpDay)
			daysOfDifference = calcDiff(today, tmpDate)
	
			if daysOfDifference >= 365:
				deltaYears = daysOfDifference // 365
				daysOfDifference = daysOfDifference - (deltaYears * 365)
				
				print("\n\t### Time Difference ###\n{1:^.0f} years and {0:^.0f} days have past between {2:} and today.\n"\
					.format(daysOfDifference, deltaYears, tmpDate.strftime("%d %b, %Y")))
				
			elif daysOfDifference >= 0:
				print("\n\t### Time Difference ###\n{:3^.0f} days have past between {:} and today.\n"\
					.format(daysOfDifference, tmpDate.strftime("%d %b, %Y")))


def displayToday():
	"""
	Precondition:
	None
	
	Postcondition:
	Displays to User
	
	Description:
	Displays to user the current date, which may be important for use in
	other parts of the program. Additionaly it tells the user how to exit
	the program once it has started running.
	"""
	
	print("\t----------------------------------")
	print("\t| Today is: {:^20s} |".format(today.strftime("%d %b, %Y")))
	print("\t----------------------------------")
	print("Enter \"END\" at any year input to exit that part of the script\n")				
	
	
def displayAmountDue():
	"""
	Precondition:
	None
	
	Postcondition:
	Displays to User
	
	Description:
	Gathers dates and daily fees from user prompts to calculate the 
	difference of dates and an amount due. After calculations are made
	the user has the amount due displayed to them.
	"""
	
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
			tmpDayDue = getDay(tmpYearDue, tmpMonthDue)
			tmpDateDue = date(tmpYearDue, tmpMonthDue, tmpDayDue)
		
		
		if stayInLoop == True:
			print("\n\t### Enter Return Date ###")
			tmpYearReturn = getYear()
			
			if tmpYearReturn == -1:
				stayInLoop = False
				
			else:
				tmpMonthReturn = getMonth()
				tmpDayReturn = getDay(tmpYearReturn, tmpMonthReturn)
				tmpDateReturn = date(tmpYearReturn, tmpMonthReturn, tmpDayReturn)
			
			print("\n\t### Enter Daily Fee ###")
			tmpFee = getDailyFee()
			
			balanceDue = calcLateFee(tmpDateReturn, tmpDateDue, tmpFee)	
			print("\n\tThe total amount due is ${:<.2f}\n".format(balanceDue))


def displayFirstFridays():
	"""
	Precondition:
	None
	
	Postcondition:
	Displays to User
	
	Description:
	From user prompts for a year, the user is displayed the first fridays
	of every month from that year.
	"""
	
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
			print("\n\t### The First Fridays that Occur in year {:} ###"\
				.format(tmpYear))
			
			for month in range(1, 13):
				monthDays = monthcalendar(tmpYear, month)
				firstWeek = monthDays[0]
				friday = firstWeek[4]
				
				if friday == 0:
					secondWeek = monthDays[1]
					friday = secondWeek[4]

				tmpDate = date(tmpYear, month, friday)
				print(tmpDate.strftime("%B %d"))
			
	



def main():
	"""
	Precondition:
	None
	
	Postcondition:
	Run Functions
	
	Description:
	Runs functions from within the program.
	"""
	
	displayToday()
	displayTimePast()
	displayAmountDue()
	displayFirstFridays()

if __name__ == "__main__":
	main()

