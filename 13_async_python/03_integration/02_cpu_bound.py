"""
Topic: CPU-Bound Tasks.

For heavy math or data processing, threads don't help much in 
Python due to the GIL. Integration with `ProcessPoolExecutor` 
is the correct approach.
"""

import asyncio
from concurrent.futures import ProcessPoolExecutor
import time

def heavy_math(n):
    """CPU intensive task."""
    print(f"  [Process] Calculating square of {n}...")
    # Simulate heavy computation
    start = time.time()
    while time.time() - start < 1.0:
        pass
    return n * n

async def main():
    loop = asyncio.get_running_loop()
    
    # Processes have their own memory and interpreter (no GIL)
    with ProcessPoolExecutor() as pool:
        print("[Main] Offloading CPU work to Process Pool...")
        start = time.time()
        
        # Dispatch to sub-processes
        results = await asyncio.gather(
            loop.run_in_executor(pool, heavy_math, 10),
            loop.run_in_executor(pool, heavy_math, 20)
        )
        
        print(f"\nResults: {results}")
        print(f"Total time: {time.time() - start:.2f}s (True parallelism)")

if __name__ == "__main__":
    asyncio.run(main())
