import Syllabus as Syl

#examples of how to use the Syllabus class
classDays = ["tuesday","thursday"]
labDays = ["tuesday","thursday"]
class1 = Syl.Syllabus("CSCE315","506",classDays ,labDays ,"11:10 - 12:25","6:40 - 7:30","ZACH","rob.lightcsce315@tamu.edu","Wednesday 9 - 11 am Or by appointment.")
print(class1.getAll())


#Syl.Syllabus(a,b,c,d,e,f,g,h,i)
# a = course
# b = section
# c = classdays[]
# d = labdays[]
# e = classTimes
# f = labTimes
# g = location
# h = profEmail
# i = officeHours

#default constructor
class2 = Syl.Syllabus("None",section = None, classDays=None, labDays = None,classTimes=None, labTimes=None ,location = None, profEmail = None, officeHours = None)
class2.classDays.append("monday")
class2.classDays.append("tuesday")
print(class2.getAll())
# or
class3 = Syl.Syllabus(None,None,None,None,None,None,None,None,None)
print(class3.getAll())
