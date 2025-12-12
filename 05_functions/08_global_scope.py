"""
Python global Keyword: Modifying Global State
==============================================

Topic: global keyword for modifying module-level variables

Real-World Applications:
- Configuration management
- Application-wide state
- Connection pools
- Caching
- Singleton patterns

Note: Use sparingly - prefer dependency injection and classes
for managing state in production applications.
"""

from typing import Dict, Optional
import threading


# GLOBAL STATE (use with caution)
DATABASE_CONNECTION_POOL: Dict[str, any] = {}
CACHE: Dict[str, any] = {}
REQUEST_COUNT = 0
MAINTENANCE_MODE = False


def initialize_database_pool(max_connections: int = 10) -> None:
    """
    Initializes global database connection pool.
    
    Args:
        max_connections: Maximum number of connections
    
    Real-world use case: Application startup initialization.
    """
    global DATABASE_CONNECTION_POOL
    
    print(f"\nInitializing connection pool (max {max_connections} connections)")
    DATABASE_CONNECTION_POOL = {
        "max_connections": max_connections,
        "active_connections": 0,
        "available_connections": max_connections
    }
    print(f"✓ Pool initialized: {DATABASE_CONNECTION_POOL}")


def get_database_connection() -> Optional[Dict]:
    """
    Gets a connection from the global pool.
    
    Returns:
        Connection dictionary or None if pool exhausted
    
    Real-world use case: Database connection management.
    """
    global DATABASE_CONNECTION_POOL
    
    if DATABASE_CONNECTION_POOL["available_connections"] > 0:
        DATABASE_CONNECTION_POOL["active_connections"] += 1
        DATABASE_CONNECTION_POOL["available_connections"] -= 1
        
        conn_id = DATABASE_CONNECTION_POOL["active_connections"]
        print(f"  ✓ Connection acquired: #{conn_id}")
        return {"id": conn_id, "status": "active"}
    
    print(f"  ✗ No connections available")
    return None


def release_database_connection() -> None:
    """Releases a connection back to the global pool."""
    global DATABASE_CONNECTION_POOL
    
    if DATABASE_CONNECTION_POOL["active_connections"] > 0:
        DATABASE_CONNECTION_POOL["active_connections"] -= 1
        DATABASE_CONNECTION_POOL["available_connections"] += 1
        print(f"  ✓ Connection released")


def cache_data(key: str, value: any) -> None:
    """
    Stores data in global cache.
    
    Args:
        key: Cache key
        value: Value to cache
    
    Real-world use case: Application-wide caching.
    """
    global CACHE
    
    CACHE[key] = value
    print(f"  Cached: {key} = {value}")


def get_cached_data(key: str) -> Optional[any]:
    """
    Retrieves data from global cache.
    
    Args:
        key: Cache key
    
    Returns:
        Cached value or None
    """
    # Reading global variable doesn't need 'global' keyword
    return CACHE.get(key)


def increment_request_counter() -> int:
    """
    Increments global request counter.
    
    Returns:
        Current request count
    
    Real-world use case: Request tracking, analytics.
    """
    global REQUEST_COUNT
    
    REQUEST_COUNT += 1
    return REQUEST_COUNT


def enable_maintenance_mode() -> None:
    """
    Enables maintenance mode globally.
    
    Real-world use case: Graceful shutdown, deploy management.
    """
    global MAINTENANCE_MODE
    
    MAINTENANCE_MODE = True
    print("\n⚠️  MAINTENANCE MODE ENABLED")
    print("New requests will be rejected")


def process_request(endpoint: str) -> Dict:
    """
    Processes API request, checking maintenance mode.
    
    Args:
        endpoint: API endpoint
    
    Returns:
        Response dictionary
    
    Real-world use case: Request handling with global flags.
    """
    # Reading global (no 'global' keyword needed)
    if MAINTENANCE_MODE:
        return {
            "status": 503,
            "error": "Service temporarily unavailable"
        }
    
    # Increment counter (needs 'global' to modify)
    request_num = increment_request_counter()
    
    return {
        "status": 200,
        "data": f"Response from {endpoint}",
        "request_number": request_num
    }


