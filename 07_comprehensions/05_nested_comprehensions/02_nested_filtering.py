"""
Topic: Complex Nested Filtering (e.g., Log Parsing).

Nested comprehensions combined with filtering allow for deep 
data extraction from complex structures like log batches.
"""

def demonstrate_nested_filter():
    batch_logs = [
        ["INFO: Start", "ERROR: Connection failed", "INFO: Retry"],
        ["INFO: Auth OK", "ERROR: DB Timeout"],
    ]
    
    # Extract only error messages from all batches
    errors = [
        log
        for batch in batch_logs
        for log in batch
        if "ERROR" in log
    ]
    
    print(f"Error logs found: {errors}")

if __name__ == "__main__":
    demonstrate_nested_filter()
