"""
Demonstrates namedtuple for creating lightweight, immutable data structures with named fields.
"""

from collections import namedtuple

def demonstrate_namedtuple() -> None:
    User = namedtuple("User", ["id", "username", "role"])
    
    admin = User(id=1, username="admin", role="admin")
    print(f"User: {admin}")
    print(f"Name: {admin.username}, Role: {admin.role}")
    print(f"First element (index 0): {admin[0]}")
    
    # Immutable
    try:
        admin.role = "super"  # type: ignore
    except AttributeError as e:
        print(f"Expected error: {e}")

if __name__ == "__main__":
    demonstrate_namedtuple()
