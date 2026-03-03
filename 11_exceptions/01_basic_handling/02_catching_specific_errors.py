"""
Topic: Catching Specific Errors.

Always catch specific exceptions rather than using a bare 'except:'. 
This prevents accidentally swallowing bugs you didn't intend to handle.
"""

from typing import Optional

def parse_int(value: str) -> Optional[int]:
    try:
        return int(value)
    except ValueError:
        print(f"'{value}' is not a valid integer.")
        return None

def get_user_age(user_data: dict, username: str) -> Optional[int]:
    try:
        return user_data[username]["age"]
    except KeyError:
        print(f"User '{username}' not found.")
        return None
    except TypeError:
        print(f"Invalid data format for '{username}'.")
        return None

if __name__ == "__main__":
    data = {"alice": {"age": 25}}
    
    print(f"Alice's age: {get_user_age(data, 'alice')}")
    print(f"Bob's age:   {get_user_age(data, 'bob')}")
    
    parse_int("abc")
