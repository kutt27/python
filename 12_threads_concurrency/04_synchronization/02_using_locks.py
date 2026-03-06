"""
Topic: Thread-Locks.

Using a Lock ensures that only one thread can execute a critical 
section of code at a time, preventing race conditions.
"""

import threading
import time

class Account:
    def __init__(self, balance=0):
        self.balance = balance
        self.lock = threading.Lock()

    def safe_deposit(self, amount: int):
        """Thread-safe update using a context manager."""
        with self.lock: # Acquires lock before code, releases after
            current = self.balance
            time.sleep(0.001) # Simulate complex work
            self.balance = current + amount

if __name__ == "__main__":
    acc = Account(0)
    threads = []
    
    print("Starting 50 safe deposits of $1...")
    for _ in range(50):
        t = threading.Thread(target=acc.safe_deposit, args=(1,))
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"Final Balance: ${acc.balance} (Should be 50)")
