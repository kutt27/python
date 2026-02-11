"""
Demonstrates deque (double-ended queue) for O(1) appends and pops from both ends.
"""

from collections import deque

def demonstrate_deque() -> None:
    # Sliding window (last 3 items)
    window: deque[int] = deque(maxlen=3)
    for i in range(5):
        window.append(i)
        print(f"Added {i}, Window: {list(window)}")
    
    # Priority handling
    tasks = deque(["normal1", "normal2"])
    tasks.appendleft("URGENT")
    print(f"\nQueue: {list(tasks)}")
    print(f"Processing: {tasks.popleft()}")

if __name__ == "__main__":
    demonstrate_deque()
