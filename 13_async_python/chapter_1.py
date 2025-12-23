"""
Python Async: Basics of Coroutines
===================================

Topic: async def, await, and the Event Loop

Real-World Applications:
- Scalable Web Servers (FastAPI/Django Async)
- High-concurrency chatbots
- WebSocket servers
"""

import asyncio
import time

# 1. Define a Coroutine
async def fetch_data(delay: float, source: str):
    """
    Simulates fetching data asynchronously.
    'await' pauses this function, yielding control back to the loop.
    """
    print(f"  [Start] Fetching from {source}...")
    
    # Non-blocking sleep (simulates network I/O)
    await asyncio.sleep(delay)
    
    print(f"  [Done]  {source}")
    return {"source": source, "data": "Sample Payload"}


# 2. Entry Point Coroutine
async def main():
    """Main entry point."""
    print("="*70)
    print("ASYNC BASICS".center(70))
    print("="*70)
    
    start_time = time.time()
    
    # Sequential await (not concurrent yet!)
    print("1. Sequential execution (await one by one):")
    result1 = await fetch_data(1.0, "API-1")
    result2 = await fetch_data(1.0, "API-2")
    
    print(f"Results: {result1}, {result2}")
    print(f"Time taken: {time.time() - start_time:.2f}s (Expect ~2.0s)")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• 'async def' defines a coroutine")
    print("• 'await' suspends execution until the awaitable completes")
    print("• Unlike threads, context switches are explicit (at await)")
    print("• To run main(): asyncio.run(main())")
    print("="*70)


if __name__ == "__main__":
    # Standard entry point for async programs
    asyncio.run(main())