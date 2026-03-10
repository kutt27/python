"""
Topic: Deadlocks.

Deadlocks occur when two or more tasks are waiting for each other 
to release locks. This stops the program's progress.
"""

import asyncio

async def worker_1(l1, l2):
    async with l1:
        print("  [Worker-1] Acquired Lock 1")
        await asyncio.sleep(0.1)
        print("  [Worker-1] Waiting for Lock 2...")
        async with l2:
            print("  [Worker-1] Success!")

async def worker_2(l1, l2):
    async with l2:
        print("  [Worker-2] Acquired Lock 2")
        await asyncio.sleep(0.1)
        print("  [Worker-2] Waiting for Lock 1...")
        async with l1:
            print("  [Worker-2] Success!")

async def main():
    lock_a = asyncio.Lock()
    lock_b = asyncio.Lock()
    
    print("Simulating potential deadlock...")
    try:
        # Use wait_for to prevent infinite hang
        await asyncio.wait_for(
            asyncio.gather(
                worker_1(lock_a, lock_b),
                worker_2(lock_a, lock_b) # Acquisition order is inconsistent!
            ),
            timeout=1.0
        )
    except asyncio.TimeoutError:
        print("\n[Main] ERROR: Application is deadlocked!")
        print("Worker 1 has Lock A, wants B. Worker 2 has Lock B, wants A.")

if __name__ == "__main__":
    asyncio.run(main())
