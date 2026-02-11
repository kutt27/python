"""
Demonstrates a simple input sanitization function.
"""

def sanitize_input(text: str) -> str:
    # Strip whitespace and remove dangerous characters
    cleaned = text.strip()
    for char in ["<", ">", "&", "'", '"']:
        cleaned = cleaned.replace(char, "")
    
    # Limit length
    return cleaned[:100]

if __name__ == "__main__":
    malicious = "  <script>alert('xss')</script>  "
    print(f"Original: {malicious}")
    print(f"Sanitized: {sanitize_input(malicious)}")
