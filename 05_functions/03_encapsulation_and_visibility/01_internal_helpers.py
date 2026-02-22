"""
Topic: Private Helper Functions.

By convention, functions starting with an underscore `_` are 
considered internal/private to the module.
"""

def _hash_password(password: str) -> str:
    """Internal helper: handles the complexity of hashing."""
    return f"hashed_{password}_secret"

def _validate_strength(password: str) -> bool:
    """Internal helper: checks security requirements."""
    return len(password) >= 8

def register_user(username: str, password: str):
    """
    Public API: The user only interacts with this.
    The internal details (hashing, validation) are encapsulated.
    """
    if not _validate_strength(password):
        print("Error: Password too weak")
        return None
    
    hashed = _hash_password(password)
    print(f"User {username} registered with hash {hashed}")
    return {"user": username, "status": "active"}

if __name__ == "__main__":
    register_user("alice", "SecurePass123")
    register_user("bob", "weak")
