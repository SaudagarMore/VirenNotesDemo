#multiple inheritance
#parent 1
class Parent1:
    def hello(self,name):
        self.name=name

#parent 2
class Parent2:
    def getnum(self,no1,no2):
        self.no1=no1
        self.no2=no2

#parent 3
class Parent3:
    def GetCarDetails(self,carname,carengine,carspeed):
        self.carname=carname
        self.carengine=carengine
        self.carspeed=carspeed

#child 1
class Child(Parent1,Parent2,Parent3):
    def GetDetails(self):
        print("My Name is:",self.name)
            
    def CalculcateMultiply(self):
        result=self.no1*self.no2
        print("Result =",result)
    
    def CarDetails(self):
        print(self.carname," ",self.carengine," ",self.carspeed)
    
#object Create
C1=Child()
C1.hello("Viren")
C1.getnum(20,30)
C1.GetCarDetails("audi","500CC",150)
C1.GetDetails()
C1.CalculcateMultiply()
C1.CarDetails()  