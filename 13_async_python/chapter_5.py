"""
Python Async: CPU-Bound Tasks
==============================

Topic: Integrating Multiprocessing with AsyncIO

Real-World Applications:
- Image processing in a web server
- Data analysis endpoints
- Heavy cryptography
"""

import asyncio
import time
import concurrent.futures
from concurrent.futures import ProcessPoolExecutor

def heavy_computation(n: int) -> int:
    """
    CPU-bound task. Blocks the CPU.
    """
    # Simple CPU waster
    pid = __import__('os').getpid()
    print(f"  [Process-{pid}] Computing factorial({n})...")
    
    # Simulate work
    start = time.time()
    while time.time() - start < 1.0:
        pass
        
    return n * n

async def keep_alive():
    """Demonstrates event loop is still responsive."""
    for i in range(5):
        print("  [EventLoop] ❤️ Heartbeat...")
        await asyncio.sleep(0.3)

async def main():
    """Demonstrates handling CPU-bound tasks."""
    print("="*70)
    print("CPU-BOUND TASKS IN ASYNCIO".center(70))
    print("="*70)
    
    # We need a ProcessPool for CPU tasks (Threads are useless due to GIL)
    # Using 'with' to ensure cleanup, but typically a global pool in apps.
    
    pool = ProcessPoolExecutor()
    loop = asyncio.get_running_loop()
    
    print("Starting CPU task + Heartbeat concurrently...")
    
    # 1. Schedule CPU Task in Process Pool
    cpu_future = loop.run_in_executor(pool, heavy_computation, 100)
    
    # 2. Run background async tasks (Heartbeat)
    # This proves the Main Thread isn't blocked!
    await keep_alive()
    
    # 3. Get Result
    result = await cpu_future
    print(f"  [Main] Compution Result: {result}")
    
    # Cleanup (Manually shutdown in this simple script context)
    pool.shutdown()
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• CPU tasks block the Event Loop if run directly")
    print("• Threads don't help (GIL)")
    print("• Use `loop.run_in_executor(process_pool, func)`")
    print("• Combines best of both worlds: Async I/O + Multicore CPU")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())