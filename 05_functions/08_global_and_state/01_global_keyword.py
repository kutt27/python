"""
Topic: Modifying Global Variables with `global`.

Variables defined at the module level are global. To *modify* 
them from inside a function, the `global` keyword must be used.
"""

# Global configuration flag
DEBUG_MODE = False

def enable_debug():
    """Modifies the global flag."""
    global DEBUG_MODE
    DEBUG_MODE = True
    print("Debug mode enabled.")

def log(message: str):
    """Reads the global flag (no 'global' keyword needed for reading)."""
    if DEBUG_MODE:
        print(f"[DEBUG] {message}")
    else:
        print(message)

if __name__ == "__main__":
    log("Hello") # Prints normally
    enable_debug()
    log("Hello") # Prints with [DEBUG] tag
