#Paul Kummer
#CSIS 153
#Program 6
#Due: 10/26/18

__author__="Paul Kummer"
__date__="10/22/18"

#Description
"""
This module will create a class object of a fraction. It requires two
integers to be passed into the class. The first integer will be the 
numerator and the second integer will be the denominator. The 
denominator will not be allowed to be zero or a negative value.
Additionally, the fraction will be reduced to the least common
denominator.  The output will be a string with a forward slash
seperating the numerator and denominator. Also, if the fraction is
negative, the negative denotation will be applied to the numerator.
"""

#import a function that returns the greatest common divisor and call the
#function with gcd instead of greatestCommonDivisor
from modUsefulFuncs import greatestCommonDivisor as gcd

#create a class for creating fraction objects
class Fraction:
	
	#set default numerator and denominator values to prevent errors
	def __init__ (self,tmpNumerator=0,tmpDenominator=1):
		
		#assign greatest common divisor by calling gcd
		self._tmpGCD=gcd(tmpNumerator,tmpDenominator)
		
		#assign default value if denominator is zero
		if tmpDenominator == 0:
			self._tmpNumerator=0
			self._tmpDenominator=1
		
		#assign values if tmpDenominator is negative
		elif tmpDenominator < 0:
			
			#inverse the signs of the numerator and denominator and
			#divide each by the greatest common divisor
			self._tmpNumerator=(-1*tmpNumerator)/self._tmpGCD
			self._tmpDenominator=(-1*tmpDenominator)/self._tmpGCD

		#denominator is greater than zero	
		else:
			
			#divide numerator and denominator by greatest common divisor
			self._tmpNumerator=tmpNumerator/self._tmpGCD
			self._tmpDenominator=tmpDenominator/self._tmpGCD
			
	#create a useful string value to be returned when the class object
	#is called. The object will look like "integer/integer"	
	def __str__ (self):
		return "{:>.0f}/{:<.0f}"\
.format(self._tmpNumerator,self._tmpDenominator)

		
			
		
		
