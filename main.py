class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        return self.fname, self.lname

class Parent(Person):
    def __init__(self, fname, lname):
        self.occupation = None
        self.alumni = False
        super().__init__(fname, lname)
    
class Student(Person):
    def __init__(self, fname, lname, student_id, house_group):
        self.student_id = student_id
        self.house_group = house_group
        self.subjects = []
        super().__init__(fname, lname)
    
    def enrol_class(self, subject_name):
        self.subjects.append(subject_name)
        subject_name.enrol_student(self.student_id)
    
    def __str__(self):
        subject_names = [subject.subject_name for subject in self.subjects]
        return ', '.join(subject_names) # i cant lie i got the first line from chatgpt BUT i did know what to do


class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.students = [] # for the student ids
    
    def print_student_list(self):
        return print(self.students)
    
    def enrol_student(self, student_id):
        self.students.append(student_id)


# the main line is here

mathsext = Subject("Maths Extension 1")
mathsadv = Subject("Maths Advanced")
englishadv = Subject("English Advanced")
software = Subject("Software Engineering")
music = Subject("Music 1")
physics = Subject("Physics")
sor = Subject("Studies of Religion 1")

stirling = Student("Stirling", "Knox", "100125", "Broughton")
stirling.enrol_class(mathsext)
stirling.enrol_class(mathsadv)
stirling.enrol_class(englishadv)
stirling.enrol_class(software)
stirling.enrol_class(music)
stirling.enrol_class(physics)
stirling.enrol_class(sor)

print(stirling)
print(stirling.printname())
mathsext.print_student_list()