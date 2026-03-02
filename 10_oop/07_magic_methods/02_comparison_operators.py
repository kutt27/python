"""
Topic: Comparison Operators.

Magic methods like `__eq__` (==) and `__lt__` (<) allow you to define 
how objects of your class are compared.
"""

class Weight:
    def __init__(self, grams):
        self.grams = grams
        
    def __eq__(self, other):
        if not isinstance(other, Weight): return False
        return self.grams == other.grams

    def __lt__(self, other):
        return self.grams < other.grams

if __name__ == "__main__":
    w1 = Weight(500)
    w2 = Weight(1000)
    w3 = Weight(500)
    
    print(f"w1 == w3: {w1 == w3}")
    print(f"w1 <  w2: {w1 < w2}")
    
    # Objects can now be sorted because __lt__ is defined
    sorted_weights = sorted([w2, w1, w3])
    print(f"Sorted: {[w.grams for w in sorted_weights]}")
