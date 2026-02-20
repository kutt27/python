"""
Duplicate Detection with positions.
"""

from typing import List, Dict

def find_duplicates_with_positions(items: List[str]) -> Dict[str, List[int]]:
    """
    Finds duplicate items and their positions.
    
    Args:
        items: List of items to check
    
    Returns:
        Dictionary mapping items to their position indices
    
    Real-world use case: Data validation, duplicate detection.
    """
    positions: Dict[str, List[int]] = {}
    
    for index, item in enumerate(items):
        if item not in positions:
            positions[item] = []
        positions[item].append(index)
    
    # Filter to only duplicates
    duplicates = {k: v for k, v in positions.items() if len(v) > 1}
    
    return duplicates


def demonstrate_duplicates() -> None:
    """
    Demonstrates duplicate detection.
    """
    data = ["apple", "banana", "apple", "cherry", "banana", "apple", "date"]
    duplicates = find_duplicates_with_positions(data)
    
    print(f"\nChecking {len(data)} items for duplicates")
    if duplicates:
        for item, positions in duplicates.items():
            print(f"  '{item}' appears {len(positions)} times at positions: {positions}")
    else:
        print("  No duplicates found")


if __name__ == "__main__":
    demonstrate_duplicates()
