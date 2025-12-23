"""
Python Walrus Operator (:=) in Loops
=====================================

Topic: Assignment expressions (walrus operator) in Python 3.8+

Real-World Applications:
- Inline data processing in loops
- Reducing redundant computations
- File processing with dynamic conditions
- API response parsing
- Stream processing
"""

from typing import List, Optional, Dict


def process_api_responses_efficient(responses: List[Dict]) -> List[Dict]:
    """
    Processes API responses using walrus operator for efficiency.
    
    Args:
        responses: List of API response dictionaries
    
    Returns:
        List of processed responses
    
    Real-world use case: API integration, response validation.
    """
    processed = []
    
    print("\nProcessing API responses with walrus operator")
    print("-" * 60)
    
    for response in responses:
        # Walrus operator: assign and use in same expression
        if (status := response.get('status')) == 'success':
            print(f"  ✓ Response {response.get('id')}: {status}")
            processed.append(response)
        else:
            print(f"  ✗ Response {response.get('id')}: {status}")
    
    return processed


def filter_large_files(files: List[Dict], threshold_mb: int = 10) -> List[str]:
    """
    Filters files above size threshold using walrus operator.
    
    Args:
        files: List of file dictionaries
        threshold_mb: Size threshold in MB
    
    Returns:
        List of large filenames
    
    Real-world use case: Storage management, cleanup scripts.
    """
    large_files = []
    
    print(f"\nFinding files larger than {threshold_mb}MB")
    print("-" * 60)
    
    for file in files:
        # Calculate size once, use in both condition and print
        if (size_mb := file['size_bytes'] / (1024 * 1024)) > threshold_mb:
            filename = file['name']
            print(f"  📁 {filename}: {size_mb:.1f}MB")
            large_files.append(filename)
    
    return large_files


def parse_log_stream(log_lines: List[str]) -> List[str]:
    """
    Parses log stream, extracting error codes using walrus.
    
    Args:
        log_lines: List of log lines
    
    Returns:
        List of error messages
    
    Real-world use case: Log analysis, real-time monitoring.
    """
    errors = []
    
    print("\nParsing log stream for errors")
    print("-" * 60)
    
    for line in log_lines:
        # Extract and check status code in one expression
        if (code := extract_status_code(line)) and code >= 400:
            print(f"  {code}: {line}")
            errors.append(line)
    
    return errors


def extract_status_code(log_line: str) -> Optional[int]:
    """Helper to extract HTTP status code from log line."""
    parts = log_line.split()
    for part in parts:
        if part.isdigit() and 100 <= int(part) <= 599:
            return int(part)
    return None


def batch_process_with_progress(items: List[Dict], batch_size: int = 5) -> int:
    """
    Processes items in batches with progress tracking using walrus.
    
    Args:
        items: Items to process
        batch_size: Batch size
    
    Returns:
        Total items processed
    
    Real-world use case: ETL pipelines, data processing.
    """
    total = 0
    
    print(f"\nBatch processing {len(items)} items")
    print("-" * 60)
    
    for i in range(0, len(items), batch_size):
        # Slice and process batch in one expression
        if (batch := items[i:i + batch_size]):
            batch_count = len(batch)
            print(f"  Processing batch of {batch_count} items...")
            total += batch_count
    
    return total


def find_and_process_match(data: List[Dict], criteria: str) -> Optional[Dict]:
    """
    Finds first match and processes it using walrus.
    
    Args:
        data: List of data dictionaries
        criteria: Matching criteria
    
    Returns:
        Processed matching item or None
    
    Real-world use case: Database queries, search operations.
    """
    print(f"\nSearching for: {criteria}")
    print("-" * 60)
    
    for item in data:
        # Find and assign match in condition
        if (match := item.get('category')) == criteria:
            # match variable available here
            print(f"  ✓ Found match: {item.get('name')} ({match})")
            return {**item, 'processed': True}
    
    print(f"  ✗ No match found for: {criteria}")
    return None


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("WALRUS OPERATOR (:=) IN LOOPS (Python 3.8+)".center(70))
    print("="*70)
    
    print("\n[1] API RESPONSE PROCESSING")
    print("-" * 70)
    
    api_responses = [
        {"id": 1, "status": "success", "data": {}},
        {"id": 2, "status": "error", "data": None},
        {"id": 3, "status": "success", "data": {}},
    ]
    
    valid = process_api_responses_efficient(api_responses)
    print(f"\nProcessed {len(valid)}/{len(api_responses)} successful responses")
    
    print("\n\n[2] LARGE FILE FILTERING")
    print("-" * 70)
    
    files_list = [
        {"name": "small.txt", "size_bytes": 1024 * 1024 * 2},  # 2MB
        {"name": "large_video.mp4", "size_bytes": 1024 * 1024 * 150},  # 150MB
        {"name": "backup.zip", "size_bytes": 1024 * 1024 * 50},  # 50MB
        {"name": "config.json", "size_bytes": 1024 * 100},  # 100KB
    ]
    
    large = filter_large_files(files_list, threshold_mb=10)
    print(f"\nFound {len(large)} large files")
    
    print("\n\n[3] LOG STREAM PARSING")
    print("-" * 70)
    
    logs = [
        "2024-12-05 10:00:00 200 GET /users",
        "2024-12-05 10:01:00 404 GET /missing",
        "2024-12-05 10:02:00 500 POST /api/data",
        "2024-12-05 10:03:00 200 GET /health",
    ]
    
    error_logs = parse_log_stream(logs)
    print(f"\nFound {len(error_logs)} error entries")
    
    print("\n\n[4] BATCH PROCESSING WITH PROGRESS")
    print("-" * 70)
    
    items_to_process = [{"id": i} for i in range(1, 13)]
    total_processed = batch_process_with_progress(items_to_process, batch_size=5)
    print(f"\nTotal processed: {total_processed} items")
    
    print("\n\n[5] FIND AND PROCESS MATCH")
    print("-" * 70)
    
    products = [
        {"name": "Laptop", "category": "electronics"},
        {"name": "Desk", "category": "furniture"},
        {"name": "Mouse", "category": "electronics"},
    ]
    
    result = find_and_process_match(products, criteria="electronics")
    if result:
        print(f"\nProcessed: {result}")
    
    print("\n\n[6] TRADITIONAL vs WALRUS COMPARISON")
    print("-" * 70)
    
    print("\nWithout walrus operator:")
    print("  response = api_call()")
    print("  if response.status == 'success':")
    print("      process(response)")
    
    print("\nWith walrus operator:")
    print("  if (response := api_call()).status == 'success':")
    print("      process(response)")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. := allows assignment within expressions (Python 3.8+)")
    print("2. Reduces code duplication and improves readability")
    print("3. Useful in loops, comprehensions, and conditionals")
    print("4. Variable persists after the expression")
    print("5. Makes code more concise without sacrificing clarity")
    print("="*70)


if __name__ == "__main__":
    main()