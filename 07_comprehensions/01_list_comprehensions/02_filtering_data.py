"""
Topic: Filtering with List Comprehensions.

You can add an `if` clause at the end of a comprehension to 
include only elements that meet certain criteria.
"""

def demonstrate_filtering():
    users = [
        {"name": "Alice", "is_active": True},
        {"name": "Bob", "is_active": False},
        {"name": "Charlie", "is_active": True},
    ]
    
    # Keep only names of active users
    active_names = [u["name"] for u in users if u["is_active"]]
    print(f"Active Users: {active_names}")
    
    # Filter numbers
    nums = range(20)
    evens = [x for x in nums if x % 2 == 0]
    print(f"Evens: {evens}")

if __name__ == "__main__":
    demonstrate_filtering()
