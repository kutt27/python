"""
Topic: Timeouts.

Use `asyncio.wait_for()` to limit how long a task can run. 
If it exceeds the timeout, it is automatically cancelled.
"""

import asyncio

async def slow_operation():
    print("  [Slow] Operation started...")
    await asyncio.sleep(5) # Too long!
    print("  [Slow] Operation finished.")
    return "Success"

async def main():
    print("[Main] Starting operation with 1s timeout...")
    try:
        # Wrap task in a timeout
        result = await asyncio.wait_for(slow_operation(), timeout=1.0)
        print(f"Result: {result}")
    except asyncio.TimeoutError:
        print("[Main] Oh no! The operation took too long and was aborted.")

if __name__ == "__main__":
    asyncio.run(main())
