"""
Find User with break.
"""

from typing import List, Optional, Dict

def find_user_by_id(users: List[Dict], target_id: int) -> Optional[Dict]:
    """
    Searches for user and stops when found (break pattern).
    
    Args:
        users: List of user dictionaries
        target_id: User ID to find
    
    Returns:
        User dictionary if found, None otherwise
    
    Real-world use case: Database search optimization, early exit.
    """
    print(f"\nSearching for user ID: {target_id}")
    print("-" * 60)
    
    for user in users:
        print(f"  Checking user {user['id']}...")
        
        if user['id'] == target_id:
            print(f"  ✓ Found: {user['name']}")
            return user  # Early exit - no need to check remaining users
    
    print(f"  ✗ User {target_id} not found")
    return None


def demonstrate_find_user() -> None:
    """
    Demonstrates finding user with early exit.
    """
    users = [
        {"id": 101, "name": "Alice"},
        {"id": 102, "name": "Bob"},
        {"id": 103, "name": "Charlie"},
        {"id": 104, "name": "Diana"},
    ]
    
    found = find_user_by_id(users, target_id=102)
    print(f"\nResult: {found}")


if __name__ == "__main__":
    demonstrate_find_user()
