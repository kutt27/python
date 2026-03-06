"""
Topic: Inter-Process Queues.

Queues are the safest way to pass data between processes. 
They handle all the underlying locking/synchronization for you.
"""

import multiprocessing
import time

def producer(q: multiprocessing.Queue):
    """Worker that generates data."""
    for i in range(5):
        msg = f"Data-Packet-{i}"
        print(f"  [Producer] generating {msg}")
        q.put(msg)
        time.sleep(1)
    q.put(None) # Sentinel value (poison pill) to signal end

def consumer(q: multiprocessing.Queue):
    """Worker that processes data."""
    while True:
        msg = q.get() # Blocks until data is available
        if msg is None:
            break
        print(f"  [Consumer] processing {msg}...")
        time.sleep(0.5)

if __name__ == "__main__":
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=producer, args=(q,))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    print("[Main] Pipeline finished.")
