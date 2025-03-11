from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
class Square(Rectangle):
    
    def __init__(self,side):
        super().__init__(side,side)
        self.__side = side

    @property
    def side(self):
        return self.__side
    
class Ellipse:

    def __init__(self, perimeter):
        self.perimeter = perimeter

    @property
    def perimeter(self):
        raise NotImplementedError()
    

class Circle(Ellipse):

    def __init__(self,radius):
        self.__radius =radius

    @property
    def radius(self):
        return self.__radius  

