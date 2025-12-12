"""
Python Async: Synchronization (Locks)
======================================

Topic: Race conditions in AsyncIO

Wait, race conditions in single-threaded async?
YES! If `await` happens during a multi-step update, state can change.

Real-World Applications:
- Controlling access to limited resources
- Updating shared caches
- Rate limiting tokens
"""

import asyncio

class SharedCounter:
    """Unsafe vs Safe counter."""
    
    def __init__(self):
        self.value = 0
        self.lock = asyncio.Lock()
        
    async def unsafe_increment(self):
        """
        Looks safe? No.
        If we 'await' in the middle, others can intervene.
        """
        temp = self.value
        # Simulate I/O or just yielding control
        await asyncio.sleep(0.001) 
        self.value = temp + 1
        
    async def safe_increment(self):
        """Protected by Async Lock."""
        async with self.lock:
            temp = self.value
            await asyncio.sleep(0.001)
            self.value = temp + 1


async def runner(counter, method_name, workers=100):
    """Run concurrent workers."""
    func = getattr(counter, method_name)
    tasks = [func() for _ in range(workers)]
    await asyncio.gather(*tasks)


async def main():
    """Demonstrates Async Race Conditions."""
    print("="*70)
    print("ASYNC SYNCHRONIZATION".center(70))
    print("="*70)
    
    # 1. Unsafe
    c1 = SharedCounter()
    await runner(c1, "unsafe_increment")
    print(f"Unsafe Counter (Expect 100): {c1.value}")
    if c1.value != 100:
        print("  ❌ RACE CONDITION! Context switched during update.")
        
    # 2. Safe
    c2 = SharedCounter()
    await runner(c2, "safe_increment")
    print(f"Safe Counter   (Expect 100): {c2.value}")
    print("  ✓ Correct.")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• AsyncIO is single-threaded, but concurrency issues exist")
    print("• Any `await` is a potential context switch point")
    print("• If an operation is not atomic (read-await-write), protect it")
    print("• Use `asyncio.Lock()` (similar to threading.Lock)")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())