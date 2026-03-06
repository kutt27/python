"""
Topic: I/O Bound Tasks with Threads.

Threads excel when the program is waiting for external resources 
(network, database, user input). Python's GIL is released 
during blocking I/O calls.
"""

import threading
import time
import random

def download_resource(name: str):
    """Simulates a network download (I/O activity)."""
    duration = random.uniform(1, 3)
    print(f"  -> Downloading {name} (est: {duration:.1f}s)...")
    time.sleep(duration) # Thread yields to others during sleep
    print(f"  <- Finished {name}!")

if __name__ == "__main__":
    resources = ["Image-1.jpg", "Image-2.jpg", "Image-3.jpg", "Image-4.jpg"]
    threads = []
    
    start = time.time()
    
    for res in resources:
        t = threading.Thread(target=download_resource, args=(res,))
        threads.append(t)
        t.start()
    
    for t in threads:
        t.join()
        
    print(f"\nTotal time: {time.time() - start:.2f}s")
    print("Sequential execution would have taken ~8s.")
