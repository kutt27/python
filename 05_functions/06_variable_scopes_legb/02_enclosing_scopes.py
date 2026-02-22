"""
Topic: Enclosing Scopes (Closures).

Variables in an outer function are accessible to inner 
(nested) functions. This is known as an Enclosing scope.
"""

def outer_function(text: str):
    # This is in the enclosing scope for 'inner'
    message = f"Message: {text}"
    
    def inner_function():
        # Inner has access to 'message'
        print(message)
    
    return inner_function

if __name__ == "__main__":
    my_func = outer_function("Hello from the outer scope!")
    my_func()
