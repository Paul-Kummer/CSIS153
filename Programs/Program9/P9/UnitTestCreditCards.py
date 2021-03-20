import unittest

from validateCreditCards import *

unkownCardType = "723456789012345"

alphaDiscover = "6 1a6534183606"
alphaVisa = "467691106b4390"
alphaMastercard = "5676c110634390"
alphaAmEx = "376769110634%9d"

validLength = "1234567890123"
validLengthTwo = "1234567890123456"

invalidLength = "123"
invalidLengthTwo = "12345678901234567"


validVisa = "404173206797802"
#Eval One: 2+8+9+6+2+7+4+4=42
#Eval Two: (0*2)+[(7*2)=14]:5+[(7*2)=14]:5+(0*2)+(3*2)+(3*2)+(1*2)+(0*2)
#0+5+5+0+6+2+0=18

validDiscover = "6007910368143632"
#Eval One: 2+6+4+8+3+1+7+0=31
#Eval Two: (3*2)+(3*2)+(1*2)+[(6*2)=12]:3+(0*2)+[(9*2)=18]:9+(0*2)+[(6*2)=12]:3
#6+6+2+3+0+9+0+3=29

validMastercard = "5438689732975942"
#Eval One: 2+9+7+2+7+8+8+4=47
#Eval Two: (4*2)+[(5*2)=10]:1+[(9*2)=18]:9+(3*2)+[(9*2)=18]:9+[(6*2)=12]:3+(3*2)+[(5*2)=10]:1
#8+1+9+6+9+3+6+1=43

validAmEx = "3737710359072582"
#Eval One:2+5+7+9+3+1+7+7=41
#Eval Two: [(8*2)=16]:7+(2*2)+(0*2)+[(5*2)=10]:1+(0*2)+[(7*2)=14]:5+(3*2)+(3*2)
#7+4+0+1+0+5+6+6=29


invalidVisa = "46146534183606"
#Eval One: 6+6+8+4+5+4+6=39
#Eval Two: 0+6+2+6+3+2+8=27

invalidDiscover = "66769110634390"
#Eval One: 0+3+3+0+1+6+6=19
#Eval Two: 9+8+3+2+9+5+3=39

invalidMastercard = "5474049196011"
#Eval One: 1+0+9+9+0+7+5=31
#Eval Two: 2+3+2+8+8+8=31

invalidAmEx = "37689682437025"
#Eval One: 5+0+3+2+6+8+7=31
#Eval Two: 4+5+8+7+9+3+6=42


#reversedEvenIndexCardNumEvaluator	
class TestEvalOne (unittest.TestCase):
	def testAlphaInCard(self):
		self.assertEqual(reversedEvenIndexCardNumEvaluator(alphaVisa),-1)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(alphaDiscover),-1)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(alphaMastercard),19)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(alphaAmEx),-1)
		
	def testValidCard(self):
		self.assertEqual(reversedEvenIndexCardNumEvaluator(validVisa),42)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(validDiscover),31)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(validMastercard),47)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(validAmEx),41)
		
	def testInvalidCard(self):
		self.assertEqual(reversedEvenIndexCardNumEvaluator(invalidVisa),39)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(invalidDiscover),19)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(invalidMastercard),31)
		self.assertEqual(reversedEvenIndexCardNumEvaluator(invalidAmEx),31)
		
#reversedOddIndexCardNumEvaluator		
class TestEvalTwo (unittest.TestCase):
	def testAlphaInCard(self):
		self.assertEqual(reversedOddIndexCardNumEvaluator(alphaVisa),44)
		self.assertEqual(reversedOddIndexCardNumEvaluator(alphaDiscover),22)
		self.assertEqual(reversedOddIndexCardNumEvaluator(alphaMastercard),-1)
		self.assertEqual(reversedOddIndexCardNumEvaluator(alphaAmEx),41)
		
	def testValidCard(self):
		self.assertEqual(reversedOddIndexCardNumEvaluator(validVisa),18)
		self.assertEqual(reversedOddIndexCardNumEvaluator(validDiscover),29)
		self.assertEqual(reversedOddIndexCardNumEvaluator(validMastercard),43)
		self.assertEqual(reversedOddIndexCardNumEvaluator(validAmEx),29)
		
	def testInvalidCard(self):
		self.assertEqual(reversedOddIndexCardNumEvaluator(invalidVisa),27)
		self.assertEqual(reversedOddIndexCardNumEvaluator(invalidDiscover),39)
		self.assertEqual(reversedOddIndexCardNumEvaluator(invalidMastercard),31)
		self.assertEqual(reversedOddIndexCardNumEvaluator(invalidAmEx),42)
	
