"""
Python For Loops: zip() for Parallel Iteration
===============================================

Topic: zip() function for iterating multiple sequences simultaneously

Real-World Applications:
- Combining data from multiple sources
- Parallel processing of related datasets
- Merging API responses
- Coordinated data updates
- Report generation from multiple data streams
"""

from typing import List, Dict, Tuple


def merge_user_data(
    ids: List[int],
    usernames: List[str],
    emails: List[str]
) -> List[Dict[str, any]]:
    """
    Merges related user data from separate lists.
    
    Args:
        ids: User IDs
        usernames: Usernames
        emails: Email addresses
    
    Returns:
        List of user dictionaries
    
    Real-world use case: Combining data from multiple database queries.
    """
    users = []
    
    for user_id, username, email in zip(ids, usernames, emails):
        user = {
            "id": user_id,
            "username": username,
            "email": email
        }
        users.append(user)
    
    return users


def calculate_transaction_totals(
    items: List[str],
    quantities: List[int],
    prices: List[float]
) -> List[Tuple[str, int, float, float]]:
    """
    Calculates totals for each transaction item.
    
    Args:
        items: Item names
        quantities: Quantities purchased
        prices: Unit prices
    
    Returns:
        List of (item, quantity, unit_price, total) tuples
    
    Real-world use case: E-commerce cart total calculation.
    """
    transactions = []
    
    for item, qty, price in zip(items, quantities, prices):
        total = qty * price
        transactions.append((item, qty, price, total))
    
    return transactions


def compare_metrics_over_time(
    dates: List[str],
    api_requests: List[int],
    errors: List[int],
    response_times: List[float]
) -> None:
    """
    Compares multiple metrics across time periods.
    
    Args:
        dates: Date strings
        api_requests: Request counts
        errors: Error counts
        response_times: Average response times
    
    Real-world use case: Performance monitoring dashboards.
    """
    print("\nPerformance Metrics Over Time")
    print("-" * 70)
    print(f"{'Date':12} | {'Requests':>8} | {'Errors':>6} | {'Avg Response':>12}")
    print("-" * 70)
    
    for date, requests, error_count, avg_time in zip(dates, api_requests, errors, response_times):
        error_rate = (error_count / requests * 100) if requests > 0 else 0
        print(f"{date:12} | {requests:>8} | {error_count:>6} | {avg_time:>10.0f}ms")


def sync_database_records(
    local_ids: List[int],
    remote_ids: List[int],
    local_hashes: List[str],
    remote_hashes: List[str]
) -> List[int]:
    """
    Identifies records that need syncing between databases.
    
    Args:
        local_ids: Local database IDs
        remote_ids: Remote database IDs
        local_hashes: Local record hashes
        remote_hashes: Remote record hashes
    
    Returns:
        List of IDs that need syncing
    
    Real-world use case: Database synchronization, data replication.
    """
    needs_sync = []
    
    print("\nDatabase Synchronization Check")
    print("-" * 60)
    
    for local_id, remote_id, local_hash, remote_hash in zip(
        local_ids, remote_ids, local_hashes, remote_hashes
    ):
        if local_hash != remote_hash:
            needs_sync.append(local_id)
            print(f"  Record {local_id}: OUT OF SYNC")
        else:
            print(f"  Record {local_id}: ✓ Synced")
    
    return needs_sync


def create_api_request_batch(
    endpoints: List[str],
    methods: List[str],
    payloads: List[Dict]
) -> List[Dict]:
    """
    Creates batch of API requests from separate lists.
    
    Args:
        endpoints: API endpoints
        methods: HTTP methods
        payloads: Request payloads
    
    Returns:
        List of request dictionaries
    
    Real-world use case: Bulk API operations, batch processing.
    """
    requests = []
    
    for endpoint, method, payload in zip(endpoints, methods, payloads):
        request = {
            "url": endpoint,
            "method": method,
            "data": payload
        }
        requests.append(request)
    
    return requests


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("FOR LOOPS: zip() FOR PARALLEL ITERATION".center(70))
    print("="*70)
    
    print("\n[1] MERGING USER DATA FROM MULTIPLE SOURCES")
    print("-" * 70)
    
    user_ids = [101, 102, 103, 104]
    usernames = ["alice", "bob", "charlie", "diana"]
    user_emails = ["alice@example.com", "bob@example.com", 
                   "charlie@example.com", "diana@example.com"]
    
    merged_users = merge_user_data(user_ids, usernames, user_emails)
    
    print("\nMerged user data:")
    for user in merged_users:
        print(f"  ID: {user['id']}, Username: {user['username']}, Email: {user['email']}")
    
    print("\n\n[2] TRANSACTION TOTAL CALCULATION")
    print("-" * 70)
    
    cart_items = ["Laptop", "Mouse", "Keyboard", "Monitor"]
    quantities = [1, 2, 1, 1]
    unit_prices = [999.99, 29.99, 79.99, 299.99]
    
    transactions = calculate_transaction_totals(cart_items, quantities, unit_prices)
    
    print("\nOrder Summary:")
    print(f"{'Item':12} | {'Qty':>3} | {'Unit Price':>10} | {'Total':>10}")
    print("-" * 50)
    
    grand_total = 0
    for item, qty, price, total in transactions:
        print(f"{item:12} | {qty:>3} | ${price:>9.2f} | ${total:>9.2f}")
        grand_total += total
    
    print("-" * 50)
    print(f"{'GRAND TOTAL':>28} | ${grand_total:>9.2f}")
    
    print("\n\n[3] PERFORMANCE METRICS COMPARISON")
    print("-" * 70)
    
    dates = ["2024-12-01", "2024-12-02", "2024-12-03", "2024-12-04"]
    requests_per_day = [10000, 12000, 11500, 13000]
    errors_per_day = [50, 120, 80, 95]
    avg_response_times = [150, 180, 165, 155]
    
    compare_metrics_over_time(dates, requests_per_day, errors_per_day, avg_response_times)
    
    print("\n\n[4] DATABASE SYNCHRONIZATION")
    print("-" * 70)
    
    local_record_ids = [1, 2, 3, 4, 5]
    remote_record_ids = [1, 2, 3, 4, 5]
    local_hash_values = ["abc123", "def456", "ghi789", "jkl012", "mno345"]
    remote_hash_values = ["abc123", "MODIFIED", "ghi789", "jkl012", "MODIFIED"]
    
    out_of_sync = sync_database_records(
        local_record_ids, remote_record_ids,
        local_hash_values, remote_hash_values
    )
    
    print(f"\n{len(out_of_sync)}/{len(local_record_ids)} records need syncing: {out_of_sync}")
    
    print("\n\n[5] BATCH API REQUEST CREATION")
    print("-" * 70)
    
    api_endpoints = ["/users/1", "/users/2", "/users/3"]
    http_methods = ["GET", "PUT", "DELETE"]
    request_payloads = [{}, {"name": "Updated"}, {}]
    
    batch_requests = create_api_request_batch(api_endpoints, http_methods, request_payloads)
    
    print("\nBatch API requests:")
    for i, req in enumerate(batch_requests, 1):
        print(f"  Request {i}: {req['method']} {req['url']}")
        if req['data']:
            print(f"    Data: {req['data']}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. zip() combines multiple iterables into tuples")
    print("2. Stops when shortest iterable is exhausted")
    print("3. Use zip_longest() from itertools for different lengths")
    print("4. Perfect for parallel data processing")
    print("5. Can zip any number of iterables: zip(a, b, c, d, ...)")
    print("="*70)


if __name__ == "__main__":
    main()