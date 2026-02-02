'''
Encasulation
---------------------
1)in this features data wrap/bind/write into the single unit/container/entity
called as for data storing and performing logical opeatons upon that data.

1)class ->
1)class is a userdefined datatype which has data members and data function are create
for data members from storing class data and data function for performing logical operations on the
class data members class is a logical entity in that have only declaration and logical creation
2)in python class declared using class keyword

2)object is a instance of class for using object we can call data members and data function
of class into the outside of the class
----------------------------------------------------
'''
#class
class Employee:
    #Data method
    def MyEmployee(self,num1,num2,eid,ename,esalary,ejdate,edeaprtment):
        self.num1=num1
        self.num2=num2
        self.empid=eid
        self.empname=ename
        self.empsalary=esalary
        self.empjdate=ejdate
        self.empdepartment=edeaprtment

    def printEmpDetails(self):
        print("Employee ID:",self.empid)
        print("Employee Name:",self.empname)
        print("Employee Salary:",self.empsalary)
        print("Employee Joined Date:",self.empjdate)
        print("Employee Department:",self.empdepartment)

    def Printloop(self):
        for j in range(1,self.num1):
            print(j)
    def CalciCube(self):
        return  self.num2*self.num2*self.num2

emp=Employee() #object of Employee Class
num1=int(input("Enter First Num:"))
num2=int(input("Enter Second Num:"))
id=int(input("Enter Employee ID:"))
name=str(input("Enter Employee Name:"))
empsal=float(input("Enter Employee Salary:"))
empjdate=str(input("Enter Employee joining Date:"))
edepart=input("Enter Employee Department:")
emp.MyEmployee(num1,num2,id,name,empsal,empjdate,edepart)
emp.printEmpDetails()
print("---------------------------")
emp.Printloop()
print("---------------------------")
print("Cube is:",emp.CalciCube())
print("---------------------------")