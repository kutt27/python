"""
Topic: Inspecting Functions with the `inspect` module.

The `inspect` module provides advanced tools to look into 
function signatures and source code.
"""

import inspect

def greet(name: str, greeted_by: str = "System") -> str:
    """Returns a greeting string."""
    return f"Hello {name}, from {greeted_by}"

if __name__ == "__main__":
    # Get the function signature
    sig = inspect.signature(greet)
    print(f"Signature: {sig}")
    
    print("\nParameter Details:")
    for name, param in sig.parameters.items():
        print(f"  {name}:")
        print(f"    Type Hint: {param.annotation}")
        print(f"    Default:   {param.default}")

    # Return type
    print(f"\nReturns: {sig.return_annotation}")
