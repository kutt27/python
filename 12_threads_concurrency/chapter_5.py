"""
Python Concurrency: ThreadPoolExecutor
=======================================

Topic: Modern threading with concurrent.futures

Real-World Applications:
- Concurrent web scraping
- Batch API processing
- Parallel file operations
"""

import concurrent.futures
import time
from typing import List

def process_image(image_id: int) -> str:
    """
    Simulate image processing task (Mixed I/O).
    Returns a result string.
    """
    print(f"  Starting image {image_id}...")
    time.sleep(1)  # Simulate work
    return f"Image-{image_id}_processed.jpg"


def main():
    """Demonstrates ThreadPoolExecutor."""
    print("="*70)
    print("THREAD POOL EXECUTOR (Modern Approach)".center(70))
    print("="*70)
    
    image_ids = range(1, 6) # 5 images
    max_workers = 3        # Process max 3 at a time
    
    print(f"Processing {len(image_ids)} images with {max_workers} threads...")
    start_time = time.time()
    
    # Context manager automatically handles cleanup/joining
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Submit tasks and get Future objects
        # map() maintains order of results
        results = executor.map(process_image, image_ids)
        
        # Results are yielded as they complete (in order)
        for result in results:
            print(f"  ✓ Finished: {result}")
            
    total_time = time.time() - start_time
    
    print("-" * 70)
    print(f"Total time: {total_time:.2f}s")
    print("Observe: Time is approx ceil(5/3) * 1s = 2s")
    
    print("\n[2] FUTURE OBJECTS")
    print("-" * 70)
    
    # submit() gives more control than map()
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(process_image, 99)
        print("  Task submitted. Doing other work...")
        
        # Check status
        print(f"  Done? {future.done()}")
        
        # Get result (blocks if not ready)
        result = future.result()
        print(f"  Result: {result}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Use ThreadPoolExecutor instead of raw threading.Thread")
    print("• Manages pool of threads efficiently")
    print("• executor.map(): easy parallel iteration")
    print("• executor.submit(): returns Future for fine-grained control")
    print("="*70)


if __name__ == "__main__":
    main()