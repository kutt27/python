"""
Topic: Dataclass Basics.

The `@dataclass` decorator automatically generates common 
methods like `__init__`, `__repr__`, and `__eq__`.
"""

from dataclasses import dataclass

@dataclass
class User:
    id: int
    username: str
    email: str
    active: bool = True # Default value

if __name__ == "__main__":
    u = User(1, "alice", "alice@example.com")
    
    # Auto-generated repr:
    print(u)
    
    # Auto-generated equality check:
    u2 = User(1, "alice", "alice@example.com")
    print(f"Match: {u == u2}")
