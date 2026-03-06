"""
Topic: Creating Processes.

Processes have their own memory space and interpreter instance. 
They are used for CPU-bound parallelism because they bypass the GIL.
"""

import multiprocessing
import os

def worker(name: str):
    """Function to run in a separate process."""
    print(f"  [Child] Process name: {name} (PID: {os.getpid()})")
    # Simulation of work
    count = sum(i for i in range(10**6))
    print(f"  [Child] Finished {name}!")

if __name__ == "__main__":
    # Mandatory guard for multiprocessing on Windows and macOS
    print(f"[Main] Parent PID: {os.getpid()}")
    
    p1 = multiprocessing.Process(target=worker, args=("Process-A",))
    p2 = multiprocessing.Process(target=worker, args=("Process-B",))
    
    p1.start()
    p2.start()
    
    p1.join()
    p2.join()
    
    print("[Main] All subprocesses finished.")
