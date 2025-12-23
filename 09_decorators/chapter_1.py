"""
Python Decorators: Basics
==========================

Topic: Function decorators, @decorator syntax, functools.wraps

Real-World Applications:
- Performance timing
- Logging/debugging
- Input validation
- Caching/memoization
- Access control
"""

from functools import wraps
import time
from typing import Callable, Any


def timer_decorator(func: Callable) -> Callable:
    """
    Times function execution.
    
    Real-world use case: Performance monitoring, optimization.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        
        elapsed = end_time - start_time
        print(f"⏱  {func.__name__}() took {elapsed:.4f}s")
        
        return result
    
    return wrapper


def debug_decorator(func: Callable) -> Callable:
    """
    Logs function calls with arguments.
    
    Real-world use case: Debugging, call tracing.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(a) for a in args]
        kwargs_repr = [f"{k}={v!r}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        
        print(f"🔍 Calling {func.__name__}({signature})")
        
        result = func(*args, **kwargs)
        
        print(f"🔍 {func.__name__}() returned {result!r}")
        
        return result
    
    return wrapper


def validate_positive(func: Callable) -> Callable:
    """
    Validates that numeric arguments are positive.
    
    Real-world use case: Input validation, data integrity.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Check all numeric arguments
        for arg in args:
            if isinstance(arg, (int, float)) and arg < 0:
                raise ValueError(f"Argument must be positive, got {arg}")
        
        for value in kwargs.values():
            if isinstance(value, (int, float)) and value < 0:
                raise ValueError(f"Argument must be positive, got {value}")
        
        return func(*args, **kwargs)
    
    return wrapper


def memoize(func: Callable) -> Callable:
    """
    Caches function results (memoization).
    
    Real-world use case: Expensive computations, API calls with same params.
    """
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"💾 Cache hit for {func.__name__}{args}")
            return cache[args]
        
        result = func(*args)
        cache[args] = result
        print(f"💾 Cached result for {func.__name__}{args}")
        
        return result
    
    return wrapper


def retry_on_failure(max_retries: int = 3):
    """
    Decorator factory: retries function on exception.
    
    Real-world use case: Network requests, database operations.
    """
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        print(f"❌ Failed after {max_retries} attempts")
                        raise
                    print(f"⚠️  Attempt {attempt + 1} failed: {e}. Retrying...")
                    time.sleep(0.5)
        
        return wrapper
    
    return decorator


# Example functions with decorators

@timer_decorator
def process_data(items: list) -> int:
    """Simulates data processing."""
    time.sleep(0.1)  # Simulate work
    return len(items)


@debug_decorator
def calculate_total(price: float, quantity: int, tax_rate: float = 0.08) -> float:
    """Calculates order total."""
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


@validate_positive
def calculate_discount(amount: float, percent: float) -> float:
    """Calculates discount (must be positive values)."""
    return amount * (percent / 100)


@memoize
def fibonacci(n: int) -> int:
    """Recursive Fibonacci with memoization."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@retry_on_failure(max_retries=3)
def unreliable_api_call(success_rate: float = 0.5) -> dict:
    """Simulates unreliable API call."""
    import random
    
    if random.random() < success_rate:
        raise ConnectionError("API temporarily unavailable")
    
    return {"status": "success", "data": [1, 2, 3]}



def demonstrate_timer_decorator() -> None:
    """
    Demonstrates adding execution timing via decorators.
    
    Real-world use case: Performance profiling, SRE metrics.
    """
    items = list(range(100))
    result = process_data(items)
    print(f"Processed {result} items")


def demonstrate_debug_decorator() -> None:
    """
    Demonstrates call tracing with arguments and return values.
    
    Real-world use case: Audit logging, development debugging.
    """
    total = calculate_total(99.99, 2, tax_rate=0.10)
    print(f"Final total: ${total:.2f}")


def demonstrate_validation_decorator() -> None:
    """
    Demonstrates pre-execution input validation.
    
    Real-world use case: Protecting sensitive logic from illegal data.
    """
    try:
        discount1 = calculate_discount(100, 20)
        print(f"✓ Valid: discount = ${discount1:.2f}")
        
        discount2 = calculate_discount(-100, 20)  # Invalid
    except ValueError as e:
        print(f"✗ Invalid: {e}")


def demonstrate_memoization() -> None:
    """
    Demonstrates transparent caching of function results.
    
    Real-world use case: Optimizing expensive recursive calls or API responses.
    """
    print("Calculating fibonacci(10):")
    fib_10 = fibonacci(10)
    print(f"Result: {fib_10}")
    
    print("\nCalculating fibonacci(10) again (should use cache):")
    fib_10_again = fibonacci(10)


def demonstrate_retry_logic() -> None:
    """
    Demonstrates automatic retries for transient failures.
    
    Real-world use case: Resilience in microservices, network robustness.
    """
    try:
        response = unreliable_api_call(success_rate=0.7)
        print(f"✓ API call succeeded: {response}")
    except ConnectionError as e:
        print(f"✗ API call failed: {e}")


def demonstrate_stacked_decorators() -> None:
    """
    Demonstrates how to combine multiple behaviors on a single function.
    
    Real-world use case: Combining logging, timing, and security checks.
    """
    @timer_decorator
    @debug_decorator
    def complex_operation(x: int, y: int) -> int:
        """Function with multiple decorators."""
        time.sleep(0.05)
        return x + y
    
    result = complex_operation(5, 10)
    print(f"Result: {result}")


def main() -> None:
    """Main function demonstrating decorator basics."""
    print("="*70)
    print("PYTHON DECORATORS: BASICS".center(70))
    print("="*70)
    
    print("\n[1] TIMER DECORATOR - Performance Monitoring")
    print("-" * 70)
    demonstrate_timer_decorator()
    
    print("\n\n[2] DEBUG DECORATOR - Call Tracing")
    print("-" * 70)
    demonstrate_debug_decorator()
    
    print("\n\n[3] VALIDATION DECORATOR - Input Checking")
    print("-" * 70)
    demonstrate_validation_decorator()
    
    print("\n\n[4] MEMOIZATION DECORATOR - Caching Results")
    print("-" * 70)
    demonstrate_memoization()
    
    print("\n\n[5] RETRY DECORATOR - Fault Tolerance")
    print("-" * 70)
    demonstrate_retry_logic()
    
    print("\n\n[6] STACKING DECORATORS")
    print("-" * 70)
    demonstrate_stacked_decorators()
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Decorators wrap functions to extend behavior without modifying source code")
    print("2. The @syntax is syntactic sugar for 'func = decorator(func)'")
    print("3. Always use @functools.wraps to preserve function metadata (docstrings, etc.)")
    print("4. Decorators can accept arguments (decorator factories)")
    print("5. Multiple decorators can be stacked; order of execution is top-to-bottom")
    print("="*70)


if __name__ == "__main__":
    main()