"""
Python Lists: Dynamic Mutable Sequences
========================================

Topic: List data type, methods, operations, and memory behavior

Real-World Applications:
- Managing collections in web applications
- Data processing pipelines and ETL
- Request queues and task management
- Dynamic configuration management
- ML batch processing and data augmentation
"""

from typing import List, Any


def demonstrate_list_mutability() -> None:
    """
    Demonstrates list mutability and in-place modifications.
    
    Lists are mutable sequences that can be modified after creation.
    This makes them ideal for dynamic collections but requires
    careful handling when passing to functions.
    
    Real-world use case: Managing API request queue, task lists.
    """
    # Example: API request queue
    request_queue: List[str] = ["GET /users", "POST /orders"]
    
    print(f"Initial queue: {request_queue}")
    print(f"Memory ID: {id(request_queue)}")
    
    # Add new request
    request_queue.append("DELETE /cache")
    print(f"\nAfter append: {request_queue}")
    print(f"Memory ID: {id(request_queue)}  <- Same object!")
    
    # Remove completed request
    completed = request_queue.pop(0)
    print(f"\nCompleted: {completed}")
    print(f"Queue now: {request_queue}")
    print(f"Memory ID: {id(request_queue)}  <- Still same object!")


def demonstrate_list_methods() -> None:
    """
    Demonstrates essential list methods for data manipulation.
    
    Real-world use case: Building and managing data collections.
    """
    # Example: Feature deployment pipeline
    deployment_stages: List[str] = ["build", "test"]
    
    print(f"\nDeployment pipeline: {deployment_stages}")
    
    # Add stage
    deployment_stages.append("deploy")
    print(f"After append: {deployment_stages}")
    
    # Insert at specific position
    deployment_stages.insert(1, "lint")
    print(f"After insert: {deployment_stages}")
    
    # Extend with multiple stages
    post_deploy = ["monitor", "notify"]
    deployment_stages.extend(post_deploy)
    print(f"After extend: {deployment_stages}")
    
    # Remove specific item
    deployment_stages.remove("lint")  # Remove by value
    print(f"After remove: {deployment_stages}")
    
    # Pop last item
    last_stage = deployment_stages.pop()
    print(f"\nPopped: {last_stage}")
    print(f"Remaining: {deployment_stages}")


def demonstrate_list_operations() -> None:
    """
    Demonstrates list operations and transformations.
    
    Real-world use case: Data aggregation, sorting, reversing.
    """
    # Example: Server response times (milliseconds)
    response_times: List[int] = [45, 23, 89, 12, 56, 34, 78]
    
    print(f"\nResponse times (ms): {response_times}")
    
    # Sorting
    response_times.sort()
    print(f"Sorted: {response_times}")
    
    # Reverse
    response_times.reverse()
    print(f"Reversed: {response_times}")
    
    # Min/Max
    print(f"\nFastest response: {min(response_times)} ms")
    print(f"Slowest response: {max(response_times)} ms")
    
    # Average (using sum and len)
    avg_response = sum(response_times) / len(response_times)
    print(f"Average response: {avg_response:.1f} ms")


def demonstrate_list_concatenation() -> None:
    """
    Demonstrates list concatenation and repetition.
    
    Real-world use case: Combining data from multiple sources.
    """
    # Example: Combining logs from different services
    service_a_logs: List[str] = ["[A] Request received", "[A] Processing"]
    service_b_logs: List[str] = ["[B] Cache miss", "[B] DB query"]
    
    # Concatenation
    all_logs = service_a_logs + service_b_logs
    print(f"\nCombined logs: {all_logs}")
    
    # Repetition (useful for initialization)
    batch_template: List[None] = [None] * 5
    print(f"\nBatch template: {batch_template}")
    print(f"Length: {len(batch_template)}")


def demonstrate_list_slicing() -> None:
    """
    Demonstrates list slicing for data extraction.
    
    Real-world use case: Pagination, batch processing, windowing.
    """
    # Example: Database query results
    records: List[int] = list(range(1, 21))  # IDs 1-20
    
    print(f"\nAll records: {records}")
    
    # Pagination: First page (5 items)
    page_size = 5
    page_1 = records[0:page_size]
    print(f"Page 1: {page_1}")
    
    # Page 2
    page_2 = records[page_size:page_size*2]
    print(f"Page 2: {page_2}")
    
    # Last 3 items
    recent = records[-3:]
    print(f"Recent 3: {recent}")
    
    # Every other item
    sample = records[::2]
    print(f"Sample (every 2nd): {sample}")


