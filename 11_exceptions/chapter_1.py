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



def demonstrate_basic_try_except() -> None:
    """
    Demonstrates basic error handling for data parsing.
    
    Real-world use case: Processing unstable user input from web forms.
    """
    inputs = ["50%", "75.5", "invalid", "100 %"]
    
    for val in inputs:
        result = parse_percentage(val)
        if result is not None:
            print(f"Parsed '{val}' -> {result:.2f}")
        else:
            print(f"Failed to parse '{val}'")


def demonstrate_dictionary_lookups() -> None:
    """
    Demonstrates handling missing keys in collections.
    
    Real-world use case: Searching for records in a cache or database mock.
    """
    # Valid user
    print(f"User 1: {fetch_user_data(1)}")
    
    # Invalid user (KeyError)
    print(f"User 99: {fetch_user_data(99)}")


def main() -> None:
    """Main function demonstrating basic exception handling."""
    print("="*70)
    print("PYTHON EXCEPTIONS: BASIC HANDLING".center(70))
    print("="*70)
    
    print("\n[1] BASIC TRY-EXCEPT - Data Parsing")
    print("-" * 70)
    demonstrate_basic_try_except()
    
    print("\n\n[2] HANDLING DICTIONARY LOOKUPS")
    print("-" * 70)
    demonstrate_dictionary_lookups()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Use try-except to wrap code that might fail at runtime")
    print("2. Always catch specific exceptions (e.g. ValueError) rather than generic ones")
    print("3. Keep try blocks as small as possible to avoid catching unrelated errors")
    print("4. Provide helpful error messages or fallback values when exceptions occur")
    print("5. Exception handling prevents application crashes on bad data")
    print("="*70)


if __name__ == "__main__":
    main()