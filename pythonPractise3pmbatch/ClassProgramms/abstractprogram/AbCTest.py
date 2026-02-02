#abstract class And Method Example
from abc import ABC,abstractmethod
#this class is abstract class
class Animal(ABC):
    #abstractmethod
    @abstractmethod
    def demo(self):#partially Implmentation
        print("By By")
    
    @abstractmethod
    def Calci(self,no1,no2):
        pass
    
    @abstractmethod
    def MyDetails(self,name,surname,age):
        pass

#non abstract class //instance method
class ShowAnimalMethod(Animal): #it is single level inheritance
    #overriding
    def demo(self):
        print("hello from demo method")
    
    def Calci(self, no1, no2):
        print(no1*no2)
    
    def MyDetails(self, name, surname, age):
        print("My name is:",name)
        print("Surname is:",surname)
        print("My age is:",age)


s1=ShowAnimalMethod()
s1.demo()
s1.Calci(30,10)
s1.MyDetails("Viren","More",25)



