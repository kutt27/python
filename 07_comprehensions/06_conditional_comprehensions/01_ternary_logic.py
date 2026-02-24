"""
Topic: Ternary Logic in Comprehensions.

You can use an `if-else` block *before* the `for` clause 
to decide which value should be included in the new list.
"""

def demonstrate_ternary():
    scores = [45, 88, 52, 91, 30]
    
    # Decide "Pass" or "Fail" for each score
    results = ["Pass" if s >= 50 else "Fail" for s in scores]
    
    print(f"Scores:  {scores}")
    print(f"Results: {results}")

if __name__ == "__main__":
    demonstrate_ternary()
