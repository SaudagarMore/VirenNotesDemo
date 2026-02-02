from  abc import ABC, abstractmethod

class Abstractclass(ABC):
    @abstractmethod
    def s1(self):
        pass

class AbstractClass1(Abstractclass):
    @abstractmethod
    def s2(self,no1,no2):
        pass

class Student(AbstractClass1):
    def s2(self, no1, no2):
        print(no1+no2)

    #abstract method
    def s1(self):
        print("This is first use")

class Details(AbstractClass1):
    def s1(self):
        print("Second use")


class MainClass(Abstractclass):
    def s1(self):
        print("This uses Abstract method")


Main=MainClass()
Main.s1()
Dt=Details()
Dt.s1()
S1=Student()
S1.s1()
S1.s2(20,40)
