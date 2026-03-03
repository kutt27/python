"""
Topic: The 'finally' block.

The 'finally' block ALWAYS runs, regardless of whether an 
exception occurred or not. It is primarily used for cleaning 
up resources like closing files or database connections.
"""

def resource_demo():
    print("Opening Resource...")
    try:
        print("  Processing stuff...")
        # Imagine a potential error here
        # raise RuntimeError("Oops!")
    except Exception as e:
        print(f"  Caught Error: {e}")
    finally:
        # This code runs no matter what
        print("Closing Resource (Cleanup)!")

if __name__ == "__main__":
    resource_demo()
