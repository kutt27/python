"""
Topic: Abstract Base Classes (ABC).

ABCs allow you to define a set of methods that MUST be implemented 
by any subclass, ensuring a consistent interface.
"""

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        """Every shape must implement this!"""
        pass

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side * self.side

if __name__ == "__main__":
    try:
        # Cannot instantiate the abstract base class directly
        s = Shape()
    except TypeError as e:
        print(f"Caught expected error: {e}")
        
    sq = Square(4)
    print(f"Square area: {sq.area()}")
