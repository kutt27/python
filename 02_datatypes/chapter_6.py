"""
Python Strings: Text Processing and Manipulation
=================================================

Topic: String data type, slicing, encoding, and common operations

Real-World Applications:
- API request/response processing
- Log parsing and analysis
- User input validation and sanitization
- Data transformation in ETL pipelines
- Internationalization (i18n) in web applications
"""

from typing import List


def demonstrate_string_basics() -> None:
    """
    Demonstrates basic string operations.
    
    Real-world use case: Processing user data and error messages.
    """
    # Example: Processing API request data
    username = "admin_user"
    api_endpoint = "/api/v1/users"
    
    request_log =f"Request to {api_endpoint} by user: {username}"
    print(f"Log entry: {request_log}")
    
    # String formatting for structured logging
    status_code = 200
    response_time_ms = 45
    log_entry = f"[{status_code}] {api_endpoint} - {response_time_ms}ms"
    print(f"Formatted log: {log_entry}")


def demonstrate_string_slicing() -> None:
    """
    Demonstrates string slicing for text extraction.
    
    Slicing syntax: string[start:end:step]
    - start: inclusive
    - end: exclusive
    - step: increment (can be negative for reverse)
    
    Real-world use case: Parsing log files, extracting data from fixed-width formats.
    """
    # Example: Parsing structured log entry
    log_message = "2024-12-05 ERROR DatabaseConnection timeout"
    
    # Extract date
    date_part = log_message[:10]
    print(f"\nDate: {date_part}")
    
    # Extract log level
    level_start = 11
    level_end = log_message.find(" ", level_start)
    log_level = log_message[level_start:level_end]
    print(f"Level: {log_level}")
    
    # Extract message
    message = log_message[level_end + 1:]
    print(f"Message: {message}")
    
    # Reverse string (useful for certain algorithms)
    reversed_msg = log_message[::-1]
    print(f"\nReversed: {reversed_msg}")


def demonstrate_string_methods() -> None:
    """
    Demonstrates essential string methods for data processing.
    
    Real-world use case: Data cleaning, validation, transformation.
    """
    # Example: Processing user input from web form
    user_email = "  Admin@Example.COM  "
    
    print(f"\nOriginal email: '{user_email}'")
    
    # Clean and normalize
    cleaned_email = user_email.strip().lower()
    print(f"Cleaned email: '{cleaned_email}'")
    
    # Validation
    is_valid = "@" in cleaned_email and "." in cleaned_email
    print(f"Valid format: {is_valid}")
    
    # Example: URL path processing
    api_path = "/api/v1/users/123/profile"
    path_parts: List[str] = api_path.strip("/").split("/")
    print(f"\nAPI path: {api_path}")
    print(f"Path components: {path_parts}")
    
    # Extract resource ID
    if len(path_parts) >= 4:
        user_id = path_parts[3]
        print(f"User ID: {user_id}")
    
    # Join path parts
    reconstructed = "/" + "/".join(path_parts)
    print(f"Reconstructed: {reconstructed}")


def demonstrate_string_searching() -> None:
    """
    Demonstrates string searching and checking methods.
    
    Real-world use case: Log analysis, pattern detection, validation.
    """
    # Example: Analyzing server logs for errors
    log_entry = "ERROR: Failed to connect to database at 127.0.0.1:5432"
    
    # Check if log contains error
    has_error = "ERROR" in log_entry
    print(f"\nContains ERROR: {has_error}")
    
    # Find position
    error_pos = log_entry.find("ERROR")
    print(f"ERROR position: {error_pos}")
    
    # Extract IP address (simplified)
    ip_start = log_entry.find("127.")
    if ip_start != -1:
        ip_end = log_entry.find(":", ip_start)
        ip_address = log_entry[ip_start:ip_end]
        print(f"IP address found: {ip_address}")
    
    # Check prefixes/suffixes (useful for file type checking)
    filename = "report.pdf"
    is_pdf = filename.endswith(".pdf")
    is_temp = filename.startswith("temp_")
    print(f"\n'{filename}' is PDF: {is_pdf}")
    print(f"'{filename}' is temp file: {is_temp}")


