"""
Python Async: Concurrency with gather
======================================

Topic: Running tasks concurrently using asyncio.gather

Real-World Applications:
- Aggregating data from multiple microservices
- Parallel database queries
"""

import asyncio
import time
import random

async def process_item(item_id: int):
    """Simulate processing a single item."""
    # Simulate variable network latency
    delay = random.uniform(0.5, 1.5)
    print(f"  Starting Item-{item_id} (est: {delay:.2f}s)")
    
    await asyncio.sleep(delay)
    
    print(f"  ✓ Finished Item-{item_id}")
    return f"Result-{item_id}"


async def main():
    """Demonstrates concurrent execution."""
    print("="*70)
    print("ASYNCIO GATHER (Concurrency)".center(70))
    print("="*70)
    
    tasks_count = 5
    print(f"Processing {tasks_count} items concurrently...")
    start_time = time.time()
    
    # 1. Create list of coroutine objects (not started yet in this pattern with gather usually, 
    # effectively scheduled when gather is called)
    coroutines = [process_item(i) for i in range(1, tasks_count + 1)]
    
    # 2. Run all concurrently and wait for all to finish
    # Returns a list of results in the matching order
    results = await asyncio.gather(*coroutines)
    
    total_time = time.time() - start_time
    
    print("-" * 70)
    print(f"All done! Results: {results}")
    print(f"Total Time: {total_time:.2f}s")
    print(f"Theoretical Max Delay was ~1.5s")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• asyncio.gather(*coros): Runs coroutines concurrently")
    print("• Waits for ALL tasks to complete")
    print("• Returns results in the same order as inputs")
    print("• Exceptions in children can propagate immediately or be aggregated")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())