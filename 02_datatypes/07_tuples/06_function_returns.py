"""
Demonstrates returning multiple values from a function using tuples.
"""

from typing import Tuple

def get_user_info(user_id: int) -> Tuple[str, str, int]:
    # Simulate database lookup
    return ("john_doe", "john@example.com", 28)

if __name__ == "__main__":
    name, email, age = get_user_info(101)
    print(f"Name: {name}, Email: {email}, Age: {age}")
