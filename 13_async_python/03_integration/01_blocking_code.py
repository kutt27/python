"""
Topic: Running Blocking Code.

AsyncIO is single-threaded. If you run a blocking call like 
`time.sleep()` or `requests.get()`, the whole loop stops. 
Use `loop.run_in_executor()` to offload these to threads.
"""

import asyncio
import time

def slow_sync_function(name):
    """A standard synchronous, blocking function."""
    print(f"  [Sync] Threaded task {name} starting...")
    time.sleep(1) # This would freeze the event loop if called directly
    print(f"  [Sync] Threaded task {name} finished!")
    return f"Result {name}"

async def main():
    loop = asyncio.get_running_loop()
    
    print("[Main] Submitting blocking work to thread pool...")
    
    # Offload to the default ThreadPoolExecutor
    # run_in_executor returns a Future that we can await
    start = time.time()
    results = await asyncio.gather(
        loop.run_in_executor(None, slow_sync_function, "A"),
        loop.run_in_executor(None, slow_sync_function, "B"),
        loop.run_in_executor(None, slow_sync_function, "C")
    )
    
    print(f"\nResults: {results}")
    print(f"Total time: {time.time() - start:.2f}s (All 3 ran in parallel threads)")

if __name__ == "__main__":
    asyncio.run(main())
