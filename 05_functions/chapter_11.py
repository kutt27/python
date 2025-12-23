"""
Python Function Types: Pure, Impure, Recursive, Lambda
=======================================================

Topic: Different function categories and their characteristics

Real-World Applications:
- Functional programming patterns
- Algorithm implementation (recursion)
- Inline transformations (lambda)
- Testable code design (pure functions)
- Side-effect management (impure functions)
"""

from typing import List, Dict, Callable
from functools import reduce


# ==============================================================================
# PURE FUNCTIONS: No side effects, same input → same output
# ==============================================================================

def calculate_total(price: float, quantity: int, tax_rate: float = 0.08) -> float:
    """
    Pure function: calculates total with no side effects.
    
    Characteristics:
    - No external state modification
    - No I/O operations
    - Deterministic: same inputs → same output
    - Easy to test and reason about
    
    Args:
        price: Unit price
        quantity: Quantity
        tax_rate: Tax rate
    
    Returns:
        Total amount
    
    Real-world use case: Calculations, data transformations.
    """
    subtotal = price * quantity
    tax = subtotal * tax_rate
    return subtotal + tax


def filter_active_users(users: List[Dict]) -> List[Dict]:
    """
    Pure function: filters users without modifying input.
    
    Args:
        users: List of user dictionaries
    
    Returns:
        New list of active users
    
    Real-world use case: Data filtering, functional pipelines.
    """
    # Returns new list, doesn't modify input
    return [user for user in users if user.get("is_active", False)]


# ==============================================================================
# IMPURE FUNCTIONS: Have side effects (I/O, state modification, etc.)
# ==============================================================================

REQUEST_COUNT = 0  # Global state

def log_request_impure(endpoint: str) -> None:
    """
    Impure function: modifies global state and performs I/O.
    
    Side effects:
    - Modifies global REQUEST_COUNT
    - Prints to console (I/O)
    
    Args:
        endpoint: API endpoint
    
    Real-world use case: Logging, metrics collection.
    """
    global REQUEST_COUNT
    REQUEST_COUNT += 1
    print(f"[{REQUEST_COUNT}] Request to {endpoint}")


def save_to_database_impure(data: Dict) -> bool:
    """
    Impure function: performs I/O operation.
    
    Side effect: Database write (simulated with print)
    
    Args:
        data: Data to save
    
    Returns:
        Success status
    
    Real-world use case: Database operations, file I/O.
    """
    print(f"Saving to database: {data}")
    # In real app: actual database write
    return True


# ==============================================================================
# RECURSIVE FUNCTIONS: Functions that call themselves
# ==============================================================================

def factorial(n: int) -> int:
    """
    Recursive function: calculates factorial.
    
    Base case: n <= 1 returns 1
    Recursive case: n * factorial(n - 1)
    
    Args:
        n: Number to calculate factorial for
    
    Returns:
        Factorial of n
    
    Real-world use case: Mathematical calculations, tree traversal.
    """
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def calculate_folder_size(folder: Dict) -> int:
    """
    Recursive function: calculates total size of folder hierarchy.
    
    Args:
        folder: Folder dictionary with 'size' and optional 'subfolders'
    
    Returns:
        Total size in bytes
    
    Real-world use case: File system operations, tree processing.
    """
    # Base case: folder's own size
    total = folder.get("size", 0)
    
    # Recursive case: add sizes of all subfolders
    for subfolder in folder.get("subfolders", []):
        total += calculate_folder_size(subfolder)
    
    return total


def traverse_json(obj: any, path: str = "") -> None:
    """
    Recursive function: traverses nested JSON structure.
    
    Args:
        obj: JSON object (dict, list, or primitive)
        path: Current path in the structure
    
    Real-world use case: JSON validation, data extraction.
    """
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_path = f"{path}.{key}" if path else key
            traverse_json(value, new_path)
    
    elif isinstance(obj, list):
        for i, item in enumerate(obj):
            new_path = f"{path}[{i}]"
            traverse_json(item, new_path)
    
    else:
        # Primitive value
        print(f"  {path}: {obj}")


# ==============================================================================
# LAMBDA FUNCTIONS: Anonymous, inline functions
# ==============================================================================

