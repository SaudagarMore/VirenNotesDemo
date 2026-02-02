#example of method overriding in polymorphism
#class Parent
class Parent:
    def Sample(self,no1,no2):
        self.no1 = no1
        self.no2 = no2
        print("This is Parent.Sample",self.no1*self.no2)

#class Child
class Child(Parent):
    def Sample(self,num1,num2):
        print("This is Child.Sample")
        super().Sample(num1,num2)

class Child2(Child):
    def Sample(self,num1,num2):
        print("This is Child2.Sample",num2-num1)
        super().Sample(num1,num2)

C1=Child2()
C1.Sample(30,20)
