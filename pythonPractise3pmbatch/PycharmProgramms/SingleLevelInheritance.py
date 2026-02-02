'''
Inheritance ->
--------------------
1)single level inheritance (2)
i)base class/super class/parent class
ii)derived class/sub class/child class

2)multiple inheritance
3)multilevel inheritance
4)hierarchical inheritance
5)hybrid inheritance
'''
#single level inheritance Example.
#class Parent Declared
class A:
    def __init__(self,no1,no2):
        self.no1=no1 #50
        self.no2=no2 #20

    def Calci(self):
        print("Multiplication of two number is:",self.no1*self.no2) #1000
        print("Output from parent class Over")

class B(A):
    def Calci2(self):
        print("Substraction of two number is:",self.no1-self.no2) #30
        print("Output from parent class Over")

b1=B(50,30)
b1.Calci()
b1.Calci2()