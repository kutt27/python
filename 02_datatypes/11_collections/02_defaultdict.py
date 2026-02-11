"""
Demonstrates defaultdict for automatically handling missing keys with a default factory.
"""

from collections import defaultdict
from typing import List

def demonstrate_defaultdict() -> None:
    # list as default factory
    req_logs: defaultdict[str, List[str]] = defaultdict(list)
    req_logs["/api/users"].append("GET")
    req_logs["/api/users"].append("POST")
    print(f"Logs: {dict(req_logs)}")
    
    # int as default factory (useful for counting)
    error_counts: defaultdict[str, int] = defaultdict(int)
    errors = ["404", "500", "404"]
    for err in errors:
        error_counts[err] += 1
    print(f"Error Counts: {dict(error_counts)}")

if __name__ == "__main__":
    demonstrate_defaultdict()
