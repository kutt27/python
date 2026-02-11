"""
Demonstrates frozenset - the immutable version of set.
"""

def demonstrate_frozenset() -> None:
    # frozensets can be used as dictionary keys because they are hashable
    ADMIN_PERMISSIONS = frozenset({"read", "write", "delete", "admin"})
    USER_PERMISSIONS = frozenset({"read", "write"})
    
    role_descriptions = {
        ADMIN_PERMISSIONS: "Full system access",
        USER_PERMISSIONS: "Standard user access"
    }
    
    print(f"Admin Permissions: {ADMIN_PERMISSIONS}")
    print(f"Role description for Admin: {role_descriptions[ADMIN_PERMISSIONS]}")
    
    # Attempting to modify raises AttributeError
    print("\nAttempting to modify frozenset...")
    try:
        ADMIN_PERMISSIONS.add("super_admin")  # type: ignore
    except AttributeError as e:
        print(f"Expected error: {e}")

if __name__ == "__main__":
    demonstrate_frozenset()
