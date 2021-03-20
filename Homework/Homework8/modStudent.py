class Student:
	_numStu = 0
	_lastIDUsed = 0
	def __init__(self,initLastName,initFirstName,initGPA):
		self._id =Student._lastIDUsed
		Student._numStu+=1
		Student._lastIDUsed+=1
		self._lastName=initLastName
		self._firstName=initFirstName
		self._gpa=initGPA
		
	def __str__(self):
		return "{:<5.0f}{:10s}{:10s}{:<3.1f}".format(self._id,\
self._lastName,self._firstName,self._gpa)

	def getStuCt():
		return Student._numStu
		
	def getID(self):
		return self._id
		
	def getLastName(self):
		return self._lastName
		
	def getFirstName(self):
		return self._firstName
		
	def getGPA(self):
		return self._GPA
		
	def setLastName(self,newName):
		self._lastName = newName
		
	def setFirstName(self,newName):
		self._firstName = newName
		
	def setGPA(self,newGPA):
		self._gpa = newGPA

