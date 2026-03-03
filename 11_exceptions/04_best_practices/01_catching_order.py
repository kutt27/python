"""
Topic: Catching Order.

Always catch specific subclasses BEFORE general base classes. 
Python matches exceptions from top to bottom.
"""

class BaseError(Exception): pass
class SpecificError(BaseError): pass

def risky_op():
    raise SpecificError("Something went wrong")

def bad_example():
    print("Bad Example:")
    try:
        risky_op()
    except BaseError:
        # This will catch SpecificError, so the next block is unreachable!
        print("  Caught by BaseError (Too broad!)")
    except SpecificError:
        print("  Caught by SpecificError")

def good_example():
    print("\nGood Example:")
    try:
        risky_op()
    except SpecificError:
        # Specific first!
        print("  Caught by SpecificError")
    except BaseError:
        print("  Caught by BaseError")

if __name__ == "__main__":
    bad_example()
    good_example()
