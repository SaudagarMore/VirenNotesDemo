#interface into the python Example
from abc import ABC,abstractmethod

class Shapedata(ABC):#it created interface
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def CalculateArea(self,height,breadth):
        pass

class Reactangle(Shapedata):
    def __init__(self,height,breadth):
        self.height=height
        self.breadth=breadth
    
    
    
class Square(Shapedata):
    def __init__(self,height,breadth):
        self.height=height
        self.breadth=breadth
    