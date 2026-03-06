"""
Topic: Process Synchronization.

Even with separate memory space, processes sometimes need to 
synchronize access to shared external resources or shared memory.
"""

import multiprocessing
import time

def update_counter(val, lock):
    """Safe update for a shared value."""
    for _ in range(10):
        time.sleep(0.01)
        with lock:
            val.value += 1

if __name__ == "__main__":
    # Shared primitive using multiprocessing.Value
    # 'i' means signed integer
    counter = multiprocessing.Value('i', 0)
    lock = multiprocessing.Lock()
    
    processes = [multiprocessing.Process(target=update_counter, args=(counter, lock)) 
                 for _ in range(5)]
    
    for p in processes:
        p.start()
    for p in processes:
        p.join()
        
    print(f"Shared Counter result: {counter.value} (Expected 50)")
