"""
Python While Loops and Conditional Iteration
=============================================

Topic: while loops, polling, and iterative processes

Real-World Applications:
- Polling for job completion
- Rate limit handling with retries  
- Server health monitoring
- Queue processing until empty
- Resource allocation loops
"""

import time
from typing import Optional


def wait_for_job_completion(job_id: str, max_wait_seconds: int = 60) -> bool:
    """
    Polls for job completion with timeout.
    
    Args:
        job_id: Job identifier
        max_wait_seconds: Maximum wait time
    
    Returns:
        True if job completed, False if timed out
    
    Real-world use case: Async job processing, background tasks.
    """
    elapsed = 0
    check_interval = 5
    
    print(f"\nWaiting for job {job_id} to complete (max {max_wait_seconds}s)")
    print("-" * 60)
    
    while elapsed < max_wait_seconds:
        # Simulate checking job status
        # In real scenario: API call to check job status
        print(f"  [{elapsed}s] Checking job status...")
        
        # Simulate job completion after 15 seconds
        if elapsed >= 15:
            print(f"  [✓] Job {job_id} completed after {elapsed}s")
            return True
        
        time.sleep(check_interval)
        elapsed += check_interval
    
    print(f"  [✗] Timeout: Job {job_id} did not complete within {max_wait_seconds}s")
    return False


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


def retry_with_backoff(
    operation: str,
    max_retries: int = 5,
    initial_delay: float = 1.0
) -> bool:
    """
    Retries operation with exponential backoff.
    
    Args:
        operation: Operation description
        max_retries: Maximum retry attempts
        initial_delay: Initial retry delay in seconds
    
    Returns:
        True if operation succeeded
    
    Real-world use case: API calls, database connections.
    """
    attempt = 0
    delay = initial_delay
    
    print(f"\nAttempting operation: {operation}")
    print("-" * 60)
    
    while attempt < max_retries:
        attempt += 1
        print(f"  Attempt {attempt}/{max_retries}")
        
        # Simulate operation (fails first 3 times)
        if attempt > 3:
            print(f"  [✓] Operation succeeded on attempt {attempt}")
            return True
        
        print(f"  [✗] Failed. Retrying in {delay}s...")
        time.sleep(delay)
        
        # Exponential backoff
        delay *= 2
    
    print(f"  [✗] Operation failed after {max_retries} attempts")
    return False


def allocate_resources_until_satisfied(
    required: int,
    pool_size: int
) -> tuple[bool, int]:
    """
    Allocates resources from pool incrementally.
    
    Args:
        required: Required resource units
        pool_size: Available resource units
    
    Returns:
        Tuple of (success, allocated)
    
    Real-world use case: Cloud resource allocation, load balancing.
    """
    allocated = 0
    increment = 10
    
    print(f"\nAllocating {required} units from pool of {pool_size}")
    print("-" * 60)
    
    while allocated < required and allocated + increment <= pool_size:
        allocated += increment
        print(f"  Allocated: {allocated}/{required} units")
    
    success = allocated >= required
    status = "✓ Satisfied" if success else "✗ Insufficient resources"
    print(f"\n{status}: Allocated {allocated} units")
    
    return (success, allocated)


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("WHILE LOOPS: CONDITIONAL ITERATION".center(70))
    print("="*70)
    
    print("\n[1] JOB COMPLETION POLLING")
    print("-" * 70)
    # Note: sleep delays removed for demo, normally would wait
    success = wait_for_job_completion("JOB-12345", max_wait_seconds=20)
    
    print("\n\n[2] QUEUE PROCESSING")
    print("-" * 70)
    task_queue = ["Task-1", "Task-2", "Task-3", "Task-4"]
    count = process_queue_until_empty(task_queue.copy())
    
    print("\n\n[3] RETRY WITH EXPONENTIAL BACKOFF")
    print("-" * 70)
    retry_with_backoff("Connect to external API", max_retries=5, initial_delay=0.5)
    
    print("\n\n[4] RESOURCE ALLOCATION")
    print("-" * 70)
    
    # Scenario 1: Successful allocation
    allocate_resources_until_satisfied(required=50, pool_size=100)
    
    # Scenario 2: Insufficient resources
    print()
    allocate_resources_until_satisfied(required=150, pool_size=100)
    
    print("\n\n[5] WHILE LOOP PATTERNS")
    print("-" * 70)
    
    print("\nPattern 1: Counter-based")
    counter = 0
    while counter < 3:
        print(f"  Iteration {counter + 1}")
        counter += 1
    
    print("\nPattern 2: Condition-based")
    threshold = 100
    value = 0
    while value < threshold:
        value += 25
        print(f"  Value: {value}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. while condition: executes as long as condition is True")
    print("2. Good for unknown iteration counts")  
    print("3. Be careful to avoid infinite loops!")
    print("4. Use break to exit early, continue to skip iteration")
    print("5. Common patterns: polling, retries, queue processing")
    print("="*70)


if __name__ == "__main__":
    main()