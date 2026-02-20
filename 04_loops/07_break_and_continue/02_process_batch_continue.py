"""
Batch Processing with continue.
"""

from typing import List, Dict

def process_batch_with_skip(items: List[Dict]) -> List[Dict]:
    """
    Processes batch, skipping invalid items (continue pattern).
    
    Args:
        items: List of items to process
    
    Returns:
        List of successfully processed items
    
    Real-world use case: ETL pipelines, data validation.
    """
    processed = []
    
    print(f"\nProcessing batch of {len(items)} items")
    print("-" * 60)
    
    for item in items:
        item_id = item.get('id')
        
        # Skip invalid items
        if not item.get('valid', True):
            print(f"  ⊘ Skipping invalid item: {item_id}")
            continue  # Skip to next iteration
        
        if not item.get('amount', 0) > 0:
            print(f"  ⊘ Skipping zero-amount item: {item_id}")
            continue
        
        # Process valid item
        print(f"  ✓ Processing item: {item_id}")
        processed.append(item)
    
    return processed


def demonstrate_batch_skip() -> None:
    """
    Demonstrates skipping invalid items.
    """
    batch = [
        {"id": "ITEM-1", "amount": 100, "valid": True},
        {"id": "ITEM-2", "amount": 0, "valid": True},  # Invalid: zero amount
        {"id": "ITEM-3", "amount": 50, "valid": False},  # Invalid: not valid
        {"id": "ITEM-4", "amount": 75, "valid": True},
    ]
    
    processed = process_batch_with_skip(batch)
    print(f"\nProcessed {len(processed)}/{len(batch)} items successfully")


if __name__ == "__main__":
    demonstrate_batch_skip()
