"""
Python Async: Deadlocks
========================

Topic: How to create (and avoid) deadlocks in AsyncIO

Real-World Scenario:
- Circular dependencies in resource locking
- Infinite waits for events that never trigger
"""

import asyncio

async def worker_a(lock1, lock2):
    """Acquires Lock 1, then wants Lock 2."""
    async with lock1:
        print("  [A] Acquired Lock 1")
        await asyncio.sleep(0.1) # Simulate holding
        print("  [A] Waiting for Lock 2...")
        async with lock2:
            print("  [A] Acquired Lock 2")

async def worker_b(lock1, lock2):
    """Acquires Lock 2, then wants Lock 1 (Circular Dependency)."""
    async with lock2:
        print("  [B] Acquired Lock 2")
        await asyncio.sleep(0.1) # Simulate holding
        print("  [B] Waiting for Lock 1...")
        async with lock1:
            print("  [B] Acquired Lock 1")


async def main():
    """Demonstrates deadlock."""
    print("="*70)
    print("ASYNC DEADLOCK SIMULATION".center(70))
    print("="*70)
    
    lock1 = asyncio.Lock()
    lock2 = asyncio.Lock()
    
    print("Starting workers with circular dependency...")
    
    # We use wait_for to prevent this script solely hanging forever for the demo
    try:
        await asyncio.wait_for(
            asyncio.gather(
                worker_a(lock1, lock2),
                worker_b(lock1, lock2)
            ),
            timeout=2.0
        )
    except asyncio.TimeoutError:
        print("\n  ❌ DEADLOCK DETECTED! (Timed out)")
        print("  Worker A holds Lock 1, wants Lock 2")
        print("  Worker B holds Lock 2, wants Lock 1")
    
    print("\n" + "="*70)
    print("Prevention Tips:")
    print("• Always acquire locks in the SAME ORDER across all tasks")
    print("• Use timeouts (wait_for) to fail fast")
    print("• Avoid nested locks if possible")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())