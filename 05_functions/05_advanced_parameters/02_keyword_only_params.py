"""
Topic: Keyword-Only Parameters (*).

The `*` symbol in the parameter list forces all following 
parameters to be passed as keyword arguments. This prevents 
accidental mistakes with boolean flags.
"""

def create_user(username: str, email: str, *, is_admin: bool = False):
    """is_admin MUST be passed as a keyword."""
    print(f"User: {username}, Admin: {is_admin}")

if __name__ == "__main__":
    # Correct usage
    create_user("alice", "alice@example.com", is_admin=True)
    
    # This would raise a TypeError:
    # create_user("bob", "bob@example.com", True)
