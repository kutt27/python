"""
Parse Log Stream with Walrus.
"""

from typing import List, Optional

def extract_status_code(log_line: str) -> Optional[int]:
    """Helper to extract HTTP status code from log line."""
    parts = log_line.split()
    for part in parts:
        if part.isdigit() and 100 <= int(part) <= 599:
            return int(part)
    return None


def parse_log_stream(log_lines: List[str]) -> List[str]:
    """
    Parses log stream, extracting error codes using walrus.
    
    Args:
        log_lines: List of log lines
    
    Returns:
        List of error messages
    
    Real-world use case: Log analysis, real-time monitoring.
    """
    errors = []
    
    print("\nParsing log stream for errors")
    print("-" * 60)
    
    for line in log_lines:
        # Extract and check status code in one expression
        if (code := extract_status_code(line)) and code >= 400:
            print(f"  {code}: {line}")
            errors.append(line)
    
    return errors


def demonstrate_log_stream() -> None:
    """
    Demonstrates log stream parsing.
    """
    logs = [
        "2024-12-05 10:00:00 200 GET /users",
        "2024-12-05 10:01:00 404 GET /missing",
        "2024-12-05 10:02:00 500 POST /api/data",
        "2024-12-05 10:03:00 200 GET /health",
    ]
    
    error_logs = parse_log_stream(logs)
    print(f"\nFound {len(error_logs)} error entries")


if __name__ == "__main__":
    demonstrate_log_stream()
