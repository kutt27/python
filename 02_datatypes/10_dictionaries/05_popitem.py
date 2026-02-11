"""
Demonstrates popitem() for removing and returning the last-inserted item.
"""

def demonstrate_popitem() -> None:
    queue = {"task1": "Email", "task2": "Report", "task3": "Cache"}
    print(f"Queue: {queue}")
    
    # Removes last item
    item = queue.popitem()
    print(f"Popped: {item}")
    print(f"Remaining: {queue}")

if __name__ == "__main__":
    demonstrate_popitem()
