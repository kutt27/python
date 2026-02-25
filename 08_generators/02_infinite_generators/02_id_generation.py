"""
Topic: ID Generation.

Generators are perfect for creating a stream of unique, 
incremental IDs for users or transactions.
"""

def id_generator(prefix: str):
    counter = 1
    while True:
        yield f"{prefix}-{counter:04d}"
        counter += 1

if __name__ == "__main__":
    user_ids = id_generator("USR")
    order_ids = id_generator("ORD")
    
    print("Users:")
    print(f"  {next(user_ids)}")
    print(f"  {next(user_ids)}")
    
    print("Orders:")
    print(f"  {next(order_ids)}")
    print(f"  {next(order_ids)}")
