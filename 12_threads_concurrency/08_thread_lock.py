"""
Python Concurrency: Locks & Synchronization
============================================

Topic: Race conditions and threading.Lock

Real-World Applications:
- Shared counters (stats, limits)
- Bank transaction processing
- Updating shared resources safely
"""

import threading
import time
from typing import List

class BankAccount:
    """Shared resource typical of race condition scenarios."""
    
    def __init__(self, balance: int = 0):
        self.balance = balance
        self.lock = threading.Lock()
        
    def unsafe_deposit(self, amount: int):
        """
        RACE CONDITION VULNERABLE!
        Read-Modify-Write cycle is not atomic.
        """
        current = self.balance
        # Simulate context switch happening here
        time.sleep(0.001) 
        self.balance = current + amount
        
    def safe_deposit(self, amount: int):
        """
        THREAD SAFE using Lock.
        Only one thread can execute this block at a time.
        """
        # Context Manager acquires lock on enter, releases on exit
        with self.lock:
            current = self.balance
            time.sleep(0.001) # Even with sleep, lock protects state
            self.balance = current + amount


def run_test(account: BankAccount, method_name: str, num_threads: int):
    """Run concurrent deposit test."""
    print(f"\nTesting: {method_name} with {num_threads} threads...")
    
    threads = []
    deposit_func = getattr(account, method_name)
    
    for _ in range(num_threads):
        t = threading.Thread(target=deposit_func, args=(1,)) # Deposit $1
        threads.append(t)
        t.start()
        
    for t in threads:
        t.join()
        
    print(f"  Expected Balance: ${num_threads}")
    print(f"  Actual Balance:   ${account.balance}")
    
    if account.balance != num_threads:
        print("  ❌ RACE CONDITION DETECTED!")
    else:
        print("  ✓ Data Consistent")


def main():
    """Demonstrates Race Conditions vs Locks."""
    print("="*70)
    print("SYNCHRONIZATION & LOCKS".center(70))
    print("="*70)
    
    # 1. Unsafe Test
    bad_account = BankAccount()
    run_test(bad_account, "unsafe_deposit", 100)
    
    # 2. Safe Test
    good_account = BankAccount()
    run_test(good_account, "safe_deposit", 100)
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Race Condition: Multiple threads modify shared state simultaneously")
    print("• Result depends on unlucky timing of thread switches")
    print("• threading.Lock(): Ensures mutual exclusion")
    print("• Use 'with lock:' pattern to guarantee release (even on error)")
    print("="*70)


if __name__ == "__main__":
    main()