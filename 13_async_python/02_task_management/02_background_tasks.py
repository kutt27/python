"""
Topic: Fire and Forget.

Sometimes you want to start a task and NOT wait for it to finish. 
However, you MUST keep a reference to the task to avoid it being 
garbage collected prematurely.
"""

import asyncio

background_tasks = set() # Standard practice: keep references in a set

async def log_event(event):
    await asyncio.sleep(1)
    print(f"  [Log] Event '{event}' recorded.")

async def handle_request():
    print("[Request] Handling incoming request...")
    await asyncio.sleep(0.1)
    
    # Fire and forget: don't await this
    task = asyncio.create_task(log_event("user_login"))
    
    # Add to set and register a callback to remove it when done
    background_tasks.add(task)
    task.add_done_callback(background_tasks.discard)
    
    print("[Request] Response sent to user.")

async def main():
    await handle_request()
    print("[Main] Server logic continuing...")
    # Give background tasks time to finish for this demo
    await asyncio.sleep(1.5)

if __name__ == "__main__":
    asyncio.run(main())
