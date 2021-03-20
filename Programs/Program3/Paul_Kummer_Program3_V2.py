#Paul Kummer
#CSIS 153
#Program3

__author__="Paul Kummer"
__date__="9/26/18"

import os.path


#go through a file and find all word-like items and return a dictionary with count of word-like items
def findWords(fileName):
	fileObject = open(fileName,"r")
	lineList = fileObject.readlines()
	fileObject.close()

	wordDict = {}
	
	for tempStr in lineList:
		
		if tempStr.endswith("\n"):
			tempStr.rstrip("\n")
			tempWordList = tempStr.split()
			
		else:
			tempWordList = tempStr.split()
	
		for word in tempWordList:
			wordInfo = wordCleaner(word)
			cleanWord = wordInfo[0]
			vowelCt = wordInfo[1]
			
			if cleanWord in wordDict:
				wordInfoList = wordDict[cleanWord]
				wordCt = wordInfoList[0]
				wordCt += 1
				wordDict[cleanWord] = [wordCt,vowelCt]
				
			else:
				wordDict[cleanWord] = [1,vowelCt]
			
	return(wordDict)	


def wordCleaner(dirtyWord):
	vowels = ("a","e","i","o","u")
	cleanWord = ""
	vowelCt = 0
	
	for ch in dirtyWord:
		if ch.isalnum():
			cleanWord += ch.lower()
		if ch.lower() in vowels:
			vowelCt += 1
			
	wordInfo = [cleanWord, vowelCt]
	return(wordInfo)


def wordAlphabetizer(wordDict):
	sortedWordList = list(wordDict.keys())
	sortedWordList.sort()
	return(sortedWordList)


def visualPintout(wordsDict):
	sortedWords = wordAlphabetizer(wordsDict)
	
	print("####################################################################")
	print("{:^20s}{:}{:^20s}{:}{:^20s}".format("Word","|","Occurences","|","Number of Vowels"))
	print("####################################################################")
	
	for word in sortedWords:
		wordOccurence = (wordsDict[word])[0]
		wordVowels = (wordsDict[word])[1]
		
		print("{:^20s}{:}{:^20.0f}{:}{:^20.0f}".format(word,"|",wordOccurence,"|",wordVowels))
		
	
def main():
	
	fileFound = False
	keepLooping = True
	while keepLooping:
		nameOfFile = input("Please enter the name of the file with file extension, or done to quit: ")
		
		if os.path.isfile(nameOfFile):
			keepLooping = False
			fileFound = True
		
		elif nameOfFile.lower() == "done":
			print("\t-Exiting-")
			keepLooping = False
			
		else:
			print("\t-File Not Found, Try Again-\n")
			
	if fileFound:
		wordsInFile = findWords(nameOfFile)
		visualPintout(wordsInFile)


if __name__ == "__main__":
	main()


