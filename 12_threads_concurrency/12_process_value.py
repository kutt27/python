"""
Python Concurrency: Shared State (Value & Array)
=================================================

Topic: Sharing memory between processes safely

Real-World Applications:
- Shared counters across worker processes
- Shared data buffers
- Performance optimization (avoiding serialization overhead)
"""

import multiprocessing
import ctypes # For C types

def increment_worker(shared_val: multiprocessing.Value, lock: multiprocessing.Lock):
    """Increments a shared counter 100 times."""
    for _ in range(100):
        # Must use lock to prevent race conditions even in processes
        with lock:
            shared_val.value += 1

def update_array(shared_arr: multiprocessing.Array):
    """Squared elements of shared array."""
    # Array doesn't need lock if each process works on different indices
    # But here we just iterate
    for i in range(len(shared_arr)):
        shared_arr[i] = shared_arr[i] * shared_arr[i]

def main():
    """Demonstrates shared memory."""
    print("="*70)
    print("SHARED MEMORY (Value & Array)".center(70))
    print("="*70)
    
    # 1. Shared Value (Single number)
    # 'i' = signed int
    counter = multiprocessing.Value('i', 0) 
    lock = multiprocessing.Lock()
    
    print("\n[Shared Value Counter]")
    workers = []
    for _ in range(4):
        p = multiprocessing.Process(target=increment_worker, args=(counter, lock))
        workers.append(p)
        p.start()
        
    for p in workers:
        p.join()
        
    print(f"Final Counter (Expected 400): {counter.value}")
    
    # 2. Shared Array (List of primitives)
    print("\n[Shared Array]")
    # 'i' = signed int, initialized with list
    arr = multiprocessing.Array('i', [1, 2, 3, 4, 5])
    
    print(f"Original: {list(arr)}")
    
    p = multiprocessing.Process(target=update_array, args=(arr,))
    p.start()
    p.join()
    
    print(f"Modified: {list(arr)}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Processes usually isolate memory")
    print("• Use Value/Array for small shared primitives")
    print("• Still requires Lock for atomic updates!")
    print("• For complex objects (dicts/lists), use multiprocessing.Manager()")
    print("="*70)


if __name__ == "__main__":
    main()