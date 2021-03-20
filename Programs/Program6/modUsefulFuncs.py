#Paul Kummer
#CSIS 153
#Useful Functions

__author__="Paul Kummer"
__date__="10/22/18"

#Reference for Euclidean Algorithm:
#https://www.khanacademy.org/computing/computer-science/cryptography/
#modarithmetic/a/the-euclidean-algorithm


def greatestCommonDivisor (tmpNumerator,tmpDenominator):
	
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
