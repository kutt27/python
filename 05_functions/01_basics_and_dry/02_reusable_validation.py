"""
Topic: Reusable validation logic.

DRY Principle: Validation logic often used in multiple places 
(registration, profile update, contact forms) - centralize it.
"""

def validate_email(email: str) -> bool:
    """
    Validates email format centrally.
    
    Real-world use case: Form validation, user input checking.
    """
    # Simplified validation
    return "@" in email and "." in email.split("@")[1]

# Example Usage:
if __name__ == "__main__":
    test_emails = [
        "user@example.com",
        "invalid.email",
        "admin@company.org",
        "@missing.com"
    ]
    
    for email in test_emails:
        is_valid = validate_email(email)
        status = "✓ Valid" if is_valid else "✗ Invalid"
        print(f"  {status}: {email}")
