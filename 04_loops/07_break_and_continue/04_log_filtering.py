"""
Log Filtering with continue/break.
"""

from typing import List

def filter_and_process_logs(log_lines: List[str]) -> List[str]:
    """
    Filters logs, skipping noise and stopping on critical errors.
    
    Args:
        log_lines: List of log messages
    
    Returns:
        List of processed error logs
    
    Real-world use case: Log processing, error detection.
    """
    errors = []
    
    print(f"\nProcessing {len(log_lines)} log lines")
    print("-" * 60)
    
    for line in log_lines:
        # Skip debug/info messages (continue)
        if "DEBUG" in line or "INFO" in line:
            continue
        
        # Stop on critical error (break)
        if "CRITICAL" in line:
            print(f"  🛑 CRITICAL ERROR FOUND - stopping processing")
            print(f"     {line}")
            break
        
        # Process errors/warnings
        if "ERROR" in line or "WARNING" in line:
            print(f"  ⚠  {line}")
            errors.append(line)
    
    return errors


def demonstrate_log_filtering() -> None:
    """
    Demonstrates log filtering with skip and stop.
    """
    logs = [
        "INFO: Server started",
        "DEBUG: Loading configuration",
        "ERROR: Database connection timeout",
        "WARNING: High memory usage",
        "CRITICAL: System failure - shutting down",
        "ERROR: This won't be processed",
    ]
    
    error_logs = filter_and_process_logs(logs)
    print(f"\nCollected {len(error_logs)} error/warning logs before critical failure")


if __name__ == "__main__":
    demonstrate_log_filtering()
