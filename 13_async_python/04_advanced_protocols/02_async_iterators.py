"""
Topic: Async Iterators and Generators.

Allows use of 'async for'. Perfect for streaming data from a 
database or paginated API results.
"""

import asyncio

class AsyncRange:
    """An simple async iterator."""
    def __init__(self, stop):
        self._stop = stop
        self._curr = 0

    def __aiter__(self):
        return self

    async def __anext__(self):
        if self._curr >= self._stop:
            raise StopAsyncIteration
        
        await asyncio.sleep(0.5) # Simulate I/O delay per item
        val = self._curr
        self._curr += 1
        return val

async def async_generator(stop):
    """The simpler way: an async generator."""
    for i in range(stop):
        await asyncio.sleep(0.3)
        yield f"Generated-{i}"

async def main():
    print("Iterating with 'async for':")
    async for i in AsyncRange(3):
        print(f"  Got item: {i}")

    print("\nIterating with async generator:")
    async for item in async_generator(3):
        print(f"  {item}")

if __name__ == "__main__":
    asyncio.run(main())
