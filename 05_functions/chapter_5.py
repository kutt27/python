"""
Python Functions: Execution Trace and Call Stack
=================================================

Topic: Understanding function execution flow, debugging

Real-World Applications:
- Debugging production issues
- Understanding performance bottlenecks
- Logging function calls
- Tracing data transformations
- Profiling applications
"""

from typing import List, Dict
from functools import wraps
import time


def trace_execution(func):
    """
    Decorator to trace function execution.
    
    Prints function name, arguments, and return value.
    Useful for debugging and understanding execution flow.
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        func_name = func.__name__
        print(f"  → Calling: {func_name}({args}, {kwargs})")
        
        result = func(*args, **kwargs)
        
        print(f"  ← Returned: {result}")
        return result
    
    return wrapper


@trace_execution
def calculate_subtotal(items: List[Dict]) -> float:
    """Calculates order subtotal."""
    total = sum(item['price'] * item['quantity'] for item in items)
    return total


@trace_execution
def apply_discount(subtotal: float, discount_percent: float) -> float:
    """Applies discount to subtotal."""
    discount = subtotal * (discount_percent / 100)
    return subtotal - discount


@trace_execution
def calculate_tax(amount: float, tax_rate: float) -> float:
    """Calculates tax on amount."""
    return amount * tax_rate


@trace_execution
def calculate_order_total(items: List[Dict], discount_percent: float = 0, tax_rate: float = 0.08) -> float:
    """
    Calculates final order total.
    
    Execution trace shows the call stack:
    1. calculate_order_total called
    2.   ↳ calls calculate_subtotal
    3.   ↳ calls apply_discount
    4.   ↳ calls calculate_tax
    5. calculate_order_total returns
    
    Args:
        items: Order items
        discount_percent: Discount percentage
        tax_rate: Tax rate
    
    Returns:
        Final total
    
    Real-world use case: Order processing with debugging.
    """
    # Step 1: Calculate subtotal
    subtotal = calculate_subtotal(items)
    
    # Step 2: Apply discount
    discounted = apply_discount(subtotal, discount_percent)
    
    # Step 3: Calculate tax
    tax = calculate_tax(discounted, tax_rate)
    
    # Step 4: Final total
    total = discounted + tax
    
    return total


def recursive_fibonacci(n: int, depth: int = 0) -> int:
    """
    Calculates Fibonacci number recursively with trace.
    
    Shows recursive call stack depth.
    
    Args:
        n: Fibonacci number to calculate
        depth: Current recursion depth (for visualization)
    
    Returns:
        Fibonacci number
    
    Real-world use case: Understanding recursion, debugging recursive algorithms.
    """
    indent = "  " * depth
    print(f"{indent}→ fib({n})")
    
    if n <= 1:
        print(f"{indent}← fib({n}) = {n}")
        return n
    
    result = recursive_fibonacci(n - 1, depth + 1) + recursive_fibonacci(n - 2, depth + 1)
    print(f"{indent}← fib({n}) = {result}")
    return result


def process_data_pipeline(data: List[Dict]) -> List[Dict]:
    """
    Data processing pipeline with execution trace.
    
    Shows each transformation step clearly.
    
    Args:
        data: Input data
    
    Returns:
        Processed data
    
    Real-world use case: ETL debugging, data transformation tracking.
    """
    print("\n=== DATA PIPELINE EXECUTION TRACE ===")
    
    print("\n[Step 1] Input Data:")
    print(f"  {len(data)} records")
    
    # Step 1: Filter
    print("\n[Step 2] Filtering invalid records...")
    filtered = [item for item in data if item.get('valid', True)]
    print(f"  Kept {len(filtered)}/{len(data)} records")
    
    # Step 2: Transform
    print("\n[Step 3] Transforming data...")
    transformed = []
    for item in filtered:
        transformed_item = {
            **item,
            'processed': True,
            'value_doubled': item.get('value', 0) * 2
        }
        transformed.append(transformed_item)
        print(f"  Transformed: {item.get('id')} → value={transformed_item['value_doubled']}")
    
    # Step 3: Sort
    print("\n[Step 4] Sorting by value...")
    sorted_data = sorted(transformed, key=lambda x: x['value_doubled'], reverse=True)
    print(f"  Sorted {len(sorted_data)} records")
    
    print("\n[Step 5] Pipeline Complete")
    return sorted_data


def main() -> None:
    """Main function demonstrating execution trace."""
    print("="*70)
    print("FUNCTION EXECUTION TRACE & CALL STACK".center(70))
    print("="*70)
    
    print("\n[1] ORDER CALCULATION - Traced Execution")
    print("="*70)
    
    order_items = [
        {"name": "Laptop", "price": 999.99, "quantity": 1},
        {"name": "Mouse", "price": 29.99, "quantity": 2},
    ]
    
    print("\nTracing order calculation:")
    total = calculate_order_total(order_items, discount_percent=10, tax_rate=0.08)
    
    print(f"\nFinal Total: ${total:.2f}")
    
    print("\n\n[2] RECURSIVE FIBONACCI - Call Stack Visualization")
    print("="*70)
    
    print("\nCalculating fib(5):")
    result = recursive_fibonacci(5)
    print(f"\nResult: {result}")
    
    print("\n\n[3] DATA PIPELINE - Step-by-Step Trace")
    print("="*70)
    
    input_data = [
        {"id": 1, "value": 100, "valid": True},
        {"id": 2, "value": 50, "valid": False},
        {"id": 3, "value": 200, "valid": True},
        {"id": 4, "value": 75, "valid": True},
    ]
    
    processed = process_data_pipeline(input_data)
    
    print("\n\n" + "="*70)
    print("Benefits of Execution Tracing:")
    print("-" * 70)
    print("✓ Debugging: See exactly what your code is doing")
    print("✓ Performance: Identify slow functions")
    print("✓ Understanding: Visualize call stack and data flow")
    print("✓ Testing: Verify function calls and arguments")
    print("✓ Logging: Track operations in production")
    print("\nTools: logging module, debuggers (pdb), profilers (cProfile)")
    print("="*70)


if __name__ == "__main__":
    main()