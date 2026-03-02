"""
Topic: Context Manager Protocol.

Implementing `__enter__` and `__exit__` allows your class to be 
used with the 'with' statement for automatic resource management.
"""

class Database:
    def __init__(self, name):
        self.name = name
        
    def __enter__(self):
        print(f"Opening connection to {self.name}...")
        # This returned value is assigned to the variable in 'as VAR'
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing connection to {self.name}.")
        # Handle exceptions if needed, return False to propagate
        return False
        
    def query(self, sql):
        print(f"Executing: {sql}")

if __name__ == "__main__":
    with Database("production_db") as db:
        db.query("SELECT * FROM users")
    
    print("Code outside 'with' block.")
