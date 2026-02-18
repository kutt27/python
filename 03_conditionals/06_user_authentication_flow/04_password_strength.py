"""
Password Strength logic.
"""

from typing import List

def determine_password_strength(password: str) -> tuple[str, List[str]]:
    """
    Determines password strength and provides feedback.
    
    Args:
        password: Password to evaluate
    
    Returns:
        Tuple of (strength_level, suggestions)
    
    Real-world use case: Password policies, user registration.
    """
    suggestions = []
    score = 0
    
    # Length check
    if len(password) < 8:
        suggestions.append("Use at least 8 characters")
    elif len(password) >= 12:
        score += 2
    else:
        score += 1
    
    # Character variety checks
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)
    
    if not has_lower:
        suggestions.append("Add lowercase letters")
    else:
        score += 1
    
    if not has_upper:
        suggestions.append("Add uppercase letters")
    else:
        score += 1
    
    if not has_digit:
        suggestions.append("Add numbers")
    else:
        score += 1
    
    if not has_special:
        suggestions.append("Add special characters (!@#$%)")
    else:
        score += 2
    
    # Determine strength level
    if score >= 7:
        strength = "strong"
    elif score >= 4:
        strength = "medium"
    else:
        strength = "weak"
    
    return (strength, suggestions)


def demonstrate_password_strength() -> None:
    """
    Demonstrates password policy evaluation and feedback.
    
    Real-world use case: User registration, security audits.
    """
    test_passwords = [
        "weak",
        "Password1",
        "MyP@ssw0rd!",
        "SuperSecure123!@#",
    ]
    
    for pwd in test_passwords:
        strength, suggestions = determine_password_strength(pwd)
        
        strength_icons = {
            "weak": "🔴",
            "medium": "🟡",
            "strong": "🟢"
        }
        
        icon = strength_icons[strength]
        print(f"{icon} {strength.upper():6} | '{pwd}'")
        if suggestions:
            for suggestion in suggestions:
                print(f"           - {suggestion}")


if __name__ == "__main__":
    demonstrate_password_strength()
