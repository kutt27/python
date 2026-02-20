"""
Authentication Methods with fallback.
"""

from typing import List, Optional

def authenticate_user(username: str, password: str, auth_methods: List[str]) -> tuple[bool, Optional[str]]:
    """
    Tries multiple authentication methods.
    
    Args:
        username: Username
        password: Password
        auth_methods: List of auth methods to try
    
    Returns:
        Tuple of (success, method_used)
    
    Real-world use case: Multi-factor authentication, auth fallback.
    """
    print(f"\nTrying authentication for user: {username}")
    print("-" * 60)
    
    for method in auth_methods:
        print(f"  Attempting {method}... ", end="")
        
        # Simulate authentication (only OAuth succeeds in this example)
        if method == "OAuth":
            print("✓ SUCCESS")
            return (True, method)
        else:
            print("✗ Failed")
    
    else:
        # No authentication method succeeded
        print("\n🚫 ALL AUTHENTICATION METHODS FAILED")
        return (False, None)


def demonstrate_auth_methods() -> None:
    """
    Demonstrates authentication methods fallback.
    """
    methods = ["LDAP", "SAML", "OAuth", "Certificate"]
    success, method = authenticate_user("alice", "password123", methods)
    
    if success:
        print(f"\n→ User authenticated via {method}")
    else:
        print("\n→ Access denied")


if __name__ == "__main__":
    demonstrate_auth_methods()
