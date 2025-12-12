"""
Python Async: Background Tasks "Fire and Forget"
=================================================

Topic: Scheduling background work (create_task)

Real-World Applications:
- Sending analytics (non-critical)
- Cache updates
- Scheduled cleanups
"""

import asyncio
import time

async def analytics_logger(user_id: str, action: str):
    """
    A background task that takes some time but shouldn't block response.
    """
    print(f"    [Background] Logging {action} for {user_id}...")
    await asyncio.sleep(2) # Slow I/O
    print(f"    [Background] Log saved.")


async def handle_request(user_id: str):
    """
    Simulates a user request handler (e.g., API endpoint).
    """
    print(f"  [Handler] Processing request for {user_id}...")
    await asyncio.sleep(0.5) # Fast core logic
    
    # Schedule background task
    # We do NOT 'await' this immediately if we want fire-and-forget
    # Note: In production, keep a reference to tasks to avoid garbage collection hazards!
    task = asyncio.create_task(analytics_logger(user_id, "login"))
    
    print(f"  [Handler] Response sent to {user_id}.")
    return "200 OK", task


async def main():
    """Demonstrates background task pattern."""
    print("="*70)
    print("BACKGROUND TASKS (Fire & Forget)".center(70))
    print("="*70)
    
    start_time = time.time()
    
    # 1. Handle Request
    response, bg_task = await handle_request("alice")
    
    # Response is ready immediately!
    print(f"User got response in: {time.time() - start_time:.2f}s")
    
    # 2. Wait for background tasks (App Shutdown phase)
    # In a real server scope, the server keeps running. 
    # Here we await to show it finishes.
    print("Server waiting for pending logs...")
    await bg_task
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use `asyncio.create_task()` to start execution immediately")
    print("• If you don't `await` it, code continues (Fire & Forget)")
    print("• Warning: Always keep a reference to tasks (sets) to prevent")
    print("  premature garbage collection in some Python versions")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())