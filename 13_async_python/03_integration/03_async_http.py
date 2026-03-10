"""
Topic: Async HTTP Pattern (Simulated).

Modern web activity in Python uses libraries like `aiohttp` or 
`httpx`. This example simulates a concurrent fetch pattern.
"""

import asyncio
import time

class AsyncClient:
    """Mock implementation of an Async HTTP client."""
    async def get(self, url):
        print(f"  [GET] {url}...")
        await asyncio.sleep(0.5) # Simulated network latency
        return f"<html>{url} content</html>"

async def fetch_all(urls):
    client = AsyncClient()
    tasks = [client.get(url) for url in urls]
    return await asyncio.gather(*tasks)

async def main():
    urls = [
        "https://api.example.com/v1",
        "https://api.example.com/v2",
        "https://api.example.com/v3"
    ]
    
    print(f"Concurrently fetching {len(urls)} URLs...")
    start = time.time()
    
    results = await fetch_all(urls)
    
    print(f"\nFetched: {results}")
    print(f"Time taken: {time.time() - start:.2f}s (Scaled by slowest request)")

if __name__ == "__main__":
    asyncio.run(main())
