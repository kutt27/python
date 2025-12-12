"""
Python Collections Module and Advanced Data Structures
=======================================================

Topic: namedtuple, defaultdict, Counter, and other specialized containers

Real-World Applications:
- Structured data modeling without classes
- Default value handling in parsing
- Frequency analysis in analytics
- Time-series data with deque
- Ordered configuration with OrderedDict (legacy)
"""

from collections import namedtuple, defaultdict, Counter, deque, OrderedDict
from typing import List, Dict
from datetime import datetime, timezone


def demonstrate_namedtuple() -> None:
    """
    Demonstrates namedtuple for lightweight data structures.
    
    namedtuple creates tuple subclasses with named fields.
    Benefits:
    - More readable than regular tuples
    - Immutable (like tuples)
    - Memory efficient (like tuples)
    - Self-documenting code
    
    Real-world use case: API response models, database query results, coordinates.
    """
    # Define a User structure
    User = namedtuple("User", ["id", "username", "email", "role"])
    
    # Create user instances
    admin = User(id=1, username="admin", email="admin@example.com", role="admin")
    user = User(id=2, username="john_doe", email="john@example.com", role="user")
    
    print(f"Admin user: {admin}")
    print(f"  Username: {admin.username}")
    print(f"  Role: {admin.role}")
    
    print(f"\nRegular user: {user}")
    print(f"  Email: {user.email}")
    
    # Named tuples are still tuples
    print(f"\nIs tuple: {isinstance(admin, tuple)}")
    print(f"Access by index: {admin[1]}")  # username
    
    # Immutable
    try:
        admin.role = "superadmin"  # type: ignore
    except AttributeError as e:
        print(f"\n✗ Cannot modify: namedtuple is immutable")


def demonstrate_defaultdict() -> None:
    """
    Demonstrates defaultdict for automatic default values.
    
    defaultdict automatically creates default values for missing keys.
    No more KeyError exceptions or manual key checking!
    
    Real-world use case: Grouping data, counting, building indexes.
    """
    # Example: Group API requests by endpoint
    request_log: defaultdict[str, List[str]] = defaultdict(list)
    
    # Add requests without checking if key exists
    request_log["/api/users"].append("GET")
    request_log["/api/users"].append("POST")
    request_log["/api/products"].append("GET")
    request_log["/api/users"].append("DELETE")
    
    print(f"\nAPI request grouping:")
    for endpoint, methods in request_log.items():
        print(f"  {endpoint}: {methods}")
    
    # Example: Count errors by type
    error_counts: defaultdict[str, int] = defaultdict(int)
    
    errors = ["TimeoutError", "ConnectionError", "TimeoutError", "ValueError", "TimeoutError"]
    
    for error in errors:
        error_counts[error] += 1  # No need to check if key exists!
    
    print(f"\nError counts:")
    for error_type, count in error_counts.items():
        print(f"  {error_type}: {count}")


def demonstrate_counter() -> None:
    """
    Demonstrates Counter for frequency counting.
    
    Counter is a specialized dict for counting hashable objects.
    Perfect for analytics and frequency analysis.
    
    Real-world use case: HTTP status code analytics, word frequency, tag counting.
    """
    # Example: HTTP status code analysis
    status_codes = [200, 200, 404, 200, 500, 200, 404, 200, 301, 200]
    
    code_counter = Counter(status_codes)
    
    print(f"\nHTTP Status Code Analysis:")
    print(f"  All counts: {code_counter}")
    print(f"  Most common:  {code_counter.most_common(3)}")
    
    # Example: Tag frequency in blog posts
    all_tags = [
        "python", "tutorial", "web", "python",
        "backend", "python", "api", "tutorial",
        "python", "web"
    ]
    
    tag_frequency = Counter(all_tags)
    
    print(f"\nTag frequency analysis:")
    for tag, count in tag_frequency.most_common():
        bar = "█" * count
        print(f"  {tag:12} {bar} ({count})")
    
    # Arithmetic operations with counters
    week1_tags = Counter(["python", "web", "api"])
    week2_tags = Counter(["python", "ml", "web"])
    
    combined = week1_tags + week2_tags
    print(f"\nCombined tags over 2 weeks: {combined}")


def demonstrate_deque() -> None:
    """
    Demonstrates deque (double-ended queue) for efficient operations.
    
    deque provides O(1) append and pop from both ends.
    Regular lists are O(n) for operations at the beginning.
    
    Real-world use case: Request queues, task scheduling, sliding windows, undo/redo.
    """
    # Example: Request rate limiting with sliding window
    request_queue: deque[str] = deque(maxlen=5)  # Keep last 5 requests
    
    requests = [f"Request-{i}" for i in range(1, 9)]
    
    print(f"\nSliding window (max 5 items):")
    for req in requests:
        request_queue.append(req)
        print(f"  Added {req}: {list(request_queue)}")
    
    # Example: Task queue with priority (process from both ends)
    task_queue: deque[str] = deque(["task1", "task2", "task3"])
    
    print(f"\nTask queue: {list(task_queue)}")
    
    # Add urgent task to front
    task_queue.appendleft("URGENT_TASK")
    print(f"After adding urgent task: {list(task_queue)}")
    
    # Process from front
    next_task = task_queue.popleft()
    print(f"Processing: {next_task}")
    print(f"Remaining: {list(task_queue)}")


