"""
Python Exceptions: Custom Exceptions - Basics
==============================================

Topic: Defining and raising user-defined exceptions

Real-World Applications:
- Domain-specific errors (InsufficientFunds, UserNotAllowed)
- Framework development
- Clearer API error reporting
"""

class AppError(Exception):
    """Base class for all application-specific exceptions."""
    pass


class ValidationError(AppError):
    """Raised when input validation fails."""
    pass


class ResourceNotFound(AppError):
    """Raised when a requested resource doesn't exist."""
    pass


def update_user_profile(user_id: int, email: str):
    """
    Simulate updating user profile with domain-specific validation.
    """
    print(f"\nUpdating user {user_id} with email '{email}'")
    
    # Simulate database lookup
    existing_ids = [101, 102]
    
    if user_id not in existing_ids:
        # Raise domain-specific error instead of generic ValueError
        raise ResourceNotFound(f"User ID {user_id} does not exist in system.")
        
    if "@" not in email or "." not in email:
        raise ValidationError(f"Invalid email format: {email}")
        
    print(f"✓ Profile updated successfully.")


def main():
    """Demonstrates basic custom exceptions."""
    print("="*70)
    print("CUSTOM EXCEPTIONS (BASICS)".center(70))
    print("="*70)
    
    scenarios = [
        (101, "valid@example.com"),   # Valid
        (999, "valid@example.com"),   # ResourceNotFound
        (101, "invalid-email"),       # ValidationError
    ]
    
    for uid, email in scenarios:
        try:
            update_user_profile(uid, email)
            
        except ResourceNotFound as e:
            print(f"✗ Not Found: {e}")
            
        except ValidationError as e:
            print(f"✗ Validation Failed: {e}")
            
        except AppError as e:
            # Catch-all for our app's errors
            print(f"✗ Generic App Error: {e}")

    print("\n" + "="*70)
    print("Key Points:")
    print("• Inherit from Exception (or a custom base class)")
    print("• Use descriptive names ending in 'Error'")
    print("• Create a base exception for your library/app (e.g. AppError)")
    print("• Allows callers to catch specific domain errors")
    print("="*70)


if __name__ == "__main__":
    main()