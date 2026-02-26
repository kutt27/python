"""
Topic: Role-Based Access Control (RBAC).

A decorator factory that takes arguments (the required role) 
to determine if a user has sufficient permissions to run 
a function.
"""

from functools import wraps

# Mock user data
USER_SESSION = {"name": "Bob", "role": "editor"}

def require_role(role_name):
    """Requires the user to have a specific role."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if USER_SESSION.get("role") != role_name:
                print(f"❌ Denied: '{role_name}' role required for {func.__name__}()")
                return None
            return func(*args, **kwargs)
        return wrapper
    return decorator

@require_role("admin")
def delete_database():
    print("Database deleted!")

@require_role("editor")
def publish_article():
    print("Article published!")

if __name__ == "__main__":
    print("Attempting to publish (as editor):")
    publish_article()
    
    print("\nAttempting to delete database (as editor):")
    delete_database()
