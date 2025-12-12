"""
Python Return Values: Patterns and Best Practices
==================================================

Topic: Return statements, multiple returns, None, early returns

Real-World Applications:
- API response formatting
- Error handling patterns
- Data transformation pipelines
- Validation result reporting
- Optional value handling
"""

from typing import Optional, Tuple, Dict, List, Any, Union


def find_user_by_email(email: str, users: List[Dict]) -> Optional[Dict]:
    """
    Finds user by email, returns None if not found.
    
    Optional return type pattern for "may not exist" scenarios.
    
    Args:
        email: Email to search for
        users: List of user dictionaries
    
    Returns:
        User dictionary or None
    
    Real-world use case: User lookup, database queries.
    """
    for user in users:
        if user.get("email") == email:
            return user  # Early return when found
    
    return None  # Not found


def validate_login(username: str, password: str) -> Tuple[bool, Optional[str], Optional[Dict]]:
    """
    Validates login credentials.
    
    Multiple return values pattern for complex results.
    
    Args:
        username: Username
        password: Password
    
    Returns:
        Tuple of (success, error_message, user_data)
    
    Real-world use case: Authentication systems.
    """
    # Early return for validation failures
    if not username or not password:
        return (False, "Username and password are required", None)
    
    if len(password) < 8:
        return (False, "Password too short", None)
    
    # Simulate user lookup
    user = {"id": 101, "username": username, "role": "user"}
    
    return (True, None, user)


def process_api_request(endpoint: str, data: Dict) -> Dict[str, Any]:
    """
    Processes API request with consistent return structure.
    
    Consistent dict return pattern for API responses.
    
    Args:
        endpoint: API endpoint
        data: Request data
    
    Returns:
        Response dictionary with status, data, and optional error
    
    Real-world use case: API endpoint handlers.
    """
    # Early return for invalid endpoints
    if not endpoint.startswith("/api/"):
        return {
            "status": "error",
            "code": 400,
            "error": "Invalid endpoint",
            "data": None
        }
    
    # Early return for missing data
    if not data:
        return {
            "status": "error",
            "code": 400,
            "error": "Request data required",
            "data": None
        }
    
    # Success case
    return {
        "status": "success",
        "code": 200,
        "error": None,
        "data": {"processed": True, "endpoint": endpoint}
    }


def calculate_order_total(items: List[Dict]) -> Union[float, None]:
    """
    Calculates order total, returns None for invalid orders.
    
    Union return type for value-or-error scenarios.
    
    Args:
        items: Order items
    
    Returns:
        Total amount or None if invalid
    
    Real-world use case: Order processing, cart calculation.
    """
    if not items:
        return None
    
    try:
        total = sum(item["price"] * item["quantity"] for item in items)
        return total
    except (KeyError, TypeError):
        return None


def process_batch_records(records: List[Dict]) -> Tuple[List[Dict], List[Dict]]:
    """
    Processes batch, returns successes and failures separately.
    
    Multiple collections return pattern for batch operations.
    
    Args:
        records: Records to process
    
    Returns:
        Tuple of (successful_records, failed_records)
    
    Real-world use case: Batch processing, ETL pipelines.
    """
    successful = []
    failed = []
    
    for record in records:
        # Simulate validation
        if record.get("valid", False):
            successful.append(record)
        else:
            failed.append(record)
    
    return (successful, failed)


def fetch_user_profile(user_id: int) -> Dict[str, Any]:
    """
    Fetches user profile, demonstrates guard clauses.
    
    Guard clause pattern: check error conditions first, early return.
    
    Args:
        user_id: User identifier
    
    Returns:
        User profile dictionary
    
    Real-world use case: User data retrieval.
    """
    # Guard clause: invalid ID
    if user_id <= 0:
        return {"error": "Invalid user ID", "profile": None}
    
    # Guard clause: user not found
    # Simulate database lookup
    if user_id > 1000:
        return {"error": "User not found", "profile": None}
    
    # Happy path - all guards passed
    return {
        "error": None,
        "profile": {
            "id": user_id,
            "name": "Alice Smith",
            "email": "alice@example.com"
        }
    }


