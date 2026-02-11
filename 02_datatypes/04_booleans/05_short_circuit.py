"""
Demonstrates short-circuit evaluation of 'and' and 'or' operators.
"""

def demonstrate_short_circuit() -> None:
    # OR returns the first Truthy value
    user_config = None
    default_config = {"theme": "dark"}
    active_config = user_config or default_config
    print(f"Active config (user_config or default): {active_config}")
    
    # AND returns the first Falsy value, or the last Truthy value
    api_key = "abc123"
    permissions = ["read", "write"]
    auth_valid = api_key and permissions
    print(f"Auth valid (key and permissions): {auth_valid}")
    
    # Practical pattern: Default values
    page_size = 0 or 10
    print(f"Page size (requested 0, defaulted to 10): {page_size}")

if __name__ == "__main__":
    demonstrate_short_circuit()
