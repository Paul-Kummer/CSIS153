#Paul Kummer
#CSIS 153
#Program 5
#Due:

__author__ = "Paul Kummer"
__date__ = "10-08-18"

#Program Description
"""
This program will test all the functionalities of the module called
"modHouse.py". the file must be in the working directory. It will make
sure that the class House will accept any number of arguments, and all
attributes of a class object should be able to be changed except the 
parcel number and profit. The method calcProfit will automatically assign
a value to "self_tmpProfit" based off of the appraisal value and selling
price. All attributes must be able to be accessed with getters.
"""

#Imports
from modHouse import House

#Globals



#main line of login
def main():
	h1 = House("18321",2014,"Bi-Level Condo",25300,6,965342.692,120343)
	h2 = House()
	print("House 1: \n",h1)
	print("House 2: \n",h2)
	
	print("Testing Getters for House 1: ")
	print("h1 Parcel #: ", h1.getParcelNum())
	print("h1 Year Built: ", h1.getYearBuilt())
	print("h1 House Type: ", h1.getHouseType())
	print("h1 Square Footage: ", h1.getSquareFootage())
	print("h1 Number of Rooms: ", h1.getNumberOfRooms())
	print("h1 Appraisal Value: ", h1.getAppraisalValue())
	print("h1 Selling Price: ", h1.getSellingPrice())
	print("h1 Amount of Profit: ", h1.getProfit())
	
	print("\nTesting Setters for House 2: ")
	print("h2 Parcel: No Set Method")
	print("h2 Year Built: Set to 2014");h2.setYearBuilt(2014)
	print("h2 House Type: Set to Modern Renassiance");h2.setHouseType("Modern Renassiance")
	print("h2 Square Footage: Set to 500");h2.setSquareFootage(500)
	print("h2 Number of Rooms: Set to 2");h2.setNumberOfRooms(2)
	print("h2 Appraisal Value: Set to $90,000");h2.setAppraisalValue(90000)
	print("h2 Selling Price: Set to $80,000");h2.setSellingPrice(80000)
	print("h2 Profit: No Set Method")
	
	print("\nNew Values for House 2: \n",h2)
	
	print("Testing Profit for House 2: ")
	print("h2 Profit: ${:<15,.2f}".format(h2.getProfit()))

	
if __name__ == "__main__":
	main()
