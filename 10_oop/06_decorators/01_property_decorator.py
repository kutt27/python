"""
Topic: `@property` Decorator.

The `@property` decorator allows a method to be accessed as if 
it were an attribute, useful for computed values or encapsulation.
"""

class Circle:
    def __init__(self, radius: float):
        self._radius = radius # Leading underscore suggests 'internal'
        
    @property
    def radius(self):
        """Getter for radius."""
        return self._radius
        
    @radius.setter
    def radius(self, value):
        """Setter with validation."""
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value
        
    @property
    def area(self):
        """Computed property."""
        import math
        return math.pi * (self._radius ** 2)

if __name__ == "__main__":
    c = Circle(5)
    print(f"Radius: {c.radius}")
    print(f"Area:   {c.area:.2f}")
    
    # Use the setter
    c.radius = 10
    print(f"New Area: {c.area:.2f}")
