"""
Python Tuples: Immutable Sequences
====================================

Topic: Tuple data type, unpacking, swapping, and memory efficiency

Real-World Applications:
- Function return values (multiple values)
- Database query results (rows as tuples)
- Configuration constants that shouldn't change
- Dictionary keys (tuples are hashable, lists are not)
- Coordinate pairs and fixed data structures
"""

from typing import Tuple, List


def demonstrate_tuple_basics() -> None:
    """
    Demonstrates tuple creation and immutability.
    
    Tuples are immutable sequences - once created, they cannot be modified.
    This makes them:
    - Memory efficient
    - Thread-safe
    - Hashable (can be dict keys)
    
    Real-world use case: Database query results, API response headers.
    """
    # Example: HTTP status tuple (code, message)
    http_response: Tuple[int, str] = (200, "OK")
    
    print(f"HTTP Response: {http_response}")
    print(f"Status Code: {http_response[0]}")
    print(f"Message: {http_response[1]}")
    print(f"Type: {type(http_response)}")
    
    # Tuples are immutable
    try:
        http_response[0] = 404  # type: ignore
    except TypeError as e:
        print(f"\n✗ Cannot modify tuple: {e}")


def demonstrate_tuple_unpacking() -> None:
    """
    Demonstrates tuple unpacking - a powerful Python feature.
    
    Unpacking allows you to assign multiple variables in one line.
    
    Real-world use case: Function returns, API responses, data extraction.
    """
    # Example: Database row as tuple
    user_record: Tuple[int, str, str] = (101, "admin", "admin@example.com")
    
    # Unpack into individual variables
    user_id, username, email = user_record
    
    print(f"\nUser record unpacking:")
    print(f"  ID: {user_id}")
    print(f"  Username: {username}")
    print(f"  Email: {email}")
    
    # Extended unpacking with * operator
    server_metrics: Tuple[str, ...] = ("CPU", "70%", "Memory", "80%", "Disk", "50%")
    metric_name,  *values = server_metrics
    
    print(f"\nExtended unpacking:")
    print(f"  First metric: {metric_name}")
    print(f"  Other values: {values}")


def demonstrate_tuple_swapping() -> None:
    """
    Demonstrates tuple swapping - an elegant Python idiom.
    
    Traditional swapping (in languages like Java/C++) requires a temp variable.
    Python tuples make swapping cleaner and more efficient.
    
    Real-world use case: Sorting algorithms, state toggling, load balancing.
    """
    # Example: Load balancing between servers
    primary_server = "server-a"
    secondary_server = "server-b"
    
    print(f"\nBefore swap:")
    print(f"  Primary: {primary_server}")
    print(f"  Secondary: {secondary_server}")
    
    # Swap using tuple unpacking (Pythonic way)
    primary_server, secondary_server = secondary_server, primary_server
    
    print(f"\nAfter swap:")
    print(f"  Primary: {primary_server}")
    print(f"  Secondary: {secondary_server}")
    
    print(f"\n{'='*60}")
    print("This is actually tuple packing and unpacking:")
    print("  (a, b) = (b, a)")    
    print("  Right side creates tuple, left side unpacks it")
    print(f"{'='*60}")


def demonstrate_tuple_as_dict_key() -> None:
    """
    Demonstrates using tuples as dictionary keys.
    
    Tuples can be dict keys because they are hashable.
    Lists cannot be keys because they are mutable.
    
    Real-world use case: Multi-dimensional caching, coordinate mapping, composite keys.
    """
    # Example: Caching API responses by (endpoint, method) combination
    api_cache: dict[Tuple[str, str], str] = {}
    
    # Store cached responses
    api_cache[("/users", "GET")] = "User list response"
    api_cache[("/users", "POST")] = "User created response"
    api_cache[("/products", "GET")] = "Product list response"
    
    print(f"\nAPI Response Cache:")
    for key, value in api_cache.items():
        endpoint, method = key
        print(f"  {method} {endpoint}: {value}")
    
    # Retrieve cached response
    cache_key = ("/users", "GET")
    cached_data = api_cache.get(cache_key, "Not cached")
    print(f"\nCache lookup for {cache_key}: {cached_data}")


def demonstrate_membership_testing() -> None:
    """
    Demonstrates membership testing in tuples.
    
    The 'in' operator checks if an element exists in the tuple.
    Time complexity: O(n) for tuples and lists.
    
    Real-world use case: Validation, permission checking, feature flags.
    """
    # Example: Allowed HTTP methods for an API endpoint
    allowed_methods = ("GET", "POST", "PUT", "DELETE")
    
    # Check if method is allowed
    request_method = "GET"
    is_allowed = request_method in allowed_methods
    
    print(f"\nHTTP Method validation:")
    print(f"  Allowed methods: {allowed_methods}")
    print(f"  Request method: {request_method}")
    print(f"  Is allowed: {is_allowed}")
    
    # Invalid method
    invalid_method = "TRACE"
    is_valid = invalid_method in allowed_methods
    print(f"\n  Invalid method '{invalid_method}': {is_valid}")


def get_user_info(user_id: int) -> Tuple[str, str, int]:
    """
    Demonstrates returning multiple values from a function.
    
    Args:
        user_id: User's ID
    
    Returns:
        Tuple of (username, email, age)
    
    Real-world use case: Database queries, API responses, computed values.
    """
    # Simulate database query
    return ("john_doe", "john@example.com", 28)


def parse_coordinates(coord_string: str) -> Tuple[float, float]:
    """
    Parses coordinate string into tuple.
    
    Args:
        coord_string: String like "40.7128,-74.0060"
    
    Returns:
        Tuple of (latitude, longitude)
    
    Real-world use case: GPS data processing, geocoding services.
    """
    parts = coord_string.split(",")
    lat = float(parts[0].strip())
    lon = float(parts[1].strip())
    return (lat, lon)


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON TUPLES: IMMUTABLE SEQUENCES".center(70))
    print("="*70)
    
    print("\n[1] TUPLE BASICS & IMMUTABILITY")
    print("-" * 70)
    demonstrate_tuple_basics()
    
    print("\n\n[2] TUPLE UNPACKING")
    print("-" * 70)
    demonstrate_tuple_unpacking()
    
    print("\n\n[3] TUPLE SWAPPING")
    print("-" * 70)
    demonstrate_tuple_swapping()
    
    print("\n\n[4] TUPLES AS DICTIONARY KEYS")
    print("-" * 70)
    demonstrate_tuple_as_dict_key()
    
    print("\n\n[5] MEMBERSHIP TESTING")
    print("-" * 70)
    demonstrate_membership_testing()
    
    print("\n\n[6] FUNCTION RETURN VALUES")
    print("-" * 70)
    username, email, age = get_user_info(101)
    print(f"User info: {username}, {email}, {age} years old")
    
    print("\n\n[7] COORDINATE PARSING")
    print("-" * 70)
    coords = "40.7128,-74.0060"  # New York City
    lat, lon = parse_coordinates(coords)
    print(f"Parsed coordinates: ({lat}, {lon})")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Tuples are immutable - cannot be modified after creation")
    print("2. Tuples are hashable - can be used as dict keys")
    print("3. Tuple unpacking enables elegant multiple assignment")
    print("4. Use tuples for fixed data, lists for variable data")
    print("5. Tuples are more memory-efficient than lists")
    print("="*70)


if __name__ == "__main__":
    main()