from  abc import  ABC,abstractmethod
#creating the interface
class Person(ABC):
    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def RolesofEntity(self):
        pass
#instance class
class Student(Person):
    def __init__(self,Sid,sname):
        self.sid = Sid
        self.sname = sname

    def info(self):
        print("Student id:",self.sid)
        print("Student name:",self.sname)

    def RolesofEntity(self):
        print("The Role Of Student Is Coming To College Regular:")
        print("---"*20)

class Teacher(Person):
    def __init__(self,Tid,tname):
        self.tid = Tid
        self.tname = tname

    def info(self):
        print("Teacher id:",self.tid)
        print("Teacher name:",self.tname)

    def RolesofEntity(self):
        print("Roles of Teacher is Teaching in class")
        print("---"*20)

class Book(Person):
    def __init__(self,Bid,Bname):
        self.Bid = Bid
        self.bname=Bname

    def info(self):
        print("Book id:",self.Bid)
        print("Book name:",self.bname)

    def RolesofEntity(self):
        print("Book Role is Maining the syllabus")
        print("---"*20)

class Parent(Person):
    def __init__(self,Pid,Pname):
        self.Pid = Pid
        self.Pname = Pname

    def info(self):
        print("Parent id:",self.Pid)
        print("Parent name:",self.Pname)

    def RolesofEntity(self):
        print("Present To School for parent meeting")
        print("---"*20)

def PrintAllDetails(Person:Person): #reference of interface
    Person.info()
    Person.RolesofEntity()

s1=Student(101,"Pravin")
t1=Teacher(102,"Prkash")
b1=Book(103,"JAva")
p1=Parent(104,"Ram")

PrintAllDetails(s1)
PrintAllDetails(t1)
PrintAllDetails(b1)
PrintAllDetails(p1)