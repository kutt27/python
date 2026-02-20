"""
Job Retries with nested loops.
"""

from typing import List

def retry_failed_jobs(job_ids: List[int], max_retries: int = 3) -> None:
    """
    Retries failed jobs with exponential backoff.
    
    Args:
        job_ids: List of failed job IDs
        max_retries: Maximum number of retry attempts
    
    Real-world use case: Job queue processing, failure recovery.
    """
    print(f"\nRetrying {len(job_ids)} failed jobs (max {max_retries} attempts)")
    print("-" * 60)
    
    for job_id in job_ids:
        for attempt in range(1, max_retries + 1):
            print(f"Job {job_id}: Attempt {attempt}/{max_retries}")
            
            # Simulate retry logic
            # In real scenario: check job status, re-execute, etc.
            
            if attempt == max_retries:
                print(f"  ✗ Job {job_id} failed after {max_retries} attempts")
            else:
                # Simulate success on attempt 2
                if attempt == 2:
                    print(f"  ✓ Job {job_id} succeeded")
                    break


def demonstrate_job_retry() -> None:
    """
    Demonstrates job retries with nested loops and range().
    
    Real-world use case: Resilience in task processing.
    """
    failed_jobs = [101, 102, 103]
    retry_failed_jobs(failed_jobs, max_retries=3)


if __name__ == "__main__":
    demonstrate_job_retry()
