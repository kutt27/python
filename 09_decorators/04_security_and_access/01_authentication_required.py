"""
Topic: Authentication Checkers.

Hides the complexity of checking user sessions behind a 
reusable '@login_required' decorator.
"""

from functools import wraps

# Simulated global user state
CURRENT_USER = {"name": "Alice", "logged_in": True}

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if not CURRENT_USER.get("logged_in"):
            print("Access Denied: Authentication required")
            return None
        return func(*args, **kwargs)
    return wrapper

@login_required
def view_secret_dashboard():
    print("Welcome to the secret dashboard!")

if __name__ == "__main__":
    # Case 1: Logged in
    view_secret_dashboard()
    
    # Case 2: Logged out
    CURRENT_USER["logged_in"] = False
    view_secret_dashboard()
