"""
CSIS 153 In-Program 8 – Inheritance

    Create a class called Vehicle and store it in a file called modVehicle.py

    class Vehicle

    class-level attribute: numVehicles (initialize to 0)

    instance-level attributes:

    -VIN : integer

    - vehType: string #car, boat, motorcycle
    - yr: integer

    - color: string #red, silver, blue, green, brown, gray

    Constructor Method: -- provide the following vin, vehType, yr, color as parameters

    Class-level method: +getNumVehicles ( ):integer

    Instance-level methods:

    Getters for vin, vehType, yr, and color
    Setters for vin, vehType, yr, and color


    calcVehicleAge( ) #subtract yrMan from the current year & return that #

    __str__( ) #return a string where each attribute is labeled AND
    includes the vehicle age



    Create a class called Car which is a child of the Vehicle class.
    Store it in the modVehicle.py file.

    class Car(Vehicle)

    class-level attribute: numHondas: integer

    instance-level attribute: vehMake #a string like Ford, Subaru, Toyota, Honda, etc.

    Constructor method ( __init__ )

    Getter and setter for vehMake

    __str__ method – returns a string with labels & values for ALL of the attributes





    Create a test class that thoroughly tests EVERY method of each of the classes. Carefully label your output to illustrate what is being tested.
    """
from datetime import date

class Vehicle:
	_numVehicles = 0
	def __init__ (self, tmpVIN=0, tmpTransportionType="None", tmpYear=0, tmpColor="None"):
		Vehicle._numVehicles += 1
		self._VIN = tmpVIN
		self._type = tmpTransportionType
		self._color = tmpColor
		self._year = tmpYear
	  
	def __str__ (self):
		return \
"### Vehicle {:} ###\n\
VIN:  {:}\n\
Type:  {:}\n\
Year:  {:}\n\
Color:  {:}\n\
Age:  {:}\n"\
.format(Vehicle._numVehicles, self._VIN, self._type\
, self._year, self._color, self.calcVehicleAge())
		
	def calcVehicleAge(self):
		today = date.today()
		vehicleAge = today.year-self._year
		return vehicleAge
		
	def getVIN(self):
		return self._VIN
		
	def getType(self):
		return self._type
		
	def getYear(self):
		return self._year
	
	def getColor(self):
		return self._color
		
		
	def setVIN(self,newVIN):
		self._VIN=newVIN
		
	def setType(self,newType):
		self._type=newType
		
	def setYear(self,newYear):
		self._year=newYear
	
	def setColor(self,newColor):
		self._color=newColor
		
class Car(Vehicle):
	_numHondas = 0
	
	def __init__ (self, tmpVIN=0, tmpTransportionType="None", tmpYear=0, tmpColor="None", tmpMake="None"):
		self._make = tmpMake
		Vehicle.__init__(self, tmpVIN, tmpTransportionType, tmpYear, tmpColor)
		
		if self._make.upper() == "HONDA":
			Car._numHondas += 1
		   
	def __str__(self):
		return Vehicle.__str__(self)+"Make: {:}\n".format(self._make)
		
	def getMake(self):
		return self._make
		
	def setMake(self,newMake):
		self._make = newMake
    
t1=Vehicle(13412234,"Train",1994,"Grey")
print(t1)

t2=Car(13434321,"Automobile",1772,"Silver","Honda")
print(t2)

print("num of Hondas: ", Car._numHondas)