def demonstrate_lambda_functions() -> None:
    """Demonstrates lambda function usage."""
    
    print("\n[LAMBDA] Sorting")
    users = [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
    
    # Lambda as sort key
    sorted_users = sorted(users, key=lambda u: u["age"])
    print(f"  Sorted by age: {[u['name'] for u in sorted_users]}")
    
    print("\n[LAMBDA] Filtering")
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Lambda for filtering
    evens = list(filter(lambda x: x % 2 == 0, numbers))
    print(f"  Even numbers: {evens}")
    
    print("\n[LAMBDA] Mapping")
    # Lambda for transformation
    squared = list(map(lambda x: x ** 2, numbers))
    print(f"  Squared: {squared}")
    
    print("\n[LAMBDA] Reducing")
    # Lambda for reduction
    total = reduce(lambda acc, x: acc + x, numbers)
    print(f"  Sum: {total}")


# ==============================================================================
# HIGHER-ORDER FUNCTIONS: Functions that take or return functions
# ==============================================================================

def create_multiplier(factor: int) -> Callable:
    """
    Higher-order function: returns a function.
    
    Args:
        factor: Multiplication factor
    
    Returns:
        Function that multiplies by factor
    
    Real-world use case: Factory functions, closures.
    """
    return lambda x: x * factor


def apply_to_list(func: Callable, items: List) -> List:
    """
    Higher-order function: takes a function as argument.
    
    Args:
        func: Function to apply
        items: List of items
    
    Returns:
        Transformed list
    
    Real-world use case: Functional programming, pipelines.
    """
    return [func(item) for item in items]


def main() -> None:
    """Main function demonstrating function types."""
    print("="*70)
    print("FUNCTION TYPES: Pure, Impure, Recursive, Lambda".center(70))
    print("="*70)
    
    print("\n[1] PURE FUNCTIONS - No Side Effects")
    print("=" * 70)
    
    total1 = calculate_total(100, 2, 0.08)
    total2 = calculate_total(100, 2, 0.08)  # Same inputs → same output
    
    print(f"Total 1: ${total1:.2f}")
    print(f"Total 2: ${total2:.2f}")
    print(f"Deterministic: {total1 == total2}")
    
    users_list = [
        {"id": 1, "name": "Alice", "is_active": True},
        {"id": 2, "name": "Bob", "is_active": False},
        {"id": 3, "name": "Charlie", "is_active": True},
    ]
    
    active = filter_active_users(users_list)
    print(f"\nActive users: {[u['name'] for u in active]}")
    
    print("\n\n[2] IMPURE FUNCTIONS - Have Side Effects")
    print("=" * 70)
    
    log_request_impure("/api/users")
    log_request_impure("/api/products")
    log_request_impure("/api/orders")
    
    print(f"\nGlobal REQUEST_COUNT modified: {REQUEST_COUNT}")
    
    save_to_database_impure({"user_id": 101, "action": "login"})
    
    print("\n\n[3] RECURSIVE FUNCTIONS")
    print("=" * 70)
    
    print("Factorial calculation:")
    for n in [1, 5, 10]:
        result = factorial(n)
        print(f"  {n}! = {result}")
    
    print("\nFolder size calculation:")
    file_system = {
        "name": "root",
        "size": 100,
        "subfolders": [
            {
                "name": "documents",
                "size": 500,
                "subfolders": [
                    {"name": "reports", "size": 300}
                ]
            },
            {"name": "downloads", "size": 1200}
        ]
    }
    
    total_size = calculate_folder_size(file_system)
    print(f"  Total size: {total_size} bytes")
    
    print("\nJSON traversal:")
    data = {
        "user": {
            "name": "Alice",
            "contacts": ["alice@example.com", "555-1234"]
        },
        "settings": {"theme": "dark", "notifications": True}
    }
    traverse_json(data)
    
    print("\n\n[4] LAMBDA FUNCTIONS")
    print("=" * 70)
    demonstrate_lambda_functions()
    
    print("\n\n[5] HIGHER-ORDER FUNCTIONS")
    print("=" * 70)
    
    # Function returns function (closure)
    double = create_multiplier(2)
    triple = create_multiplier(3)
    
    print(f"double(5) = {double(5)}")
    print(f"triple(5) = {triple(5)}")
    
    # Function takes function
    numbers = [1, 2, 3, 4, 5]
    doubled = apply_to_list(lambda x: x * 2, numbers)
    print(f"\nApply doubling: {doubled}")
    
    print("\n" + "="*70)
    print("Function Types Summary:")
    print("-" * 70)
    print("Pure Functions:")
    print("  ✓ No side effects, deterministic")
    print("  ✓ Easy to test, reason about, and parallelize")
    print("  ✓ Preferred for calculations and transformations")
    
    print("\nImpure Functions:")
    print("  • Have side effects (I/O, state modification)")
    print("  • Necessary for real applications")
    print("  • Keep side effects isolated and documented")
    
    print("\nRecursive Functions:")
    print("  • Call themselves with simpler inputs")
    print("  • Require base case to prevent infinite recursion")
    print("  • Great for tree/graph traversal, divide-and-conquer")
    
    print("\nLambda Functions:")
    print("  • Anonymous, inline functions")
    print("  • Best for simple, one-line operations")
    print("  • Use named functions for complex logic")
    
    print("="*70)


if __name__ == "__main__":
    main()