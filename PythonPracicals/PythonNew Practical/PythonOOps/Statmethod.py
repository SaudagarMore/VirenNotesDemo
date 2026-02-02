class person:
    @staticmethod
    def insertdata(name,salary):
        person.name1=name  #local
        person.salary=salary #local
        
    @staticmethod
    def printmydetails():        
        print("From PErintDetais",person.name1," ",person.salary)
    
    def Instancemethod(self,roll):
        self.roll=roll
        print("From Instancemethod",person.name1," ",person.salary)

person.insertdata("abc",5000)
person.printmydetails()   

p1=person()
p1.Instancemethod(1023)
print(p1.roll)
print(person.name1) 
print(p1.name1)








