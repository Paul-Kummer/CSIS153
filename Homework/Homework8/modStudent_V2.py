class Person:
	_lastIDUsed = 0
	_totalPopulation = 0
	def __init__ (self,tmpLastName,tmpFirstName):
		self._personID = Person._lastIDUsed
		self._tmpLastName=tmpLastName
		self._tmpFirstName=tmpFirstName
		
		Person._lastIDUsed+=1
		Person._totalPopulation+=1
		
	def __str__ (self):
		return "Person ID: {0:<5.0f}\nName: {2:10s}{1:10s}".format(self._personID,\
self._tmpLastName,self._tmpFirstName)
		
	def getPersonID(self):
		return self._personID
			
	def getFirstName(self):
		return self._tmpFirstName
		
	def getLastName(self):
		return self._tmpLastName
		
	def getPopulation():
		return Person._totalPopulation
		
	def setFirstName(self,newName):
		self._tmpFirstName = newName
		
	def setLastName(self,newName):
		self._tmpLastName = newName

#inheritence: https://stackoverflow.com/questions/576169/understanding-
#python-super-with-init-methods
class Student(Person):
	_numStu = 0
	_lastIDUsed = 0
	def __init__ (self,tmpLastName,tmpFirstName,initGPA):
		#looked up on stackoverflow
		super().__init__(tmpLastName,tmpFirstName)
		
		self._gpa=initGPA
		self._studentID=Student._lastIDUsed
		Student._numStu+=1
		Student._lastIDUsed+=1
		
	def __str__ (self):
		return "{:<5.0f}{:10s}{:10s}{:<3.1f}".format(self._studentID,\
self._tmpLastName,self._tmpFirstName,self._gpa)

	def getStuCt():
		return Student._numStu
		
	def getStudentID(self):
		return self._studentID

	def getGPA(self):
		return self._GPA
		
	def setGPA(self,newGPA):
		self._gpa = newGPA

