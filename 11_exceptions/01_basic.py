"""
Python Exceptions: Basics
==========================

Topic: Basic try-except usage

Real-World Applications:
- External API calls
- Data conversion
- Input validation
"""

from typing import Union, Optional


def parse_percentage(value: str) -> Optional[float]:
    """
    Parse a string value into a percentage float.
    
    Real-world scenario: Processing user input from a web form
    where data comes as strings.
    """
    try:
        # Attempt to convert string to float
        result = float(value.strip('% '))
        return result / 100.0
    except ValueError as e:
        # Handle the specific error case where conversion fails
        print(f"Error parsing '{value}': {e}")
        return None
    except Exception as e:
        # Catch-all for unexpected errors (use sparingly)
        print(f"Unexpected error: {e}")
        return None


def fetch_user_data(user_id: int) -> dict:
    """
    Simulate fetching user data with error handling.
    """
    # Simulate database
    users = {1: "Alice", 2: "Bob"}
    
    try:
        # Dangerous operation: could fail if ID not found or invalid type
        return {"id": user_id, "name": users[user_id]}
    except KeyError:
        print(f"User ID {user_id} not found.")
        return {}
    except TypeError:
        print("Invalid User ID type provided.")
        return {}


def main():
    """Demonstrates basic exception handling."""
    print("="*70)
    print("EXCEPTION HANDLING BASICS".center(70))
    print("="*70)
    
    print("\n[1] BASIC TRY-EXCEPT")
    print("-" * 70)
    
    inputs = ["50%", "75.5", "invalid", "100 %"]
    
    for val in inputs:
        result = parse_percentage(val)
        if result is not None:
            print(f"Parsed '{val}' -> {result:.2f}")
        else:
            print(f"Failed to parse '{val}'")
            
    print("\n[2] HANDLING DICTIONARY LOOKUPS")
    print("-" * 70)
    
    # Valid user
    print(f"User 1: {fetch_user_data(1)}")
    
    # Invalid user (KeyError)
    print(f"User 99: {fetch_user_data(99)}")
    
    # Invalid type (simulated via direct call usually caught by type checkers, 
    # but runtime data can be messy)
    # Using a string explicitly to trigger TypeError in implementation logic if we didn't type hint
    # logic depending on how dictionary keys work
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use try-except to handle potential runtime errors")
    print("• Catch specific exceptions (ValueError, KeyError) over generic Exception")
    print("• Keep try blocks minimal - only wrap code that might fail")
    print("="*70)


if __name__ == "__main__":
    main()