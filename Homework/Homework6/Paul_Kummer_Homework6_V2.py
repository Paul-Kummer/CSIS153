#Paul Kummer
#CSIS 153 Fall 2018
#Homework 6
#Due: 

__author__ = "Paul Kummer"
__date__ = "09/20/2018"


#Assignment
"""
Homework 6 CSIS 153 Dictionaries part 2 

Create an empty dictionary called
vehicleRoster
It will map vehicle identification numbers (VINs)  to a list containing make, 
year, and manufacturer’s retail price (MSRP)  like this:
{  vin: [make, year, MSRP],  id:[make,year, MSRP] , etc.}

Step 2:  Adding information to 
the dictionary:
vehicleRoster[“B200”] = [“Ford”, 2016, 14000]
vehicleRoster [“A100”] = [“Mazda”, 2010, 7000]
vehicleRoster [“D400”] = [“Nissan”, 2018, 24000]
vehicleRoster [“B999”] = [“Ford”, 2015, 12000]

Step 3: Print the dictionary
print(vehicleRoster)

Step 4:  Print the following 
information
- vin and make
-number of vehicles less than 4 years old
- average MSRP of the vehicles

Step 5: 
Ask the user to enter a make and print all of the information for vehicles of 
that make

Step 6:
Ask the user to enter a year and print all of the information for vehicles that
are that year or newer
"""


#import module allowing the program to fetch the current year
import datetime
year = datetime.datetime.now().year


#1.
vehicleRoster = {}

#2.
vehicleRoster["B200"] = ["Ford", 2016, 14000]
vehicleRoster ["A100"] = ["Mazda", 2010, 7000]
vehicleRoster ["D400"] = ["Nissan", 2018, 24000]
vehicleRoster ["B999"] = ["Ford", 2015, 12000]

#3.
print(vehicleRoster)

#4.

#accumulators for total vehicle cost and how many vehicles under 4yrs old
totMSRP = 0
newerVehicle = 0

#start creation of table for visual output
print("\n{:20s}\t{:20s}".format("Vin","Make"))
print("-----------------------------------------")

#iterate through keys in vehicleRoster dictionary
for currentKey in vehicleRoster:
	
	#assign values to every piece of information retrieved based on key and value index locations
	vehicleInfo = vehicleRoster[currentKey]
	vehicleVin = currentKey
	vehicleMake = vehicleInfo[0]
	vehicleYear = vehicleInfo[1]
	vehicleMSRP = vehicleInfo[2]
	
	#add item to table
	print("{:20s}\t{:20s}".format(vehicleVin,vehicleMake))
	
	#add to newerVehicle accumulator if the vehicle is less than 4yrs old from the current year
	if year-vehicleYear < 4:
		newerVehicle += 1
	
	#add to the accumulator of the combined MSRP of all vehicles	
	totMSRP += vehicleMSRP

#output to user the quantity of vehicles less than 4yrs old	
print("Vehicles Less Than Four Years Old: {}\n".format(newerVehicle))

#check lenght of dictionary to prevent divide by zero error
#if lenght of dictionary is greater than zero then average MSRP is calcualated
if len(vehicleRoster) > 0:
	print("Average Vehicle MSRP: ${:n}\n\n".format(totMSRP/len(vehicleRoster)))

else:
	print("No Average Vehicle MSRP. No Vehicles In Array")
	
#5.
selectedMake = input("Please enter the make of vehicles you would like information for: ")

#create two sentinels that can escape loop when either a make is found or nothing was found
#if a make is found the loop exists early and begins creating a table
#if no make is found the table doesn't initialize and the user is told there is no make
makeNotExists = True
stayInLoop = True

#checks for at least one make entry in vehicleRoster equal to user inputed make
while makeNotExists and stayInLoop:
	for currentKey in vehicleRoster:
		vehicleInfo = vehicleRoster[currentKey]
		vehicleMake = vehicleInfo[0]
		
		if vehicleMake == selectedMake:
			makeNotExists = False
	
	stayInLoop=False

