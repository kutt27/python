"""
Python Dictionaries: Key-Value Mappings
========================================

Topic: Dictionary data type, methods, and operations

Real-World Applications:
- Configuration management
- Caching and memoization
- JSON API request/response handling
- Database ORM result mapping
- Session management in web applications
- Feature flags and A/B testing configuration
"""

from typing import Dict, Any, Optional, List


def demonstrate_dict_creation() -> None:
    """
    Demonstrates different ways to create dictionaries.
    
    Real-world use case: API responses, configuration files, data models.
    """
    # Using dict() constructor
    api_response = dict(status=200, message="Success", data={})
    print(f"API response: {api_response}")
    
    # Using literal syntax (preferred for readability)
    user_config: Dict[str, Any] = {
        "theme": "dark",
        "language": "en",
        "notifications": True,
        "max_retry": 3
    }
    print(f"\nUser config: {user_config}")
    
    # Empty dictionary
    cache: Dict[str, str] = {}
    print(f"\nEmpty cache: {cache}")
    print(f"Type: {type(cache)}")


def demonstrate_dict_access() -> None:
    """
    Demonstrates accessing dictionary values.
    
    Real-world use case: Reading configuration, parsing API responses.
    """
    # Example: Database connection configuration
    db_config: Dict[str, Any] = {
        "host": "localhost",
        "port": 5432,
        "database": "production",
        "user": "admin"
    }
    
    print(f"\nDatabase config: {db_config}")
    
    # Direct access (raises KeyError if key doesn't exist)
    host = db_config["host"]
    print(f"\nDatabase host: {host}")
    
    # Safe access with get() method (returns None or default)
    password = db_config.get("password", "default_password")
    print(f"Password (with default): {password}")
    
    # Check if key exists
    has_ssl = "ssl" in db_config
    print(f"\nHas SSL config: {has_ssl}")


def demonstrate_dict_modification() -> None:
    """
    Demonstrates modifying dictionaries.
    
    Real-world use case: Updating configuration, caching values.
    """
    # Example: API request metadata
    request_meta: Dict[str, Any] = {
        "method": "GET",
        "endpoint": "/api/users"
    }
    
    print(f"\nInitial metadata: {request_meta}")
    
    # Add new key-value pair
    request_meta["timestamp"] = "2024-12-05T10:00:00Z"
    print(f"After adding timestamp: {request_meta}")
    
    # Update existing value
    request_meta["method"] = "POST"
    print(f"After changing method: {request_meta}")
    
    # Delete key
    del request_meta["endpoint"]
    print(f"After deleting endpoint: {request_meta}")
    
    # Update multiple values at once
    additional_headers = {"user_agent": "Python/3.11", "auth": "Bearer token123"}
    request_meta.update(additional_headers)
    print(f"\nAfter update: {request_meta}")


def demonstrate_dict_methods() -> None:
    """
    Demonstrates essential dictionary methods.
    
    Real-world use case: Iterating over configuration, extracting data.
    """
    # Example: Service health status
    service_status: Dict[str, str] = {
        "api": "healthy",
        "database": "healthy",
        "cache": "degraded",
        "queue": "healthy"
    }
    
    print(f"\nService status: {service_status}")
    
    # Get all keys
    services = service_status.keys()
    print(f"\nServices: {list(services)}")
    
    # Get all values
    statuses = service_status.values()
    print(f"Statuses: {list(statuses)}")
    
    # Get all key-value pairs
    items = service_status.items()
    print(f"\nService items:")
    for service, status in items:
        health_icon = "✓" if status == "healthy" else "⚠"
        print(f"  {health_icon} {service}: {status}")


def demonstrate_dict_popitem() -> None:
    """
    Demonstrates popitem() for removing and returning items.
    
    Real-world use case: Processing queues, consuming tasks.
    """
    # Example: Task queue (LIFO - Last In First Out)
    task_queue: Dict[str, str] = {
        "task1": "Send email",
        "task2": "Generate report",
        "task3": "Update cache"
    }
    
    print(f"\nInitial queue: {task_queue}")
    
    # Remove and process last item (in Python 3.7+ dicts maintain insertion order)
    last_task = task_queue.popitem()
    print(f"\nRemoved task: {last_task}")
    print(f"Remaining queue: {task_queue}")


