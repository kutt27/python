"""
Topic: Avoiding Bare Except.

Never use 'except:' (bare except) or 'except Exception:'. 
Doing so catches SystemExit and KeyboardInterrupt (Ctrl+C), 
making it hard to stop your program.
"""

def process():
    try:
        # Imagine a real bug here
        return 1 / 0
    except: # BAD: Bare except
        print("Something went wrong, but I don't know what.")

def better_process():
    try:
        return 1 / 0
    except ZeroDivisionError as e: # GOOD: Specific exception
        print(f"Error: {e}")

if __name__ == "__main__":
    process()
    better_process()
