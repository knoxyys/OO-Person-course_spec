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
    
    def showclasses(self):
        return [subject.subject_name for subject in self.subjects] # fix :)

class Teacher(Person):
    def __init__(self, fname, lname, subject_teach):
        self.subject_teach = subject_teach
        super().__init__(fname, lname)
    
    def get_info(self):
        return self.fname, self.lname, self.subject_teach

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.students = [] # for the student ids
    def print_student_list(self):
        return print(self.students)
    
    def enrol_student(self, student_id):
        self.students.append(student_id)
    
    def print_info(self):
        return print(f"Subject: {self.subject_name}, Students: {self.students}, Teacher: {self.subject_name.teacher.fname} {self.subject_name.teacher.lname}")



# the main line is here

mathsext = Subject("Maths Extension 1")
mathsadv = Subject("Maths Advanced")
englishadv = Subject("English Advanced")
software = Subject("Software Engineering")
music = Subject("Music 1")
physics = Subject("Physics")
sor = Subject("Studies of Religion 1")

mrstor = Teacher("Sarah", "Tor", "Software Engineering")
print(mrstor.get_info())

stirling = Student("Stirling", "Knox", "100125", "Broughton")
stirling.enrol_class(mathsext)
stirling.enrol_class(mathsadv)
stirling.enrol_class(englishadv)
stirling.enrol_class(software)
stirling.enrol_class(music)
stirling.enrol_class(physics)
stirling.enrol_class(sor)

print(stirling.showclasses())
print(stirling.printname())
mathsext.print_student_list()
software.print_student_list()
software.print_info()