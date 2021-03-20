#Paul Kummer
#CSIS 153
#Program 7
#Due: 10/31/18

__author__="Paul Kummer"
__date__="10/31/18"


"""
Description: 

V1:
This module will create a class object of a fraction. It requires two
integers to be passed into the class. The first integer will be the 
numerator and the second integer will be the denominator. The 
denominator will not be allowed to be zero or a negative value.
Additionally, the fraction will be reduced to the least common
denominator.  The output will be a string with a forward slash
seperating the numerator and denominator. Also, if the fraction is
negative, the negative denotation will be applied to the numerator.

V2:
Created Methods to allow mathematical operations to be performed with
Fraction objects and other Fraction objects as well as Integers

Note: must have modUsefulFuncs in working directory
"""

#import a function that returns the greatest common divisor and call the
#function with gcd instead of greatestCommonDivisor
from modUsefulFuncs import greatestCommonDivisor as gcd

#class for creating fraction objects
class Fraction:
	
	
	#set default numerator and denominator values to prevent errors
	def __init__ (self,tmpNumerator=0,tmpDenominator=1):
		"""
		Pre-conditon: must pass no more than two rational numbers to Fraction
		
		Post-conditions: make private attributes numerator and denominator 
							with values reduced
		
		Description: create fraction object with numerator and denominator
		"""
		
		
		
		#assign greatest common divisor by calling gcd
		self._fractionGCD=gcd(tmpNumerator,tmpDenominator)
		
		#assign default value if denominator is zero
		if tmpDenominator == 0:
			self._numerator=0
			self._denominator=1
		
		#assign values if tmpDenominator is negative
		#this must be an elif otherwise divide by zero can occur
		elif tmpDenominator < 0:
			
			#inverse the signs of the numerator and denominator and
			#divide each by the greatest common divisor
			self._numerator=(-1*tmpNumerator)/self._fractionGCD
			self._denominator=(-1*tmpDenominator)/self._fractionGCD

		#denominator is greater than zero	
		else:
			
			#divide numerator and denominator by greatest common divisor
			self._numerator=tmpNumerator/self._fractionGCD
			self._denominator=tmpDenominator/self._fractionGCD
			
			
	#create a useful string value to be returned when the class object
	#is called. The object will look like "integer/integer"	
	def __str__ (self):
		
		"""
		Pre-conditon: None
		
		Post-conditions: None
		
		Description: Returns a string when fraction object is called
		"""
		
		return "{:>.0f}/{:<.0f}"\
				.format(self._numerator,self._denominator)



	def getNumerator(self):
		"""
		Pre-conditon: One argument of fraction object
		
		Post-conditions: None
		
		Description: Returns numerator of fraction object
		"""
		
		return(self._numerator)
	
	
	
	def getDenominator(self):
		"""
		Pre-conditon: One argument of fraction object
		
		Post-conditions: None
		
		Description: Returns denominator of fraction object
		"""
		return(self._denominator)



	def __add__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object
		
		Post-conditions: Adds the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments.
		"""
		
		#isinstance(tmpObject,class) 
		#from https://stackoverflow.com/questions/18499614/check-if-class-object
		#both are instances of Fraction
		if isinstance(tmpValue,Fraction):
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue.getNumerator()
			operandTwoDenominator = tmpValue.getDenominator()

			newNumerator = operandOneDenominator*operandTwoNumerator+\
						   operandTwoDenominator*operandOneNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue
			operandTwoDenominator = 1
			
			newNumerator = operandOneDenominator*operandTwoNumerator+\
						   operandTwoDenominator*operandOneNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
		
		
	#radd from https://www.python-course.eu/python3_magic_methods.php
	#adding from left to right failed so python adds from right to left
	def __radd__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object, including float and int
		
		Post-conditions: Adds the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments. Only executes if initially a 
						non-fraction object was attempted to be added to 
						a fraction object.
		"""
	
		#tmpValue is not an instance of Fraction
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		operandTwoNumerator = tmpValue
		operandTwoDenominator = 1
			
		newNumerator = operandOneDenominator*operandTwoNumerator+\
					   operandTwoDenominator*operandOneNumerator

		newDenominator = operandTwoDenominator*operandOneDenominator
			
		newFraction = Fraction(newNumerator,newDenominator)
		return newFraction
		
		
		
	def __sub__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object
		
		Post-conditions: subtracts the numerical values of both arguments 
							to create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments.
		"""
		if isinstance(tmpValue,Fraction):
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue.getNumerator()
			operandTwoDenominator = tmpValue.getDenominator()

			newNumerator = operandOneNumerator*operandTwoDenominator-\
						   operandOneDenominator*operandTwoNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue
			operandTwoDenominator = 1
			
			newNumerator = operandTwoDenominator*operandOneNumerator-\
						   operandOneDenominator*operandTwoNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
		
		
	#subtracting from left to right failed so python adds from right to left
	def __rsub__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: subtracts the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments. Only executes if initially a 
						non-fraction object was attempted to be subtracted
						to a fraction object.
		"""
	
		#tmpValue is not an instance of Fraction
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		operandTwoNumerator = tmpValue
		operandTwoDenominator = 1
			
		newNumerator = \
