"""
Topic: Composition (HAS-A relationship).

Composition is a design principle where a class contains 
instances of other classes instead of inheriting from them. 
This is often more flexible than deep inheritance.
"""

class Engine:
    def start(self):
        print("Engine goes VROOM!")

class Tires:
    def rotate(self):
        print("Tires spinning...")

class Car:
    """A Car HAS-A Engine and HAS-A set of Tires."""
    def __init__(self):
        self.engine = Engine()
        self.tires = Tires()
        
    def drive(self):
        self.engine.start()
        self.tires.rotate()
        print("Car is moving.")

if __name__ == "__main__":
    my_car = Car()
    my_car.drive()
