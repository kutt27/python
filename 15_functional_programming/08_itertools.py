"""
Functional Python: Itertools
=============================

Topic: Efficient Iterators & Pipelines

Real-World Applications:
- Handling large streams of data (Logs, generic sequences)
- Combinatorics
- Grouping data
"""

import itertools
import time

def main():
    print("="*70)
    print("ITERTOOLS".center(70))
    print("="*70)
    
    # 1. Infinite Iterators (count, cycle, repeat)
    print("\n[1] Infinite Iterators")
    counter = itertools.count(start=10, step=2)
    print("Count:", [next(counter) for _ in range(5)])
    
    cycler = itertools.cycle(['A', 'B', 'C'])
    print("Cycle:", [next(cycler) for _ in range(7)])
    
    # 2. Accumulate (Running totals)
    print("\n[2] Accumulate")
    data = [1, 2, 3, 4, 5]
    running_sum = list(itertools.accumulate(data))
    print(f"Data: {data}")
    print(f"Sum : {running_sum}")
    
    # 3. Chain (Merging iterables)
    print("\n[3] Chain")
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    merged = list(itertools.chain(list1, list2))
    print(f"Merged: {merged}")
    
    # 4. GroupBy (Requires sorted data)
    print("\n[4] GroupBy")
    users = [
        {"role": "admin", "name": "Alice"},
        {"role": "user",  "name": "Bob"},
        {"role": "admin", "name": "Charlie"},
        {"role": "user",  "name": "Dave"},
    ]
    # groupby needs data sorted by key first
    users.sort(key=lambda u: u['role'])
    
    for role, group in itertools.groupby(users, key=lambda u: u['role']):
        names = [u['name'] for u in group]
        print(f"Role: {role} -> {names}")
        
    # 5. Combinations / Permutations
    print("\n[5] Combinatorics")
    letters = ['A', 'B', 'C']
    print(f"Permutations (2): {list(itertools.permutations(letters, 2))}")
    print(f"Combinations (2): {list(itertools.combinations(letters, 2))}")
    
    print("\n" + "="*70)
    print("Key Takeaway:")
    print("• `itertools` provides fast, memory-efficient tools")
    print("• They process items one-by-one (Lazy evaluation)")
    print("• Essential for building data pipelines")
    print("="*70)


if __name__ == "__main__":
    main()
