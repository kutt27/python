"""
Batch Updates with progress.
"""

from typing import List, Dict

def batch_update_with_progress(items: List[Dict], batch_size: int = 5) -> None:
    """
    Performs batch updates with progress reporting.
    
    Args:
        items: Items to update
        batch_size: Size of each batch
    
    Real-world use case: Database batch updates, bulk operations.
    """
    total = len(items)
    print(f"\nBatch updating {total} items (batch size: {batch_size})")
    print("-" * 60)
    
    for index, item in enumerate(items):
        # Determine batch number and position
        batch_num = (index // batch_size) + 1
        position_in_batch = (index % batch_size) + 1
        
        print(f"Batch {batch_num}, Item {position_in_batch}/{batch_size}: Updating {item.get('id')}")
        
        # Commit batch when complete
        if (index + 1) % batch_size == 0 or (index + 1) == total:
            items_in_batch = min(batch_size, total - (batch_num - 1) * batch_size)
            print(f"  → Committing batch {batch_num} ({items_in_batch} items)")


def demonstrate_batch_updates() -> None:
    """
    Demonstrates batch updates with progress.
    """
    items_to_update = [
        {"id": f"ITEM-{i}"} for i in range(1, 13)
    ]
    
    batch_update_with_progress(items_to_update, batch_size=5)


if __name__ == "__main__":
    demonstrate_batch_updates()
