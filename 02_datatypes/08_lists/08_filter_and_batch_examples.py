"""
Demonstrates practical list filtering and batching logic.
"""

from typing import List, Any

def filter_errors(logs: List[str]) -> List[str]:
    return [log for log in logs if "ERROR" in log.upper()]

def batch_data(items: List[Any], size: int) -> List[List[Any]]:
    return [items[i:i + size] for i in range(0, len(items), size)]

if __name__ == "__main__":
    logs = ["INFO: OK", "ERROR: Failed", "INFO: OK", "ERROR: Timeout"]
    print(f"Errors: {filter_errors(logs)}")
    
    data = list(range(1, 21))
    print(f"\nBatches (size 8):")
    for b in batch_data(data, 8):
        print(f"  {b}")
