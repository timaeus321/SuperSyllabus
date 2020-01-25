#Syllabus class
class Syllabus:

#All the variables defined with an empty string
    # course = ""
    # section = ""
    # classDays = ["monday","tuesday",etc]
    # labDays = ["monday","tuesday",etc]
    # classTimes = ""
    # labTimes = ""
    # location = ""
    # profEmail = ""
    # officeHours = ""

#constructor
    def __init__(self):
        self.course = ""
        self.section = ""
        self.classDays = []
        self.labDays = []
        self.classTimes = ""
        self.labTimes = ""
        self.location = ""
        self.profEmail = ""
        self.officeHours = ""

    def __init__(self, course, section, classDays, labDays, classTimes, labTimes, location, profEmail, officeHours):
        self.course = course
        self.section = section
        self.classDays = classDays
        self.labDays = labDays
        self.classTimes = classTimes
        self.labTimes = labTimes
        self.location = location
        self.profEmail = profEmail
        self.officeHours = officeHours

#Getter and Setters and not needed because all varibles are public
#=============================================================

#getters
#getAll will return everything the order above
    def getAll(self):
        return self.course, self.section, self.classDays, self.classTimes, self.labTimes, self.location, self.profEmail, self.officeHours

#setters
    def setAll(self, course, section, classDays, labDays, classTimes, labTimes, location, profEmail, officeHours):
        self.course = course
        self.section = section
        self.classDays = classDays
        self.labDays = labDays
        self.classTimes = classTimes
        self.labTimes = labTimes
        self.location = location
        self.profEmail = profEmail
        self.officeHours = officeHours
