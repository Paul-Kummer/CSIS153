#Paul Kummer
__author__ = "Paul Kummer"
__date__ = "10-1-18"


def displayProf:

def

main


























#student id to student info (major,phone numbers)
myDict = {"22":["CSIC",["222-2222","333-3333","555-5555"]],"1":["Physics",["432-2232","773-3733","205-5995"]]}

#stuID = input("enter student id: ")


majorList = []

for key in myDict:
    stuInfo = myDict[key]
    stuMajor = stuInfo[0]
    stuPhones = stuInfo[1]
    stuWkPhone = stuPhones[0]
    stuHmPhone =stuPhones[1]
    stuEmerPhone =stuPhones[2]

    majorList.append(stuMajor)

majorList.sort()
print(majorList)


    
