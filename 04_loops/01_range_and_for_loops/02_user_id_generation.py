"""
User ID Generation with range().
"""

from typing import List

def generate_user_ids(start: int, count: int) -> List[int]:
    """
    Generates sequential user IDs.
    
    Args:
        start: Starting ID
        count: Number of IDs to generate
    
    Returns:
        List of user IDs
    
    Real-world use case: Test data generation, ID allocation.
    """
    user_ids = []
    for user_id in range(start, start + count):
        user_ids.append(user_id)
    return user_ids


def demonstrate_id_generation() -> None:
    """
    Demonstrates sequential ID generation using range().
    
    Real-world use case: Mock data generation, sequential indexing.
    """
    user_ids = generate_user_ids(start=1000, count=10)
    print(f"Generated user IDs: {user_ids}")


if __name__ == "__main__":
    demonstrate_id_generation()
