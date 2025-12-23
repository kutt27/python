"""
Python Concurrency: Process Lifecycle & Identification
=======================================================

Topic: Identifying processes, naming, and termination

Real-World Applications:
- Worker process management
- Debugging parallel applications
- Managing long-running process groups
"""

import multiprocessing
import time
import os

def worker_task():
    """Worker function that reports identity."""
    p = multiprocessing.current_process()
    print(f"  Child: {p.name} (PID: {p.pid}, OS PID: {os.getpid()})")
    print("  Child: Working...")
    time.sleep(1)
    print("  Child: Done.")

def main():
    """Demonstrates process identification."""
    print("="*70)
    print("PROCESS LIFECYCLE & NAMING".center(70))
    print("="*70)
    
    print(f"Main: Name={multiprocessing.current_process().name}")
    print(f"Main: PID={os.getpid()}")
    
    # 1. Naming Processes
    print("\n[Spawning Named Process]")
    p1 = multiprocessing.Process(name="DataWorker-1", target=worker_task)
    p2 = multiprocessing.Process(name="DataWorker-2", target=worker_task)
    
    # Start
    p1.start()
    p2.start()
    
    # Check alive status
    print(f"Main: Is {p1.name} alive? {p1.is_alive()}")
    
    # Wait
    p1.join()
    p2.join()
    
    print(f"Main: Is {p1.name} alive? {p1.is_alive()}")
    
    # 2. Terminating a Process (Force Kill)
    print("\n[Terminating Process]")
    p_hang = multiprocessing.Process(name="HangingWorker", target=time.sleep, args=(10,))
    p_hang.start()
    print(f"Main: Started {p_hang.name}, waiting a bit...")
    time.sleep(0.5)
    
    if p_hang.is_alive():
        print(f"Main: Terminating {p_hang.name} forcefully...")
        p_hang.terminate() # SIGTERM (Unix) or TerminateProcess (Windows)
        p_hang.join() # Still good practice to join after terminate
        
    print(f"Main: {p_hang.name} exit code: {p_hang.exitcode}")
    print("      (-15 usually means SIGTERM)")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Useful attributes: .name, .pid, .is_alive()")
    print("• .terminate(): Forcefully kills the process (use with caution)")
    print("• .exitcode: Check how process ended (None=running, 0=success, <0=signal)")
    print("="*70)


if __name__ == "__main__":
    main()