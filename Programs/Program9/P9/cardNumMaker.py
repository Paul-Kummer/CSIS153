import sys
import random

creditCardList = []
			
cardLength = 11
while cardLength < 16:
	
	cardsMade = 0
	while cardsMade <= 20:
		visa = "4"
		mastercard = "5"
		americanExpress = "37"
		discover = "6"
		
		for tmpCardLenCt in range(cardLength):
			tmpNumStr = str(random.randint(0,9))
			
			if cardLength > 11:
				visa += tmpNumStr
				mastercard += tmpNumStr
				discover += tmpNumStr
			if cardLength < 15:
				americanExpress += tmpNumStr
		
		if len(visa) >= 13:	
			creditCardList.append(visa)
		if len(mastercard) >= 13:
			creditCardList.append(mastercard)
		if len(americanExpress) >= 13:
			creditCardList.append(americanExpress)
		if len(discover) >= 13:
			creditCardList.append(discover)
		
		cardsMade += 1
		
	cardLength += 1


fileOfCards = open("creditCards.txt", "w")
fileOfCards.close()
fileOfCards = open("creditCards.txt", "a+")

for card in creditCardList:
	fileOfCards.write(card+"\n")
	
fileOfCards.close()
