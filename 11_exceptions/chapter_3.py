"""
Python Exceptions: Complex Error Handling
==========================================

Topic: Combining try-except-else-finally

Real-World Applications:
- Resource management (files, network connections)
- Complex data pipelines
- Cleanup operations that must always run
"""

import time
from typing import List, Optional

class DatabaseConnection:
    """Simulated database connection."""
    def __init__(self, name: str):
        self.name = name
        self.is_connected = False
        
    def connect(self):
        print(f"  [DB] Connecting to {self.name}...")
        self.is_connected = True
        
    def disconnect(self):
        print(f"  [DB] Closing connection to {self.name}...")
        self.is_connected = False
        
    def execute(self, query: str):
        if not self.is_connected:
            raise ConnectionError("Not connected to DB")
        if "FAIL" in query:
            raise RuntimeError("SQL execution failed")
        print(f"  [DB] Executed: {query}")
        return ["row1", "row2"]


def run_etl_job(query: str):
    """
    Run an Extract-Transform-Load (ETL) job.
    Demonstrates the full try-except-else-finally structure.
    """
    print(f"\nRunning job: {query}")
    db = DatabaseConnection("AnalyticsDB")
    
    try:
        # 1. Setup & Risky Operations
        db.connect()
        results = db.execute(query)
        
    except ConnectionError as e:
        # Handle specific connection issues
        print(f"✗ Connection Error: {e}")
        
    except RuntimeError as e:
        # Handle query execution failures
        print(f"✗ Runtime Error: {e}")
        
    except Exception as e:
        # Safety net for unforeseen errors
        print(f"✗ Unexpected Error: {type(e).__name__}: {e}")
        
    else:
        # 2. Success Logic (Process results)
        # Runs only if try block succeeded
        print(f"✓ Query successful. Processing {len(results)} rows...")
        # Simulate processing time
        # time.sleep(0.1) 
        print("✓ Data transformation complete.")
        
    finally:
        # 3. Cleanup
        # ALWAYS runs, regardless of success or error
        # Critical for releasing resources
        if db.is_connected:
            db.disconnect()
        print("  [System] Job cleanup finished.")


def main():
    """Demonstrates full exception lifecycle."""
    print("="*70)
    print("COMPLEX ERROR HANDLING (Try-Except-Else-Finally)".center(70))
    print("="*70)
    
    # 1. Success case
    run_etl_job("SELECT * FROM users")
    
    # 2. Failure case (RuntimeError)
    run_etl_job("SELECT FAIL FROM users")
    
    # 3. Simulated unexpected error (mocking by passing invalid type to execute if we could, 
    # or just trusting the pattern example covers it)
    
    print("\n" + "="*70)
    print("Structure Recap:")
    print("• try:     Code that might raise an exception")
    print("• except:  Handle specific errors")
    print("• else:    Run if NO exception occurred (happy path)")
    print("• finally: Always run (cleanup, closing resources)")
    print("="*70)


if __name__ == "__main__":
    main()