"""
Topic: Execution Timing Decorator.

A practical decorator to measure how long a function takes 
to execute.
"""

from functools import wraps
import time

def time_it(func):
    """Timer that prints execution time."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱  {func.__name__} took: {end - start:.4f}s")
        return result
    return wrapper

@time_it
def heavy_process():
    print("Working...")
    time.sleep(0.5)
    return "Done"

if __name__ == "__main__":
    heavy_process()
