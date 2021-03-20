#Attributes
"""
-instance-level: own unique place in memory
-class-level: 
"""

#class level
_iD = 0
class Student:
        def__init__(self,tmpName):
                #student self is instance level
                self._id = Student._iD
                
