"""
Python Built-in Functions and Introspection
============================================

Topic: Built-in functions, function metadata, introspection

Real-World Applications:
- Dynamic function inspection
- Documentation generation
- Testing and debugging
- Plugin systems
- API documentation
"""

from typing import Callable, List, Dict
import inspect


def calculate_discount(amount: float, discount_percent: float = 10) -> float:
    """
    Calculates discounted amount.
    
    This is a sample function to demonstrate introspection.
    
    Args:
        amount: Original amount
        discount_percent: Discount percentage (default: 10%)
    
    Returns:
        Discounted amount
    
    Examples:
        >>> calculate_discount(100, 20)
        80.0
        >>> calculate_discount(50)
        45.0
    """
    return amount * (1 - discount_percent / 100)


def demonstrate_function_metadata() -> None:
    """Demonstrates function metadata and introspection."""
    
    print("\n[METADATA] Function Attributes")
    print("-" * 70)
    
    # Function name
    print(f"Function name: {calculate_discount.__name__}")
    
    # Docstring
    print(f"\nDocstring:\n{calculate_discount.__doc__}")
    
    # Module
    print(f"Module: {calculate_discount.__module__}")
    
    # Annotations (type hints)
    print(f"\nAnnotations: {calculate_discount.__annotations__}")
    
    # Defaults
    print(f"Defaults: {calculate_discount.__defaults__}")


def demonstrate_inspection() -> None:
    """Demonstrates function inspection with inspect module."""
    
    print("\n[INSPECTION] Using inspect Module")
    print("-" * 70)
    
    # Get signature
    sig = inspect.signature(calculate_discount)
    print(f"Signature: {sig}")
    
    # Parameters
    print("\nParameters:")
    for param_name, param in sig.parameters.items():
        default = param.default if param.default != inspect.Parameter.empty else "no default"
        annotation = param.annotation if param.annotation != inspect.Parameter.empty else "no type hint"
        print(f"  {param_name}: {annotation} (default: {default})")
    
    # Return annotation
    return_type = sig.return_annotation
    print(f"\nReturn type: {return_type}")
    
    # Source code
    source = inspect.getsource(calculate_discount)
    print(f"\nSource code:\n{source[:200]}...")  # First 200 chars


def demonstrate_built_in_functions() -> None:
    """Demonstrates commonly used built-in functions."""
    
    print("\n[BUILT-IN] Commonly Used Functions")
    print("-" * 70)
    
    # len()
    data = [1, 2, 3, 4, 5]
    print(f"len([1,2,3,4,5]): {len(data)}")
    
    # max(), min(), sum()
    print(f"max(): {max(data)}")
    print(f"min(): {min(data)}")
    print(f"sum(): {sum(data)}")
    
    # sorted()
    unsorted = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"\nsorted([3,1,4,1,5,9,2,6]): {sorted(unsorted)}")
    
    # reversed()
    print(f"list(reversed([1,2,3])): {list(reversed([1, 2, 3]))}")
    
    # enumerate()
    print("\nenumerate(['a','b','c']):")
    for i, letter in enumerate(['a', 'b', 'c']):
        print(f"  {i}: {letter}")
    
    # zip()
    names = ['Alice', 'Bob']
    ages = [30, 25]
    print(f"\nzip(names, ages): {list(zip(names, ages))}")
    
    # all(), any()
    print(f"\nall([True, True, True]): {all([True, True, True])}")
    print(f"any([False, False, True]): {any([False, False, True])}")
    
    # isinstance(), type()
    value = "hello"
    print(f"\nisinstance('hello', str): {isinstance(value, str)}")
    print(f"type('hello'): {type(value)}")


def demonstrate_callable_and_help() -> None:
    """Demonstrates callable() and help() functions."""
    
    print("\n[BUILT-IN] callable() and help()")
    print("-" * 70)
    
    # callable()
    print(f"callable(calculate_discount): {callable(calculate_discount)}")
    print(f"callable('not a function'): {callable('not a function')}")
    
    # help() - using __doc__ instead of actual help() for cleaner demo
    print(f"\nFunction help (from docstring):")
    print(f"{calculate_discount.__name__}: {calculate_discount.__doc__[:100]}...")


def validate_function_signature(func: Callable) -> Dict:
    """
    Validates and extracts function signature information.
    
    Real-world use case: API validation, documentation generation.
    
    Args:
        func: Function to inspect
    
    Returns:
        Dictionary with signature information
    """
    sig = inspect.signature(func)
    
    params_info = []
    for name, param in sig.parameters.items():
        params_info.append({
            "name": name,
            "type": str(param.annotation) if param.annotation != inspect.Parameter.empty else "Any",
            "has_default": param.default != inspect.Parameter.empty,
            "default": param.default if param.default != inspect.Parameter.empty else None
        })
    
    return {
        "function_name": func.__name__,
        "parameters": params_info,
        "return_type": str(sig.return_annotation) if sig.return_annotation != inspect.Signature.empty else "Any",
        "docstring": func.__doc__
    }


def main() -> None:
    """Main function demonstrating built-in functions."""
    print("="*70)
    print("BUILT-IN FUNCTIONS & INTROSPECTION".center(70))
    print("="*70)
    
    print("\n[1] FUNCTION METADATA")
    print("=" * 70)
    demonstrate_function_metadata()
    
    print("\n\n[2] FUNCTION INSPECTION")
    print("=" * 70)
    demonstrate_inspection()
    
    print("\n\n[3] COMMONLY USED BUILT-INS")
    print("=" * 70)
    demonstrate_built_in_functions()
    
    print("\n\n[4] CALLABLE AND HELP")
    print("=" * 70)
    demonstrate_callable_and_help()
    
    print("\n\n[5] SIGNATURE VALIDATION")
    print("=" * 70)
    
    signature_info = validate_function_signature(calculate_discount)
    
    print(f"\nFunction: {signature_info['function_name']}")
    print(f"Return type: {signature_info['return_type']}")
    print("\nParameters:")
    for param in signature_info['parameters']:
        default_str = f" = {param['default']}" if param['has_default'] else ""
        print(f"  {param['name']}: {param['type']}{default_str}")
    
    print("\n" + "="*70)
    print("Essential Built-in Functions:")
    print("-" * 70)
    print("Data Operations:")
    print("  • len(), max(), min(), sum() - aggregate operations")
    print("  • sorted(), reversed() - ordering")
    print("  • enumerate(), zip() - iteration helpers")
    
    print("\nType Checking:")
    print("  • isinstance(), type() - type inspection")
    print("  • callable() - check if object is callable")
    
    print("\nIntrospection (inspect module):")
    print("  • inspect.signature() - get function signature")
    print("  • inspect.getsource() - get source code")
    print("  • inspect.getmembers() - get object members")
    
    print("\nDocumentation:")
    print("  • help() - interactive help")
    print("  • __doc__ - docstring access")
    print("  • __name__ - function name")
    print("  • __annotations__ - type hints")
    
    print("\nUse Cases:")
    print("  ✓ API documentation generation")
    print("  ✓ Testing and validation")
    print("  ✓ Plugin systems")
    print("  ✓ Dynamic function calling")
    print("="*70)


if __name__ == "__main__":
    main()