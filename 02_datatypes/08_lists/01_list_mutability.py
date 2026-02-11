"""
Demonstrates list mutability and in-place modifications.
"""

def demonstrate_list_mutability() -> None:
    queue = ["GET /users", "POST /orders"]
    print(f"Initial: {queue}, ID: {id(queue)}")
    
    # Add item
    queue.append("DELETE /cache")
    print(f"After append: {queue}, ID: {id(queue)} (Same!)")
    
    # Remove item
    queue.pop(0)
    print(f"After pop(0): {queue}, ID: {id(queue)} (Still same!)")

if __name__ == "__main__":
    demonstrate_list_mutability()
