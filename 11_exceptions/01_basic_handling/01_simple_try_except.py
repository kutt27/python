"""
Topic: Basic Try-Except.

The simplest form of error handling. Wrap risky code in a try block 
and handle the error in an except block if it occurs.
"""

def safe_divide(a, b):
    try:
        # Risky operation
        result = a / b
        return result
    except ZeroDivisionError:
        # Handle the specific error
        print("Error: Cannot divide by zero!")
        return None

if __name__ == "__main__":
    print(f"10 / 2 = {safe_divide(10, 2)}")
    print(f"10 / 0 = {safe_divide(10, 0)}")
