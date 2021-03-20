#Paul Kummer
#CSIS 153
#House Module for Program 5

__author__ = "Paul Kummer"
__date__ = "10/08/18"

#Description
"""
This module allows the creation of a house object with attributes of 
parcel #, year built, house type, square ft, # of rooms, apprasial value,
selling price, and profit. parcel # and profit are not allowed to be set,
and profit is not allowed as an argument. All attributes are accessible 
with getters. Profit is calculated with it's own method and assigns
a value to the attribute profit. When a object of class house is called
a string displaying it's attributes with labels will be displayed.
"""


class House:
	
	#parcel:str, yearBuilt:int, houseType:str, sqFt:int, numRoom:int, 
	#appraise:float, sell:float
	
	#kwargs: https://stackoverflow.com/questions/18087030/how-do-we-get
	#-an-optional-class-attribute-in-python
	def __init__(self,tmpParcelNum = "NA",tmpYearBuilt = 0,tmpHouseType = "NA",\
	tmpSquareFootage = 0,tmpNumRooms = 0,tmpAppraisalValue = 0,tmpSellPrice = 0):
		
		self._tmpParcelNum = tmpParcelNum
		self._tmpYearBuilt = tmpYearBuilt
		self._tmpHouseType = tmpHouseType
		self._tmpSquareFootage = tmpSquareFootage
		self._tmpNumRooms = tmpNumRooms
		self._tmpAppraisalValue = tmpAppraisalValue
		self._tmpSellPrice = tmpSellPrice
		self._tmpProfit = self.calcProfit()
		
	def __str__(self):
		#I don't know why there is a space before parcel number
		tmpString =\
"{:20s}{:<15s}\n\
{:20s}{:<15,.0f}\n\
{:20s}{:<15s}\n\
{:20s}{:<15.0f}\n\
{:20s}{:<15.0f}\n\
{:20s}${:<15,.2f}\n\
{:20s}${:<15,.2f}\n".format(\
"Parcel Number: ",self._tmpParcelNum,\
"Year Built: ",self._tmpYearBuilt,\
"Year Built: ",self._tmpHouseType,\
"Square Footage: ",self._tmpSquareFootage,\
"Number of Rooms: ",self._tmpNumRooms,\
"Appraisal Value: ",self._tmpAppraisalValue,\
"Selling Price: ",self._tmpSellPrice)

		return tmpString
		
	def getParcelNum (self):
		return self._tmpParcelNum
		
	def getYearBuilt (self):
		return  self._tmpYearBuilt
		
	def setYearBuilt (self,newYear):
		self._tmpYearBuilt = newYear
		
	def getHouseType (self):
		return self._tmpHouseType
		
	def setHouseType (self,newType):
		self._tmpHouseType = newType
			
	def getSquareFootage (self):
		return self._tmpSquareFootage
		
	def setSquareFootage (self,newFootage):
		self._tmpSquareFootage = newFootage
		
	def getNumberOfRooms (self):
		return self._tmpNumRooms
		
	def setNumberOfRooms (self,newRoomNum):
		self._tmpNumRooms = newRoomNum
		
	def getAppraisalValue (self):
		return self._tmpAppraisalValue
		
	def setAppraisalValue (self,newAppraisal):
		self._tmpAppraisalValue = newAppraisal
		self.calcProfit()
		
	def getSellingPrice (self):
		return self._tmpSellPrice
		
	def setSellingPrice (self,newPrice):
		self._tmpSellPrice = newPrice
		self.calcProfit()
		
	def getProfit (self):
		return self._tmpProfit
		
	def calcProfit (self):
		self._tmpProfit = self._tmpSellPrice - self._tmpAppraisalValue

		
