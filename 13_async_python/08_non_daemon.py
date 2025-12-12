"""
Python Async: Async Context Managers
=====================================

Topic: __aenter__ and __aexit__

Real-World Applications:
- Database transactions (asyncpg)
- HTTP Sessions (aiohttp.ClientSession)
- Redis pipelines
"""

import asyncio

class AsyncDatabase:
    """Simulated Async Database Connection."""
    
    def __init__(self, name: str):
        self.name = name
        self.connected = False
        
    async def __aenter__(self):
        """Async setup."""
        print(f"  [DB] Connecting to {self.name}...")
        await asyncio.sleep(0.5) # I/O
        self.connected = True
        print(f"  [DB] Connected.")
        return self
    
    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async teardown."""
        print(f"  [DB] Closing connection...")
        await asyncio.sleep(0.2) # I/O
        self.connected = False
        print(f"  [DB] Closed.")
        
    async def query(self, sql: str):
        if not self.connected:
            raise ConnectionError("Not connected")
        print(f"    [Exec] {sql}")
        return ["row1", "row2"]


async def main():
    """Demonstrates async connection management."""
    print("="*70)
    print("ASYNC CONTEXT MANAGERS".center(70))
    print("="*70)
    
    print("Starting transaction block...")
    
    # 'async with' is required for __aenter__/__aexit__
    async with AsyncDatabase("PostgreSQL") as db:
        data = await db.query("SELECT * FROM users")
        print(f"    [Result] {data}")
        
    print("End of block.")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use `async with` for async context managers")
    print("• Classes define `__aenter__` and `__aexit__`")
    print("• Allows awaiting I/O during setup/teardown (unlike standard context managers)")
    print("• Standard in all modern async libraries (databases, http)")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())