operandOneDenominator*operandTwoNumerator-operandTwoDenominator*operandOneNumerator

		newDenominator = operandTwoDenominator*operandOneDenominator
			
		newFraction = Fraction(newNumerator,newDenominator)
		return newFraction
	
		
		
	def __mul__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: multiplies the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments.
		"""
		
		if isinstance(tmpValue,Fraction):
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue.getNumerator()
			operandTwoDenominator = tmpValue.getDenominator()

			newNumerator = operandTwoNumerator*operandOneNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue
			operandTwoDenominator = 1
			
			newNumerator = operandOneNumerator*operandTwoNumerator

			newDenominator = operandTwoDenominator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
			
		
	def __rmul__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: multiplies the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments. Only executes if initially a 
						non-fraction object was attempted to be multiplied
						to a fraction object.
		"""
		
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		operandTwoNumerator = tmpValue
		operandTwoDenominator = 1
		
		newNumerator = operandOneNumerator*operandTwoNumerator

		newDenominator = operandTwoDenominator*operandOneDenominator
		
		newFraction = Fraction(newNumerator,newDenominator)
		return newFraction	
	
	
	
	def __truediv__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments.
		
		Post-conditions: fraction object created from floor division is 
							assigned a variable
		
		Description: Takes two arguments and makes them arguments of
						floor division. Then whatever is returned from
						floor division is returned by true division.
		"""
		
		tmpFraction = self.__floordiv__(tmpValue)
		return tmpFraction
			
			
	
	def __rtruediv__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments.
		
		Post-conditions: fraction object created from floor division is 
							assigned a variable
		
		Description: Takes two arguments and makes them arguments of
						floor division. Then whatever is returned from
						floor division is returned by true division. Only 
						executes if initially a non-fraction object was 
						attempted to be true divided to a fraction object.
		"""
		
		tmpFraction = self.__rfloordiv__(tmpValue)
		return tmpFraction
		
		
	def __floordiv__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: divides the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments.
		"""
		
		if isinstance(tmpValue,Fraction):
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue.getNumerator()
			operandTwoDenominator = tmpValue.getDenominator()

			newNumerator = operandTwoDenominator*operandOneNumerator

			newDenominator = operandTwoNumerator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneNumerator = self._numerator
			operandOneDenominator = self._denominator
			operandTwoNumerator = tmpValue
			operandTwoDenominator = 1
			
			newNumerator = operandTwoDenominator*operandOneNumerator

			newDenominator = operandTwoNumerator*operandOneDenominator
			
			newFraction = Fraction(newNumerator,newDenominator)
			return newFraction
			
			
		
	def __rfloordiv__ (self,tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: divides the numerical values of both arguments to
							create a new numerator and denominator. These
							are then used to create a new fraction object
		
		Description: A new fraction object is created and returned from
						two arguments. Only executes if initially a 
						non-fraction object was attempted to be divided
						to a fraction object.
		"""
		
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		operandTwoNumerator = tmpValue
		operandTwoDenominator = 1
		
		newNumerator = operandTwoDenominator*operandOneNumerator

		newDenominator = operandTwoNumerator*operandOneDenominator
		
		newFraction = Fraction(newNumerator,newDenominator)
		return newFraction
	
	
	#there is no __rlt__(self,value)
	def __lt__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is less than
						The second, True is returned. Otherwise False is
						returned.
		"""
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue < operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue < operandTwoValue:
				return True
			
			else:
				return False
	
	
		
	def __le__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is less than
						or equal to the second, True is returned. 
						Otherwise False is returned.
		"""
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue <= operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue <= operandTwoValue:
				return True
			
			else:
				return False
	
	
		
	def __eq__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is equal to
						The second, True is returned. Otherwise False is
						returned.
		"""		
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue == operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue == operandTwoValue:
				return True
			
			else:
				return False
	
		
		
	def __ne__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: is True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is not equal 
						to The second, True is returned. Otherwise False
						is returned.
		"""		
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue != operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue != operandTwoValue:
				return True
			
			else:
				return False
	
	
	
	def __gt__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: is True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is greater than
						The second, True is returned. Otherwise False is
						returned.
		"""		
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue > operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue > operandTwoValue:
				return True
			
			else:
				return False
	
	
		
	def __ge__(self, tmpValue):
		"""
		Pre-conditon: Requires two arguments. the first argument to be a 
						fraction object and the second to be a rational 
						number or fraction object. 
		
		Post-conditions: True or False
		
		Description: The first numerical value is compared to the second
						numerical value. If the first Value is greater than
						or equal to the second, True is returned. 
						Otherwise False is returned.
		"""		
		
		if isinstance(tmpValue,Fraction):
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue.getNumerator()/tmpValue.getDenominator()

			if operandOneValue >= operandTwoValue:
				return True
			
			else:
				return False
			
		#tmpValue is not an instance of Fraction
		else:
			operandOneValue = self._numerator/self._denominator
			operandTwoValue = tmpValue
			
			if operandOneValue >= operandTwoValue:
				return True
			
			else:
				return False
	
	
				
	def __float__ (self):
		"""
		Pre-conditon: One fraction object argument
		
		Post-conditions: Floating number
		
		Description: A fraction object is converted to its decimal 
						equivalent.
		"""			
		
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		return float(operandOneNumerator/operandOneDenominator)
		
	
	def __int__ (self):
		"""
		Pre-conditon: One fraction object argument
		
		Post-conditions: Integer
		
		Description: A fraction object is converted to its integer 
						equivalent.
		"""			
		
		operandOneNumerator = self._numerator
		operandOneDenominator = self._denominator
		return int(operandOneNumerator/operandOneDenominator)
		
		
	def __invert__ (self):
		"""
		Pre-conditon: One fraction object argument
		
		Post-conditions: inverse of float value from fraction object is
							assigned to variable. Then a new fraction 
							object is created from inverse float.
		
		Description: A fraction object is converted to an inverted
						fraction object and returned.
		"""			
		
		#the initial fractions floating value is inverted by taking it to
		#the negative one power. This numerical value is used to create a 
		#new fraction object, which is the inverse of the original object
		tmpFloat = self.__float__()
		if tmpFloat != 0:
			inverseFloat = tmpFloat**-1
		else:
			inverseFloat = 0
		return Fraction(inverseFloat)
		
		