#if a make exists in vehicleRoster a table is initialized	
if makeNotExists != True:
	print("\t-For the {} make there is the following information-\n".format(selectedMake))
	print("{:20s}\t{:20s}\t{:20s}".format("Vin #","Year","MSRP"))
	print("--------------------------------------------------------------------")
	
	#every make in vehicleRoster that matches user inputted make has all its information added to a table
	for currentKey in vehicleRoster:
		vehicleInfo = vehicleRoster[currentKey]
		vehicleVin = currentKey
		vehicleMake = vehicleInfo[0]
		vehicleYear = vehicleInfo[1]
		vehicleMSRP = vehicleInfo[2]
		
		if vehicleMake == selectedMake:
			
			#information on .format alignment from 
			#https://www.digitalocean.com/community/tutorials/how-to-use-string-formatters-in-python-3
			#"<"=left justify, ">"=right justify, "^"=center justify, ".0f"=float zero decimal
			print("{:20s}\t{:<20.0f}\t${:<20.0f}".format(vehicleVin,vehicleYear,vehicleMSRP))
		
else:
	print("\t-For the {} make there is no information-".format(selectedMake))

		
#6.
#Enter validation loop for error checking of user input
notValidEntry = True

#Ensure the user inputs a valid integer
while notValidEntry:
	selectedYear = input("\nPlease enter the  minimum year of vehicles you would like information for: ")
	
	#if user inputted year is an integer, the loop is exited by making notValidEntry False
	if selectedYear.isdigit():
		selectedYear = int(selectedYear)
		notValidEntry = False
	else:
		print("\t-Invalid Entry: Please enter only an integer-\n")

#create two sentinels that can escape loop when either a year or greater is found or nothing was found
#if a year or greater is found the loop exists early and begins creating a table
#if no year or greater is found the table doesn't initialize and the user is told there are no vehicles		
yearNotExists = True
stayInLoop = True

#checks for at least one year entry in vehicleRoster equal to or greater than the user inputed year
while yearNotExists and stayInLoop:
	for currentKey in vehicleRoster:
		vehicleInfo = vehicleRoster[currentKey]
		vehicleYear = vehicleInfo[1]
		
		if vehicleYear >= selectedYear:
			yearNotExists = False
	
	stayInLoop=False

#if a vehicle with a year greater than or equal to user inputted year exists in vehicleRoster a table is initialized	
if yearNotExists != True:
	print("\t-For the {} year or newer there is the following information-\n".format(selectedYear))
	print("{:20s}\t{:20s}\t{:20s}\t{:20s}".format("Vin #","Make","Year","MSRP"))
	print("------------------------------------------------------------------------------------")
	
	#every year in vehicleRoster that equals or is greater than the user inputted year has all its information added to a table
	for currentKey in vehicleRoster:
		vehicleInfo = vehicleRoster[currentKey]
		vehicleVin = currentKey
		vehicleMake = vehicleInfo[0]
		vehicleYear = vehicleInfo[1]
		vehicleMSRP = vehicleInfo[2]
		
		if vehicleYear >= selectedYear:
			print("{:20s}\t{:20s}\t{:<20.0f}\t${:<20.0f}".format(vehicleVin,vehicleMake,vehicleYear,vehicleMSRP))
		
else:
	print("\t-For the {} year or newer there is no information-".format(selectedYear))
	
	
#Code Output
"""
{'B999': ['Ford', 2015, 12000], 'A100': ['Mazda', 2010, 7000], 'D400': ['Nissan', 2018, 24000], 'B200': ['Ford', 2016, 14000]}

Vin                 	Make                
-----------------------------------------
B999                	Ford                
A100                	Mazda               
D400                	Nissan              
B200                	Ford                
Vehicles Less Than Four Years Old: 3

Average Vehicle MSRP: $14250


Please enter the make of vehicles you would like information for: Ford
	-For the Ford make there is the following information-

Vin #               	Year                	MSRP                
--------------------------------------------------------------------
B999                	2015                	$12000               
B200                	2016                	$14000               

Please enter the  minimum year of vehicles you would like information for: 2002
	-For the 2002 year or newer there is the following information-

Vin #               	Make                	Year                	MSRP                
------------------------------------------------------------------------------------
B999                	Ford                	2015                	$12000               
A100                	Mazda               	2010                	$7000                
D400                	Nissan              	2018                	$24000               
B200                	Ford                	2016                	$14000    
"""
