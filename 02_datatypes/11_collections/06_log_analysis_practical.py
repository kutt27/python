"""
Practical example using Counter and defaultdict to analyze log entries.
"""

from collections import Counter, defaultdict
from typing import List, Dict

def analyze_logs(logs: List[str]) -> Dict:
    counts = Counter()
    for entry in logs:
        if "ERROR" in entry: counts["ERROR"] += 1
        elif "WARNING" in entry: counts["WARNING"] += 1
        else: counts["INFO"] += 1
    
    return {
        "summary": dict(counts),
        "most_frequent": counts.most_common(1)[0]
    }

if __name__ == "__main__":
    data = [
        "INFO: Start", "ERROR: DB Failed", "INFO: Ok", 
        "WARNING: Low Mem", "ERROR: Timeout"
    ]
    print(f"Analysis: {analyze_logs(data)}")
