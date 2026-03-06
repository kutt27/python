"""
Topic: Creating Threads.

Threads are lightweight, shared-memory concurrent tasks. 
They are perfect for I/O-bound tasks (network calls, file input, etc).
"""

import threading
import time

def task(name: str):
    """Function to run in a thread."""
    print(f"  [Thread-{name}] starting...")
    time.sleep(1) # Simulate I/O bound wait
    print(f"  [Thread-{name}] finished!")

if __name__ == "__main__":
    print("[Main] Creating manually controlled threads...")
    
    # Target: function to run, Args: tuple of arguments
    t1 = threading.Thread(target=task, args=("A",))
    t2 = threading.Thread(target=task, args=("B",))
    
    # 1. Start the threads
    t1.start()
    t2.start()
    
    # 2. Main thread continues immediately
    print("[Main] Threads are running concurrently...")
    
    # 3. Join threads to wait for their completion
    t1.join()
    t2.join()
    
    print("[Main] All threads finished. Exiting.")
