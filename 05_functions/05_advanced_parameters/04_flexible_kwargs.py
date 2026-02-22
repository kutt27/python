"""
Topic: Flexible Keyword Arguments (**kwargs).

Allows a function to accept any number of keyword arguments 
as a dictionary.
"""

def log_event(event: str, **metadata):
    """Metadata is captured as a dictionary."""
    print(f"Event: {event}")
    for key, value in metadata.items():
        print(f"  {key}: {value}")

if __name__ == "__main__":
    log_event("login", user_id=101, ip="127.0.0.1", browser="Chrome")
    
    log_event("purchase", amount=99.99, promo_code="SUMMER24")
