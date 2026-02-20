"""
Queue Processing until empty.
"""

from typing import List

def process_queue_until_empty(queue: list) -> int:
    """
    Processes items from queue until empty.
    
    Args:
        queue: List acting as queue
    
    Returns:
        Number of items processed
    
    Real-world use case: Message queues, task processing.
    """
    processed = 0
    
    print(f"\nProcessing queue ({len(queue)} items)")
    print("-" * 60)
    
    while queue:  # Continue while queue has items
        item = queue.pop(0)
        print(f"  Processing: {item}")
        processed += 1
    
    print(f"\nQueue empty. Processed {processed} items.")
    return processed


def demonstrate_queue_processing() -> None:
    """
    Demonstrates queue processing.
    """
    task_queue = ["Task-1", "Task-2", "Task-3", "Task-4"]
    process_queue_until_empty(task_queue.copy())


if __name__ == "__main__":
    demonstrate_queue_processing()
