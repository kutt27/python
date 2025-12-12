"""
Python For Loops: Range and Iteration Basics
=============================================

Topic: for loops with range() function

Real-World Applications:
- Batch processing in ETL pipelines
- Pagination handling in APIs
- Task scheduling and job execution
- Database record processing
- Rate-limited API calls
"""

from time import sleep
from typing import List, Dict


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


def generate_user_ids(start: int, count: int) -> List[int]:
    """
    Generates sequential user IDs.
    
    Args:
        start: Starting ID
        count: Number of IDs to generate
    
    Returns:
        List of user IDs
    
    Real-world use case: Test data generation, ID allocation.
    """
    user_ids = []
    for user_id in range(start, start + count):
        user_ids.append(user_id)
    return user_ids


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


def paginate_results(total_items: int, page_size: int = 20) -> List[tuple]:
    """
    Generates pagination ranges for API responses.
    
    Args:
        total_items: Total number of items
        page_size: Items per page
    
    Returns:
        List of (page_number, start_index, end_index) tuples
    
    Real-world use case: API pagination, database query chunking.
    """
    pages = []
    total_pages = (total_items + page_size - 1) // page_size
    
    for page in range(1, total_pages + 1):
        start = (page - 1) * page_size
        end = min(start + page_size, total_items)
        pages.append((page, start, end))
    
    return pages


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("FOR LOOPS: RANGE & ITERATION".center(70))
    print("="*70)
    
    print("\n[1] BATCH REQUEST PROCESSING")
    print("-" * 70)
    process_batch_requests(total_requests=45, batch_size=10)
    
    print("\n\n[2] USER ID GENERATION")
    print("-" * 70)
    user_ids = generate_user_ids(start=1000, count=10)
    print(f"Generated user IDs: {user_ids}")
    
    print("\n\n[3] JOB RETRY MECHANISM")
    print("-" * 70)
    failed_jobs = [101, 102, 103]
    retry_failed_jobs(failed_jobs, max_retries=3)
    
    print("\n\n[4] API PAGINATION")
    print("-" * 70)
    total_records = 87
    page_size = 20
    
    pages = paginate_results(total_records, page_size)
    print(f"\nTotal records: {total_records}, Page size: {page_size}")
    print(f"Total pages: {len(pages)}\n")
    
    for page_num, start, end in pages:
        items_count = end - start
        print(f"Page {page_num}: Records {start}-{end} ({items_count} items)")
    
    print("\n\n[5] RANGE VARIATIONS")
    print("-" * 70)
    
    # Basic range
    print("range(5):", list(range(5)))
    
    # Start and stop
    print("range(1, 6):", list(range(1, 6)))
    
    # With step
    print("range(0, 10, 2):", list(range(0, 10, 2)))
    
    # Reverse
    print("range(10, 0, -1):", list(range(10, 0, -1)))
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. range(stop) generates 0 to stop-1")
    print("2. range(start, stop) generates start to stop-1")
    print("3. range(start, stop, step) allows custom increments")
    print("4. Use negative step for reverse iteration")
    print("5. range is memory-efficient (generates values on-the-fly)")
    print("="*70)


if __name__ == "__main__":
    main()