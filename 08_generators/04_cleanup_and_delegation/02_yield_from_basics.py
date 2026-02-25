"""
Topic: Delegation with `yield from`.

`yield from` is a shorter way to yield all values from another 
iterable (like a list or another generator). It "delegates" 
the iteration to a sub-generator.
"""

def sub_generator():
    yield "A"
    yield "B"

def main_generator():
    yield "Start"
    # Instead of 'for x in sub(): yield x'
    yield from sub_generator()
    yield "End"

if __name__ == "__main__":
    for item in main_generator():
        print(item)
