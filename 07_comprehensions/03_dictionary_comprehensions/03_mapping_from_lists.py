"""
Topic: Creating Dictionaries from Lists.

Dictionary comprehensions are perfect for turning a list of 
records or objects into a dictionary for O(1) fast lookup.
"""

def demonstrate_mapping():
    user_list = [
        {"id": 1, "username": "alice", "email": "alice@example.com"},
        {"id": 2, "username": "bob", "email": "bob@example.com"},
    ]
    
    # Create a map of id -> user_record
    user_map = {user["id"]: user for user in user_list}
    
    print(f"User 1: {user_map[1]}")
    print(f"User 2: {user_map[2]}")

if __name__ == "__main__":
    demonstrate_mapping()
