"""
Demonstrates truthiness for input validation.
"""

def validate_user_input(username: str, email: str) -> bool:
    # Leveraging truthiness: empty strings are Falsy
    if not username or not email:
        print("✗ Validation failed: Username and Email are required")
        return False
    
    print(f"✓ Validation passed for: {username}")
    return True

if __name__ == "__main__":
    validate_user_input("john_doe", "john@example.com")
    validate_user_input("", "")

if __name__ == "__main__":
    # The above is redundant but following the pattern
    pass
