"""
Python OOP: Context Managers
=============================

Topic: __enter__, __exit__, with statement, resource management

Real-World Applications:
- File handling
- Database connections
- Lock management
- Temporary state changes
"""

from typing import Optional
import time


class DatabaseConnection:
    """Database connection context manager."""
    
    def __init__(self, host: str, database: str):
        self.host = host
        self.database = database
        self.connection = None
    
    def __enter__(self):
        """Called when entering 'with' block."""
        print(f"Connecting to {self.host}/{self.database}...")
        self.connection = f"Connection to {self.database}"
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        """Called when exiting 'with' block."""
        print(f"Closing connection to {self.database}")
        self.connection = None
        # Return False to propagate exceptions
        return False
    
    def query(self, sql: str):
        """Execute query."""
        if self.connection:
            print(f"Executing: {sql}")
            return ["result1", "result2"]
        raise RuntimeError("No connection")


class Timer:
    """Timer context manager."""
    
    def __init__(self, name: str = "Operation"):
        self.name = name
        self.start_time = None
    
    def __enter__(self):
        self.start_time = time.time()
        print(f"Starting: {self.name}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        elapsed = time.time() - self.start_time
        print(f"Finished: {self.name} ({elapsed:.4f}s)")
        return False


class TemporaryValue:
    """Temporarily change a value, restore on exit."""
    
    def __init__(self, obj, attr: str, temp_value):
        self.obj = obj
        self.attr = attr
        self.temp_value = temp_value
        self.original_value = None
    
    def __enter__(self):
        self.original_value = getattr(self.obj, self.attr)
        setattr(self.obj, self.attr, self.temp_value)
        print(f"Temporarily set {self.attr} to {self.temp_value}")
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        setattr(self.obj, self.attr, self.original_value)
        print(f"Restored {self.attr} to {self.original_value}")
        return False


class FileLock:
    """File lock context manager."""
    
    def __init__(self, filename: str):
        self.filename = filename
        self.locked = False
    
    def __enter__(self):
        print(f"Acquiring lock on {self.filename}")
        self.locked = True
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        print(f"Releasing lock on {self.filename}")
        self.locked = False
        return False


def main():
    """Demonstrates context managers."""
    print("="*70)
    print("CONTEXT MANAGERS".center(70))
    print("="*70)
    
    print("\n[1] DATABASE CONNECTION")
    print("-" * 70)
    
    with DatabaseConnection("localhost", "app_db") as db:
        results = db.query("SELECT * FROM users")
        print(f"Results: {results}")
    # __exit__ automatically called, connection closed
    
    print("\n[2] TIMER")
    print("-" * 70)
    
    with Timer("Data processing"):
        time.sleep(0.1)  # Simulate work
        print("  Processing data...")
    
    print("\n[3] TEMPORARY VALUE CHANGE")
    print("-" * 70)
    
    class Config:
        debug = False
    
    config = Config()
    print(f"Debug mode: {config.debug}")
    
    with TemporaryValue(config, "debug", True):
        print(f"  Inside context: debug = {config.debug}")
    
    print(f"After context: debug = {config.debug}")
    
    print("\n[4] FILE LOCK")
    print("-" * 70)
    
    with FileLock("data.txt") as lock:
        print(f"  Lock acquired: {lock.locked}")
        print("  Performing file operations...")
    
    print("\n[5] EXCEPTION HANDLING")
    print("-" * 70)
    
    try:
        with DatabaseConnection("localhost", "test_db") as db:
            print("  Inside context")
            raise ValueError("Something went wrong!")
    except ValueError as e:
        print(f"  ✗ Caught exception: {e}")
    
    print("  Connection was still properly closed")
    
    print("\n[6] MULTIPLE CONTEXT MANAGERS")
    print("-" * 70)
    
    with DatabaseConnection("localhost", "db1") as db1, \
         DatabaseConnection("localhost", "db2") as db2:
        print("  Both connections active")
    
    print("\n" + "="*70)
    print("Context Manager Protocol:")
    print("-" * 70)
    print("class MyContext:")
    print("    def __enter__(self):")
    print("        # Setup code")
    print("        return self")
    print("    ")
    print("    def __exit__(self, exc_type, exc_val, exc_tb):")
    print("        # Cleanup code")
    print("        return False  # Propagate exceptions")
    print("\nUsage:")
    print("  with MyContext() as ctx:")
    print("      # Use ctx")
    print("\nCommon Use Cases:")
    print("✓ File I/O (automatic close)")
    print("✓ Database connections")
    print("✓ Locks and semaphores")
    print("✓ Temporary state changes")
    print("✓ Resource acquisition/release")
    print("="*70)


if __name__ == "__main__":
    main()
