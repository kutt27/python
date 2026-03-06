"""
Topic: Future Objects.

When you use `.submit()` instead of `.map()`, it returns a 
'Future' object which represents an eventual result.
"""

from concurrent.futures import ThreadPoolExecutor
import time

def long_task(name: str):
    time.sleep(1)
    return f"Result of {name}"

if __name__ == "__main__":
    with ThreadPoolExecutor() as executor:
        # submit() does not block and returns immediately
        future = executor.submit(long_task, "Task-1")
        
        print(f"Task submitted. Done? {future.done()}")
        print("Main thread is doing other work...")
        time.sleep(0.5)
        
        # result() blocks the main thread until the result is ready
        print(f"Still done? {future.done()}")
        res = future.result()
        print(f"Final Outcome: {res}")
