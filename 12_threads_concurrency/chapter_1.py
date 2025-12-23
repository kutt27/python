"""
Python Concurrency: Threading Basics
=====================================

Topic: Creating and running threads using threading.Thread

Real-World Applications:
- Sending emails in background (I/O bound)
- Writing logs to disk
- API calls that don't need to block main execution
"""

import threading
import time
import random
from typing import List


def send_email_task(email_id: int, recipient: str):
    """
    Simulate an I/O bound task (sending email).
    Threads are excellent for I/O bound operations.
    """
    print(f"  [Thread-{email_id}] Starting email send to {recipient}...")
    
    # Simulate network latency (I/O)
    delay = random.uniform(0.5, 1.5)
    time.sleep(delay)
    
    print(f"  [Thread-{email_id}] ✓ Email sent to {recipient} ({delay:.2f}s)")


def main():
    """Demonstrates manual thread creation."""
    print("="*70)
    print("THREADING BASICS (I/O Bound)".center(70))
    print("="*70)
    
    users = ["alice@example.com", "bob@example.com", "charlie@example.com"]
    threads: List[threading.Thread] = []
    
    start_time = time.time()
    
    # 1. Create Threads
    print("Creating threads...")
    for i, user in enumerate(users, 1):
        # target: function to run
        # args: arguments to pass
        t = threading.Thread(target=send_email_task, args=(i, user))
        threads.append(t)
        t.start()  # Start immediately
    
    print(f"All {len(users)} threads started. Main thread continues...")
    
    # 2. Wait for completion (Join)
    # Without join(), main program might exit before threads finish
    for t in threads:
        t.join()
        
    total_time = time.time() - start_time
    print("-" * 70)
    print(f"All emails sent in {total_time:.2f} seconds.")
    print("Note: In sync version, this would take users * sum(delays)")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Threads run concurrently (interleaved execution)")
    print("• Best for I/O bound tasks (Network, File Ops)")
    print("• t.start(): Begins execution")
    print("• t.join(): Blocks calling thread until thread terminates")
    print("="*70)


if __name__ == "__main__":
    main()