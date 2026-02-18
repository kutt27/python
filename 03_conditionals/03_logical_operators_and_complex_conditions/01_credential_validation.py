"""
Credential Validation logic.
"""

def validate_user_credentials(
    username: str,
    password: str,
    min_password_length: int = 8
) -> tuple[bool, str]:
    """
    Validates user credentials with multiple conditions.
    
    Args:
        username: User's username
        password: User's password
        min_password_length: Minimum required password length
    
    Returns:
        Tuple of (is_valid, message)
    
    Real-world use case: User registration, authentication systems.
    """
    # Multiple conditions with AND operator
    if not username or not password:
        return (False, "Username and password are required")
    
    if len(username) < 3 or len(password) < min_password_length:
        return (False, f"Username must be 3+ chars, password must be {min_password_length}+ chars")
    
    # Check for special characters (simplified)
    has_number = any(c.isdigit() for c in password)
    has_letter = any(c.isalpha() for c in password)
    
    if not (has_number and has_letter):
        return (False, "Password must contain both letters and numbers")
    
    return (True, "")


def demonstrate_credential_validation() -> None:
    """
    Demonstrates credential validation using logical operators.
    
    Real-world use case: User registration systems.
    """
    test_credentials = [
        ("admin", "Pass123", "Valid credentials"),
        ("ab", "Pass123", "Username too short"),
        ("admin", "short", "Password too short"),
        ("admin", "password", "Password missing number"),
    ]
    
    for username, password, description in test_credentials:
        is_valid, message = validate_user_credentials(username, password)
        status = "✓ VALID" if is_valid else "✗ INVALID"
        print(f"{status:10} | {description:30} | {message}")


if __name__ == "__main__":
    demonstrate_credential_validation()
