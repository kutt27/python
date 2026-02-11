"""
Demonstrates checking if an item exists in a tuple using the 'in' operator.
"""

def demonstrate_membership() -> None:
    allowed_methods = ("GET", "POST", "PUT", "DELETE")
    
    method = "GET"
    print(f"Is {method} allowed? {method in allowed_methods}")
    
    method = "TRACE"
    print(f"Is {method} allowed? {method in allowed_methods}")

if __name__ == "__main__":
    demonstrate_membership()
