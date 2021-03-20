

def reversedOddIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	oddIndexNumList = []
	for indexLocation in range (cardLen-2,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		tmpNumInt = int(tmpNumStr)
		
		if tmpNumInt*2 > 9:
			doubledTmpNumInt = tmpNumInt*2
			
			firstTmpNumStr = str(doubledTmpNumInt)[0]
			secondTmpNumStr = str(doubledTmpNumInt)[1]
			
			firstTmpNumInt = int(firstTmpNumStr)
			secondTmpNumInt = int(secondTmpNumStr)
			
			newNumInt = firstTmpNumInt + secondTmpNumInt
			
			oddIndexNumList.append(newNumInt)
			
		else:
			oddIndexNumList.append(tmpNumInt)
			
		return sum(oddIndexList)
	
def reversedEvenIndexCardNumEvaluator (cardNumStr):	
	cardLen = len(cardNumStr)
	evenIndexNumList = []		
	for indexLocation in range (cardLen-1,-1,-2):
		tmpNumStr = cardNumStr[indexLocation]
		tmpNumInt = int(tmpNumStr)
		evenIndexNumList.append(tmpNumInt)
		
	return sum(evenIndexNumList)

		
def main():
	print("MasterCard")
	testCardOne = "512345678912345"
	print("testCard 1: ",testCardOne,reversedEvenIndexCardNumEvaluator(testCardOne))
	
	print("\nVisa")
	testCardTwo = "412345678912345"
	print("testCard 2: ",testCardTwo,reversedEvenIndexCardNumEvaluator(testCardTwo))
	
	print("\nAmericanExpress")
	testCardThree ="3712345678912345"
	print("testCard 3: ",testCardThree,reversedEvenIndexCardNumEvaluator(testCardThree))
	
	print("\nDiscover")
	testCardFour = "612345678912345"
	print("testCard 4: ",testCardFour,reversedEvenIndexCardNumEvaluator(testCardFour))
	
	#testCardFive = input("\nEnter Card Num: ")



if __name__ == "__main__":
	main()
