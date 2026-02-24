"""
Topic: Lazy Evaluation with Generators.

Generators don't do any work until you iterate over them. 
This is great for processing heavy data streams one piece 
at a time.
"""

def demonstrate_lazy():
    print("Creating generator...")
    # This doesn't run the math yet
    squares = (print(f"Computing {x}*2...") or x**2 for x in range(3))
    
    print("Generator created. Now consuming it:")
    for result in squares:
        print(f"Got result: {result}")

if __name__ == "__main__":
    demonstrate_lazy()
