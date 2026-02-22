"""
Topic: Variadic Arguments (*args).

Allows a function to accept any number of positional arguments.
"""

def sum_all(*numbers: float) -> float:
    """Takes any number of numeric inputs."""
    return sum(numbers)

if __name__ == "__main__":
    print(f"Sum (2 args): {sum_all(10, 20)}")
    print(f"Sum (4 args): {sum_all(1, 2, 3, 4)}")
    
    # Unpacking a list into args
    data = [100, 200, 300]
    print(f"Sum (unpacked): {sum_all(*data)}")
