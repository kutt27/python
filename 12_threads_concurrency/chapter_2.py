"""
Python Concurrency: Multiprocessing Basics
===========================================

Topic: Creating and running processes with multiprocessing

Real-World Applications:
- Heavy numerical computations (Data Science)
- Image/Video processing
- CPU-bound tasks that need to bypass GIL
"""

import multiprocessing
import time
import os

def cpu_bound_task(number: int):
    """
    Simulate a heavy CPU task (calculating sum of squares).
    Processes get their own memory space and Python interpreter,
    bypassing the Global Interpreter Lock (GIL).
    """
    pid = os.getpid()
    print(f"  [Process-{pid}] Starting calculation for {number}...")
    
    # Heavy computation loop
    result = sum(i * i for i in range(10**7))
    
    print(f"  [Process-{pid}] ✓ Finished. Result preview: {result % 100}")


def main():
    """Demonstrates manual process creation."""
    print("="*70)
    print("MULTIPROCESSING BASICS (CPU Bound)".center(70))
    print("="*70)
    
    print(f"Main Process ID: {os.getpid()}")
    print(f"CPU Cores Available: {multiprocessing.cpu_count()}")
    
    processes = []
    start_time = time.time()
    
    # 1. Create Processes
    print("\nSpawning processes...")
    for i in range(3):
        p = multiprocessing.Process(target=cpu_bound_task, args=(i,))
        processes.append(p)
        p.start()
        
    print("All processes started. Waiting for completion...")
    
    # 2. Join (Wait)
    for p in processes:
        p.join()
        
    total_time = time.time() - start_time
    print("-" * 70)
    print(f"Total time: {total_time:.2f} seconds")
    print("Note: With threading, this would take ~3x longer due to GIL.")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Processes are heavier than threads (memory overhead)")
    print("• Each process has its own GIL (True parallelism)")
    print("• Best for CPU-bound tasks")
    print("• Use 'if __name__ == \"__main__\":' guard is MANDATORY on Windows")
    print("="*70)


if __name__ == "__main__":
    main()