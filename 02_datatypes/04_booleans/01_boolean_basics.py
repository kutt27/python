"""
Demonstrates basic boolean type and logical operations (and, or, not).
"""

def demonstrate_boolean_basics() -> None:
    feature_enabled = True
    user_in_beta = False
    
    print(f"Feature enabled: {feature_enabled}")
    print(f"User in beta: {user_in_beta}")
    
    # Logical AND
    print(f"Show feature (AND): {feature_enabled and user_in_beta}")
    
    # Logical OR
    print(f"Allow access (OR): {feature_enabled or user_in_beta}")
    
    # Logical NOT
    print(f"Feature disabled (NOT): {not feature_enabled}")

if __name__ == "__main__":
    demonstrate_boolean_basics()
