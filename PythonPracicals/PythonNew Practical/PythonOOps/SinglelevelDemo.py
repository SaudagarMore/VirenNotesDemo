#class super
class Emp:    
    def AddIdSal(self,id,salary):
        self.empid=id
        self.empsal=salary  
    
    def ShowId(self):
        print("Emp id is:",self.empid)
        
#class Sub   
class Manager(Emp):
    def gEtidsalfromempadddeart(self,department):
        self.empdepartment=department
        
    def PrintEmpDetails(self):
        self.ShowId()
        print("Emp Salry is:",self.empsal)
        print("Emp Department is:",self.empdepartment)
    
m=Manager() #object Create
m.AddIdSal(1001,37500)
m.gEtidsalfromempadddeart('IT')
m.PrintEmpDetails()