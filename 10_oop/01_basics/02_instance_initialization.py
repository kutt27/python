"""
Topic: Object Initialization with `__init__`.

The `__init__` method is called automatically when a new instance is created. 
It is used to set up the initial state of the object.
"""

class Product:
    def __init__(self, name: str, price: float, category: str = "General"):
        """Initialize product with basic info and validation."""
        if price < 0:
            raise ValueError("Price cannot be negative")
            
        self.name = name
        self.price = price
        self.category = category
        self.created_at = "2024-01-01" # Simulating a timestamp

    def __repr__(self):
        return f"Product(name='{self.name}', price={self.price})"

if __name__ == "__main__":
    p1 = Product("Laptop", 999.99, "Electronics")
    p2 = Product("Coffee Mug", 12.50) # Uses default category
    
    print(f"Product 1: {p1}")
    print(f"Product 2: {p2} (Category: {p2.category})")
    
    try:
        p_invalid = Product("Broken", -10)
    except ValueError as e:
        print(f"Caught expected error: {e}")
