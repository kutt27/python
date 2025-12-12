"""
Python For Loops: Iterating Over Collections
=============================================

Topic: for loops with lists, iterating over sequences

Real-World Applications:
- Processing database query rests
- Handling API response arrays
- Log file analysis
- Email/notification dispatch
- Data transformation in pipelines
"""

from typing import List, Dict, Tuple


def process_database_results(records: List[Dict]) -> None:
    """
    Processes database query results.
    
    Args:
        records: List of database records
    
    Real-world use case: ORM result processing, data validation.
    """
    print(f"\nProcessing {len(records)} database records")
    print("-" * 60)
    
    for record in records:
        user_id = record.get("id")
        username = record.get("username")
        status = record.get("status", "unknown")
        
        # Process each record
        print(f"User {user_id}: {username} (Status: {status})")


def send_notifications(users: List[str], message: str) -> List[Tuple[str, bool]]:
    """
    Sends notifications to list of users.
    
    Args:
        users: List of usernames/emails
        message: Notification message
    
    Returns:
        List of (user, success) tuples
    
    Real-world use case: Bulk email sending, push notifications.
    """
    results = []
    
    print(f"\nSending notification: '{message}'")
    print("-" * 60)
    
    for user in users:
        # Simulate sending notification
        print(f"  → Sending to {user}")
        
        # Simulate success/failure
        success = len(user) > 0  # Simplified
        results.append((user, success))
    
    return results


def analyze_api_errors(error_logs: List[str]) -> Dict[str, int]:
    """
    Analyzes API error logs and counts error types.
    
    Args:
        error_logs: List of error log messages
    
    Returns:
        Dictionary of error type counts
    
    Real-world use case: Log analysis, error monitoring.
    """
    error_counts: Dict[str, int] = {}
    
    for log in error_logs:
        # Extract error type (simplified)
        if "Timeout" in log:
            error_counts["Timeout"] = error_counts.get("Timeout", 0) + 1
        elif "404" in log:
            error_counts["NotFound"] = error_counts.get("NotFound", 0) + 1
        elif "500" in log:
            error_counts["ServerError"] = error_counts.get("ServerError", 0) + 1
        else:
            error_counts["Other"] = error_counts.get("Other", 0) + 1
    
    return error_counts


def transform_user_data(raw_data: List[Dict]) -> List[Dict]:
    """
    Transforms raw user data for API response.
    
    Args:
        raw_data: Raw database records
    
    Returns:
        Transformed data for API
    
    Real-world use case: Data transformation, API serialization.
    """
    transformed = []
    
    for record in raw_data:
        # Transform each record
        transformed_record = {
            "id": record.get("user_id"),
            "name": record.get("full_name", "").title(),
            "email": record.get("email_address", "").lower(),
            "active": record.get("status") == "active"
        }
        transformed.append(transformed_record)
    
    return transformed


def filter_valid_orders(orders: List[Dict]) -> List[Dict]:
    """
    Filters list to keep only valid orders.
    
    Args:
        orders: List of order dictionaries
    
    Returns:
        List of valid orders
    
    Real-world use case: Data validation, order processing.
    """
    valid_orders = []
    
    print(f"\nFiltering {len(orders)} orders")
    print("-" * 60)
    
    for order in orders:
        order_id = order.get("id")
        amount = order.get("amount", 0)
        status = order.get("status")
        
        # Validation rules
        is_valid = (
            amount > 0 and
            status in ["pending", "processing", "completed"] and
            order_id is not None
        )
        
        if is_valid:
            valid_orders.append(order)
            print(f"  ✓ Order {order_id}: ${amount:.2f} ({status})")
        else:
            print(f"  ✗ Order {order_id}: INVALID")
    
    return valid_orders


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("FOR LOOPS: ITERATING OVER COLLECTIONS".center(70))
    print("="*70)
    
    print("\n[1] DATABASE QUERY RESULTS")
    print("-" * 70)
    
    db_records = [
        {"id": 1, "username": "alice", "status": "active"},
        {"id": 2, "username": "bob", "status": "inactive"},
        {"id": 3, "username": "charlie", "status": "active"},
    ]
    
    process_database_results(db_records)
    
    print("\n\n[2] BULK NOTIFICATIONS")
    print("-" * 70)
    
    users = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    results = send_notifications(users, "System maintenance tonight at 2 AM")
    
    successful = sum(1 for _, success in results if success)
    print(f"\nSent {successful}/{len(results)} notifications successfully")
    
    print("\n\n[3] ERROR LOG ANALYSIS")
    print("-" * 70)
    
    logs = [
        "2024-12-05 ERROR: Timeout connecting to database",
        "2024-12-05 ERROR: 404 Not Found /api/users/999",
        "2024-12-05 ERROR: 500 Internal Server Error",
        "2024-12-05 ERROR: Timeout on external API call",
        "2024-12-05 ERROR: 404 Not Found /api/products/123",
    ]
    
    error_summary = analyze_api_errors(logs)
    print(f"\nAnalyzed {len(logs)} error logs:")
    for error_type, count in error_summary.items():
        print(f"  {error_type}: {count}")
    
    print("\n\n[4] DATA TRANSFORMATION")
    print("-" * 70)
    
    raw_user_data = [
        {"user_id": 1, "full_name": "alice smith", "email_address": "ALICE@EXAMPLE.COM", "status": "active"},
        {"user_id": 2, "full_name": "bob jones", "email_address": "bob@EXAMPLE.com", "status": "inactive"},
    ]
    
    transformed_data = transform_user_data(raw_user_data)
    print("\nTransformed data:")
    for user in transformed_data:
        print(f"  {user}")
    
    print("\n\n[5] ORDER VALIDATION")
    print("-" * 70)
    
    orders = [
        {"id": "ORD-001", "amount": 99.99, "status": "completed"},
        {"id": "ORD-002", "amount": 0, "status": "pending"},  # Invalid: zero amount
        {"id": "ORD-003", "amount": 49.99, "status": "cancelled"},  # Invalid: cancelled status
        {"id": "ORD-004", "amount": 149.99, "status": "processing"},
    ]
    
    valid = filter_valid_orders(orders)
    print(f"\n{len(valid)}/{len(orders)} orders are valid")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. for item in collection: iterates over each element")
    print("2. Works with lists, tuples, strings, dictionaries, sets")
    print("3. Use enumerate() to get index: for i, item in enumerate(list)")
    print("4. Use zip() to iterate multiple lists: for a, b in zip(list1, list2)")
    print("5. Dictionary iteration: for key, value in dict.items()")
    print("="*70)


if __name__ == "__main__":
    main()