"""
Demonstrates string slicing syntax: string[start:end:step].
"""

def demonstrate_string_slicing() -> None:
    log_message = "2024-12-05 ERROR DatabaseConnection timeout"
    
    # Extract parts
    date = log_message[:10]
    level = log_message[11:16]
    message = log_message[17:]
    
    print(f"Original: {log_message}")
    print(f"Date: {date}")
    print(f"Level: {level}")
    print(f"Message: {message}")
    
    # Reverse string
    print(f"Reversed: {log_message[::-1]}")

if __name__ == "__main__":
    demonstrate_string_slicing()
