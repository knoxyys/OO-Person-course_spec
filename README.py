class Person:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
    
    def printname(self):
        return self.fname, self.lname
    
class Student(Person):
    def __init__(self, fname, lname, student_id, house_group):
        self.student_id = student_id
        self.house_group = house_group
        self.subjects = []
        super().__init__(fname, lname)
    
    def enrol_class(self, subject_name):
        self.subjects.append(subject_name)
        subject_name.enrol_student(self.student_id)
    
    def show_classes(self):
        return self.subjects

class Subject:
    def __init__(self, subject_name):
        self.subject_name = subject_name
        self.students = [] # for the student ids
    
    def student_list(self):
        return self.students
    
    def enrol_student(self, student_id):
        self.students.append(student_id)

maths = Subject("Maths")
english = Subject("English")
software = Subject("Software Engineering")

lucas = Student("Lucas", "Smith", 12345, "Gryffindor")
lucas.enrol_class(maths)
lucas.enrol_class(english)
print(lucas.show_classes()) # this doesnt work yet, it only prints the memory address