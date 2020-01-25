#Syllabus class
class Syllabus:

#All the variables defined with an empty string
    course = ""
    section = ""
    classDays = ""
    labDays = ""
    classTimes = ""
    labTimes = ""
    location = ""
    profEmail = ""
    officeHours = ""

#constructor
    def __init__(self):
        self.course = "HOWDY"
        self.section = ""
        self.classDays = ""
        self.labDays = ""
        self.classTimes = ""
        self.labTimes = ""
        self.location = ""
        self.profEmail = ""
        self.officeHours = ""

#getters
#getAll() will return everything the order above
    def getAll(self):
        return self.course, self.section, self.classDays, self.classTimes, self.labTimes, self.location, self.profEmail, self.officeHours

    def getCourse(self):
        return self.course

#setters
    def