class TestCardType (unittest.TestCase):
	def testUnknownCard (self):
		self.assertEqual(getCardType(unkownCardType),"N/A")
	
	def testVisa (self):
		self.assertEqual(getCardType(validVisa),"Visa")
		
	def testDiscover (self):
		self.assertEqual(getCardType(validDiscover),"Discover")
		
	def testMastercard (self):
		self.assertEqual(getCardType(validMastercard),"Mastercard")
		
	def testAmEx (self):
		self.assertEqual(getCardType(validAmEx),"American Express")
		
	
class TestCardEvaluator (unittest.TestCase):
	def testAlphaInCard(self):
		self.assertEqual(cardNumEvaluator(alphaVisa),False)
		self.assertEqual(cardNumEvaluator(alphaDiscover),False)
		self.assertEqual(cardNumEvaluator(alphaMastercard),False)
		self.assertEqual(cardNumEvaluator(alphaAmEx),False)
		
	def testValidCard(self):
		self.assertEqual(cardNumEvaluator(validVisa),True)
		self.assertEqual(cardNumEvaluator(validDiscover),True)
		self.assertEqual(cardNumEvaluator(validMastercard),True)
		self.assertEqual(cardNumEvaluator(validAmEx),True)
		
	def testInvalidCard(self):
		self.assertEqual(cardNumEvaluator(invalidVisa),False)
		self.assertEqual(cardNumEvaluator(invalidDiscover),False)
		self.assertEqual(cardNumEvaluator(invalidMastercard),False)
		self.assertEqual(cardNumEvaluator(invalidAmEx),False)
	
class TestIsValidCard (unittest.TestCase):
	def testUnknownCard (self):
		self.assertEqual(isValidCreditCard(unkownCardType),False)
		
	def testValidCardLen (self):
		self.assertEqual(isValidCreditCard(validLength),False)
		self.assertEqual(isValidCreditCard(validLengthTwo),False)
		
	def testLongCardLen (self):
		self.assertEqual(isValidCreditCard(invalidLengthTwo),False)
		
	def testShortCardLen (self):
		self.assertEqual(isValidCreditCard(invalidLength),False)
	
	def testAlphaInCard(self):
		self.assertEqual(isValidCreditCard(alphaVisa),False)
		self.assertEqual(isValidCreditCard(alphaDiscover),False)
		self.assertEqual(isValidCreditCard(alphaMastercard),False)
		self.assertEqual(isValidCreditCard(alphaAmEx),False)
		
	def testValidCard(self):
		self.assertEqual(isValidCreditCard(validVisa),True)
		self.assertEqual(isValidCreditCard(validDiscover),True)
		self.assertEqual(isValidCreditCard(validMastercard),True)
		self.assertEqual(isValidCreditCard(validAmEx),True)
		
	def testInvalidCard(self):
		self.assertEqual(isValidCreditCard(invalidVisa),False)
		self.assertEqual(isValidCreditCard(invalidDiscover),False)
		self.assertEqual(isValidCreditCard(invalidMastercard),False)
		self.assertEqual(isValidCreditCard(invalidAmEx),False)
	

def main():	
	print("\t---Checking reversedEvenIndexCardNumEvaluator function---")		
	suiteOne = unittest.TestLoader().loadTestsFromTestCase(TestEvalOne)
	unittest.TextTestRunner(verbosity=2).run(suiteOne)
	
	print("\n\t---Checking reversedOddIndexCardNumEvaluator function---")
	suiteTwo = unittest.TestLoader().loadTestsFromTestCase(TestEvalTwo)
	unittest.TextTestRunner(verbosity=2).run(suiteTwo)
	
	print("\n\t---Checking getCardType function---")
	suiteThree = unittest.TestLoader().loadTestsFromTestCase(TestCardType)
	unittest.TextTestRunner(verbosity=2).run(suiteThree)
	
	print("\n\t---Checking cardNumEvaluator function---")
	suiteFour = unittest.TestLoader().loadTestsFromTestCase(TestCardEvaluator)
	unittest.TextTestRunner(verbosity=2).run(suiteFour)
	
	print("\n\t---Checking isValidCreditCard function---")
	suiteFive = unittest.TestLoader().loadTestsFromTestCase(TestIsValidCard)
	unittest.TextTestRunner(verbosity=2).run(suiteFive)


if __name__ == "__main__":
	main()
