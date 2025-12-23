"""
Python Concurrency: Concurrent Downloads
=========================================

Topic: Real-world threading example (I/O Bound)

Real-World Applications:
- Downloading multiple files
- Querying multiple APIs concurrently
- Web scraping
"""

import threading
import time
import random
from typing import List, Dict

# Simulated file server
FILES = {
    "file1.data": 2,    # size/duration
    "file2.data": 1,
    "file3.data": 3,
    "photo.jpg": 1.5,
    "doc.pdf": 0.5
}

class Downloader:
    """Simulates file downloader."""
    
    def __init__(self):
        self.results: Dict[str, str] = {}
        
    def download_file(self, filename: str):
        """Simulate download task."""
        duration = FILES.get(filename, 1)
        print(f"  [START] {filename} (est: {duration}s)")
        
        # Simulate Network I/O
        time.sleep(duration)
        
        status = "Completed"
        print(f"  [DONE]  {filename}")
        self.results[filename] = status

def main():
    """Demonstrates concurrent downloads."""
    print("="*70)
    print("CONCURRENT DOWNLOADER EXERCISE".center(70))
    print("="*70)
    
    files_to_download = list(FILES.keys())
    downloader = Downloader()
    threads: List[threading.Thread] = []
    
    print(f"Queue: {files_to_download}")
    start_time = time.time()
    
    # 1. Start all downloads concurrently
    for filename in files_to_download:
        t = threading.Thread(target=downloader.download_file, args=(filename,))
        threads.append(t)
        t.start()
        
    # 2. Wait for completion
    for t in threads:
        t.join()
        
    total_time = time.time() - start_time
    
    print("-" * 70)
    print("Summary:")
    for name, status in downloader.results.items():
        print(f"  {name}: {status}")
        
    print(f"\nTotal Time: {total_time:.2f}s")
    
    # Calculate sequential time
    sequential_time = sum(FILES.values())
    speedup = sequential_time / total_time
    print(f"Sequential Estimate: {sequential_time:.2f}s")
    print(f"Speedup Factor: {speedup:.1f}x")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• I/O bound tasks scale well with threads")
    print("• GIL is released during I/O wait (sleep, network read)")
    print("• Significant performance gain over sequential execution")
    print("="*70)


if __name__ == "__main__":
    main()