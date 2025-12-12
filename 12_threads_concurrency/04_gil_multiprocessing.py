"""
Python Concurrency: Bypassing the GIL
======================================

Topic: Using Multiprocessing to bypass the GIL

Real-World Context:
- Utilizing all CPU cores
- High-performance Python computing
"""

import multiprocessing
import time

def heavy_computation():
    """Simulate heavy CPU work."""
    _ = [x**2 for x in range(10**7)]

def main():
    """Demonstrates Parallelism with Processes."""
    print("="*70)
    print("BYPASSING GIL: MULTIPROCESSING".center(70))
    print("="*70)
    
    # Recalculate baseline for fair comparison
    start_time = time.time()
    print("Ref: Sequential run (1x)...")
    heavy_computation()
    single_run_time = time.time() - start_time
    print(f"Single run approx: {single_run_time:.2f}s")
    
    # Run with Processes
    print("\nRunning with 2 Processes (Parallel)...")
    p1 = multiprocessing.Process(target=heavy_computation)
    p2 = multiprocessing.Process(target=heavy_computation)
    
    start_proc = time.time()
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
    proc_time = time.time() - start_proc
    print(f"Multiprocessing Time: {proc_time:.2f}s")
    
    print("-" * 70)
    print("Analysis:")
    ideal_time = single_run_time # Ideally 2 cores do 2 jobs in time of 1
    overhead = proc_time - ideal_time
    
    print(f"Speedup vs Sequential (2 jobs): { (single_run_time * 2) / proc_time :.2f}x")
    print("(Ideal is 2.0x, reality is slightly less due to creation overhead)")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Multiprocessing creates separate Interpreters")
    print("• Each has its own GIL, so they run in PARALLEL")
    print("• Use this for CPU-heavy tasks to utilize multi-core CPUs")
    print("="*70)


if __name__ == "__main__":
    main()