def demonstrate_list_comprehension_preview() -> None:
    """
    Demonstrates basic list transformation (preview of comprehensions).
    
    Real-world use case: Data transformation in pipelines.
    """
    # Example: Extract status codes from log entries
    log_entries = [
        "200 OK /users",
        "404 Not Found /missing",
        "500 Error /broken",
        "200 OK /health"
    ]
    
    # Extract just the status codes
    status_codes: List[str] = []
    for entry in log_entries:
        code = entry.split()[0]
        status_codes.append(code)
    
    print(f"\nLog entries: {len(log_entries)}")
    print(f"Status codes: {status_codes}")


def demonstrate_bytearray() -> None:
    """
    Demonstrates bytearray for mutable byte sequences.
    
    Use cases:
    - Network protocol implementation
    - Binary file manipulation
    - Low-level data processing
    
    Real-world use case: Building network packets, image processing.
    """
    # Example: Building a simple network packet
    packet = bytearray(b"HTTP")
    
    print(f"\nInitial packet: {packet}")
    
    # Modify in place
    packet.extend(b"/1.1")
    print(f"Extended packet: {packet}")
    
    # Replace bytes
    packet = packet.replace(b"HTTP", b"HTTPS")
    print(f"Modified packet: {packet}")
    
    # Convert back to string
    packet_str = packet.decode("utf-8")
    print(f"As string: {packet_str}")


def filter_errors(logs: List[str]) -> List[str]:
    """
    Filters error messages from log list.
    
    Args:
        logs: List of log messages
    
    Returns:
        List containing only error messages
    
    Real-world use case: Log analysis, error monitoring.
    """
    errors: List[str] = []
    for log in logs:
        if "ERROR" in log or "error" in log.lower():
            errors.append(log)
    return errors


def batch_data(items: List[Any], batch_size: int) -> List[List[Any]]:
    """
    Splits data into batches for processing.
    
    Args:
        items: List of items to batch
        batch_size: Number of items per batch
    
    Returns:
        List of batches
    
    Real-world use case: ML batch processing, API rate limiting.
    """
    batches: List[List[Any]] = []
    for i in range(0, len(items), batch_size):
        batch = items[i:i + batch_size]
        batches.append(batch)
    return batches


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON LISTS: DYNAMIC MUTABLE SEQUENCES".center(70))
    print("="*70)
    
    print("\n[1] LIST MUTABILITY")
    print("-" * 70)
    demonstrate_list_mutability()
    
    print("\n\n[2] LIST METHODS")
    print("-" * 70)
    demonstrate_list_methods()
    
    print("\n\n[3] LIST OPERATIONS")
    print("-" * 70)
    demonstrate_list_operations()
    
    print("\n\n[4] LIST CONCATENATION")
    print("-" * 70)
    demonstrate_list_concatenation()
    
    print("\n\n[5] LIST SLICING")
    print("-" * 70)
    demonstrate_list_slicing()
    
    print("\n\n[6] LIST TRANSFORMATION")
    print("-" * 70)
    demonstrate_list_comprehension_preview()
    
    print("\n\n[7] BYTEARRAY")
    print("-" * 70)
    demonstrate_bytearray()
    
    print("\n\n[8] PRACTICAL EXAMPLES")
    print("-" * 70)
    
    # Error filtering
    sample_logs = [
        "INFO: Server started",
        "ERROR: Connection failed",
        "INFO: Request processed",
        "ERROR: Timeout occurred"
    ]
    errors = filter_errors(sample_logs)
    print(f"Total logs: {len(sample_logs)}")
    print(f"Errors found: {errors}")
    
    # Batch processing
    data_points = list(range(1, 26))  # 25 items
    batches = batch_data(data_points, batch_size=10)
    print(f"\nBatching {len(data_points)} items:")
    for i, batch in enumerate(batches, 1):
        print(f"  Batch {i}: {len(batch)} items - {batch}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Lists are mutable - modify in place (unlike tuples)")
    print("2. append(), extend(), insert() for adding elements")
    print("3. pop(), remove() for removing elements")
    print("4. sort(), reverse() modify list in place")
    print("5. Slicing creates new list, useful for pagination")
    print("6. Bytearray for mutable byte sequences")
    print("="*70)


if __name__ == "__main__":
    main()