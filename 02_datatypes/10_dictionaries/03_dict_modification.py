"""
Demonstrates adding, updating, and deleting dictionary items.
"""

def demonstrate_modification() -> None:
    meta = {"method": "GET"}
    print(f"Initial: {meta}")
    
    # Add
    meta["timestamp"] = "2024-12-05"
    print(f"Added timestamp: {meta}")
    
    # Update
    meta["method"] = "POST"
    print(f"Updated method: {meta}")
    
    # Update multiple
    meta.update({"user_agent": "Python", "auth": "Token123"})
    print(f"Bulk update: {meta}")
    
    # Delete
    del meta["auth"]
    print(f"After delete: {meta}")

if __name__ == "__main__":
    demonstrate_modification()
