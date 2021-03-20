#Paul Kummer
#CSIS 153
#Program3

__author__="Paul Kummer"
__date__="9/26/18"

#Program description
"""
This program will ask for the user to enter a name of a text file in the directory of the program. If the file exists,
the program will count the number of occurences of each word, the number of vowels in each word, covert all uppercase characters
to lowercase characters, remove all punctuation, and printout a visual table of all the information for each word.
"""

#allows the program to find the current directory
import os.path

#go through a verified file name and find all word-like items then return a dictionary with words as keys and values of lists containing frequency of word-like items and number of vowels
def findWords(fileName):
	
	#create a file-object that will be opened in read only mode
	fileObject = open(fileName,"r")
	
	#create a list of every line in the file-object, which is denoted by \n
	lineList = fileObject.readlines()
	
	#close the file after the lines have been read
	fileObject.close()
	
	#create and empty dictionary that will be populated with words as keys and values of a list with number of occurence and vowel count
	wordDict = {}
	
	#iterate through every line in the list of lines, which are long strings
	for tempStr in lineList:
		
		#checks if the line was the last line in the file. If it is not the last line it will remove "\n" from the end of the string
		#also, the string is seperated into individual words based on a space between words
		#this check could also be accomplished by checking the index position against the length of the list
		if tempStr.endswith("\n"):
			tempStr.rstrip("\n")
			tempWordList = tempStr.split()
		
			
		else:
			tempWordList = tempStr.split()
		
		#iterated through the word list in the current line being evaluated
		for word in tempWordList:
			
			#send the current word being evaluated to the wordCleaner function to remove punctuation and case as well as count vowels
			wordInfo = wordCleaner(word)
			
			#assign more meaningful names to information pertaining to each word
			cleanWord = wordInfo[0]
			vowelCt = wordInfo[1]
			
			#check the word dictionary if the word already exists. if it does not exist, it is added to the dictionary with a list of occurence of one and the number of vowels.
			#If the word is already in the dictionary, the number of occurences is increased by one in the list assigned to the keys value.
			if cleanWord in wordDict:
				wordInfoList = wordDict[cleanWord]
				
				#assign meaningful name to index 0 of the value list
				wordCt = wordInfoList[0]
				
				#increase word occurence by one
				wordCt += 1
				
				#create a new list as a value of the word with updated information
				wordDict[cleanWord] = [wordCt,vowelCt]
				
			else:
				#create a list for the value for the new word
				wordDict[cleanWord] = [1,vowelCt]
	
	#send the word dictionary to whatever called the function		
	return(wordDict)	

#from a string remove all punctuation, make characters lowercase, and count the number of values then return a list of the formated word and vowel count
def wordCleaner(dirtyWord):
	
	#create a tuple of definate vowels excluding the possible "y"
	vowels = ("a","e","i","o","u")
	
	#the word that will be created as its formated character by character
	cleanWord = ""
	
	#accumulator for number of vowels
	vowelCt = 0
	
	#iterate through characters in word to be formated
	for ch in dirtyWord:
		
		#check if the character is a number or letter
		if ch.isalnum():
			
			#concatenate the string cleanWord with the lowercase character being evaluated
			cleanWord += ch.lower()
			
		#check if the current character is a vowel and add to the accumulator
		if ch.lower() in vowels:
			vowelCt += 1
	
	#create a list of word information containing the formated word and the number of vowels
	wordInfo = [cleanWord, vowelCt]
	
	#return the word information as a list
	return(wordInfo)

#make an alphabetized list of keys from a dictionary and return that sorted word list
def wordAlphabetizer(wordDict):
	
	#create a list of keys in the word dictionary
	sortedWordList = list(wordDict.keys())
	
	#alphabetize the list from a to z
	sortedWordList.sort()
	
	#return the alphabetized list
	return(sortedWordList)

#from a dictionary, make a table of words in a file, number occurences of word, and how many vowels in each word
def visualPrintout(wordsDict):
	
	#send the word dictionary to the wordAlphabetizer function to get an alphabetized list of keys
	sortedWords = wordAlphabetizer(wordsDict)
	
	#print a header for the table 
	print("####################################################################")
	print("{:^20s}{:}{:^20s}{:}{:^20s}".format("Word","|","Occurences","|","Number of Vowels"))
	print("####################################################################")
	
	#iterate through the words in the alphabetized list
	for word in sortedWords:
		
		#assign meaningful names to values from the word dictionary for each word
		wordOccurence = (wordsDict[word])[0]
		wordVowels = (wordsDict[word])[1]
		
		#print each word, frequency, and vowels in alphabetical order and centered with 20 character padding for each column seperated by "|"
		print("{:^20s}{:}{:^20.0f}{:}{:^20.0f}".format(word,"|",wordOccurence,"|",wordVowels))
		
#main line of logic	
def main():
	
	#flag to trigger if the file is found
	fileFound = False
	
	#sentinel to exit loop when false
	keepLooping = True
	
	#loop that continues until a correct file name is entered or the user enters done
	while keepLooping:
		
		#ask user to input the name of a file with it's extension
		nameOfFile = input("Please enter the name of the file with file extension, or done to quit: ")
		
		#check if the user entered file is in the current directory
		if os.path.isfile(nameOfFile):
			
			#exit the loop
			keepLooping = False
			
			#indicate that file was found
			fileFound = True
		
		#exit the loop if user enters any form of "done"
		elif nameOfFile.lower() == "done":
			print("\t-Exiting-")
			keepLooping = False
		
		#if the file name does not exists or the user does not enter done, prompt user to re-enter input
		else:
			print("\t-File Not Found, Try Again-\n")
	
	#if the file does exist and the user didn't type done pass the name of the file to the function wordsInFile then make a table to view	
	if fileFound:
		
		#pass the string of the file name to the function wordsInFile to have dictionary returned with keys that are lowercase without punctuation and values that are lists with frequency and vowels
		wordsInFile = findWords(nameOfFile)
		
		#pass the word dictionary into the function visualPrintout to have a visual table created with all the word information from the file
		visualPrintout(wordsInFile)

#check if the program was imported, and execute the main function if it was not
if __name__ == "__main__":
	main()
	
#Output of myPaper.txt
"""
Please enter the name of the file with file extension, or done to quit: myPaper.txt
####################################################################
        Word        |     Occurences     |  Number of Vowels  
####################################################################
         a          |         33         |         1          
       about        |         3          |         3          
       after        |         1          |         2          
        all         |         15         |         1          
       always       |         1          |         2          
        and         |         69         |         1          
      another       |         2          |         3          
        any         |         1          |         1          
        are         |         5          |         2          
         as         |         9          |         1          
       asked        |         1          |         2          
         at         |         14         |         1          
        away        |         6          |         2          
        back        |         2          |         1          
        bad         |         2          |         1          
        ball        |         5          |         1          
         be         |         7          |         1          
        bed         |         1          |         1          
etc...
"""


