#Paul Kummer
#CSIS 153
#Useful Functions

__author__="Paul Kummer"
__date__="10/22/18"

#Reference for Euclidean Algorithm:
#https://www.khanacademy.org/computing/computer-science/cryptography/
#modarithmetic/a/the-euclidean-algorithm

"""
Description:

This module contains useful fuctions to be used in other python scripts.
Currently it contains;
1. greatestCommonDivisor
	*find and return the greatest common divisor between two numbers
2. random
	*generate a random number within a range and divisibility
"""

from datetime import datetime
import time

def greatestCommonDivisor (tmpNumerator,tmpDenominator):
	
	"""
	Pre-condition: Requires two arguments that are real numbers
	
	Post-condition: Numerator equals the greatest common divisor and
						denominator equals zero
	
	Description: Returns the greatest common divisor of a numerator and 
					a denominator
	"""
	
	#prevent divide by zero errors by not allowing a 0 denominator
	if tmpDenominator != 0:
		
		#set initial values for the fraction
		tmpNumerator = abs(tmpNumerator)
		tmpDenominator = abs(tmpDenominator)
		tmpRemainder = tmpNumerator%tmpDenominator
		
		
		#enter the loop that divides the previous denominator by 
		#the remainder of the previous numerator and denomintor
		findingLowestTerm=True
		while findingLowestTerm:
			
			#denominator becomes the numerator
			workingNumerator = tmpDenominator
				
			#remainder becomes the denominator
			workingDenominator = tmpRemainder
			
			#check if the greatest common divisor is found, making
			#workingDenominator equal zero. This indicates that there 
			#is no more remainders to be found
			if tmpRemainder == 0:
				
				#exit loop
				findingLowestTerm=False
				
			#continue looping, since there is a greater divisor
			else:
				
				#update values for numerator, denominator, and remainder
				tmpNumerator = workingNumerator
				tmpDenominator = workingDenominator
				tmpRemainder = workingNumerator%workingDenominator
				

				
		#workingNumerator is returned as the greatest common divisor
		#since there are no more remainders
		return workingNumerator
		
	#returns zero if initial denominator is 0
	else:
		return 0
		

#PRNG, pseudo random number generator, not tested for cryptographic use
def random (tmpNumStart=0,tmpNumStop=100, tmpNumDivisor=1):
	"""
	Pre-condition: tmpNumStart,tmpNumStop, and tmpNumDivisor must be integers
	
	Post-condition: RandomNumList populated with possible values
					indexSelection is chose from memory location and current time
					memorySeed is assigned value of today's memory address
					timeSeed is assigned the current microsecond of today
					pauseTime is assigned from .05 seconds multiplied by length of randomNumList divided by indexSelection
					randomNumber is assigned value from index selection from randomNumList
	
	Description: Based on user specifications a random number is returned
				from a range and divisibility
	"""
	
	startNum = tmpNumStart
	stopNum = tmpNumStop+1
	divisor = tmpNumDivisor
	today = datetime.today()
	
	
	randomNumList = []
	
	#create possible options
	for number in range(startNum,stopNum):
		if number%divisor == 0:
			randomNumList.append(number)
	
	#seeds for choosing random number
	memorySeed = int(id(today))
	timeSeed = int(today.microsecond)
	
	while memorySeed < timeSeed:
		memorySeed *= memorySeed
	
	indexSelection = memorySeed//timeSeed
	while indexSelection > len(randomNumList):
		indexSelection -=len(randomNumList)
	
	#pause for creating new seed
	pauseTime = .05/(len(randomNumList)//indexSelection)
	time.sleep(pauseTime)
	
	#selection of random Number
	randomNumber = randomNumList[indexSelection-1]
	
	return randomNumber
