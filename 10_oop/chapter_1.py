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



def demonstrate_instance_creation() -> None:
    """
    Demonstrates how to create and distinguish instances of a class.
    
    Real-world use case: Creating individual user objects.
    """
    user1 = User()
    user2 = User()
    
    print(f"user1: {user1}")
    print(f"user2: {user2}")
    print(f"Same object? {user1 is user2}")


def demonstrate_type_checking() -> None:
    """
    Demonstrates how to verify the type of an instance.
    
    Real-world use case: Type validation in API handlers.
    """
    user = User()
    print(f"type(user1): {type(user)}")
    print(f"isinstance(user1, User): {isinstance(user, User)}")


def demonstrate_class_attributes() -> None:
    """
    Demonstrates shared class-level attributes.
    
    Real-world use case: Shared configuration or constants.
    """
    req1 = APIRequest()
    req2 = APIRequest()
    
    print(f"req1.default_timeout: {req1.default_timeout}")
    print(f"req2.default_timeout: {req2.default_timeout}")
    
    # Shared attribute
    APIRequest.default_timeout = 60
    print(f"After changing class attribute:")
    print(f"req1.default_timeout: {req1.default_timeout}")
    print(f"req2.default_timeout: {req2.default_timeout}")


def demonstrate_instance_methods() -> None:
    """
    Demonstrates basic instance method calls.
    
    Real-world use case: Domain model behaviors.
    """
    product = Product()
    product.display_info()


def main() -> None:
    """Main function to run all demonstrations for simple classes."""
    print("="*70)
    print("PYTHON OOP: SIMPLE CLASSES".center(70))
    print("="*70)
    
    print("\n[1] CREATING INSTANCES")
    print("-" * 70)
    demonstrate_instance_creation()
    
    print("\n\n[2] TYPE CHECKING")
    print("-" * 70)
    demonstrate_type_checking()
    
    print("\n\n[3] CLASS ATTRIBUTES")
    print("-" * 70)
    demonstrate_class_attributes()
    
    print("\n\n[4] INSTANCE METHODS")
    print("-" * 70)
    demonstrate_instance_methods()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Classes define new types and blueprints for objects")
    print("2. Instances are unique objects created from a class")
    print("3. Class attributes are shared across all instances of that class")
    print("4. Instance methods allow objects to perform behaviors")
    print("5. use isinstance() to verify an object's type inheritance")
    print("="*70)


if __name__ == "__main__":
    main()