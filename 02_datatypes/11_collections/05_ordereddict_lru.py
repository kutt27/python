"""
Demonstrates OrderedDict and how to use it for a simple LRU cache pattern.
"""

from collections import OrderedDict

def demonstrate_lru_cache() -> None:
    # Max size 3
    cache: OrderedDict[str, str] = OrderedDict()
    
    def access(k: str, v: str):
        if k in cache:
            cache.move_to_end(k)
        else:
            if len(cache) >= 3:
                # Remove oldest (first item)
                oldest = next(iter(cache))
                print(f"Evicting {oldest}")
                cache.popitem(last=False)
            cache[k] = v
        print(f"Cache keys: {list(cache.keys())}")

    access("a", "1")
    access("b", "2")
    access("c", "3")
    access("a", "1") # Move 'a' to end
    access("d", "4") # Evicts 'b'

if __name__ == "__main__":
    demonstrate_lru_cache()
