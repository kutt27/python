"""
Topic: Using `functools.lru_cache`.

Python's standard library provides a highly optimized 
Least-Recently-Used (LRU) cache decorator.
"""

from functools import lru_cache

@lru_cache(maxsize=128) # Saves the results of the last 128 unique calls
def fetch_user_data(user_id):
    # Simulate an expensive DB query
    print(f"-> Fetching user data for ID: {user_id}")
    return {"id": user_id, "name": f"User-{user_id}"}

if __name__ == "__main__":
    # First call will result in a "Fetching..." print
    print(fetch_user_data(101))
    
    # Second call for the same ID will return the cached result
    # with no printing!
    print(fetch_user_data(101))
