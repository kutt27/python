"""
Python Generator Expressions
=============================

Topic: Generator expressions for memory-efficient iteration

Real-World Applications:
- Large dataset processing
- Log file analysis
- Stream processing
- Memory-efficient filtering
- Lazy evaluation pipelines
"""

from typing import Generator
import sys


def main() -> None:
    """Main function demonstrating generator expressions."""
    print("="*70)
    print("GENERATOR EXPRESSIONS".center(70))
    print("="*70)
    
    print("\n[1] BASIC GENERATOR - Memory Efficiency")
    print("-" * 70)
    
    # List comprehension - creates entire list in memory
    numbers_list = [x**2 for x in range(1000000)]
    
    # Generator expression - computes values on-demand
    numbers_gen = (x**2 for x in range(1000000))
    
    print(f"List size: {sys.getsizeof(numbers_list):,} bytes")
    print(f"Generator size: {sys.getsizeof(numbers_gen):,} bytes")
    print(f"Memory savings: {(1 - sys.getsizeof(numbers_gen)/sys.getsizeof(numbers_list))*100:.1f}%")
    
    del numbers_list  # Free memory
    
    print("\n\n[2] LAZY EVALUATION - Sum Calculation")
    print("-" * 70)
    
    # Generator doesn't compute until consumed
    large_numbers = (x**2 for x in range(10))
    
    print("Generator created (nothing computed yet)")
    print(f"  Generator object: {large_numbers}")
    
    # Compute sum (consumes generator)
    total = sum(large_numbers)
    print(f"\nSum computed: {total}")
    
    # Generator is exhausted
    print(f"Generator exhausted: {list(large_numbers)}")
    
    print("\n\n[3] FILTERING LARGE LOGS")
    print("-" * 70)
    
    # Simulate large log file
    log_lines = [
        "INFO: Server started at 10:00",
        "ERROR: Database connection failed",
        "INFO: Request received from 192.168.1.1",
        "ERROR: Timeout after 30 seconds",
        "INFO: Response sent successfully",
        "ERROR: Invalid authentication token",
    ]
    
    # Generator for error logs only
    error_logs = (
        line
        for line in log_lines
        if "ERROR" in line
    )
    
    print("Processing error logs:")
    for error in error_logs:
        print(f"  {error}")
    
    print("\n\n[4] DATA TRANSFORMATION PIPELINE")
    print("-" * 70)
    
    # Raw sensor data
    sensor_readings = [10.5, 22.3, 15.8, 30.2, 18.9, 25.1]
    
    # Multi-stage pipeline using generators
    # Step 1: Convert Celsius to Fahrenheit
    fahrenheit = (temp * 9/5 + 32 for temp in sensor_readings)
    
    # Step 2: Round to 1 decimal
    rounded = (round(temp, 1) for temp in fahrenheit)
    
    # Step 3: Filter (keep readings > 60°F)
    filtered = (temp for temp in rounded if temp > 60)
    
    # Nothing computed until we iterate
    print("Processing pipeline (Celsius → Fahrenheit → round → filter > 60°F):")
    for temp in filtered:
        print(f"  {temp}°F")
    
    print("\n\n[5] BATCH PROCESSING")
    print("-" * 70)
    
    # Process user IDs in batches
    user_ids = range(1, 21)  # 20 users
    batch_size = 5
    
    # Generator for batch processing
    def batch_generator(items, size):
        """Yields batches of items."""
        items_list = list(items)
        for i in range(0, len(items_list), size):
            yield items_list[i:i + size]
    
    print(f"Processing {len(list(user_ids))} users in batches of {batch_size}:")
    for batch_num, batch in enumerate(batch_generator(range(1, 21), batch_size), 1):
        print(f"  Batch {batch_num}: {list(batch)}")
    
    print("\n\n[6] INFINITE SEQUENCE")
    print("-" * 70)
    
    def fibonacci_gen():
        """Generates Fibonacci sequence indefinitely."""
        a, b = 0, 1
        while True:
            yield a
            a, b = b, a + b
    
    # Take first 10 Fibonacci numbers
    fib_gen = fibonacci_gen()
    first_10_fib = [next(fib_gen) for _ in range(10)]
    
    print(f"First 10 Fibonacci numbers: {first_10_fib}")
    
    print("\n\n[7] API PAGINATION SIMULATION")
    print("-" * 70)
    
    def paginated_api_results(total_items, page_size):
        """Simulates paginated API responses."""
        for page in range(1, (total_items // page_size) + 2):
            start = (page - 1) * page_size
            end = min(start + page_size, total_items)
            
            if start >= total_items:
                break
            
            # Simulate API call
            yield {
                "page": page,
                "items": list(range(start + 1, end + 1)),
                "total": total_items
            }
    
    print("Fetching paginated results (50 items, 15 per page):")
    for response in paginated_api_results(total_items=50, page_size=15):
        print(f"  Page {response['page']}: {len(response['items'])} items")
    
    print("\n\n[8] CSV ROW PROCESSING")
    print("-" * 70)
    
    # Simulate CSV rows
    csv_data = [
        "name,age,city",
        "Alice,30,NYC",
        "Bob,25,LA",
        "Charlie,35,Chicago",
    ]
    
    # Generator to parse CSV (skip header)
    parsed_rows = (
        dict(zip(csv_data[0].split(','), row.split(',')))
        for row in csv_data[1:]
    )
    
    print("Parsed CSV data:")
    for row in parsed_rows:
        print(f"  {row}")
    
    print("\n\n[9] CHAINING GENERATORS")
    print("-" * 70)
    
    # Multiple data sources
    source1 = [1, 2, 3]
    source2 = [4, 5, 6]
    source3 = [7, 8, 9]
    
    # Chain generators
    def chain_generators(*iterables):
        """Chains multiple iterables into single generator."""
        for iterable in iterables:
            for item in iterable:
                yield item
    
    # Or use generator expression
    chained = (item for source in [source1, source2, source3] for item in source)
    
    print(f"Chained results: {list(chained)}")
    
    print("\n\n[10] CONDITIONAL GENERATOR - File Filtering")
    print("-" * 70)
    
    files = [
        "document.pdf",
        "image.jpg",
        "presentation.pptx",
        "data.csv",
        "photo.png",
        "report.pdf",
    ]
    
    # Generator for PDFs only
    pdf_files = (f for f in files if f.endswith('.pdf'))
    
    # Generator for images
    image_files = (f for f in files if f.endswith(('.jpg', '.png')))
    
    print(f"PDF files: {list(pdf_files)}")
    
    # Note: pdf_files generator is exhausted, create new one for images
    image_files_new = (f for f in files if f.endswith(('.jpg', '.png')))
    print(f"Image files: {list(image_files_new)}")
    
    print("\n" + "="*70)
    print("Generator Expression Syntax:")
    print("-" * 70)
    print("(expression for item in iterable if condition)")
    print("\nList vs Generator:")
    print("  [x**2 for x in range(1000)]  # List - all in memory")
    print("  (x**2 for x in range(1000))  # Generator - lazy evaluation")
    print("\nKey Characteristics:")
    print("• Memory efficient - computes values on-demand")
    print("• Single-use - exhausted after iteration")
    print("• Lazy evaluation - nothing computed until consumed")
    print("• Can represent infinite sequences")
    print("\nWhen to Use:")
    print("✓ Large datasets that don't fit in memory")
    print("✓ Pipeline transformations")
    print("✓ Stream processing")
    print("✓ When you only iterate once")
    print("\nWhen to Use List Instead:")
    print("✗ Need to iterate multiple times")
    print("✗ Need indexing/slicing")
    print("✗ Need len() or other list operations")
    print("="*70)


if __name__ == "__main__":
    main()