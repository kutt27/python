"""
Topic: Race Conditions.

When two or more threads attempt to modify the same variable 
at the same time, the state can become corrupted.
"""

import threading
import time

class Counter:
    def __init__(self):
        self.value = 0

    def unsafe_update(self):
        """Not thread safe! The update isn't atomic."""
        local_copy = self.value
        # Simulate an unlucky context switch between read and write
        time.sleep(0.001)
        self.value = local_copy + 1

if __name__ == "__main__":
    c = Counter()
    threads = []
    
    print("Starting 100 unsafe updates...")
    for _ in range(100):
        t = threading.Thread(target=c.unsafe_update)
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Final Counter: {c.value} (Expected 100 if safe)")
    print("If result < 100, you have a race condition.")
