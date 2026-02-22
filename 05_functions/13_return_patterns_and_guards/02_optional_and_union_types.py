"""
Topic: Optional and Union Return Types.

- Optional: Used when a function might not find a result (returns T or None).
- Union: Used when a function can return different types (e.g., Result or Error).
"""

from typing import Optional, Union, List, Dict

def find_user(user_id: int, users: List[Dict]) -> Optional[Dict]:
    """Returns a user dict or None if not found."""
    for user in users:
        if user["id"] == user_id:
            return user
    return None

def calculate_sqrt(n: float) -> Union[float, str]:
    """Returns number or error message string."""
    if n < 0:
        return "Cannot calculate square root of negative number"
    return n ** 0.5

if __name__ == "__main__":
    db = [{"id": 1, "name": "Alice"}]
    print(f"User 1: {find_user(1, db)}")
    print(f"User 2: {find_user(2, db)}")
    
    print(f"SQRT(16): {calculate_sqrt(16)}")
    print(f"SQRT(-1): {calculate_sqrt(-1)}")
