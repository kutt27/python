"""
Topic: The GIL and Threading.

The Global Interpreter Lock (GIL) prevents multiple threads from 
running Python code at the same time. This is why threads don't 
speed up pure-Python CPU tasks.
"""

import threading
import time

def heavy_calc():
    """CPU intensive task."""
    _ = [x**2 for x in range(10**7)]

if __name__ == "__main__":
    # Two threads try to share the GIL for CPU-heavy work
    t1 = threading.Thread(target=heavy_calc)
    t2 = threading.Thread(target=heavy_calc)
    
    start = time.time()
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    
    print(f"Total time with Threads: {time.time() - start:.2f}s")
    print("Conclusion: Threads often take longer for CPU work due to GIL contention.")
