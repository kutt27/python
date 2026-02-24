"""
Topic: Set Comprehensions for Deduplication.

Set comprehensions use curly braces `{}` and automatically 
ensure all elements are unique, making them perfect for 
removing duplicates from data.
"""

def demonstrate_deduplication():
    # List with many duplicates
    user_ids = [101, 102, 101, 105, 102, 103, 101]
    
    # Set comprehension removes duplicates automatically
    unique_ids = {uid for uid in user_ids}
    
    print(f"Original: {user_ids}")
    print(f"Unique:   {unique_ids}")

if __name__ == "__main__":
    demonstrate_deduplication()
