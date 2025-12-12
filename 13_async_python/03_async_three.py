"""
Python Async: Async HTTP Requests
==================================

Topic: Real-world IO pattern with aiohttp (simulated)

Real-World Applications:
- High-performance web scrapers
- API gateways
- Microservice communication
"""

import asyncio
import time
from typing import List, Dict

# In real world: import aiohttp

class MockValidationService:
    """Simulates an external API."""
    
    async def validate_user(self, user_id: int) -> Dict:
        """Simulate network call."""
        # Simulated Network Lag
        await asyncio.sleep(0.5)
        
        # Simulated logic
        valid = user_id % 2 != 0 # Odd IDs are valid
        return {
            "user_id": user_id, 
            "valid": valid, 
            "status": "active" if valid else "suspended"
        }


async def main():
    """Demonstrates async API interactions."""
    print("="*70)
    print("ASYNC HTTP PATTERNS".center(70))
    print("="*70)
    
    service = MockValidationService()
    user_ids = range(101, 111) # 10 users
    
    print(f"Validating {len(user_ids)} users against Mock API...")
    start_time = time.time()
    
    # Scenario: We need to call the API for each user
    
    # 1. Create Tasks (Explicit Task Creation)
    # asyncio.create_task schedules coroutine immediately
    tasks = []
    for uid in user_ids:
        task = asyncio.create_task(service.validate_user(uid))
        tasks.append(task)
        
    print("  Requests sent. Waiting for responses...")
    
    # 2. Wait for completion
    results = await asyncio.gather(*tasks)
    
    # 3. Process results
    valid_count = sum(1 for r in results if r['valid'])
    
    total_time = time.time() - start_time
    print("-" * 70)
    print(f"Processed {len(results)} responses in {total_time:.2f}s")
    print(f"Valid Users: {valid_count}")
    print(f"Invalid Users: {len(results) - valid_count}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Network I/O is where AsyncIO shines")
    print("• 10 requests took ~0.5s total (concurrency) vs ~5.0s (serial)")
    print("• Use 'asyncio.create_task()' to schedule background execution")
    print("• In prod, use 'aiohttp' or 'httpx' for actual requests")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())