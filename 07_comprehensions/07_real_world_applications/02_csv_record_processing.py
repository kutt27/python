"""
Topic: Processing CSV-like Records.

Combining `zip` and generator expressions to efficiently 
parse "rows" of data into dictionaries.
"""

def process_records():
    headers = ["timestamp", "user", "action"]
    raw_logs = [
        "2024-01-01 10:00,admin,login",
        "2024-01-01 10:05,user_1,view_page",
        "2024-01-01 10:10,admin,logout"
    ]
    
    # Efficiently parse rows into a generator of dicts
    parsed_logs = (
        dict(zip(headers, row.split(",")))
        for row in raw_logs
    )
    
    print("Parsed Action Stream:")
    for log in parsed_logs:
        print(f"  {log['user']} performed {log['action']} at {log['timestamp']}")

if __name__ == "__main__":
    process_records()
