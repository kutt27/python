"""
Topic: Async Context Managers.

Allows use of 'async with'. Useful for objects that require 
async setup (open connection) and teardown (close connection).
"""

import asyncio

class AsyncConnection:
    def __init__(self, resource_name):
        self.resource = resource_name

    async def __aenter__(self):
        print(f"  [CM] Opening connection to {self.resource}...")
        await asyncio.sleep(0.5) # Simulated async setup
        print(f"  [CM] Session active.")
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        print(f"  [CM] Closing connection to {self.resource}...")
        await asyncio.sleep(0.2) # Simulated async cleanup
        print(f"  [CM] Session closed.")

    async def execute(self, command):
        print(f"    [Exec] Running: {command}")
        return "SUCCESS"

async def main():
    print("Entering 'async with' block:")
    async with AsyncConnection("S3_Bucket") as conn:
        result = await conn.execute("LIST_FILES")
        print(f"    [Result] {result}")
    
    print("\nBlock finished. Connection is closed.")

if __name__ == "__main__":
    asyncio.run(main())
