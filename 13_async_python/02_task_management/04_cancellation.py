"""
Topic: Task Cancellation.

You can manually cancel a task using `task.cancel()`. The coroutine 
receives an `asyncio.CancelledError` at its next 'await'.
"""

import asyncio

async def long_running_service():
    try:
        print("  [Service] Running indefinitely...")
        while True:
            await asyncio.sleep(1)
            print("  [Service] Pulse check...")
    except asyncio.CancelledError:
        print("  [Service] Cancellation received! Cleaning up...")
        # Logic for graceful shutdown goes here
        raise # Good practice to re-raise to indicate clean exit

async def main():
    service_task = asyncio.create_task(long_running_service())
    
    await asyncio.sleep(2.5)
    print("[Main] Stopping service...")
    
    service_task.cancel()
    
    try:
        await service_task
    except asyncio.CancelledError:
        print("[Main] Service task successfully terminated.")

if __name__ == "__main__":
    asyncio.run(main())
