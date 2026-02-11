"""
Demonstrates sorting, reversing, and basic aggregations (min, max, sum) on lists.
"""

def demonstrate_operations() -> None:
    times = [45, 23, 89, 12, 56, 34, 78]
    print(f"Times: {times}")
    
    times.sort()
    print(f"Sorted: {times}")
    
    times.reverse()
    print(f"Reversed: {times}")
    
    print(f"Min: {min(times)}, Max: {max(times)}")
    print(f"Average: {sum(times)/len(times):.1f}")

if __name__ == "__main__":
    demonstrate_operations()
