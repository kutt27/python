"""
Topic: `@classmethod` Decorator.

Class methods receive the CLASS (cls) instead of the instance (self). 
Commonly used for alternative constructors (factory methods).
"""

class User:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        
    @classmethod
    def from_string(cls, data_str):
        """Factory method to create a user from 'First-Last' string."""
        first, last = data_str.split("-")
        # 'cls' refers to the User class itself
        return cls(first, last)

if __name__ == "__main__":
    # Standard creation
    u1 = User("Alice", "Smith")
    
    # Creation via factory method
    u2 = User.from_string("Bob-Jones")
    
    print(f"User 1: {u1.first}")
    print(f"User 2: {u2.first}")
