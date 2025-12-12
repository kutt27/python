"""
Python Concurrency: ProcessPoolExecutor
========================================

Topic: Modern multiprocessing with concurrent.futures

Real-World Applications:
- Batch data processing
- Parallel encryption/hashing
- CPU-intensive ETL steps
"""

import concurrent.futures
import time
import math

def expensive_calculation(n: int) -> str:
    """
    Simulate CPU-intensive calculation (prime factorization or similar).
    """
    print(f"  [Worker] Processing {n}...")
    # Simulate heavy math
    math.factorial(50000 + n) 
    return f"Factorial({50000+n}) Calculated"


def main():
    """Demonstrates ProcessPoolExecutor."""
    print("="*70)
    print("PROCESS POOL EXECUTOR".center(70))
    print("="*70)
    
    numbers = [1, 2, 3, 4]
    
    print(f"Submitting {len(numbers)} heavy tasks...")
    start_time = time.time()
    
    # ProcessPoolExecutor uses typical 'number of cores' workers by default
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # Submit tasks
        results = executor.map(expensive_calculation, numbers)
        
        # Iterate results
        for res in results:
            print(f"  ✓ {res}")
            
    total_time = time.time() - start_time
    print("-" * 70)
    print(f"Total time: {total_time:.2f}s")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Higher abstraction than multiprocessing.Process")
    print("• Handles pool management and worker reuse")
    print("• Best practice for modern CPU parallelism")
    print("• Remember: Arguments must be pickleable (serializable)")
    print("="*70)


if __name__ == "__main__":
    main()