def demonstrate_string_encoding() -> None:
    """
    Demonstrates string encoding and decoding.
    
    Critical for:
    - API communication (JSON, XML)
    - Database storage
    - File I/O
    - Internationalization
    
    Real-world use case: Handling multilingual content, API payloads.
    """
    # Example: Processing multilingual product names
    product_name = "Café Spécial ☕"
    
    print(f"\nOriginal text: {product_name}")
    print(f"Type: {type(product_name)}")
    
    # Encode to bytes (for storage/transmission)
    encoded_utf8 = product_name.encode("utf-8")
    print(f"\nUTF-8 encoded: {encoded_utf8}")
    print(f"Type: {type(encoded_utf8)}")
    print(f"Byte length: {len(encoded_utf8)} bytes")
    
    # Decode back to string
    decoded = encoded_utf8.decode("utf-8")
    print(f"\nDecoded: {decoded}")
    
    # Different encodings
    encoded_latin1 = product_name.encode("latin-1", errors="ignore")
    print(f"\nLatin-1 encoded: {encoded_latin1}")
    
    print(f"\n{'='*60}")
    print("IMPORTANT: Always specify encoding explicitly")
    print("  Default encoding is platform-dependent")
    print("  Use UTF-8 for maximum compatibility")
    print(f"{'='*60}")


def demonstrate_string_formatting() -> None:
    """
    Demonstrates modern string formatting techniques.
    
    Real-world use case: Generating reports, logging, API responses.
    """
    # Example: Generating system health report
    service_name = "AuthService"
    uptime_hours = 168.5
    request_count = 1_234_567
    error_rate = 0.0023
    
    # f-strings (Python 3.6+) - RECOMMENDED
    report = f"""
Service Health Report
{'='*50}
Service: {service_name}
Uptime: {uptime_hours:.1f} hours
Requests: {request_count:,}
Error Rate: {error_rate:.2%}
Status: {'✓ HEALTHY' if error_rate < 0.01 else '✗ DEGRADED'}
{'='*50}
"""
    print(report)
    
    # Format specifications
    print(f"\nFormatting examples:")
    print(f"  Integer with commas: {request_count:,}")
    print(f"  Percentage: {error_rate:.2%}")
    print(f"  Fixed decimals: {uptime_hours:.2f}")
    print(f"  Padded string: {service_name:>20}")
    print(f"  Zero-padded number: {42:05d}")


def sanitize_user_input(user_input: str) -> str:
    """
    Sanitizes user input for security.
    
    Args:
        user_input: Raw user input
    
    Returns:
        Sanitized string
    
    Real-world use case: Preventing injection attacks, data validation.
    """
    # Remove leading/trailing whitespace
    cleaned = user_input.strip()
    
    # Remove potentially dangerous characters (simplified example)
    dangerous_chars = ["<", ">", "&", "'", '"']
    for char in dangerous_chars:
        cleaned = cleaned.replace(char, "")
    
    # Limit length
    max_length = 100
    if len(cleaned) > max_length:
        cleaned = cleaned[:max_length]
    
    return cleaned


def main() -> None:
    """Main function to run all demonstrations."""
    print("="*70)
    print("PYTHON STRINGS: TEXT PROCESSING".center(70))
    print("="*70)
    
    print("\n[1] STRING BASICS")
    print("-" * 70)
    demonstrate_string_basics()
    
    print("\n\n[2] STRING SLICING")
    print("-" * 70)
    demonstrate_string_slicing()
    
    print("\n\n[3] STRING METHODS")
    print("-" * 70)
    demonstrate_string_methods()
    
    print("\n\n[4] STRING SEARCHING")
    print("-" * 70)
    demonstrate_string_searching()
    
    print("\n\n[5] ENCODING & DECODING")
    print("-" * 70)
    demonstrate_string_encoding()
    
    print("\n\n[6] STRING FORMATTING")
    print("-" * 70)
    demonstrate_string_formatting()
    
    print("\n\n[7] INPUT SANITIZATION")
    print("-" * 70)
    malicious_input = "  <script>alert('xss')</script>  "
    sanitized = sanitize_user_input(malicious_input)
    print(f"Original: {malicious_input}")
    print(f"Sanitized: {sanitized}")
    
    print("\n" + "="*70)
    print("Key Takeaways:")
    print("1. Strings are immutable - operations create new strings")
    print("2. Use f-strings for formatting (Python 3.6+)")
    print("3. Always specify encoding (UTF-8 recommended)")
    print("4. Sanitize user input to prevent security vulnerabilities")
    print("5. Use str.strip(), str.lower() for data normalization")
    print("="*70)


if __name__ == "__main__":
    main()