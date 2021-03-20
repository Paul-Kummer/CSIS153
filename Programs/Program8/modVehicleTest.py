#Paul Kummer
#CSIS 153
#Program 8

__author__="Paul Kummer"
__date__="11/01/18"


from modVehicle import *
#Vehicle(self, tmpVIN=0, tmpTransportionType="None", tmpYear=0, tmpColor="None")

print("creating instances of Vehicle:\n")
v1=Vehicle()
v2=Vehicle(122342)
v3=Vehicle(324144,"Boat")
v4=Vehicle(523434,"Train",2014)
v5=Vehicle(909022,"Plane",2011,"Gold")
v6=Vehicle(902302,"Helicopter",1600,"Blue")

print("Vehicle One: \n",v1)
print("Vehicle Two: \n",v2)
print("Vehicle Three: \n",v3)
print("Vehicle Four: \n",v4)
print("Vehicle Five: \n",v5)
print("Vehicle Six: \n",v6)

print("testing setters:")
v1.setVIN(123423)
print("set V1's VIN to 123423: ")
v1.setType("Hot Air Balloon")
print("set V1's Type to Hot Air Balloon: ")
v1.setYear(2017)
print("set V1's Year to 2017: ")
v1.setColor("Clear")
print("set V1's Color to Clear: ")
print("\nupdated v1: \n",v1)

print("testing getters:")
print("v1's VIN: ",v1.getVIN())
print("v1's Type: ",v1.getType())
print("v1's Year: ",v1.getYear())
print("v1's Color: ",v1.getColor())
print("v1's Age: ",v1.calcVehicleAge())

print("\ncreating instance of Car:\n")
c1=Car(342342,"Car",2000,"Silver","Honda")

print("Car One:\n",c1)

print("testing car setter")
c1.setVIN(9999999)
print("set C1's VIN to 9999999: ")
c1.setType("Supercar")
print("set C1's Type to Supercar: ")
c1.setYear(1998)
print("set C1's Year to 1998: ")
c1.setColor("Green")
print("set C1's Color to Green: ")
c1.setMake("Mazda")
print("set C1's Make to Mazda: ")
print("\nupdated c1: \n",c1)

print("number of Hondas: ",Car.getNumHondas(),"\n")
print("set C1 to Honda")
c1.setMake("Honda")
print("number of Hondas: ",Car.getNumHondas(),"\n")
print("set C1 to Honda")
c1.setMake("Honda")
print("number of Hondas: ",Car.getNumHondas(),"\n")
c1.setMake("Mazda")
print("set C1 to Mazda: ")
print("number of Hondas: ",Car.getNumHondas(),"\n\n")



print("number of Cars: ",Car.getNumCars())
print("number of Vehicles: ",Vehicle.getNumVehicles())


