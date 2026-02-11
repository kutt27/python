"""
Demonstrates that sets are mutable and maintain the same identity when modified.
"""

def demonstrate_set_mutability() -> None:
    # Example: User permissions in an authentication system
    user_permissions: set[str] = set()
    
    # old Set method
    # from typing import Set
    # user_permissions: Set[str] = set()
    
    print(f"Initial permissions: {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}")
    
    # Adding permissions (in-place modification)
    user_permissions.add("read")
    print(f"\nAfter adding 'read': {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}  <- SAME object!")
    
    user_permissions.add("write")
    print(f"After adding 'write': {user_permissions}")
    print(f"Memory ID: {id(user_permissions)}  <- Still SAME object!")

if __name__ == "__main__":
    demonstrate_set_mutability()
