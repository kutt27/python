"""
Python Concurrency: The GIL (Threading)
========================================

Topic: Global Interpreter Lock limitations with CPU-bound tasks

Real-World Context:
- Why Python threads are slow for CPU work
- Understanding when NOT to use threads
"""

import threading
import time

def heavy_computation():
    """Simulate heavy CPU work."""
    _ = [x**2 for x in range(10**7)]

def main():
    """Demonstrates GIL impact on threads."""
    print("="*70)
    print("THE GIL DEMO: THREADING (CPU Bound)".center(70))
    print("="*70)
    
    start_time = time.time()
    
    # 1. Sequential Execution (Baseline)
    print("Running sequentially (2x)...")
    heavy_computation()
    heavy_computation()
    
    seq_time = time.time() - start_time
    print(f"Sequential Time: {seq_time:.2f}s")
    
    # 2. Threaded Execution
    print("\nRunning with threads (2x)...")
    t1 = threading.Thread(target=heavy_computation)
    t2 = threading.Thread(target=heavy_computation)
    
    start_thread = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    thread_time = time.time() - start_thread
    print(f"Threaded Time:   {thread_time:.2f}s")
    
    print("-" * 70)
    print("Analysis:")
    if thread_time >= seq_time:
        print("⚠ Threads were SLOWER or SAME speed!")
        print("Reason: The GIL prevents threads from running Python bytecodes")
        print("simultaneously on multiple cores.")
    else:
        # Uncommon for pure Python code, might happen if system is weirdly loaded
        print("Threads were faster (Unexpected for pure Python CPU task!)")
        
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• Do NOT use standard threads for CPU-Intensive work")
    print("• The GIL enforces one thread at a time per process")
    print("• Use Multiprocessing for CPU tasks instead")
    print("="*70)


if __name__ == "__main__":
    main()