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
			cleanWord = wordCleaner(word)
			
			if cleanWord in wordDict:
				wordCt = wordDict[cleanWord]
				wordDict[cleanWord] = wordCt + 1
				
			else:
				wordDict[cleanWord] = 1
			
	return(wordDict)	


def wordCleaner(dirtyWord):
	cleanWord = ""
	for ch in dirtyWord:
		if ch.isalnum():
			cleanWord += ch.lower()
	return(cleanWord)
	
	
def main():
	
	fileFound = False
	keepLooping = True
	while keepLooping:
		#nameOfFile = input("Please enter the name of the file with file extension, or done to quit: ")
		nameOfFile = "myPaper.txt"
		
		if os.path.isfile(nameOfFile):
			keepLooping = False
			fileFound = True
		
		elif nameOfFile.lower() == "done":
			print("\t-Exiting-")
			keepLooping = False
			
		else:
			print("\t-File Not Found, Try Again-\n")
			
	if fileFound:
		fileWords = findWords(nameOfFile)
		print(fileWords)
			
		
 
##def enterWords ():
##    myDict = {}
##    mySentence = input("Please enter sentence: ")
##    
##    while mySentence.lower() != "done":
##    
##        myWords = mySentence.split()
##
##        for word in myWords:
##            cleanWord = wordCleaner(word)
##            if cleanWord in myDict:
##                wordCt = myDict[cleanWord]
##                myDict[cleanWord] = wordCt + 1
##                print("Word Count", wordCt)
##            else:
##                myDict[cleanWord] = 1
##        mySentence = input("Please enter antoher sentence, or done: ")
##
##        
##    print(myDict)
##    
##enterWords()
if __name__ == "__main__":
	main()


