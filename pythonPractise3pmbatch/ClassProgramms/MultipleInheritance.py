class Person:#parent 1
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def showpersonDetails(self):
        print("Person Name is:",self.name)
        print("Person Age is:",self.age)

class Employee: #parent 2
    def __init__(self,empid,department):
        self.empid=empid
        self.department=department
    
    def ShowEmp_details(self):
        print("Emp id :",self.empid)
        print("Emp Department is:",self.department)

#child class 1        
class Login(Person,Employee):#multiple inheritance logic
    def __init__(self, name, age,empid,department,logintime):
        Person.__init__(self,name,age)
        Employee.__init__(self,empid,department)
        self.logintime=logintime
    
    def Show_login_time(self):
        print("Employee Login Time is:",self.logintime)

#object Create Of Child class
login=Login("Viren More",26,1001,"IT","10AM")
login.showpersonDetails()
login.ShowEmp_details()
login.Show_login_time()        