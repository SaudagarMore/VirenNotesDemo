class Person:#parent class
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def ShowPersonDetails(self):
        print("Preson name is:",self.name)
        print("Person age is:",self.age)
        
class Student(Person):# it is Single level inheritance
    def __init__(self, name, age,roll):
        Person.__init__(self,name, age)
        self.roll=roll
    
    def ShowStudentRoll(self):
        self.ShowPersonDetails()
        print("Student Roll no is:",self.roll)

class Teacher(Person):
    def __init__(self, name, age,subject):
        Person.__init__(self,name, age)
        self.subject=subject
    
    def ShowTeacher(self):
        self.ShowPersonDetails()
        print("Suject is:",self.subject)
    
class RoleMixin:
    def duty(self):
        print("Maintain disiplin in the class")

class Monitor(RoleMixin,Student):#multiple inheritance example
    def __init__(self, name, age, roll):
        Student.__init__(self,name, age, roll)
    
    def show_monitor(self):
        self.ShowStudentRoll()
        self.duty()


print(" Students details printed---------------------")
M=Monitor("Rohit",15,23)
M.show_monitor()
print(" teacher details printed---------------------")
T1=Teacher("Rohan",35,"Python")
T1.ShowTeacher()        