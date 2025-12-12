"""
Python Integer Operations and Arithmetic
=========================================

Topic: Integer data type, arithmetic operations, and numeric computations

Real-World Applications:
- Financial calculations in payment processing
- Metric aggregation in analytics systems
- Resource allocation in cloud infrastructure
- Batch size calculations in ML training pipelines
"""

from typing import Tuple


def demonstrate_basic_arithmetic() -> None:
    """
    Demonstrates fundamental arithmetic operations with integers.
    
    Real-world use case: Calculating resource usage and costs in cloud systems.
    """
    # Example: Cloud resource calculation
    cpu_cores_server1 = 16
    cpu_cores_server2 = 8
    
    # Addition: Total resources
    total_cores = cpu_cores_server1 + cpu_cores_server2
    print(f"Total CPU cores across servers: {total_cores}")
    
    # Subtraction: Available resources
    reserved_cores = 10
    available_cores = total_cores - reserved_cores
    print(f"Available cores after reservation: {available_cores}")
    
    # Division (float result)
    users_count = 1000
    servers_count = 4
    users_per_server = users_count / servers_count
    print(f"Average users per server: {users_per_server}")
    
    print(f"\n{'='*60}")
    print("Note: Division (/) always returns a float, even for integers")
    print(f"  Type of {users_per_server}: {type(users_per_server)}")
    print(f"{'='*60}")


def demonstrate_integer_division() -> None:
    """
    Demonstrates floor division and modulo operations.
    
    Critical for:
    - Pagination in APIs
    - Batch processing
    - Load balancing
    - Resource distribution
    
    Real-world use case: Distributing database records across worker processes.
    """
    # Example: Distributing 1000 records across worker processes
    total_records = 1000
    worker_processes = 6
    
    # Floor division: Records per worker (rounded down)
    records_per_worker = total_records // worker_processes
    print(f"\nRecords per worker process: {records_per_worker}")
    print(f"  (Floor division: 1000 // 6 = {records_per_worker})")
    
    # Modulo: Remaining records that don't divide evenly
    remaining_records = total_records % worker_processes
    print(f"Remaining records (unassigned): {remaining_records}")
    print(f"  (Modulo: 1000 % 6 = {remaining_records})")
    
    print(f"\n{'='*60}")
    print("Distribution strategy:")
    print(f"  - {worker_processes - remaining_records} workers get"
          f" {records_per_worker} records")
    print(f"  - {remaining_records} workers get"
          f" {records_per_worker + 1} records")
    print(f"  - Total: {records_per_worker * worker_processes + remaining_records}")
    print(f"{'='*60}")


def calculate_pagination(total_items: int, page_size: int) -> Tuple[int, int]:
    """
    Calculates pagination for API responses.
    
    Args:
        total_items: Total number of items in database
        page_size: Number of items per page
    
    Returns:
        Tuple of (total_pages, items_on_last_page)
    
    Real-world use case: REST API pagination calculation.
    """
    total_pages = (total_items + page_size - 1) // page_size  # Ceiling division
    items_on_last_page = total_items % page_size or page_size
    
    return total_pages, items_on_last_page


def demonstrate_exponentiation() -> None:
    """
    Demonstrates exponentiation for scaling and exponential growth calculations.
    
    Common use cases:
    - Exponential backoff in retry logic
    - Compound interest calculations
    - Scaling factors in ML model complexity
    - Binary tree depth calculations
    """
    # Example: Exponential backoff for API retry logic
    base_delay_seconds = 2
    retry_attempt = 3
    
    # Calculate delay: 2^3 = 8 seconds
    retry_delay = base_delay_seconds ** retry_attempt
    print(f"\nRetry delay for attempt {retry_attempt}: {retry_delay} seconds")
    print(f"  Formula: {base_delay_seconds}^{retry_attempt} = {retry_delay}")
    
    # Example: Data growth estimation
    print(f"\nData growth projection:")
    initial_records = 1000
    growth_rate = 2  # Doubles each period
    
    for period in range(5):
        projected_records = initial_records * (growth_rate ** period)
        print(f"  Period {period}: {projected_records:,} records")


def demonstrate_large_numbers() -> None:
    """
    Demonstrates Python's arbitrary precision integers.
    
    Python can handle integers of any size (limited only by available memory).
    This is crucial for:
    - Cryptographic operations
    - Financial calculations (avoiding floating-point errors)
    - Big data analytics
    - High-precision scientific computing
    """
    # Example: Processing large-scale data metrics
    # Using underscores for readability (Python 3.6+)
    daily_requests = 1_000_000_000  # 1 billion requests/day
    days_in_year = 365
    
    annual_requests = daily_requests * days_in_year
    print(f"\nAnnual API requests: {annual_requests:,}")
    print(f"  Formatted with underscores: {annual_requests:_}")
    
    # Example: Memory calculations
    bytes_per_record = 1024  # 1 KB
    total_records = 10_000_000  # 10 million records
    
    total_bytes = bytes_per_record * total_records
    total_megabytes = total_bytes // (1024 * 1024)
    total_gigabytes = total_megabytes / 1024
    
    print(f"\nDatabase size calculation:")
    print(f"  Records: {total_records:,}")
    print(f"  Total: {total_bytes:,} bytes")
    print(f"  Total: {total_megabytes:,} MB")
    print(f"  Total: {total_gigabytes:.2f} GB")


def demonstrate_numeric_methods() -> None:
    """
    Demonstrates useful integer methods and operations.
    """
    # Example: Status code analysis in web server logs
    status_code = 404
    
    print(f"\nHTTP Status Code: {status_code}")
    print(f"  Bit length: {status_code.bit_length()} bits")
    print(f"  Binary representation: {bin(status_code)}")
    print(f"  Hexadecimal: {hex(status_code)}")
    print(f"  Octal: {oct(status_code)}")
    
    # Absolute value (useful for error calculations)
    error_delta = -42
    absolute_error = abs(error_delta)
    print(f"\nError delta: {error_delta}")
    print(f"Absolute error: {absolute_error}")


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON INTEGERS: ARITHMETIC & OPERATIONS".center(70))
    print("="*70)
    
    print("\n[1] BASIC ARITHMETIC")
    print("-" * 70)
    demonstrate_basic_arithmetic()
    
    print("\n\n[2] FLOOR DIVISION & MODULO")
    print("-" * 70)
    demonstrate_integer_division()
    
    # Pagination example
    print("\n\n[3] PAGINATION CALCULATION")
    print("-" * 70)
    total_items = 1000
    page_size = 25
    pages, last_page_items = calculate_pagination(total_items, page_size)
    print(f"Items: {total_items}, Page size: {page_size}")
    print(f"Result: {pages} pages, {last_page_items} items on last page")
    
    print("\n\n[4] EXPONENTIATION")
    print("-" * 70)
    demonstrate_exponentiation()
    
    print("\n\n[5] LARGE NUMBERS")
    print("-" * 70)
    demonstrate_large_numbers()
    
    print("\n\n[6] NUMERIC METHODS")
    print("-" * 70)
    demonstrate_numeric_methods()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Python integers have arbitrary precision (no overflow)")
    print("2. / always returns float, // returns integer (floor division)")
    print("3. Use underscores for readability: 1_000_000")
    print("4. Modulo (%) is perfect for distribution and pagination")
    print("5. ** operator for exponentiation (2**10 = 1024)")
    print("="*70)


if __name__ == "__main__":
    main()