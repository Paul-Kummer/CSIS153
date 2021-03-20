#Paul Kummer
#CSIS 153
#Program 8

__author__="Paul Kummer"
__date__="11/12/18"

"""
Description:
This program creates two classes. The first class is a Vehicle, which is
the parent class of Car. Each class has a class level attribute that 
counts the number of objects created of that class type.

Vehicle Attributes, parent of Car:
Vin Number, Transportation Type, Year Built, Color

Car Attributes, child of Vehicle:
Vin Number, Transportation Type, Year Built, Color, Make
"""

#import date for determining age of vehicle
from datetime import date

class Vehicle:
	#keep count of vehicle objects created
	_numVehicles = 0
	
	def __init__ (self, tmpVIN=0, tmpTransportionType="None", tmpYear=0, tmpColor="None"):
		"""
		Pre-Condition:
		*tmpVIN and tmpYear must be an integer
		*tmpTransportationType and tmpColor must be a string
		
		Post-Condition:
		*Vehicle._numVehicles increased by one
		*user arguments assigned names for Vehicle instance
		
		Description:
		user defined arguments are assigned as attributes for the new object
		and the number of vehicles is increased
		"""
		
		Vehicle._numVehicles += 1
		self._vehicleCreated = Vehicle._numVehicles
		self._VIN = tmpVIN
		self._type = tmpTransportionType
		self._color = tmpColor
		self._year = tmpYear
		
	  
	def __str__ (self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		String with values of object attributes is created
		
		Description:
		Return a string listing object's attributes
		"""
		return \
"### Vehicle {:} ###\n\
VIN:  {:}\n\
Type:  {:}\n\
Year:  {:}\n\
Color:  {:}\n\
Age:  {:}\n"\
.format(self._vehicleCreated, self._VIN, self._type\
, self._year, self._color, self.calcVehicleAge())
		
	def calcVehicleAge(self):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*date must be imported and Vehicle year must be an integer
		
		Post-Condition:
		VehicleAge is assigned integer from current year minus year built
		
		Description:
		Returns the age of the vehicle based on current date
		"""
		
		today = date.today()
		vehicleAge = today.year-self._year
		return vehicleAge
		
	def getVIN(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		None
		
		Description:
		Returns vehicles VIN
		"""
		
		return self._VIN
		
	def getType(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		None
		
		Description:
		Returns vehicles type
		"""
		
		return self._type
		
	def getYear(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		None
		
		Description:
		Returns year vehicle was built
		"""
		
		return self._year
	
	def getColor(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		None
		
		Description:
		Returns the color of vehicle
		"""
		
		return self._color
		
	def getNumVehicles():
		"""
		Pre-Condition:
		None
		
		Post-Condition:
		None
		
		Description:
		Returns the number of vehicles
		"""
		
		return Vehicle._numVehicles
		
	def setVIN(self,newVIN):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*newVIN must be an integer
		
		Post-Condition:
		instance's VIN is assigned new integer value
		
		Description:
		VIN is changed for a vehicle
		"""
		
		self._VIN=newVIN
		
	def setType(self,newType):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*newType must be a string
		
		Post-Condition:
		instance's Type is assigned new string value
		
		Description:
		Type is changed for a vehicle
		"""
		
		self._type=newType
		
	def setYear(self,newYear):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*newYear must be an integer
		
		Post-Condition:
		instance's Year is assigned new integer value
		
		Description:
		Year built for a vehicle is changed
		"""
		
		self._year=newYear
	
	def setColor(self,newColor):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*newColor must be a string
		
		Post-Condition:
		instance's color is assigned new string value
		
		Description:
		Color of vehicle is changed
		"""
		
		self._color=newColor
		
		
		
class Car(Vehicle):
	#keep count of Hondas and Cars
	_numHondas = 0
	_numCars = 0
	
	def __init__ (self, tmpVIN=0, tmpTransportionType="None", tmpYear=0, tmpColor="None", tmpMake="None"):
		"""
		Pre-Condition:
		*tmpVIN and tmpYear must be an integer
		*tmpTransportationType, tmpColor, and tmpMake must be a string
		*Vehicle class must exist and handle tmpVIN, tmpTransportationType
			tmpYear, and tmpColor arguments
		
		Post-Condition:
		*Vehicle._numVehicles increased by one
		*user arguments assigned names for Vehicle instance
		*Car._numCars increased by one
		*Car._numHondas increased by one if make is honda
		
		Description:
		user defined arguments are assigned as attributes for the new object
		and the number of vehicles and cars is increased
		"""
		
		Car._numCars += 1
		self._make = tmpMake
		Vehicle.__init__(self, tmpVIN, tmpTransportionType, tmpYear, tmpColor)
		
		if self._make.upper() == "HONDA":
			Car._numHondas += 1
		   
	def __str__(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		String with values of object attributes is created
		
		Description:
		Return a string listing object's attributes
		"""
		
		return Vehicle.__str__(self)+"Make: {:}\n".format(self._make)
		
	def getMake(self):
		"""
		Pre-Condition:
		self must be an Object of Vehicle
		
		Post-Condition:
		None
		
		Description:
		Returns the make of Car
		"""
		
		return self._make
		
	def getNumCars():
		"""
		Pre-Condition:
		None
		
		Post-Condition:
		None
		
		Description:
		Returns the number of cars
		"""
		return Car._numCars
		
	def getNumHondas():
		"""
		Pre-Condition:
		None
		
		Post-Condition:
		None
		
		Description:
		Returns the number of Hondas
		"""
		
		return Car._numHondas
		
	def setMake(self,newMake):
		"""
		Pre-Condition:
		*self must be an Object of Vehicle
		*newMake must be a String
		
		Post-Condition:
		*An object of car has it's make changed to the string newMake
		*if Make is changed to Honda and wasn't previouse Honda the count
			of Hondas is increased by one. If make was Honda and changed
			to something different, Honda count decreases by one.
		
		Description:
		
		"""
		
		#changing make from Honda to Other
		if self.getMake().upper() == "HONDA" and newMake.upper() != "HONDA":
			Car._numHondas -= 1
		
		#changing make from Other to Honda	
		if self.getMake().upper() != "HONDA" and newMake.upper() == "HONDA":
			Car._numHondas += 1
			
		self._make = newMake