def demonstrate_ordered_dict() -> None:
    """
    Demonstrates OrderedDict (mostly legacy now).
    
    Note: Since Python 3.7+, regular dicts maintain insertion order.
    OrderedDict still useful for:
    - Equality comparison that considers order
    - Moving items to end/beginning
    - Reverse iteration
    
    Real-world use case: LRU cache implementation, configuration ordering.
    """
    # Example: LRU (Least Recently Used) cache pattern
    cache: OrderedDict[str, Dict] = OrderedDict()
    max_cache_size = 3
    
    def cache_access(key: str, value: Dict) -> None:
        """Simulate LRU cache access."""
        if key in cache:
            # Move to end (most recently used)
            cache.move_to_end(key)
        else:
            cache[key] = value
            # Evict oldest if over capacity
            if len(cache) > max_cache_size:
                oldest = next(iter(cache))
                print(f"  Evicting: {oldest}")
                cache.pop(oldest)
    
    print(f"\nLRU Cache simulation (max size: {max_cache_size}):")
    
    cache_access("user:1", {"name": "Alice"})
    print(f"  Cache: {list(cache.keys())}")
    
    cache_access("user:2", {"name": "Bob"})
    print(f"  Cache: {list(cache.keys())}")
    
    cache_access("user:3", {"name": "Charlie"})
    print(f"  Cache: {list(cache.keys())}")
    
    cache_access("user:1", {"name": "Alice"})  # Access again
    print(f"  Cache: {list(cache.keys())}")  # user:1 moved to end
    
    cache_access("user:4", {"name": "David"})  # Triggers eviction
    print(f"  Cache: {list(cache.keys())}")


def analyze_log_file(log_entries: List[str]) -> Dict:
    """
    Analyzes log entries using collections module.
    
    Args:
        log_entries: List of log messages
    
    Returns:
        Analysis dictionary with statistics
    
    Real-world use case: Log analysis, monitoring dashboards.
    """
    level_counter = Counter()
    hourly_requests: defaultdict[int, int] = defaultdict(int)
    
    for entry in log_entries:
        # Extract log level
        if "ERROR" in entry:
            level_counter["ERROR"] += 1
        elif "WARNING" in entry:
            level_counter["WARNING"] += 1
        else:
            level_counter["INFO"] += 1
    
    return {
        "total_entries": len(log_entries),
        "by_level": dict(level_counter),
        "most_common_level": level_counter.most_common(1)[0] if level_counter else None
    }


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON COLLECTIONS: ADVANCED DATA STRUCTURES".center(70))
    print("="*70)
    
    print("\n[1] NAMEDTUPLE - Lightweight Data Structures")
    print("-" * 70)
    demonstrate_namedtuple()
    
    print("\n\n[2] DEFAULTDICT - Automatic Defaults")
    print("-" * 70)
    demonstrate_defaultdict()
    
    print("\n\n[3] COUNTER - Frequency Counting")
    print("-" * 70)
    demonstrate_counter()
    
    print("\n\n[4] DEQUE - Double-Ended Queue")
    print("-" * 70)
    demonstrate_deque()
    
    print("\n\n[5] ORDEREDDICT - Ordered Dictionary")
    print("-" * 70)
    demonstrate_ordered_dict()
    
    print("\n\n[6] PRACTICAL EXAMPLE: Log Analysis")
    print("-" * 70)
    
    sample_logs = [
        "INFO: Server started",
        "ERROR: Database connection failed",
        "INFO: Request processed",
        "WARNING: High memory usage",
        "ERROR: Timeout",
        "INFO: Request processed"
    ]
    
    analysis = analyze_log_file(sample_logs)
    print(f"\nLog Analysis Results:")
    print(f"  Total entries: {analysis['total_entries']}")
    print(f"  By level: {analysis['by_level']}")
    print(f"  Most common: {analysis['most_common_level']}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. namedtuple: Lightweight, immutable data structures")
    print("2. defaultdict: Auto-creates default values (no KeyError)")
    print("3. Counter: Frequency counting and analytics")
    print("4. deque: O(1) operations at both ends")
    print("5. Use these instead of plain dicts/lists when appropriate")
    print("="*70)


if __name__ == "__main__":
    main()