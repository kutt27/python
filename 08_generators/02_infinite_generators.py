"""
Python Generators: Infinite Sequences
======================================

Topic: Infinite generators, itertools, stateful generators

Real-World Applications:
- ID generation
- Timestamp streams
- Monitoring/polling systems
- Event streams
- Sequence generation
"""

from typing import Generator
import itertools
from datetime import datetime, timedelta


def generate_ids(prefix: str = "ID") -> Generator[str, None, None]:
    """
    Generates unique IDs indefinitely.
    
    Args:
        prefix: ID prefix
    
    Yields:
        Unique ID
    
    Real-world use case: User ID, order ID, transaction ID generation.
    """
    counter = 1
    while True:
        yield f"{prefix}-{counter:06d}"
        counter += 1


def generate_timestamps(interval_seconds: int = 1) -> Generator[str, None, None]:
    """
    Generates timestamps at specified interval.
    
    Args:
        interval_seconds: Interval between timestamps
    
    Yields:
        Timestamp string
    
    Real-world use case: Time-series data, logging, monitoring.
    """
    current_time = datetime.now()
    
    while True:
        yield current_time.strftime("%Y-%m-%d %H:%M:%S")
        current_time += timedelta(seconds=interval_seconds)


def poll_api_endpoint(endpoint: str, interval: int = 5) -> Generator[Dict, None, None]:
    """
    Polls API endpoint indefinitely.
    
    Args:
        endpoint: API endpoint to poll
        interval: Polling interval in seconds
    
    Yields:
        API response dict
    
    Real-world use case: Health monitoring, status checking, data synchronization.
    """
    request_count = 0
    
    while True:
        request_count += 1
        
        # Simulate API call
        response = {
            "endpoint": endpoint,
            "status": 200 if request_count % 10 != 0 else 500,
            "timestamp": datetime.now().isoformat(),
            "request_number": request_count
        }
        
        yield response


def fibonacci_infinite() -> Generator[int, None, None]:
    """
    Generates Fibonacci sequence indefinitely.
    
    Yields:
        Next Fibonacci number
    
    Real-world use case: Mathematical modeling, algorithm demonstrations.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def cycle_through_values(values: List) -> Generator:
    """
    Cycles through values indefinitely.
    
    Args:
        values: List of values to cycle
    
    Yields:
        Next value in cycle
    
    Real-world use case: Load balancing, round-robin scheduling.
    """
    while True:
        for value in values:
            yield value


def main() -> None:
    """Main function demonstrating infinite generators."""
    print("="*70)
    print("INFINITE GENERATORS".center(70))
    print("="*70)
    
    print("\n[1] ID GENERATION")
    print("-" * 70)
    
    order_id_gen = generate_ids("ORD")
    user_id_gen = generate_ids("USR")
    
    print("Generating 5 order IDs:")
    for _ in range(5):
        print(f"  {next(order_id_gen)}")
    
    print("\nGenerating 3 user IDs:")
    for _ in range(3):
        print(f"  {next(user_id_gen)}")
    
    print("\n\n[2] TIMESTAMP STREAM")
    print("-" * 70)
    
    timestamp_gen = generate_timestamps(interval_seconds=60)  # Every minute
    
    print("Next 5 timestamps (1-minute intervals):")
    for _ in range(5):
        print(f"  {next(timestamp_gen)}")
    
    print("\n\n[3] API POLLING")
    print("-" * 70)
    
    health_check = poll_api_endpoint("/api/health", interval=5)
    
    print("Polling API (simulating 6 requests):")
    for _ in range(6):
        response = next(health_check)
        status_icon = "✓" if response["status"] == 200 else "✗"
        print(f"  {status_icon} Request #{response['request_number']}: Status {response['status']}")
    
    print("\n\n[4] FIBONACCI SEQUENCE (Infinite)")
    print("-" * 70)
    
    fib_gen = fibonacci_infinite()
    
    print("First 15 Fibonacci numbers:")
    fib_list = [next(fib_gen) for _ in range(15)]
    print(f"  {fib_list}")
    
    print("\n\n[5] ROUND-ROBIN LOAD BALANCING")
    print("-" * 70)
    
    servers = ["server1.example.com", "server2.example.com", "server3.example.com"]
    load_balancer = cycle_through_values(servers)
    
    print("Distributing 10 requests across servers:")
    for request_num in range(1, 11):
        server = next(load_balancer)
        print(f"  Request #{request_num} → {server}")
    
    print("\n\n[6] USING itertools - Infinite Iterators")
    print("-" * 70)
    
    # itertools.count() - infinite counter
    counter = itertools.count(start=1, step=1)
    print("itertools.count() - First 5:")
    print(f"  {[next(counter) for _ in range(5)]}")
    
    # itertools.cycle() - cycle through sequence
    colors = itertools.cycle(["red", "green", "blue"])
    print("\nitertools.cycle(['red', 'green', 'blue']) - First 7:")
    print(f"  {[next(colors) for _ in range(7)]}")
    
    # itertools.repeat() - repeat value
    repeated = itertools.repeat("API_KEY_123", 3)
    print("\nitertools.repeat('API_KEY_123', 3):")
    print(f"  {list(repeated)}")
    
    print("\n\n[7] STATEFUL GENERATOR - Request Throttling")
    print("-" * 70)
    
    def rate_limited_requests(max_per_minute: int = 60):
        """Generator that enforces rate limiting."""
        request_count = 0
        minute_start = 0
        
        while True:
            current_minute = request_count // max_per_minute
            
            if current_minute > minute_start:
                minute_start = current_minute
                print(f"  [Minute {minute_start + 1}] Rate limit reset")
            
            position_in_minute = request_count % max_per_minute
            
            yield {
                "request_number": request_count + 1,
                "minute": current_minute + 1,
                "position": position_in_minute + 1,
                "allowed": True
            }
            
            request_count += 1
    
    throttle = rate_limited_requests(max_per_minute=10)
    
    print("Rate-limited requests (10/minute):")
    for _ in range(25):
        req = next(throttle)
        if req["position"] == 1:
            print(f"  Request #{req['request_number']} (Minute {req['minute']})")
    
    print("\n\n[8] EVENT STREAM GENERATOR")
    print("-" * 70)
    
    def event_stream():
        """Simulates infinite event stream."""
        event_types = ["login", "page_view", "click", "logout"]
        event_counter = itertools.count(1)
        event_cycle = itertools.cycle(event_types)
        
        while True:
            yield {
                "event_id": next(event_counter),
                "event_type": next(event_cycle),
                "timestamp": datetime.now().isoformat()
            }
    
    events = event_stream()
    
    print("Event stream (first 8 events):")
    for _ in range(8):
        event = next(events)
        print(f"  Event #{event['event_id']}: {event['event_type']}")
    
    print("\n" + "="*70)
    print("Infinite Generator Characteristics:")
    print("-" * 70)
    print("• Never stops yielding (no StopIteration)")
    print("• Maintains internal state across yields")
    print("• Memory efficient (doesn't store all values)")
    print("• Must be stopped externally (break, limit)")
    print("\nCommon Patterns:")
    print("1. while True: yield ...")
    print("2. itertools.count(), cycle(), repeat()")
    print("3. Stateful counters and accumulators")
    print("\nUse Cases:")
    print("✓ ID/sequence generation")
    print("✓ Monitoring and polling")
    print("✓ Event streams")
    print("✓ Load balancing")
    print("✓ Rate limiting")
    print("="*70)


if __name__ == "__main__":
    main()