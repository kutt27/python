"""
Access Control logic.
"""

def check_access_permission(user_role: str, resource: str) -> bool:
    """
    Checks if user role has permission to access resource.
    
    Args:
        user_role: User's role (guest/user/admin/superadmin)
        resource: Resource being accessed
    
    Returns:
        True if access granted, False otherwise
    
    Real-world use case: Authorization systems, RBAC (Role-Based Access Control).
    """
    # Admin and superadmin have access to everything
    if user_role in ["admin", "superadmin"]:
        return True
    
    # Users can read and write
    if user_role == "user" and resource in ["read", "write"]:
        return True
    
    # Guests can only read
    if user_role == "guest" and resource == "read":
        return True
    
    # Default deny
    return False


def demonstrate_access_control() -> None:
    """
    Demonstrates role-based access control (RBAC).
    
    Real-world use case: Authorization systems.
    """
    roles = ["guest", "user", "admin", "superadmin"]
    resources = ["read", "write", "delete", "admin"]
    
    print(f"\n{'Role':12} | {'read':6} | {'write':6} | {'delete':6} | {'admin':6}")
    print("-" * 55)
    
    for role in roles:
        permissions = [check_access_permission(role, res) for res in resources]
        perm_str = " | ".join(["✓" if p else "✗" for p in permissions])
        print(f"{role:12} | {perm_str}")


if __name__ == "__main__":
    demonstrate_access_control()
