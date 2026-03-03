"""
Topic: Robust File I/O.

Always use a context manager ('with' statement) for file operations. 
It ensures the file is closed automatically, even if an exception 
occurs inside the block.
"""

import os

def process_file(filename):
    print(f"\nReading: {filename}")
    try:
        with open(filename, "r") as f:
            content = f.read()
            print(f"Content: {content}")
    except FileNotFoundError:
        print("Error: The file was not found.")
    except PermissionError:
        print("Error: You do not have permission to read this file.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    # Setup dummy file
    with open("sample.txt", "w") as f:
        f.write("Hello Exceptions!")
        
    process_file("sample.txt")
    process_file("missing.txt")
    
    os.remove("sample.txt")
