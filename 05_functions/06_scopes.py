"""
Python Variable Scopes: LEGB Rule
==================================

Topic: Local, Enclosing, Global, Built-in scopes

Real-World Applications:
- Configuration management (global config vs local overrides)
- State management in applications
- Closure-based caching
- Plugin systems with scoped variables
- Namespacing in large applications
"""

from typing import Callable, Dict
import time


# GLOBAL SCOPE
DATABASE_URL = "postgresql://localhost/production"
DEBUG_MODE = False
MAX_CONNECTIONS = 100


def demonstrate_local_scope() -> None:
    """
    Demonstrates local variable scope.
    
    Local variables exist only within the function.
    
    Real-world use case: Temporary calculations, function-specific state.
    """
    # LOCAL SCOPE
    api_key = "secret_key_12345"  # Only exists in this function
    request_count = 0
    
    print(f"  Local api_key: {api_key}")
    print(f"  Local request_count: {request_count}")
    
    # These variables disappear after function returns


def demonstrate_global_access() -> None:
    """
    Demonstrates accessing global variables.
    
    Functions can READ global variables without declaration.
    
    Real-world use case: Reading configuration settings.
    """
    # Reading global variables (no 'global' keyword needed)
    print(f"  Database URL (global): {DATABASE_URL}")
    print(f"  Debug mode (global): {DEBUG_MODE}")
    print(f"  Max connections (global): {MAX_CONNECTIONS}")


CONNECTION_POOL_SIZE = 10  # Global


def modify_global_variable() -> None:
    """
    Demonstrates modifying global variables.
    
    Must use 'global' keyword to MODIFY global variables.
    
    Real-world use case: Updating global state, connection pools.
    """
    global CONNECTION_POOL_SIZE
    
    print(f"  Before modification: {CONNECTION_POOL_SIZE}")
    CONNECTION_POOL_SIZE = 20
    print(f"  After modification: {CONNECTION_POOL_SIZE}")


def create_rate_limiter(max_calls: int, time_window: int) -> Callable:
    """
    Creates a rate limiter using closure and enclosing scope.
    
    Enclosing scope: variables from outer function are accessible
    in inner function (closure).
    
    Args:
        max_calls: Maximum calls allowed
        time_window: Time window in seconds
    
    Returns:
        Rate limiter function
    
    Real-world use case: API rate limiting, request throttling.
    """
    # ENCLOSING SCOPE (captured by closure)
    call_times: list = []
    
    def is_allowed() -> bool:
        """Inner function - has access to enclosing scope."""
        nonlocal call_times  # Access enclosing scope variable
        
        current_time = time.time()
        
        # Remove old timestamps outside window
        call_times  = [t for t in call_times if current_time - t < time_window]
        
        # Check if under limit
        if len(call_times) < max_calls:
            call_times.append(current_time)
            return True
        
        return False
    
    return is_allowed


def create_counter() -> Callable:
    """
    Creates a counter using closure.
    
    Demonstrates enclosing scope with state preservation.
    
    Returns:
        Counter function
    
    Real-world use case: Request counters, metrics tracking.
    """
    # ENCLOSING SCOPE
    count = 0
    
    def increment() -> int:
        nonlocal count  # Modify enclosing scope variable
        count += 1
        return count
    
    return increment


def demonstrate_legb_precedence() -> None:
    """
    Demonstrates LEGB lookup order.
    
    LEGB Rule:
    1. Local: Check function's local scope first
    2. Enclosing: Check enclosing function scopes
    3. Global: Check module's global scope
    4. Built-in: Check Python's built-in namespace
    
    Real-world use case: Understanding variable resolution.
    """
    # Global variable
    value = "global"
    
    def outer():
        # Enclosing variable
        value = "enclosing"
        
        def inner():
            # Local variable
            value = "local"
            print(f"    Local: {value}")  # Finds 'local' first
        
        inner()
        print(f"  Enclosing: {value}")
    
    outer()
    print(f"Global: {value}")


def main() -> None:
    """Main function demonstrating variable scopes."""
    print("="*70)
    print("VARIABLE SCOPES: LEGB RULE".center(70))
    print("="*70)
    
    print("\n[1] LOCAL SCOPE - Function-Specific Variables")
    print("=" * 70)
    demonstrate_local_scope()
    
    print("\n\n[2] GLOBAL SCOPE - Reading Configuration")
    print("=" * 70)
    demonstrate_global_access()
    
    print("\n\n[3] MODIFYING GLOBAL VARIABLES")
    print("=" * 70)
    print(f"Global CONNECTION_POOL_SIZE before: {CONNECTION_POOL_SIZE}")
    modify_global_variable()
    print(f"Global CONNECTION_POOL_SIZE after: {CONNECTION_POOL_SIZE}")
    
    print("\n\n[4] ENCLOSING SCOPE - Rate Limiter Closure")
    print("=" * 70)
    
    # Create rate limiter: max 3 calls per 2 seconds
    rate_limiter = create_rate_limiter(max_calls=3, time_window=2)
    
    print("Testing rate limiter (3 calls/2 seconds):")
    for i in range(5):
        allowed = rate_limiter()
        status = "✓ ALLOWED" if allowed else "✗ BLOCKED"
        print(f"  Call {i+1}: {status}")
    
    print("\n\n[5] ENCLOSING SCOPE - Counter Closure")
    print("=" * 70)
    
    # Create two independent counters
    counter1 = create_counter()
    counter2 = create_counter()
    
    print("Counter 1:")
    for _ in range(3):
        count = counter1()
        print(f"  Count: {count}")
    
    print("\nCounter 2 (independent):")
    for _ in range(2):
        count = counter2()
        print(f"  Count: {count}")
    
    print("\n\n[6] LEGB PRECEDENCE DEMONSTRATION")
    print("=" * 70)
    demonstrate_legb_precedence()
    
    print("\n\n[7] BUILT-IN SCOPE")
    print("=" * 70)
    print("Built-in functions available without import:")
    print(f"  len([1, 2, 3]) = {len([1, 2, 3])}")
    print(f"  max([1, 5, 3]) = {max([1, 5, 3])}")
    print(f"  abs(-42) = {abs(-42)}")
    print("\nNote: Don't shadow built-ins (e.g., don't name variable 'list')")
    
    print("\n" + "="*70)
    print("LEGB Rule Summary:")
    print("-" * 70)
    print("L - Local: Function's local variables")
    print("E - Enclosing: Variables in enclosing functions (closures)")
    print("G - Global: Module-level variables")
    print("B - Built-in: Python's built-in names")
    print("\nPython searches in this order: L → E → G → B")
    print("\nKeywords:")
    print("  • global: Modify global variables from function")
    print("  • nonlocal: Modify enclosing scope variables from nested function")
    print("="*70)


if __name__ == "__main__":
    main()