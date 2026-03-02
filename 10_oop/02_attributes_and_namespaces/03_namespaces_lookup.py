"""
Topic: Namespace Lookup Order.

Python searches for attributes in this order:
1. The Instance's own `__dict__`
2. The Class's `__dict__`
3. Parent classes (if any)
"""

class Base:
    shared = "base"

class Child(Base):
    pass

if __name__ == "__main__":
    obj = Child()
    obj.local = "i am local"
    
    print(f"1. Instance lookup (local): {obj.local}")
    print(f"2. Parent lookup (shared): {obj.shared}")
    
    # Peek into the namespaces
    print(f"\nInstance namespace: {obj.__dict__}")
    print(f"Child class namespace keys: {list(Child.__dict__.keys())}")
    print(f"Base class namespace keys: {list(Base.__dict__.keys())}")
