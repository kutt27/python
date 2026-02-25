"""
Topic: Infinite Sequences.

Generators can represent infinite mathematical sequences because 
they don't need to store all values at once.
"""

def infinite_count(start: int = 0):
    while True:
        yield start
        start += 1

def infinite_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

if __name__ == "__main__":
    count_gen = infinite_count(10)
    print("Infinite Counting:")
    for _ in range(5):
        print(f"  {next(count_gen)}")
        
    fib_gen = infinite_fibonacci()
    print("\nInfinite Fibonacci:")
    for _ in range(10):
        print(f"  {next(fib_gen)}", end=" ")
    print()
