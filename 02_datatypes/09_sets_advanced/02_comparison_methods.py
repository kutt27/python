"""
Demonstrates set comparison methods: issubset, issuperset, and isdisjoint.
"""

def demonstrate_comparisons() -> None:
    admin = {"read", "write", "delete", "admin"}
    user = {"read", "write"}
    guest = {"read"}
    premium = {"export_pdf", "api_access"}
    
    print(f"User is subset of Admin? {user.issubset(admin)}")
    print(f"Admin is superset of User? {admin.issuperset(user)}")
    print(f"Guest and Premium are disjoint? {guest.isdisjoint(premium)}")

if __name__ == "__main__":
    demonstrate_comparisons()