def compute_statistics(numbers: List[float]) -> Optional[Dict[str, float]]:
    """
    Computes statistics, returns None for empty list.
    
    Optional dict return for conditional results.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Statistics dictionary or None
    
    Real-world use case: Analytics, data processing.
    """
    if not numbers:
        return None
    
    return {
        "count": len(numbers),
        "sum": sum(numbers),
        "average": sum(numbers) / len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }


def main() -> None:
    """Main function demonstrating return patterns."""
    print("="*70)
    print("RETURN VALUES: PATTERNS & BEST PRACTICES".center(70))
    print("="*70)
    
    print("\n[1] OPTIONAL RETURN - User Lookup")
    print("=" * 70)
    
    users_db = [
        {"id": 1, "name": "Alice", "email": "alice@example.com"},
        {"id": 2, "name": "Bob", "email": "bob@example.com"},
    ]
    
    found = find_user_by_email("alice@example.com", users_db)
    not_found = find_user_by_email("missing@example.com", users_db)
    
    print(f"Found: {found}")
    print(f"Not found: {not_found}")
    
    print("\n\n[2] TUPLE RETURN - Multiple Values")
    print("=" * 70)
    
    login_attempts = [
        ("alice", "SecurePass123"),
        ("bob", "short"),
        ("", "password"),
    ]
    
    for username, password in login_attempts:
        success, error, user = validate_login(username, password)
        
        if success:
            print(f"  ✓ Login successful: {user['username']}")
        else:
            print(f"  ✗ Login failed: {error}")
    
    print("\n\n[3] CONSISTENT DICT RETURN - API Responses")
    print("=" * 70)
    
    requests = [
        ("/api/users", {"name": "Alice"}),
        ("/invalid", {"data": "test"}),
        ("/api/products", {}),
    ]
    
    for endpoint, data in requests:
        response = process_api_request(endpoint, data)
        
        if response["status"] == "success":
            print(f"  ✓ {endpoint}: {response['data']}")
        else:
            print(f"  ✗ {endpoint}: {response['error']}")
    
    print("\n\n[4] UNION RETURN - Value or None")
    print("=" * 70)
    
    order_scenarios = [
        [{"price": 10.0, "quantity": 2}, {"price": 15.0, "quantity": 1}],
        [],
        [{"price": 10.0}],  # Missing quantity
    ]
    
    for i, items in enumerate(order_scenarios, 1):
        total = calculate_order_total(items)
        
        if total is not None:
            print(f"  Order {i}: ${total:.2f}")
        else:
            print(f"  Order {i}: Invalid")
    
    print("\n\n[5] MULTIPLE COLLECTIONS RETURN - Batch Processing")
    print("=" * 70)
    
    batch = [
        {"id": 1, "valid": True},
        {"id": 2, "valid": False},
        {"id": 3, "valid": True},
        {"id": 4, "valid": False},
    ]
    
    successful, failed = process_batch_records(batch)
    
    print(f"Successful: {len(successful)} records")
    print(f"Failed: {len(failed)} records")
    
    print("\n\n[6] GUARD CLAUSES - Early Returns")
    print("=" * 70)
    
    user_ids = [101, -5, 1001]
    
    for uid in user_ids:
        result = fetch_user_profile(uid)
        
        if result["error"]:
            print(f"  User {uid}: ✗ {result['error']}")
        else:
            print(f"  User {uid}: ✓ {result['profile']['name']}")
    
    print("\n\n[7] OPTIONAL DICT RETURN - Statistics")
    print("=" * 70)
    
    datasets = [
        [10, 20, 30, 40, 50],
        [],
    ]
    
    for i, data in enumerate(datasets, 1):
        stats = compute_statistics(data)
        
        if stats:
            print(f"  Dataset {i}: avg={stats['average']:.1f}, min={stats['min']}, max={stats['max']}")
        else:
            print(f"  Dataset {i}: No data")
    
    print("\n" + "="*70)
    print("Return Value Best Practices:")
    print("-" * 70)
    print("✓ Use Optional[T] for values that may not exist")
    print("✓ Use Tuple for multiple related values")
    print("✓ Use Dict for structured, labeled results")
    print("✓ Use Union[T, None] for value-or-error scenarios")
    print("✓ Early returns for error cases (guard clauses)")
    print("✓ Consistent return structure across similar functions")
    print("✗ Avoid returning different types based on conditions")
    print("✗ Document what None/empty returns mean")
    print("="*70)


if __name__ == "__main__":
    main()