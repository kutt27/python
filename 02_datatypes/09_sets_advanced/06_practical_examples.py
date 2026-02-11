"""
Demonstrates finding common interests and aggregating unique tags using sets.
"""

from typing import Set, List

def find_common(s1: Set[str], s2: Set[str]) -> Set[str]:
    return s1 & s2

def aggregate_tags(tag_sets: List[Set[str]]) -> Set[str]:
    result = set()
    for s in tag_sets:
        result |= s
    return result

if __name__ == "__main__":
    alice = {"python", "ml", "hiking"}
    bob = {"python", "webdev", "gaming"}
    print(f"Common interests: {find_common(alice, bob)}")
    
    sets = [{"python", "tutorial"}, {"python", "async"}, {"javascript"}]
    print(f"Combined tags: {aggregate_tags(sets)}")
