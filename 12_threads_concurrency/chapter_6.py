"""
Python Concurrency: Daemon Threads
===================================

Topic: Background threads vs Foreground threads

Real-World Applications:
- Health check 'heartbeats'
- Autosave features
- Background garbage collection
- Monitoring agents
"""

import threading
import time
import sys

def background_autosave():
    """
    Simulate a background task that runs forever.
    Daemon threads are killed automatically when main program exits.
    """
    print("  [Daemon] Autosave service started...")
    while True:
        time.sleep(1.0)
        print("  [Daemon] Saving workspace... (Autosave)")

def user_input_task():
    """
    Simulate main user interaction.
    """
    print("  [Main] User working on document...")
    time.sleep(1.5)
    print("  [Main] User typing...")
    time.sleep(1.5)
    print("  [Main] User finished work. Exiting.")

def main():
    """Demonstrates daemon threads."""
    print("="*70)
    print("DAEMON THREADS".center(70))
    print("="*70)
    
    # 1. Create Daemon Thread
    # daemon=True means: "Don't keep program alive for me"
    saver_thread = threading.Thread(target=background_autosave, daemon=True)
    saver_thread.start()
    
    # 2. Run Main Foreground Logic
    user_input_task()
    
    print("-" * 70)
    print("Main thread reaching end...")
    print("Daemon thread will be abruptly terminated now.")
    print("Unlike normal threads, we DON'T join() daemon threads.")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Daemon threads run in background")
    print("• Program exits when only daemon threads are left")
    print("• Use 'daemon=True' in constructor")
    print("• Good for infinite background services (heartbeats, logs)")
    print("="*70)


if __name__ == "__main__":
    main()
