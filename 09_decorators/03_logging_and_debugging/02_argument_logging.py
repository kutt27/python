"""
Topic: Detailed Argument Logging.

Captures all positional (*args) and keyword (**kwargs) 
arguments for more helpful debugging logs.
"""

from functools import wraps

def debug_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Format args for printing
        args_str = ", ".join(repr(a) for a in args)
        kwargs_str = ", ".join(f"{k}={v!r}" for k, v in kwargs.items())
        
        all_args = ", ".join(filter(None, [args_str, kwargs_str]))
        print(f"🔍 Tracing: {func.__name__}({all_args})")
        
        result = func(*args, **kwargs)
        print(f"✅ Result: {result}")
        return result
    return wrapper

@debug_args
def update_profile(user_id, name, age=None):
    return "Done"

if __name__ == "__main__":
    update_profile(101, "Alice", age=25)