def reset_global_state() -> None:
    """
    Resets all global state (useful for testing).
    
    Real-world use case: Test suite cleanup, application restart.
    """
    global DATABASE_CONNECTION_POOL, CACHE, REQUEST_COUNT, MAINTENANCE_MODE
    
    DATABASE_CONNECTION_POOL = {}
    CACHE = {}
    REQUEST_COUNT = 0
    MAINTENANCE_MODE = False
    
    print("\n✓ All global state reset")


def main() -> None:
    """Main function demonstrating global keyword."""
    print("="*70)
    print("GLOBAL KEYWORD: MODULE-LEVEL STATE".center(70))
    print("="*70)
    
    print("\n[1] DATABASE CONNECTION POOL")
    print("=" * 70)
    
    initialize_database_pool(max_connections=3)
    
    print("\nAcquiring connections:")
    conn1 = get_database_connection()
    conn2 = get_database_connection()
    conn3 = get_database_connection()
    conn4 = get_database_connection()  # Should fail
    
    print("\nReleasing a connection:")
    release_database_connection()
    
    print("\nAcquiring another:")
    conn5 = get_database_connection()  # Should succeed now
    
    print(f"\nFinal pool state: {DATABASE_CONNECTION_POOL}")
    
    print("\n\n[2] GLOBAL CACHE")
    print("=" * 70)
    
    print("\nCaching data:")
    cache_data("user:101", {"name": "Alice", "email": "alice@example.com"})
    cache_data("config:timeout", 30)
    cache_data("api:version", "v2.1")
    
    print("\nRetrieving from cache:")
    user = get_cached_data("user:101")
    timeout = get_cached_data("config:timeout")
    print(f"  User data: {user}")
    print(f"  Timeout: {timeout}s")
    
    print(f"\nCache contents: {CACHE}")
    
    print("\n\n[3] REQUEST COUNTING")
    print("=" * 70)
    
    print("\nProcessing requests:")
    for i in range(5):
        response = process_request(f"/api/endpoint{i}")
        print(f"  Request #{response['request_number']}: {response['status']} - {response.get('data', response.get('error'))}")
    
    print(f"\nTotal requests processed: {REQUEST_COUNT}")
    
    print("\n\n[4] MAINTENANCE MODE")
    print("=" * 70)
    
    enable_maintenance_mode()
    
    print("\nAttempting requests in maintenance mode:")
    for i in range(2):
        response = process_request(f"/api/test{i}")
        print(f"  {response['status']}: {response.get('error')}")
    
    print("\n\n[5] GLOBAL STATE RESET")
    print("=" * 70)
    
    print(f"\nBefore reset:")
    print(f"  Request count: {REQUEST_COUNT}")
    print(f"  Maintenance mode: {MAINTENANCE_MODE}")
    print(f"  Cache size: {len(CACHE)}")
    
    reset_global_state()
    
    print(f"\nAfter reset:")
    print(f"  Request count: {REQUEST_COUNT}")
    print(f"  Maintenance mode: {MAINTENANCE_MODE}")
    print(f"  Cache size: {len(CACHE)}")
    
    print("\n" + "="*70)
    print("Best Practices:")
    print("-" * 70)
    print("✓ Use global for application-wide configuration")
    print("✓ Use for connection pools, caches, counters")
    print("✓ Document clearly that functions modify global state")
    print("✗ Avoid excessive use - makes code hard to test")
    print("✗ Consider dependency injection or class-based state instead")
    print("✗ Be careful with threading - use locks for mutable globals")
    print("\nAlternatives: Classes, dependency injection, context managers")
    print("="*70)


if __name__ == "__main__":
    main()