#Paul Kummer
#CSIS 153 Fall 2018
#Homework 2
#Due September 5

__author__ = "Paul Kummer"
__date__ = "8/29/2018"


#Problem 1: 
def calcAvg(listOfNums):
        runningTotal=0#invalid as sum

        if len(listOfNums) > 0:
                count=len(listOfNums)#use len of list and verify list isn't zero

                for num in listOfNums:
                        runninTotal+=num

                averageOfList= int(runningTotal)/int(count)

                print("The average of the List is: ",averageOfList)
        else:
                print("There is nothing in the list")

        
        
