"""
Log Parsing with line numbers.
"""

from typing import List, Tuple

def parse_log_file_with_line_numbers(log_lines: List[str]) -> List[Tuple[int, str]]:
    """
    Parses log file and tracks line numbers for errors.
    
    Args:
        log_lines: List of log file lines
    
    Returns:
        List of (line_number, error_message) tuples
    
    Real-world use case: Log file analysis, error tracking.
    """
    errors = []
    
    print(f"\nParsing {len(log_lines)} log lines")
    print("-" * 60)
    
    for line_num, line in enumerate(log_lines, start=1):
        if "ERROR" in line:
            errors.append((line_num, line.strip()))
            print(f"  Line {line_num}: Found error - {line.strip()}")
    
    return errors


def demonstrate_log_parsing() -> None:
    """
    Demonstrates log file parsing with line numbers.
    """
    log_lines = [
        "2024-12-05 10:00:00 INFO Server started",
        "2024-12-05 10:01:23 ERROR Database connection failed",
        "2024-12-05 10:02:15 INFO Request processed",
        "2024-12-05 10:03:45 ERROR Timeout on external API",
        "2024-12-05 10:04:00 INFO Shutting down",
    ]
    
    errors = parse_log_file_with_line_numbers(log_lines)
    print(f"\nFound {len(errors)} errors in log file")


if __name__ == "__main__":
    demonstrate_log_parsing()
