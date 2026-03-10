"""
Topic: The Event Loop.

The event loop is the engine that runs async tasks. `asyncio.run()` 
is the high-level entry point that creates a loop and closes it 
when finished.
"""

import asyncio
import time

async def compute_something():
    await asyncio.sleep(1)
    return 42

async def main():
    print("Starting computation...")
    start = time.time()
    
    # Sequential await: This takes 1 second
    result = await compute_something()
    
    print(f"Result: {result} (Time: {time.time() - start:.2f}s)")

if __name__ == "__main__":
    # asyncio.run handles the lifecycle of the loop
    asyncio.run(main())
