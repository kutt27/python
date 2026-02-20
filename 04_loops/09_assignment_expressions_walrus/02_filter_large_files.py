"""
Filter Large Files with Walrus.
"""

from typing import List, Dict

def filter_large_files(files: List[Dict], threshold_mb: int = 10) -> List[str]:
    """
    Filters files above size threshold using walrus operator.
    
    Args:
        files: List of file dictionaries
        threshold_mb: Size threshold in MB
    
    Returns:
        List of large filenames
    
    Real-world use case: Storage management, cleanup scripts.
    """
    large_files = []
    
    print(f"\nFinding files larger than {threshold_mb}MB")
    print("-" * 60)
    
    for file in files:
        # Calculate size once, use in both condition and print
        if (size_mb := file['size_bytes'] / (1024 * 1024)) > threshold_mb:
            filename = file['name']
            print(f"  📁 {filename}: {size_mb:.1f}MB")
            large_files.append(filename)
    
    return large_files


def demonstrate_file_filtering() -> None:
    """
    Demonstrates filtering large files.
    """
    files_list = [
        {"name": "small.txt", "size_bytes": 1024 * 1024 * 2},  # 2MB
        {"name": "large_video.mp4", "size_bytes": 1024 * 1024 * 150},  # 150MB
        {"name": "backup.zip", "size_bytes": 1024 * 1024 * 50},  # 50MB
        {"name": "config.json", "size_bytes": 1024 * 100},  # 100KB
    ]
    
    large = filter_large_files(files_list, threshold_mb=10)
    print(f"\nFound {len(large)} large files")


if __name__ == "__main__":
    demonstrate_file_filtering()
