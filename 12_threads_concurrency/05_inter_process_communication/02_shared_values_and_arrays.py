"""
Topic: Shared Memory Basics.

`Value` and `Array` allow you to share simple data structures 
between processes directly in memory (bypassing serialization).
"""

import multiprocessing

def mutate_array(shared_arr):
    """Squares every number in the shared array."""
    for i in range(len(shared_arr)):
        shared_arr[i] = shared_arr[i] ** 2

if __name__ == "__main__":
    # 'i' stands for int, 'd' for double
    numbers = [1, 2, 3, 4, 5]
    shared_arr = multiprocessing.Array('i', numbers)
    
    print(f"Before: {list(shared_arr)}")
    
    p = multiprocessing.Process(target=mutate_array, args=(shared_arr,))
    p.start()
    p.join()
    
    print(f"After:  {list(shared_arr)}")
