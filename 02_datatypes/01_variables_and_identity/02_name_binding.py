"""
Demonstrates Python's name binding mechanism and variable reassignment.
"""

def demonstrate_name_binding() -> None:
    # Example: API rate limit configuration
    max_requests = 100  # Initial rate limit
    print(f"Initial rate limit: {max_requests}")
    print(f"Memory address of 100: {id(max_requests)}")
    
    # Changing configuration
    max_requests = 1000  # New rate limit for premium users
    print(f"\nUpdated rate limit: {max_requests}")
    print(f"Memory address of 1000: {id(max_requests)}")
    
    # Key insight: The name 'max_requests' now points to a different object
    print("\nIMPORTANT: Integer objects are IMMUTABLE")
    print("Reassignment changes the REFERENCE, not the VALUE")

if __name__ == "__main__":
    demonstrate_name_binding()
