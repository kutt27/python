"""
Python Concurrency: Inter-Process Communication (Queue)
========================================================

Topic: Exchanging data between processes using Queues

Real-World Applications:
- Producer-Consumer pipelines
- Log aggregation
- Job distribution systems
"""

import multiprocessing
import time
import queue # For the Empty exception class

def producer(q: multiprocessing.Queue, count: int):
    """Produces items and puts them into the queue."""
    print("  [Producer] Starting...")
    for i in range(count):
        item = f"Job-{i+1}"
        print(f"  [Producer] Produced {item}")
        q.put(item)
        time.sleep(0.1) # Simulate production time
    
    # Signal completion
    q.put(None) 
    print("  [Producer] Done.")


def consumer(q: multiprocessing.Queue):
    """Consumes items from the queue."""
    print("  [Consumer] Starting...")
    while True:
        try:
            # Block until item available
            item = q.get(timeout=2) 
            
            if item is None:
                print("  [Consumer] Received stop signal.")
                break # Exit loop
                
            print(f"  [Consumer] Processing {item}...")
            time.sleep(0.2) # Simulate processing time
            
        except queue.Empty:
            print("  [Consumer] Queue empty/timeout.")
            break
            
    print("  [Consumer] Done.")


def main():
    """Demonstrates IPC with Queue."""
    print("="*70)
    print("IPC: PRODUCER-CONSUMER QUEUE".center(70))
    print("="*70)
    
    # Multiprocessing Queue is thread and process safe
    q = multiprocessing.Queue()
    
    p1 = multiprocessing.Process(target=producer, args=(q, 5))
    p2 = multiprocessing.Process(target=consumer, args=(q,))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Processes do not share memory space")
    print("• Use multiprocessing.Queue for data exchange")
    print("• Pipeline pattern: One process produces, another consumes")
    print("• Queue is pickle-based (objects must be serializable)")
    print("="*70)


if __name__ == "__main__":
    main()