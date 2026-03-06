"""
Topic: ThreadPoolExecutor.

The modern way to manage threads. It handles pool creation, 
recycling, and provides a 'map' interface for parallel iteration.
"""

from concurrent.futures import ThreadPoolExecutor
import time

def process_api(id: int):
    """Simulate API request."""
    print(f"  [API] Requesting data for ID-{id}...")
    time.sleep(0.5)
    return f"Response for {id}"

if __name__ == "__main__":
    ids = [101, 102, 103, 104, 105]
    
    # max_workers limits number of concurrent threads
    with ThreadPoolExecutor(max_workers=3) as executor:
        # map() iterates values and submits them to the pool
        results = executor.map(process_api, ids)
        
        # results are yielded as they become ready (maintaining input order)
        for res in results:
            print(f"  ✓ {res}")
