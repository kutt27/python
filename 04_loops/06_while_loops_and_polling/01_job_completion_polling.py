"""
Job Completion Polling with while loops.
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
        
        # Reduced sleep for demo speed
        time.sleep(0.5) 
        elapsed += check_interval
    
    print(f"  [✗] Timeout: Job {job_id} did not complete within {max_wait_seconds}s")
    return False


def demonstrate_job_polling() -> None:
    """
    Demonstrates job completion polling.
    """
    wait_for_job_completion("JOB-12345", max_wait_seconds=20)


if __name__ == "__main__":
    demonstrate_job_polling()
