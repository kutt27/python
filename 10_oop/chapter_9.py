"""
Python OOP: Static Methods
===========================

Topic: @staticmethod decorator, utility functions

Real-World Applications:
- Utility functions related to class
- Factory methods
- Helper functions
"""

from datetime import datetime


class MathUtils:
    """Math utilities."""
    
    @staticmethod
    def is_prime(n: int) -> bool:
        """Check if number is prime."""
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    @staticmethod
    def factorial(n: int) -> int:
        """Calculate factorial."""
        if n <= 1:
            return 1
        return n * MathUtils.factorial(n - 1)


class Validator:
    """Input validation utilities."""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Validate email format."""
        return "@" in email and "." in email.split("@")[1]
    
    @staticmethod
    def validate_password(password: str) -> bool:
        """Validate password strength."""
        return len(password) >= 8


def main():
    """Demonstrates static methods."""
    print("="*70)
    print("STATIC METHODS".center(70))
    print("="*70)
    
    print("\n[1] CALLING STATIC METHODS")
    print("-" * 70)
    
    # Can call via class
    print(f"Is 17 prime? {MathUtils.is_prime(17)}")
    print(f"Is 18 prime? {MathUtils.is_prime(18)}")
    print(f"5! = {MathUtils.factorial(5)}")
    
    # Can also call via instance (but unusual)
    utils = MathUtils()
    print(f"Is 29 prime? {utils.is_prime(29)}")
    
    print("\n[2] VALIDATION UTILITIES")
    print("-" * 70)
    
    emails = ["valid@example.com", "invalid.email", "test@test.io"]
    for email in emails:
        valid = Validator.validate_email(email)
        print(f"  {email}: {'✓ Valid' if valid else '✗ Invalid'}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Static methods don't receive self or cls")
    print("• Called via ClassName.method()")
    print("• Use for utility functions related to class")
    print("• Don't need instance or class state")
    print("="*70)


if __name__ == "__main__":
    main()