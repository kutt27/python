"""
Python Exceptions: Robust File Handling
========================================

Topic: Exceptions in file I/O operations

Real-World Applications:
- Log processing systems
- Configuration loading
- Data persistence
- Preventing resource leaks
"""

import os

def read_log_file_safe(filename: str):
    """
    Demonstrates safe file reading pattern.
    """
    print(f"\nAttempting to read: {filename}")
    
    file_handle = None
    try:
        file_handle = open(filename, 'r', encoding='utf-8')
        content = file_handle.read()
        print(f"✓ Read {len(content)} characters.")
        return content
        
    except FileNotFoundError:
        print(f"✗ Error: File '{filename}' does not exist.")
        return None
        
    except PermissionError:
        print(f"✗ Error: No permission to read '{filename}'.")
        return None
        
    except UnicodeDecodeError:
        print(f"✗ Error: File '{filename}' is not valid text.")
        return None
        
    except Exception as e:
        print(f"✗ Unexpected error: {e}")
        return None
        
    finally:
        # Crucial: Ensure file is closed even if errors happened above
        if file_handle:
            file_handle.close()
            print("  [System] File handle closed successfully.")


def read_with_context_manager(filename: str):
    """
    The Pythonic way: Using 'with' statement.
    Automatically handles closing, even with exceptions.
    """
    print(f"\n[Context Manager] Reading: {filename}")
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            print(f"✓ File opened. First line: {f.readline().strip()}")
            # If an error happens here, file closes automatically
            
    except FileNotFoundError:
        print("✗ File not found.")
    except Exception as e:
        print(f"✗ Error: {e}")


def main():
    """Demonstrates file exception handling."""
    print("="*70)
    print("ROBUST FILE HANDLING".center(70))
    print("="*70)
    
    # Setup dummy file
    dummy_file = "test_log.txt"
    with open(dummy_file, "w") as f:
        f.write("Log Entry 1\nLog Entry 2")
        
    # 1. Traditional Try-Finally
    read_log_file_safe(dummy_file)
    read_log_file_safe("non_existent.txt")
    
    # 2. Modern Context Manager
    read_with_context_manager(dummy_file)
    
    # Cleanup
    if os.path.exists(dummy_file):
        os.remove(dummy_file)
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• File I/O is prone to runtime errors (missing, perm, full disk)")
    print("• ALWAYS ensure files are closed to prevent resource leaks")
    print("• 'finally' block handles cleanup in manual approach")
    print("• 'with open(...) as f' is preferred (auto-cleanup)")
    print("="*70)


if __name__ == "__main__":
    main()