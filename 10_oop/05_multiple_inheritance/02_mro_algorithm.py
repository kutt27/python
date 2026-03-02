"""
Topic: Method Resolution Order (MRO).

When using multiple inheritance, MRO defines the order in which 
Python searches for a method in the parent classes.
"""

class A:
    def greet(self):
        print("Hello from A")

class B(A):
    def greet(self):
        print("Hello from B")

class C(A):
    def greet(self):
        print("Hello from C")

class D(B, C):
    """Diamond Problem: Inheritance from B then C."""
    pass

if __name__ == "__main__":
    d = D()
    d.greet() # Which one is called?
    
    print("\nMethod Resolution Order (MRO):")
    # Python uses C3 Linearization to determine the order
    for cls in D.__mro__:
        print(f"  - {cls.__name__}")
