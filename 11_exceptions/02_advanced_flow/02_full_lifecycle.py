"""
Topic: Full Exception Lifecycle.

Combining try, except, else, and finally in a single workflow 
to handle all possible outcomes of a risky operation.
"""

def complex_workflow(filename):
    print(f"\n--- Processing: {filename} ---")
    try:
        print(f"1. Attempting to open {filename}")
        if filename == "error.txt":
            raise IOError("Disk read failure")
        print("2. Successfully read data.")
    except IOError as e:
        print(f"3. Error Handled: {e}")
    else:
        print("4. Success Path: Transforming data...")
    finally:
        print("5. Always Run: Releasing system locks.")

if __name__ == "__main__":
    complex_workflow("data.txt")
    complex_workflow("error.txt")
