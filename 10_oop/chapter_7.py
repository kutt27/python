"""
Python OOP: Base Classes and Inheritance
=========================================

Topic: Parent/child classes, super(), method overriding

Real-World Applications:
- Framework design
- Polymorphism
- Code reuse
"""


class Vehicle:
    """Base vehicle class."""
    
    def __init__(self, make: str, model: str, year: int):
        self.make = make
        self.model = model
        self.year = year
    
    def start(self):
        """Start the vehicle."""
        print(f"Starting {self.make} {self.model}...")
    
    def get_description(self) -> str:
        """Get vehicle description."""
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Vehicle):
    """Electric car subclass."""
    
    def __init__(self, make: str, model: str, year: int, battery_capacity: int):
        super().__init__(make, model, year)  # Call parent __init__
        self.battery_capacity = battery_capacity
    
    def start(self):
        """Override start method."""
        print("Silently powering on...")
        super().start()  # Call parent method too
    
    def charge(self):
        """Electric-specific method."""
        print(f"Charging {self.battery_capacity}kWh battery...")


def main():
    """Demonstrates inheritance."""
    print("="*70)
    print("BASE CLASSES & INHERITANCE".center(70))
    print("="*70)
    
    print("\n[1] PARENT CLASS")
    print("-" * 70)
    
    vehicle = Vehicle("Toyota", "Camry", 2020)
    print(vehicle.get_description())
    vehicle.start()
    
    print("\n[2] CHILD CLASS")
    print("-" * 70)
    
    tesla = ElectricCar("Tesla", "Model 3", 2023, 75)
    print(tesla.get_description())  # Inherited method
    tesla.start()  # Overridden method
    tesla.charge()  # New method
    
    print("\n[3] INHERITANCE HIERARCHY")
    print("-" * 70)
    
    print(f"isinstance(tesla, ElectricCar): {isinstance(tesla, ElectricCar)}")
    print(f"isinstance(tesla, Vehicle): {isinstance(tesla, Vehicle)}")
    print(f"issubclass(ElectricCar, Vehicle): {issubclass(ElectricCar, Vehicle)}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Subclasses inherit parent attributes/methods")
    print("• super() calls parent class methods")
    print("• Can override parent methods")
    print("• Can add new methods/attributes")
    print("="*70)


if __name__ == "__main__":
    main()