from abc import ABC, abstractmethod

class Polygon(ABC):  # a child class of ABC

    def eat(self):  # a normal method for Polygon class
        print('You ate the polygon')

    @abstractmethod  # an abstract method for Polygon class
    def sides(self):
        pass


class Triangle(Polygon):  # a child class of Polygon

    def sides(self):  # implementation of an abstract class
        print('The triangle has 3 sides')



tri = Triangle()  # make a triangle object
tri.sides()  # use the the abstract class method 'sides'
tri.eat()  # use the parent class' normal method
