"""
Topic: Daemon Threads.

Daemon threads run in the background. Unlike normal threads, 
they do not keep the program alive. They are terminated 
abruptly when the main program finishes.
"""

import threading
import time

def background_monitor():
    """Infinite background task."""
    print("  [Daemon] Monitor agent starting...")
    while True:
        time.sleep(0.5)
        print("  [Daemon] Checking system health... (OK)")

def main_app():
    """Foreground user task."""
    print("  [Main] App is running...")
    time.sleep(2)
    print("  [Main] User task finished.")

if __name__ == "__main__":
    # Create a DAEMON thread
    monitor = threading.Thread(target=background_monitor, daemon=True)
    monitor.start()
    
    # Run main logic
    main_app()
    
    print("\n[Main] Exiting now. The daemon thread will be killed automatically.")
