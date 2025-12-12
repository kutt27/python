"""
Python nonlocal Keyword: Modifying Enclosing Scope
===================================================

Topic: nonlocal keyword for nested function state

Real-World Applications:
- Closures with mutable state
- Factory functions
- Decorators with state
- State machines
- Accumulator patterns
"""

from typing import Callable, List, Dict
from datetime import datetime


def create_accumulator(initial: float = 0) -> Callable:
    """
    Creates an accumulator function using nonlocal.
    
    Returns:
        Function that accumulates values
    
    Real-world use case: Running totals, metrics collection.
    """
    total = initial  # Enclosing scope variable
    
    def add(value: float) -> float:
        nonlocal total  # Modify enclosing scope
        total += value
        return total
    
    return add


def create_logger_with_context(service_name: str) -> Callable:
    """
    Creates a logger with contextual information.
    
    Uses nonlocal to maintain request count.
    
    Args:
        service_name: Service identifier
    
    Returns:
        Logging function
    
    Real-world use case: Contextual logging, request tracking.
    """
    request_count = 0  # Enclosing scope
    
    def log(message: str, level: str = "INFO") -> None:
        nonlocal request_count
        request_count += 1
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{service_name}] [{level}] (#{request_count}) {message}")
    
    return log


def create_rate_limited_function(func: Callable, max_calls: int) -> Callable:
    """
    Creates a rate-limited version of a function.
    
    Uses nonlocal to track call count.
    
    Args:
        func: Function to wrap
        max_calls: Maximum allowed calls
    
    Returns:
        Rate-limited function
    
    Real-world use case: API rate limiting, resource throttling.
    """
    calls_made = 0  # Enclosing scope
    
    def wrapper(*args, **kwargs):
        nonlocal calls_made
        
        if calls_made >= max_calls:
            return {"error": "Rate limit exceeded", "max_calls": max_calls}
        
        calls_made += 1
        result = func(*args, **kwargs)
        return result
    
    return wrapper


def create_state_machine() -> Dict[str, Callable]:
    """
    Creates a simple state machine using nonlocal.
    
    Returns:
        Dictionary of state machine operations
    
    Real-world use case: Order processing, workflow management.
    """
    current_state = "pending"  # Enclosing scope
    state_history: List[str] = []
    
    def get_state() -> str:
        return current_state
    
    def transition(new_state: str) -> bool:
        nonlocal current_state
        
        valid_transitions = {
            "pending": ["processing", "cancelled"],
            "processing": ["completed", "failed"],
            "completed": [],
            "failed": ["pending"],
            "cancelled": []
        }
        
        if new_state in valid_transitions.get(current_state, []):
            state_history.append(f"{current_state} → {new_state}")
            current_state = new_state
            return True
        
        return False
    
    def history() -> List[str]:
        return state_history.copy()
    
    return {
        "get_state": get_state,
        "transition": transition,
        "history": history
    }


def create_retry_function(func: Callable, max_retries: int = 3) -> Callable:
    """
    Creates a function that retries on failure.
    
    Uses nonlocal to track attempts.
    
    Args:
        func: Function to wrap
        max_retries: Maximum retry attempts
    
    Returns:
        Retry-wrapped function
    
    Real-world use case: Network requests, database operations.
    """
    def wrapper(*args, **kwargs):
        attempts = 0  # Local to each call
        last_error = None
        
        while attempts < max_retries:
            attempts_remaining = max_retries - attempts
            
            try:
                result = func(*args, **kwargs)
                if attempts > 0:
                    print(f"  ✓ Succeeded on attempt {attempts + 1}")
                return result
            
            except Exception as e:
                last_error = e
                attempts += 1
                if attempts < max_retries:
                    print(f"  ✗ Attempt {attempts} failed, {max_retries - attempts} retries left")
        
        print(f"  ✗ All {max_retries} attempts failed")
        raise last_error
    
    return wrapper


def main() -> None:
    """Main function demonstrating nonlocal."""
    print("="*70)
    print("NONLOCAL KEYWORD: MODIFYING ENCLOSING SCOPE".center(70))
    print("="*70)
    
    print("\n[1] ACCUMULATOR - Running Total")
    print("=" * 70)
    
    sales_total = create_accumulator(initial=0)
    
    print("Recording sales:")
    print(f"  Sale 1: ${sales_total(99.99):.2f}")
    print(f"  Sale 2: ${sales_total(149.99):.2f}")
    print(f"  Sale 3: ${sales_total(75.00):.2f}")
    print(f"  Total: ${sales_total(0):.2f}")  # Add 0 to get current total
    
    print("\n\n[2] CONTEXTUAL LOGGER")
    print("=" * 70)
    
    api_logger = create_logger_with_context("API-Service")
    
    api_logger("Server started")
    api_logger("Processing request", "INFO")
    api_logger("Database connection established", "DEBUG")
    api_logger("Request completed")
    
    print("\n\n[3] RATE-LIMITED FUNCTION")
    print("=" * 70)
    
    def fetch_data(query: str) -> Dict:
        return {"results": f"Data for {query}"}
    
    limited_fetch = create_rate_limited_function(fetch_data, max_calls=3)
    
    print("Making API calls (max 3):")
    for i in range(5):
        result = limited_fetch(f"query_{i+1}")
        if "error" in result:
            print(f"  Call {i+1}: ✗ {result['error']}")
        else:
            print(f"  Call {i+1}: ✓ {result}")
    
    print("\n\n[4] STATE MACHINE")
    print("=" * 70)
    
    order_sm = create_state_machine()
    
    print(f"Initial state: {order_sm['get_state']()}")
    
    transitions = [
        ("processing", "Start processing"),
        ("cancelled", "Try to cancel (invalid)"),
        ("completed", "Complete order"),
        ("failed", "Try to fail (invalid)"),
    ]
    
    for new_state, description in transitions:
        current = order_sm['get_state']()
        success = order_sm['transition'](new_state)
        
        if success:
            print(f"  ✓ {description}: {current} → {new_state}")
        else:
            print(f"  ✗ {description}: Invalid transition from {current}")
    
    print(f"\nFinal state: {order_sm['get_state']()}")
    print(f"History: {order_sm['history']()}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. nonlocal modifies variables in enclosing (not global) scope")
    print("2. Enables stateful closures and factory functions")
    print("3. Perfect for decorators that need to track state")
    print("4. Use for counters, accumulators, state machines")
    print("5. Maintains encapsulation while allowing modification")
    print("="*70)


if __name__ == "__main__":
    main()