"""
Find and Process Match with Walrus.
"""

from typing import List, Dict, Optional

def find_and_process_match(data: List[Dict], criteria: str) -> Optional[Dict]:
    """
    Finds first match and processes it using walrus.
    
    Args:
        data: List of data dictionaries
        criteria: Matching criteria
    
    Returns:
        Processed matching item or None
    
    Real-world use case: Database queries, search operations.
    """
    print(f"\nSearching for: {criteria}")
    print("-" * 60)
    
    for item in data:
        # Find and assign match in condition
        if (match := item.get('category')) == criteria:
            # match variable available here
            print(f"  ✓ Found match: {item.get('name')} ({match})")
            return {**item, 'processed': True}
    
    print(f"  ✗ No match found for: {criteria}")
    return None


def demonstrate_match_processing() -> None:
    """
    Demonstrates finding and processing match.
    """
    products = [
        {"name": "Laptop", "category": "electronics"},
        {"name": "Desk", "category": "furniture"},
        {"name": "Mouse", "category": "electronics"},
    ]
    
    result = find_and_process_match(products, criteria="electronics")
    if result:
        print(f"\nProcessed: {result}")


if __name__ == "__main__":
    demonstrate_match_processing()
