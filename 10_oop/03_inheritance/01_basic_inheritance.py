"""
Topic: Basic Inheritance.

Inheritance allows a class (child) to inherit attributes and methods 
from another class (parent), promoting code reuse.
"""

class Vehicle:
    """Parent Class"""
    def __init__(self, brand: str):
        self.brand = brand
        
    def start_engine(self):
        print(f"The {self.brand} engine is starting...")

class ElectricCar(Vehicle):
    """Child Class inheriting from Vehicle"""
    def charge_battery(self):
        print(f"The {self.brand} is now charging.")

if __name__ == "__main__":
    my_tesla = ElectricCar("Tesla")
    
    my_tesla.start_engine()  # Inherited method
    my_tesla.charge_battery() # Specific child method
    
    print(f"Is tesla a Vehicle? {isinstance(my_tesla, Vehicle)}")
