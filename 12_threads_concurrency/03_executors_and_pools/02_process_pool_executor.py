"""
Topic: ProcessPoolExecutor.

High-level interface for CPU parallelism. Ideal for processing 
large datasets or complex math in parallel across cores.
"""

from concurrent.futures import ProcessPoolExecutor
import math
import time

def calculate_factorial(n: int) -> int:
    """Heavy operation on a specific number."""
    print(f"  [Worker] Calculating factorial for {n}...")
    return len(str(math.factorial(n)))

if __name__ == "__main__":
    # List of massive numbers
    inputs = [10000, 20000, 30000, 40000]
    
    start = time.time()
    with ProcessPoolExecutor() as executor:
        # Map tasks across multiple processes
        results = executor.map(calculate_factorial, inputs)
        
        for res in results:
            print(f"  ✓ Digits in result: {res}")
    
    print(f"\nAll tasks finished in {time.time() - start:.2f}s")
