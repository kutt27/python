"""
Topic: The 'else' block.

The 'else' block runs ONLY if the try block succeeds without any 
exceptions. It is useful for code that should only execute if 
the prerequisite operations were successful.
"""

def process_data(value):
    try:
        # Prerequisite: string parsing
        num = int(value)
    except ValueError:
        print(f"Invalid input: {value}")
    else:
        # Success path: calculation
        # This only runs if int(value) worked
        result = num * 2
        print(f"Processing success: {value} * 2 = {result}")

if __name__ == "__main__":
    process_data("10")
    process_data("hello")
