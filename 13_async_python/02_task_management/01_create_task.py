"""
Topic: Scheduling Tasks.

`asyncio.create_task()` schedules a coroutine to run on the loop 
immediately. It returns a Task object that can be awaited later.
"""

import asyncio

async def background_work():
    print("  [Task] Background work started...")
    await asyncio.sleep(2)
    print("  [Task] Background work finished!")
    return "Complete"

async def main():
    print("[Main] Scheduling task...")
    # This starts the task but doesn't wait for it yet
    task = asyncio.create_task(background_work())
    
    print("[Main] Doing other stuff while task runs...")
    await asyncio.sleep(1)
    print("[Main] Checking task status: done?", task.done())
    
    # Now we wait for the result
    result = await task
    print(f"[Main] Task result: {result}")

if __name__ == "__main__":
    asyncio.run(main())
