"""
Python OOP: Simple Classes
===========================

Topic: Basic class definition, creating instances, type checking

Real-World Applications:
- User account models
- API request/response objects
- Configuration classes
- Data models
"""

from typing import List


class User:
    """
    Simple user class.
    
    Real-world use case: User account model.
    """
    pass  # Empty class, just defines a type


class APIRequest:
    """
    API request model.
    
    Real-world use case: HTTP request representation.
    """
    # Class-level attribute (shared by all instances)
    default_timeout = 30


class Product:
    """Product model with attributes."""
    
    def display_info(self):
        """Display product information."""
        print(f"Product: {type(self).__name__}")


def main():
    """Demonstrates simple classes."""
    print("="*70)
    print("SIMPLE CLASSES".center(70))
    print("="*70)
    
    print("\n[1] CREATING INSTANCES")
    print("-" * 70)
    
    # Create user instances
    user1 = User()
    user2 = User()
    
    print(f"user1: {user1}")
    print(f"user2: {user2}")
    print(f"Same object? {user1 is user2}")
    
    print("\n[2] TYPE CHECKING")
    print("-" * 70)
    
    print(f"type(user1): {type(user1)}")
    print(f"isinstance(user1, User): {isinstance(user1, User)}")
    
    print("\n[3] CLASS ATTRIBUTES")
    print("-" * 70)
    
    req1 = APIRequest()
    req2 = APIRequest()
    
    print(f"req1.default_timeout: {req1.default_timeout}")
    print(f"req2.default_timeout: {req2.default_timeout}")
    
    # Shared attribute
    APIRequest.default_timeout = 60
    print(f"After changing class attribute:")
    print(f"req1.default_timeout: {req1.default_timeout}")
    print(f"req2.default_timeout: {req2.default_timeout}")
    
    print("\n[4] INSTANCE METHODS")
    print("-" * 70)
    
    product = Product()
    product.display_info()
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Classes define new types")
    print("• Instances are created by calling class: obj = ClassName()")
    print("• Class attributes are shared by all instances")
    print("• Instance methods take 'self' as first parameter")
    print("="*70)


if __name__ == "__main__":
    main()