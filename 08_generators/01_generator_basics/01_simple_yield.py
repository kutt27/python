"""
Topic: Simple yield statement.

Generators use 'yield' to produce a series of values over time, 
suspending execution between each one.
"""

def simple_countdown(n: int):
    print("Starting countdown...")
    while n > 0:
        yield n
        n -= 1
    print("Countdown finished!")

if __name__ == "__main__":
    # Calling the function returns a generator object
    counter = simple_countdown(3)
    print(f"Generator Object: {counter}")
    
    # Values are produced only when we iterate
    for num in counter:
        print(f"  Received: {num}")
