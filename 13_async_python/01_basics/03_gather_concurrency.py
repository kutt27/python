"""
Topic: Concurrent execution with gather.

`asyncio.gather()` allows you to run multiple awaitables concurrently 
and wait for all of them to finish.
"""

import asyncio
import time

async def fetch_url(url, delay):
    print(f"  [Start] Fetching {url}...")
    await asyncio.sleep(delay)
    print(f"  [Done] {url}")
    return f"Data from {url}"

async def main():
    print("Fetching multiple URLs concurrently:")
    start = time.time()
    
    # Schedule multiple coroutines to run at once
    results = await asyncio.gather(
        fetch_url("google.com", 1.5),
        fetch_url("python.org", 1.0),
        fetch_url("github.com", 0.5)
    )
    
    print(f"\nFinal Results: {results}")
    print(f"Total time: {time.time() - start:.2f}s (Expect ~1.5s, not 3.0s)")

if __name__ == "__main__":
    asyncio.run(main())
