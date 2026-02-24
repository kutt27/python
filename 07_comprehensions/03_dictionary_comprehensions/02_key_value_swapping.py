"""
Topic: Key-Value Swapping.

A common pattern is reversing a dictionary (swapping keys 
and values) for easier lookup in the opposite direction.
"""

def demonstrate_swap():
    # ID -> Username
    id_to_user = {101: "alice", 102: "bob", 103: "charlie"}
    
    # Username -> ID
    user_to_id = {user: uid for uid, user in id_to_user.items()}
    
    print(f"Original: {id_to_user}")
    print(f"Reversed: {user_to_id}")

if __name__ == "__main__":
    demonstrate_swap()