def demonstrate_get_with_default() -> None:
    """
    Demonstrates using get() method with defaults.
    
    Real-world use case: Configuration with fallback values.
    """
    # Example: Application configuration
    config: Dict[str, Any] = {
        "debug": True,
        "port": 8000
    }
    
    print(f"\nConfiguration: {config}")
    
    # Get with defaults for missing keys
    debug_mode = config.get("debug", False)
    port = config.get("port", 3000)
    workers = config.get("workers", 4)  # Not in config, uses default
    
    print(f"\nDebug mode: {debug_mode}")
    print(f"Port: {port}")
    print(f"Workers: {workers} (default)")


def cache_user_data(user_id: int, cache: Dict[int, Dict[str, Any]]) -> Dict[str, Any]:
    """
    Demonstrates caching pattern with dictionaries.
    
    Args:
        user_id: User's ID
        cache: Cache dictionary
    
    Returns:
        User data (from cache or "database")
    
    Real-world use case: Reducing database queries with caching.
    """
    # Check cache first
    if user_id in cache:
        print(f"  Cache HIT for user {user_id}")
        return cache[user_id]
    
    # Simulate database query
    print(f"  Cache MISS for user {user_id} - fetching from DB")
    user_data = {
        "id": user_id,
        "name": f"User{user_id}",
        "email": f"user{user_id}@example.com"
    }
    
    # Store in cache
    cache[user_id] = user_data
    return user_data


def merge_configs(defaults: Dict[str, Any], user_config: Dict[str, Any]) -> Dict[str, Any]:
    """
    Merges user configuration with defaults.
    
    Args:
        defaults: Default configuration
        user_config: User-specific configuration
    
    Returns:
        Merged configuration (user overrides defaults)
    
    Real-world use case: Application configuration management.
    """
    merged = defaults.copy()  # Start with defaults
    merged.update(user_config)  # Override with user values
    return merged


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON DICTIONARIES: KEY-VALUE MAPPINGS".center(70))
    print("="*70)
    
    print("\n[1] DICTIONARY CREATION")
    print("-" * 70)
    demonstrate_dict_creation()
    
    print("\n\n[2] DICTIONARY ACCESS")
    print("-" * 70)
    demonstrate_dict_access()
    
    print("\n\n[3] DICTIONARY MODIFICATION")
    print("-" * 70)
    demonstrate_dict_modification()
    
    print("\n\n[4] DICTIONARY METHODS")
    print("-" * 70)
    demonstrate_dict_methods()
    
    print("\n\n[5] POPITEM METHOD")
    print("-" * 70)
    demonstrate_dict_popitem()
    
    print("\n\n[6] GET WITH DEFAULTS")
    print("-" * 70)
    demonstrate_get_with_default()
    
    print("\n\n[7] PRACTICAL EXAMPLES")
    print("-" * 70)
    
    # Caching example
    print("\nCaching example:")
    user_cache: Dict[int, Dict[str, Any]] = {}
    
    # First access - cache miss
    user1 = cache_user_data(101, user_cache)
    print(f"  Retrieved: {user1}")
    
    # Second access - cache hit
    user1_again = cache_user_data(101, user_cache)
    print(f"  Retrieved: {user1_again}")
    
    # Configuration merging
    print("\n\nConfiguration merging:")
    defaults = {"theme": "light", "language": "en", "timeout": 30}
    user_prefs = {"theme": "dark", "notifications": True}
    
    final_config = merge_configs(defaults, user_prefs)
    print(f"  Defaults: {defaults}")
    print(f"  User preferences: {user_prefs}")
    print(f"  Final config: {final_config}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Dictionaries map keys to values (like JSON objects)")
    print("2. Use dict.get(key, default) for safe access")
    print("3. Keys must be hashable (int, str, tuple, not list)")
    print("4. Since Python 3.7+, dicts maintain insertion order")
    print("5. Perfect for configuration, caching, and data modeling")
    print("="*70)


if __name__ == "__main__":
    main()