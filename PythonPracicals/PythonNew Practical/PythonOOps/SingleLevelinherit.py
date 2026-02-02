#single level inheritance
#Parent class
class Parent:
    def AddTwoValues(self,no1,no2):
        self.num1=no1
        self.num2=no2
    
    def MinMax(self):
        #local varialble
        if self.num1>self.num2:
            return self.num1    
        else:
            return self.num2

class Child(Parent):#single level inheritance
    def GetInputUsingParentClass(self,no1,no2):
        self.AddTwoValues(no1,no2)
        print("Max value is:",self.MinMax())
    
    def CheckEvenOrodd(self):
        if self.num1%2==0 and self.num2%2==0:
            print("Both Are Even")
        elif self.num1 %2==0:
            print("Only Num1 is even",self.num1)
        elif self.num2 %2==0:
            print("only Num2 is even and num1 is odd",self.num2)
        else:
            print("Both Are Odd")
            
# p1=Parent()
# p1.AddTwoValues(30,50)
# print(p1.MinMax())
C1=Child() #object Created of child classs
C1.GetInputUsingParentClass(42,32)
C1.CheckEvenOrodd()
