"""
Python OOP: Magic/Dunder Methods
=================================

Topic: Special methods (__str__, __repr__, __eq__, __len__, etc.)

Real-World Applications:
- Custom string representations
- Operator overloading
- Container protocols
- Comparison operations
"""


class Product:
    """Product with magic methods."""
    
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.name} (${self.price:.2f})"
    
    def __repr__(self) -> str:
        """Developer-friendly representation."""
        return f"Product(name='{self.name}', price={self.price}, quantity={self.quantity})"
    
    def __eq__(self, other) -> bool:
        """Equality comparison."""
        if not isinstance(other, Product):
            return False
        return self.name == other.name and self.price == other.price
    
    def __lt__(self, other) -> bool:
        """Less than comparison (for sorting)."""
        return self.price < other.price
    
    def __add__(self, other):
        """Add operator overloading."""
        if isinstance(other, Product):
            return self.price + other.price
        return self.price + other


class ShoppingCart:
    """Shopping cart with container protocols."""
    
    def __init__(self):
        self.items = []
    
    def add(self, item: Product):
        """Add item to cart."""
        self.items.append(item)
    
    def __len__(self) -> int:
        """Support len() function."""
        return len(self.items)
    
    def __getitem__(self, index):
        """Support indexing cart[0]."""
        return self.items[index]
    
    def __contains__(self, item) -> bool:
        """Support 'in' operator."""
        return item in self.items
    
    def __iter__(self):
        """Support iteration."""
        return iter(self.items)


def main():
    """Demonstrates magic methods."""
    print("="*70)
    print("MAGIC/DUNDER METHODS".center(70))
    print("="*70)
    
    print("\n[1] STRING REPRESENTATIONS")
    print("-" * 70)
    
    product = Product("Laptop", 999.99, 5)
    
    print(f"str(product): {str(product)}")  # Calls __str__
    print(f"repr(product): {repr(product)}")  # Calls __repr__
    print(f"print: {product}")  # Uses __str__
    
    print("\n[2] COMPARISON OPERATORS")
    print("-" * 70)
    
    p1 = Product("Mouse", 29.99, 10)
    p2 = Product("Keyboard", 79.99, 5)
    p3 = Product("Mouse", 29.99, 8)
    
    print(f"p1 == p3: {p1 == p3}  (same name & price)")
    print(f"p1 < p2: {p1 < p2}  (price comparison)")
    
    # Sorting
    products = [p2, p1, Product("Monitor", 299.99, 3)]
    sorted_products = sorted(products)
    print(f"\nSorted by price: {[str(p) for p in sorted_products]}")
    
    print("\n[3] OPERATOR OVERLOADING")
    print("-" * 70)
    
    total = p1 + p2
    print(f"p1 + p2 = ${total:.2f}")
    
    print("\n[4] CONTAINER PROTOCOL")
    print("-" * 70)
    
    cart = ShoppingCart()
    cart.add(p1)
    cart.add(p2)
    
    print(f"Cart length: {len(cart)}")
    print(f"First item: {cart[0]}")
    print(f"p1 in cart: {p1 in cart}")
    
    print("\nIterating cart:")
    for item in cart:
        print(f"  - {item}")
    
    print("\n" + "="*70)
    print("Common Magic Methods:")
    print("-" * 70)
    print("String: __str__, __repr__")
    print("Comparison: __eq__, __ne__, __lt__, __gt__, __le__, __ge__")
    print("Arithmetic: __add__, __sub__, __mul__, __truediv__")
    print("Container: __len__, __getitem__, __setitem__, __contains__")
    print("Iteration: __iter__, __next__")
    print("Context: __enter__, __exit__")
    print("="*70)


if __name__ == "__main__":
    main()
