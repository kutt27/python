"""
Topic: Iteration and Exhaustion.

Generators are single-use iterators. Once they finish yielding 
all their values, they are "exhausted" and cannot be restarted.
"""

def fruit_generator():
    yield "Apple"
    yield "Banana"
    yield "Cherry"

if __name__ == "__main__":
    gen = fruit_generator()
    
    print("First iteration:")
    for fruit in gen:
        print(f"  {fruit}")
        
    print("\nSecond iteration (on the same object):")
    # This will print nothing because the generator is exhausted
    for fruit in gen:
        print(f"  {fruit}")
    
    print("Zero items returned above because the generator is exhausted.")
