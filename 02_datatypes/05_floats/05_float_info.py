"""
Demonstrates Python's internal float limits and representation.
"""

import sys

def demonstrate_float_info() -> None:
    print(f"Max float: {sys.float_info.max}")
    print(f"Min positive float: {sys.float_info.min}")
    print(f"Precision digits: {sys.float_info.dig}")
    print(f"Epsilon: {sys.float_info.epsilon}")

if __name__ == "__main__":
    demonstrate_float_info()
