"""
Topic: Practical Log File Processing.

A real-world pattern for processing large log files line-by-line 
without crashing memory.
"""

def read_logs():
    # Simulated log lines
    lines = [
        "INFO: Application Start",
        "ERROR: Database Connection Lost",
        "INFO: Retrying...",
        "ERROR: Auth Failure"
    ]
    for line in lines:
        yield line

def filter_errors(log_stream):
    for line in log_stream:
        if "ERROR" in line:
            yield line

if __name__ == "__main__":
    # Chain generators together: File -> Filter
    logs = read_logs()
    errors = filter_errors(logs)
    
    print("Error Report:")
    for error in errors:
        print(f"  [Found] {error}")
