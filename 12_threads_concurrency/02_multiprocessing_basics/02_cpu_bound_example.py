"""
Topic: CPU-Bound Parallelism.

Processes are ideal for heavy mathematical or data-processing 
tasks. Each process runs on a different CPU core simultaneously.
"""

import multiprocessing
import time

def calculate_squares(n: int):
    """Simulate heavy CPU calculation."""
    _ = [i * i for i in range(n)]

if __name__ == "__main__":
    n = 10**7 # Heavy task
    
    # 1. Sequential run (baseline)
    start_seq = time.time()
    calculate_squares(n)
    calculate_squares(n)
    print(f"Sequential Time: {time.time() - start_seq:.2f}s")
    
    # 2. Parallel run with Processes
    p1 = multiprocessing.Process(target=calculate_squares, args=(n,))
    p2 = multiprocessing.Process(target=calculate_squares, args=(n,))
    
    start_proc = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print(f"Parallel Time:   {time.time() - start_proc:.2f}s (Speedup!)")
