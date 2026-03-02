"""
Topic: `@staticmethod` Decorator.

Static methods don't receive either 'self' or 'cls'. 
They behave like regular functions but are namespace-organized 
within the class because they are logically related to it.
"""

class MathUtils:
    @staticmethod
    def is_even(num):
        return num % 2 == 0
        
    @staticmethod
    def add(a, b):
        return a + b

if __name__ == "__main__":
    # Can call via class without creating an instance
    print(f"Is 10 even? {MathUtils.is_even(10)}")
    print(f"Result:     {MathUtils.add(5, 7)}")
