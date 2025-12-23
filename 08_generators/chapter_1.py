"""
Python Generators: Basics with yield
=====================================

Topic: Generator functions, yield statement, lazy evaluation

Real-World Applications:
- Streaming large datasets
- Log file processing
- Database result pagination
- Real-time data feeds
- Memory-efficient iteration
"""

from typing import Generator, List, Dict
import time


def read_log_lines(filename: str) -> Generator[str, None, None]:
    """
    Simulates reading log file line by line (memory efficient).
    
    Generator doesn't load entire file into memory.
    
    Args:
        filename: Log file path
    
    Yields:
        One log line at a time
    
    Real-world use case: Processing large log files.
    """
    # Simulated log lines
    log_data = [
        "2024-01-01 10:00:00 INFO Server started",
        "2024-01-01 10:05:23 ERROR Database connection failed",
        "2024-01-01 10:05:45 INFO Retrying connection",
        "2024-01-01 10:06:00 INFO Connection established",
        "2024-01-01 10:10:15 ERROR Request timeout",
    ]
    
    print(f"Opening file: {filename}")
    for line in log_data:
        yield line
    print(f"Closing file: {filename}")


def paginate_database_results(query: str, page_size: int = 10) -> Generator[List[Dict], None, None]:
    """
    Paginates database query results.
    
    Yields one page at a time instead of loading all results.
    
    Args:
        query: SQL query
        page_size: Results per page
    
    Yields:
        Page of results
    
    Real-world use case: Database pagination, API result fetching.
    """
    # Simulate database with 35 records
    all_records = [{"id": i, "name": f"User_{i}"} for i in range(1, 36)]
    
    print(f"Executing query: {query}")
    print(f"Total records: {len(all_records)}, Page size: {page_size}\n")
    
    for i in range(0, len(all_records), page_size):
        page = all_records[i:i + page_size]
        page_num = (i // page_size) + 1
        print(f"Fetching page {page_num}...")
        yield page


def stream_api_data(endpoint: str) -> Generator[Dict, None, None]:
    """
    Streams API data one record at a time.
    
    Args:
        endpoint: API endpoint
    
    Yields:
        One record at a time
    
    Real-world use case: Streaming API responses, real-time data.
    """
    # Simulated API data
    api_data = [
        {"user_id": 101, "action": "login", "timestamp": "10:00:00"},
        {"user_id": 102, "action": "view_page", "timestamp": "10:01:15"},
        {"user_id": 101, "action": "logout", "timestamp": "10:05:30"},
    ]
    
    print(f"Streaming data from {endpoint}...")
    for record in api_data:
        # Simulate API delay
        time.sleep(0.1)
        yield record


def fibonacci_generator(limit: int) -> Generator[int, None, None]:
    """
    Generates Fibonacci numbers up to limit.
    
    Args:
        limit: Maximum number of Fibonacci numbers to generate
    
    Yields:
        Next Fibonacci number
    
    Real-world use case: Mathematical sequences, algorithm demonstrations.
    """
    a, b = 0, 1
    count = 0
    
    while count < limit:
        yield a
        a, b = b, a + b
        count += 1


def process_batch_with_yield(items: List, batch_size: int) -> Generator[List, None, None]:
    """
    Processes items in batches using generator.
    
    Args:
        items: Items to process
        batch_size: Batch size
    
    Yields:
        One batch at a time
    
    Real-world use case: Batch API requests, ETL processing.
    """
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        print(f"Processing batch of {len(batch)} items...")
        yield batch



def demonstrate_log_streaming() -> None:
    """
    Demonstrates memory-efficient log streaming.
    
    Real-world use case: Processing multi-gigabyte log files.
    """
    log_gen = read_log_lines("app.log")
    print(f"Generator created: {log_gen}")
    print("\nReading log lines:")
    for line in log_gen:
        print(f"  {line}")


def demonstrate_db_pagination() -> None:
    """
    Demonstrates lazy database result pagination.
    
    Real-world use case: Dynamic loading of UI elements (infinite scroll).
    """
    results_gen = paginate_database_results("SELECT * FROM users", page_size=10)
    
    # Fetch first 2 pages only
    page1 = next(results_gen)
    print(f"Page 1: {len(page1)} records")
    print(f"  First record: {page1[0]}")
    print(f"  Last record: {page1[-1]}")
    
    page2 = next(results_gen)
    print(f"\nPage 2: {len(page2)} records")
    print(f"  First record: {page2[0]}")


def demonstrate_api_streaming() -> None:
    """
    Demonstrates real-time API data streaming.
    
    Real-world use case: WebSocket data handling, live dashboards.
    """
    api_stream = stream_api_data("/api/events")
    for event in api_stream:
        print(f"  Received: User {event['user_id']} - {event['action']} at {event['timestamp']}")


def demonstrate_fibonacci() -> None:
    """
    Demonstrates generating infinite-like mathematical sequences.
    
    Real-world use case: Algorithmic modeling, sequence analysis.
    """
    fib_gen = fibonacci_generator(limit=10)
    fib_numbers = list(fib_gen)
    print(f"First 10 Fibonacci numbers: {fib_numbers}")


def demonstrate_batch_processing() -> None:
    """
    Demonstrates chunked processing of large collections.
    
    Real-world use case: ETL pipelines, bulk API uploads.
    """
    items = list(range(1, 26))  # 25 items
    batch_gen = process_batch_with_yield(items, batch_size=7)
    
    for batch_num, batch in enumerate(batch_gen, 1):
        print(f"  Batch {batch_num}: {batch[:3]}... ({len(batch)} items total)")


def demonstrate_memory_efficiency() -> None:
    """
    Demonstrates memory footprint difference between lists and generators.
    
    Real-world use case: High-performance data processing.
    """
    def get_numbers_list(n):
        return [i ** 2 for i in range(n)]
    
    def get_numbers_generator(n):
        for i in range(n):
            yield i ** 2
    
    n = 10
    nums_list = get_numbers_list(n)
    nums_gen = get_numbers_generator(n)
    
    print(f"List (all in memory): {nums_list}")
    print(f"Generator (lazy): {nums_gen}")
    print(f"\nIterating generator:")
    for num in nums_gen:
        print(f"  {num}", end=" ")
    print()


def main() -> None:
    """Main function demonstrating generator basics with yield."""
    print("="*70)
    print("PYTHON GENERATORS: yield STATEMENT".center(70))
    print("="*70)
    
    print("\n[1] BASIC GENERATOR - File Processing")
    print("-" * 70)
    demonstrate_log_streaming()
    
    print("\n\n[2] DATABASE PAGINATION")
    print("-" * 70)
    demonstrate_db_pagination()
    
    print("\n\n[3] API DATA STREAMING")
    print("-" * 70)
    demonstrate_api_streaming()
    
    print("\n\n[4] FIBONACCI SEQUENCE")
    print("-" * 70)
    demonstrate_fibonacci()
    
    print("\n\n[5] BATCH PROCESSING")
    print("-" * 70)
    demonstrate_batch_processing()
    
    print("\n\n[6] MEMORY COMPARISON")
    print("-" * 70)
    demonstrate_memory_efficiency()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Generators use 'yield' to produce values one-at-a-time (lazily)")
    print("2. They maintain execution state (variables, etc.) between yields")
    print("3. Extremely memory-efficient as they don't store entire sequences")
    print("4. Generators are iterators - they are single-use and can be exhausted")
    print("5. Ideal for processing large files, database results, or infinite feeds")
    print("="*70)


if __name__ == "__main__":
    main()