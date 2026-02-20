"""
Batch Process with Progress using Walrus.
"""

from typing import List, Dict

def batch_process_with_progress(items: List[Dict], batch_size: int = 5) -> int:
    """
    Processes items in batches with progress tracking using walrus.
    
    Args:
        items: Items to process
        batch_size: Batch size
    
    Returns:
        Total items processed
    
    Real-world use case: ETL pipelines, data processing.
    """
    total = 0
    
    print(f"\nBatch processing {len(items)} items")
    print("-" * 60)
    
    for i in range(0, len(items), batch_size):
        # Slice and process batch in one expression
        if (batch := items[i:i + batch_size]):
            batch_count = len(batch)
            print(f"  Processing batch of {batch_count} items...")
            total += batch_count
    
    return total


def demonstrate_batch_progress() -> None:
    """
    Demonstrates batch processing with progress.
    """
    items_to_process = [{"id": i} for i in range(1, 13)]
    total_processed = batch_process_with_progress(items_to_process, batch_size=5)
    print(f"\nTotal processed: {total_processed} items")


if __name__ == "__main__":
    demonstrate_batch_progress()
