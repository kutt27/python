"""
Python Loop Control: break and continue
========================================

Topic: break and continue statements for loop control

Real-World Applications:
- Early termination on error/success
- Skipping invalid data
- Optimized search operations
- Filtering during processing
- Circuit breaker patterns
"""

from typing import List, Optional, Dict


def find_user_by_id(users: List[Dict], target_id: int) -> Optional[Dict]:
    """
    Searches for user and stops when found (break pattern).
    
    Args:
        users: List of user dictionaries
        target_id: User ID to find
    
    Returns:
        User dictionary if found, None otherwise
    
    Real-world use case: Database search optimization, early exit.
    """
    print(f"\nSearching for user ID: {target_id}")
    print("-" * 60)
    
    for user in users:
        print(f"  Checking user {user['id']}...")
        
        if user['id'] == target_id:
            print(f"  ✓ Found: {user['name']}")
            return user  # Early exit - no need to check remaining users
    
    print(f"  ✗ User {target_id} not found")
    return None


def process_batch_with_skip(items: List[Dict]) -> List[Dict]:
    """
    Processes batch, skipping invalid items (continue pattern).
    
    Args:
        items: List of items to process
    
    Returns:
        List of successfully processed items
    
    Real-world use case: ETL pipelines, data validation.
    """
    processed = []
    
    print(f"\nProcessing batch of {len(items)} items")
    print("-" * 60)
    
    for item in items:
        item_id = item.get('id')
        
        # Skip invalid items
        if not item.get('valid', True):
            print(f"  ⊘ Skipping invalid item: {item_id}")
            continue  # Skip to next iteration
        
        if not item.get('amount', 0) > 0:
            print(f"  ⊘ Skipping zero-amount item: {item_id}")
            continue
        
        # Process valid item
        print(f"  ✓ Processing item: {item_id}")
        processed.append(item)
    
    return processed


def check_service_health(services: List[str]) -> tuple[bool, Optional[str]]:
    """
    Checks services health, stops on first failure (break pattern).
    
    Args:
        services: List of service names
    
    Returns:
        Tuple of (all_healthy, failed_service)
    
    Real-world use case: Health check monitoring, startup validation.
    """
    print(f"\nChecking health of {len(services)} services")
    print("-" * 60)
    
    for service in services:
        # Simulate health check
        is_healthy = "cache" not in service.lower()  # Simplified: cache service fails
        
        if is_healthy:
            print(f"  ✓ {service}: Healthy")
        else:
            print(f"  ✗ {service}: FAILED")
            return (False, service)  # Stop checking on first failure
    
    return (True, None)


def filter_and_process_logs(log_lines: List[str]) -> List[str]:
    """
    Filters logs, skipping noise and stopping on critical errors.
    
    Args:
        log_lines: List of log messages
    
    Returns:
        List of processed error logs
    
    Real-world use case: Log processing, error detection.
    """
    errors = []
    
    print(f"\nProcessing {len(log_lines)} log lines")
    print("-" * 60)
    
    for line in log_lines:
        # Skip debug/info messages (continue)
        if "DEBUG" in line or "INFO" in line:
            continue
        
        # Stop on critical error (break)
        if "CRITICAL" in line:
            print(f"  🛑 CRITICAL ERROR FOUND - stopping processing")
            print(f"     {line}")
            break
        
        # Process errors/warnings
        if "ERROR" in line or "WARNING" in line:
            print(f"  ⚠  {line}")
            errors.append(line)
    
    return errors


def process_paginated_api(max_pages: int = 10) -> int:
    """
    Processes paginated API results, stops when no more data.
    
    Args:
        max_pages: Maximum pages to fetch
    
    Returns:
        Total items processed
    
    Real-world use case: API pagination handling.
    """
    total_items = 0
    page = 1
    
    print(f"\nFetching paginated API data (max {max_pages} pages)")
    print("-" * 60)
    
    while page <= max_pages:
        # Simulate API call
        items_in_page = 20 if page < 5 else 0  # No more data after page 4
        
        if items_in_page == 0:
            print(f"  Page {page}: No more data - stopping")
            break  # No more pages to fetch
        
        print(f"  Page {page}: Fetched {items_in_page} items")
        total_items += items_in_page
        page += 1
    
    return total_items


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("LOOP CONTROL: break and continue".center(70))
    print("="*70)
    
    print("\n[1] EARLY EXIT WITH break - User Search")
    print("-" * 70)
    
    users = [
        {"id": 101, "name": "Alice"},
        {"id": 102, "name": "Bob"},
        {"id": 103, "name": "Charlie"},
        {"id": 104, "name": "Diana"},
    ]
    
    found = find_user_by_id(users, target_id=102)
    print(f"\nResult: {found}")
    
    print("\n\n[2] SKIP INVALID ITEMS WITH continue - Batch Processing")
    print("-" * 70)
    
    batch = [
        {"id": "ITEM-1", "amount": 100, "valid": True},
        {"id": "ITEM-2", "amount": 0, "valid": True},  # Invalid: zero amount
        {"id": "ITEM-3", "amount": 50, "valid": False},  # Invalid: not valid
        {"id": "ITEM-4", "amount": 75, "valid": True},
    ]
    
    processed = process_batch_with_skip(batch)
    print(f"\nProcessed {len(processed)}/{len(batch)} items successfully")
    
    print("\n\n[3] HEALTH CHECK WITH break - Stop on First Failure")
    print("-" * 70)
    
    service_list = ["API", "Database", "Cache", "Queue"]
    all_healthy, failed = check_service_health(service_list)
    
    if all_healthy:
        print("\n✓ All services healthy")
    else:
        print(f"\n✗ Service failure detected: {failed}")
    
    print("\n\n[4] LOG PROCESSING - Skip and Stop")
    print("-" * 70)
    
    logs = [
        "INFO: Server started",
        "DEBUG: Loading configuration",
        "ERROR: Database connection timeout",
        "WARNING: High memory usage",
        "CRITICAL: System failure - shutting down",
        "ERROR: This won't be processed",
    ]
    
    error_logs = filter_and_process_logs(logs)
    print(f"\nCollected {len(error_logs)} error/warning logs before critical failure")
    
    print("\n\n[5] PAGINATED API Processing")
    print("-" * 70)
    
    total = process_paginated_api(max_pages=10)
    print(f"\nTotal items fetched: {total}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. break: Exits the loop immediately")
    print("2. continue: Skips remaining code and starts next iteration")
    print("3. Use break for early exit (found result, error occurred)")
    print("4. Use continue to skip invalid/unwanted items")
    print("5. Improves performance by avoiding unnecessary work")
    print("="*70)


if __name__ == "__main__":
    main()