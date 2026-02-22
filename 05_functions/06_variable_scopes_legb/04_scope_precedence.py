"""
Topic: LEGB Scope Precedence.

Python searches for variables in this specific order:
1. L: Local
2. E: Enclosing
3. G: Global
4. B: Built-in
"""

def demonstrate_precedence():
    # Global 'x'
    x = "global"
    
    def outer():
        # Enclosing 'x' shadows global
        x = "enclosing"
        
        def inner():
            # Local 'x' shadows enclosing
            x = "local"
            print(f"Inside inner: {x}")
        
        inner()
        print(f"Inside outer: {x}")

    print(f"Module level: {x}")
    outer()

if __name__ == "__main__":
    demonstrate_precedence()
