"""
Batch Processing with range().
"""

from typing import List

def process_batch_requests(total_requests: int, batch_size: int = 10) -> None:
    """
    Processes API requests in batches using for loop with range.
    
    Args:
        total_requests: Total number of requests to process
        batch_size: Number of requests per batch
    
    Real-world use case: Rate-limited API calls, bulk operations.
    """
    print(f"\nProcessing {total_requests} requests in batches of {batch_size}")
    print("-" * 60)
    
    for batch_num in range(1, (total_requests // batch_size) + 1):
        start_idx = (batch_num - 1) * batch_size + 1
        end_idx = min(batch_num * batch_size, total_requests)
        
        print(f"Batch #{batch_num}: Processing requests {start_idx}-{end_idx}")
        # Simulate processing time
        # In real scenario: make API calls, process data, etc.


def demonstrate_batch_processing() -> None:
    """
    Demonstrates batch request processing using range().
    
    Real-world use case: Large-scale API calls, database batching.
    """
    process_batch_requests(total_requests=45, batch_size=10)


if __name__ == "__main__":
    demonstrate_batch_processing()
