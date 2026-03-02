"""
Topic: Basic Class Definition.

A class is a blueprint for creating objects. It defines a new type with 
its own attributes and methods.
"""

class UserAccount:
    """Simple class representing a user profile."""
    pass

if __name__ == "__main__":
    # Create instances (objects) of the class
    user1 = UserAccount()
    user2 = UserAccount()
    
    print(f"user1: {user1}")
    print(f"user2: {user2}")
    
    # Each instance is a unique object in memory
    print(f"Same object? {user1 is user2}")
    
    # Type checking
    print(f"Is user1 a UserAccount? {isinstance(user1, UserAccount)}")
