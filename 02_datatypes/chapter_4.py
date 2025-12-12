"""
Python Boolean Logic and Type Coercion
=======================================

Topic: Boolean data type, truthiness, type coercion, and logical operations

Real-World Applications:
- Feature flag systems in production deployments
- Access control and authentication logic
- Validation in data processing pipelines
- Circuit breaker patterns in distributed systems
"""

from typing import Any, Optional


def demonstrate_boolean_basics() -> None:
    """
    Demonstrates boolean type and basic logical operations.
    
    Booleans are fundamental for:
    - Conditional logic
    - Feature toggles
    - Status flags
    - Permission checks
    
    Real-world use case: Feature flag management in A/B testing.
    """
    # Example: Feature flags for gradual rollout
    feature_enabled = True
    user_in_beta_group = False
    
    print(f"Feature enabled: {feature_enabled}")
    print(f"User in beta group: {user_in_beta_group}")
    print(f"Type: {type(feature_enabled)}")
    
    # Logical AND: Both conditions must be true
    show_feature = feature_enabled and user_in_beta_group
    print(f"\nShow feature (AND): {show_feature}")
    print("  ✓ Feature must be enabled AND user in beta")
    
    # Logical OR: At least one condition must be true
    allow_access = feature_enabled or user_in_beta_group
    print(f"\nAllow access (OR): {allow_access}")
    print("  ✓ Feature enabled OR user in beta grants access")
    
    # Logical NOT: Inverts the boolean value
    feature_disabled = not feature_enabled
    print(f"\nFeature disabled (NOT): {feature_disabled}")


def demonstrate_type_coercion() -> None:
    """
    Demonstrates automatic type coercion between bool and int.
    
    In Python:
    - True is internally represented as 1
    - False is internally represented as 0
    - This allows arithmetic operations with booleans
    
    Real-world use case: Counting boolean conditions in metrics.
    """
    # Example: Counting successful health checks
    service_a_healthy = True
    service_b_healthy = True
    service_c_healthy = False
    
    # Type coercion: True = 1, False = 0
    total_healthy = service_a_healthy + service_b_healthy + service_c_healthy
    print(f"\nHealthy services count: {total_healthy}")
    print(f"  Service A: {service_a_healthy} ({int(service_a_healthy)})")
    print(f"  Service B: {service_b_healthy} ({int(service_b_healthy)})")
    print(f"  Service C: {service_c_healthy} ({int(service_c_healthy)})")
    
    # Calculate availability percentage
    total_services = 3
    availability = (total_healthy / total_services) * 100
    print(f"\nSystem availability: {availability:.1f}%")
    
    print(f"\n{'='*60}")
    print("IMPORTANT: bool is a subclass of int")
    print(f"  isinstance(True, int): {isinstance(True, int)}")
    print(f"  True + 5 = {True + 5}")
    print(f"  False * 10 = {False * 10}")
    print(f"{'='*60}")


def demonstrate_truthiness() -> None:
    """
    Demonstrates truthiness - how Python evaluates non-boolean values as bool.
    
    Falsy values in Python:
    - None
    - False
    - 0 (zero in any numeric type)
    - Empty sequences: '', [], (), {}
    - Empty sets: set()
    
    Everything else is truthy.
    
    Real-world use case: Validation and default value handling.
    """
    # Example: API response validation
    print(f"\nTruthiness evaluation:")
    
    # Numbers
    active_connections = 0
    print(f"  Active connections (0): {bool(active_connections)} - Falsy")
    
    active_connections = 5
    print(f"  Active connections (5): {bool(active_connections)} - Truthy")
    
    # Strings
    user_input = ""
    print(f"  Empty string (''): {bool(user_input)} - Falsy")
    
    user_input = "admin"
    print(f"  String ('admin'): {bool(user_input)} - Truthy")
    
    # Collections
    error_list = []
    print(f"  Empty list ([]): {bool(error_list)} - Falsy")
    
    error_list = ["Error 404"]
    print(f"  List with items: {bool(error_list)} - Truthy")
    
    # None
    optional_value: Optional[str] = None
    print(f"  None: {bool(optional_value)} - Falsy")


def validate_user_input(username: str, email: str) -> bool:
    """
    Demonstrates practical use of truthiness in validation.
    
    Args:
        username: User's username
        email: User's email address
    
    Returns:
        True if both inputs are valid (non-empty), False otherwise
    
    Real-world use case: Form validation in web applications.
    """
    # Leveraging truthiness for validation
    is_valid = bool(username) and bool(email)
    
    if not is_valid:
        print(f"\n✗ Validation failed:")
        if not username:
            print(f"  - Username is required")
        if not email:
            print(f"  - Email is required")
    else:
        print(f"\n✓ Validation passed")
        print(f"  Username: {username}")
        print(f"  Email: {email}")
    
    return is_valid


def demonstrate_logical_operators() -> None:
    """
    Demonstrates logical operators with short-circuit evaluation.
    
    Short-circuit behavior:
    - 'and': Returns first falsy value, or last value if all truthy
    - 'or': Returns first truthy value, or last value if all falsy
    
    Real-world use case: Default value handling and conditional execution.
    """
    # Example: Configuration with defaults
    print(f"\nShort-circuit evaluation:")
    
    # OR operator: Returns first truthy value
    user_config = None
    default_config = {"theme": "dark", "language": "en"}
    
    active_config = user_config or default_config
    print(f"  user_config or default_config = {active_config}")
    print(f"  (Returns default_config since user_config is None)")
    
    # AND operator: Returns first falsy value
    api_key = "abc123"
    permissions = ["read", "write"]
    
    auth_valid = api_key and permissions
    print(f"\n  api_key and permissions = {auth_valid}")
    print(f"  (Returns permissions since api_key is truthy)")
    
    # Practical pattern: Default values
    page_size = 0  # Invalid
    default_page_size = 10
    actual_page_size = page_size or default_page_size
    print(f"\n  Requested page size: {page_size}")
    print(f"  Actual page size used: {actual_page_size}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON BOOLEANS: LOGIC & TRUTHINESS".center(70))
    print("="*70)
    
    print("\n[1] BOOLEAN BASICS")
    print("-" * 70)
    demonstrate_boolean_basics()
    
    print("\n\n[2] TYPE COERCION (bool ↔ int)")
    print("-" * 70)
    demonstrate_type_coercion()
    
    print("\n\n[3] TRUTHINESS")
    print("-" * 70)
    demonstrate_truthiness()
    
    print("\n\n[4] VALIDATION EXAMPLE")
    print("-" * 70)
    validate_user_input("john_doe", "john@example.com")
    validate_user_input("", "")  # Invalid case
    
    print("\n\n[5] LOGICAL OPERATORS & SHORT-CIRCUIT")
    print("-" * 70)
    demonstrate_logical_operators()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. bool is a subclass of int (True=1, False=0)")
    print("2. Falsy values: None, False, 0, empty sequences/collections")
    print("3. Everything else is truthy")
    print("4. Logical operators short-circuit and return actual values")
    print("5. Use truthiness for elegant validation and default values")
    print("="*70)


if __name__ == "__main__":
    main()