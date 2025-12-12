"""
Functional Python: Decorators
==============================

Topic: Decorators from a Functional Perspective

Concept:
Input: Function -> Output: Function
Decorators are essentially higher-order functions that apply composition.
"""

from functools import wraps
from typing import Callable, Any

# 1. Functional Decorator (Trace)
def trace(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        arg_str = ", ".join(map(str, args))
        print(f"➜ call {func.__name__}({arg_str})")
        
        result = func(*args, **kwargs)
        
        print(f"<- return {result}")
        return result
    return wrapper

# 2. Composition (Retry)
def retry(times: int):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(times):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"   (Try {i+1} failed: {e})")
            print("   (Giving up)")
            return None
        return wrapper
    return decorator

# Applying functions to functions
@retry(times=3)
@trace
def flaky_api_call(status: str) -> str:
    if status == "fail":
        raise ValueError("Network Error")
    return "Success Payload"


def main():
    print("="*70)
    print("FUNCTIONAL DECORATORS".center(70))
    print("="*70)
    
    print("\n[1] Successful Call")
    flaky_api_call("ok")
    
    print("\n[2] Failing Call with Retry")
    flaky_api_call("fail")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Decorators wrap behavior around functions")
    print("• Stacking decorators = Function Composition")
    print("• f(g(x)) -> @f then @g")
    print("="*70)


if __name__ == "__main__":
    main()
