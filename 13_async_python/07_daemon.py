"""
Python Async: Task Cancellation
================================

Topic: Cancelling running tasks (Timeouts & Shutdowns)

Real-World Applications:
- Request timeouts (SLA enforcement)
- User cancelled operations
- Graceful shutdowns
"""

import asyncio
import time

async def long_running_operation():
    """Simulates a task that takes too long."""
    print("  [Task] Started long operation...")
    try:
        for i in range(10):
            print(f"  [Task] Working step {i+1}...")
            await asyncio.sleep(1)
            
        return "Success"
        
    except asyncio.CancelledError:
        # Crucial: Cleanup logic when cancelled
        print("  [Task] ! I was cancelled! Cleaning up resources...")
        # e.g., close DB connection, rollback transaction
        raise # Re-raise to let caller know

async def main():
    """Demonstrates cancellation and timeouts."""
    print("="*70)
    print("TASK CANCELLATION & TIMEOUTS".center(70))
    print("="*70)
    
    print("\n[1] Manual Cancellation")
    print("-" * 70)
    
    task = asyncio.create_task(long_running_operation())
    
    await asyncio.sleep(2.5) # Let it run briefly
    
    print("Main: Decided to cancel task.")
    task.cancel() # Request cancellation
    
    try:
        await task
    except asyncio.CancelledError:
        print("Main: Caught cancellation confirmation.")
        
    print("\n[2] asyncio.wait_for (Timeouts)")
    print("-" * 70)
    
    try:
        # Wraps execution in a timeout
        # If it takes > 3s, it CANCELS the task automatically
        await asyncio.wait_for(long_running_operation(), timeout=3.0)
    except asyncio.TimeoutError:
        print("Main: Operation timed out!")
        
    print("\n" + "="*70)
    print("Key Points:")
    print("• Tasks can be cancelled via `.cancel()`")
    print("• `CancelledError` is raised inside the coroutine at the `await` point")
    print("• Use `try/finally` in coroutines to ensure cleanup")
    print("• `asyncio.wait_for(coro, timeout)` is the standard timeout pattern")
    print("="*70)


if __name__ == "__main__":
    asyncio.run(main())