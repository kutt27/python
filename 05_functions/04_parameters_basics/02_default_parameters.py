"""
Topic: Default Parameters.

Provides a fallback value if one isn't provided by the caller.
"""

def send_notification(message: str, channel: str = "email"):
    """Channel defaults to 'email' if not specified."""
    print(f"[{channel.upper()}] Sending: {message}")

if __name__ == "__main__":
    # Uses default
    send_notification("Welcome!")
    
    # Overrides default
    send_notification("Your code is 1234", channel="sms")
