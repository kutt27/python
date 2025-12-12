"""
Python Async: Blocking Code & Executors
========================================

Topic: Running blocking (synchronous) code in AsyncIO

Real-World Applications:
- Using legacy sync libraries (requests, SQLAlchemy sync)
- File I/O (which is blocking)
- CPU-heavy functions that freeze the event loop
"""

import asyncio
import time
import requests # Hypothetical sync library

def blocking_io_call(url: str):
    """
    Simulates a BLOCKING function (standard synchronous code).
    If run directly in async loop, it would freeze everything.
    """
    print(f"  [Sync] Requesting {url}...")
    time.sleep(1) # Blocks the thread!
    print(f"  [Sync] Done {url}")
    return 200

async def async_couroutine():
    """Proper async function."""
    print("  [Async] Doing async work...")
    await asyncio.sleep(0.5)
    print("  [Async] Async work done")

async def main():
    """Demonstrates running sync code in async loop."""
    print("="*70)
    print("BLOCKING CODE IN ASYNCIO".center(70))
    print("="*70)
    
    # 1. The Problem: Blocking calls freeze the loop
    # We won't demo the freeze here to save time, but trust me.
    
    # 2. The Solution: run_in_executor
    print("Running blocking calls in thread pool...")
    loop = asyncio.get_running_loop()
    
    start_time = time.time()
    
    # Submit blocking function to default ThreadPoolExecutor
    future1 = loop.run_in_executor(None, blocking_io_call, "http://example.com/1")
    future2 = loop.run_in_executor(None, blocking_io_call, "http://example.com/2")
    
    # Run async work concurrently!
    await async_couroutine()
    
    # Wait for blocking calls
    response1 = await future1
    response2 = await future2
    
    total_time = time.time() - start_time
    print("-" * 70)
    print(f"Total time: {total_time:.2f}s")
    print("Observation: Took ~1s, not 2s or 2.5s!")
    print("The sync calls ran in parallel threads, while async loop kept running.")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• NEVER call blocking code (time.sleep, requests.get) directly in async def")
    print("• Use `loop.run_in_executor(None, func, *args)`")
    print("• This offloads blocking work to a ThreadPool")
    print("• Essential for integrating legacy libraries")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())