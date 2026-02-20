"""
Retry with Exponential Backoff.
"""

import time

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
        # Reduced sleep for demo speed
        time.sleep(delay * 0.1)
        
        # Exponential backoff
        delay *= 2
    
    print(f"  [✗] Operation failed after {max_retries} attempts")
    return False


def demonstrate_retry() -> None:
    """
    Demonstrates retry with exponential backoff.
    """
    retry_with_backoff("Connect to external API", max_retries=5, initial_delay=0.5)


if __name__ == "__main__":
    demonstrate_retry()
