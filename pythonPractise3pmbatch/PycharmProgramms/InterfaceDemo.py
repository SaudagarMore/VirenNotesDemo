# interface into the python Example
from abc import ABC, abstractmethod
class Shapedata(ABC):  # it created interface
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def CalculateArea(self):
        pass

class Reactangle(Shapedata):
    def __init__(self, height, breadth):
        self.height = height
        self.breadth = breadth

    def MyNewReactMethod(selfs):
        print("hello i am from Reactangle class")

    def area(self):
        print("Hello This is Area Method And Reactangle Calulated")

    def CalculateArea(self):
        print("Rectangle is:",self.height+self.breadth)

class Square(Shapedata):
    def __init__(self, height, breadth):
        self.height = height
        self.breadth = breadth

    def area(self):
        print("Square calulcate")

    def CalculateArea(self):
        print("Square is:",self.height*self.breadth)

R1=Reactangle(20,5)
R1.CalculateArea()
R1.area()
R1.MyNewReactMethod()
S1=Square(30,50)
S1.CalculateArea()
S1.area()