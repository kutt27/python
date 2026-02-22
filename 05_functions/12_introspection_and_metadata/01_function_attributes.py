"""
Topic: Function Attributes and Metadata.

Functions are objects in Python and have metadata like 
their name and docstrings available through attributes.
"""

def process_data(data: list):
    """Processes a list of items and returns a report."""
    return f"Processed {len(data)} items"

if __name__ == "__main__":
    print(f"Name:     {process_data.__name__}")
    print(f"Doc:      {process_data.__doc__}")
    print(f"Module:   {process_data.__module__}")
    
    # Annotations (if provided)
    print(f"Hint:     {process_data.__annotations__}")
