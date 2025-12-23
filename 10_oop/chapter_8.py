"""
Python OOP: Method Resolution Order (MRO)
==========================================

Topic: Multiple inheritance, MRO, C3 linearization

Real-World Applications:
- Mixins
- Multiple inheritance patterns
- Understanding method lookup
"""


class A:
    def method(self):
        print("A.method()")


class B(A):
    def method(self):
        print("B.method()")


class C(A):
    def method(self):
        print("C.method()")


class D(B, C):  # Multiple inheritance
    pass


class LoggerMixin:
    """Mixin for logging functionality."""
    
    def log(self, message: str):
        print(f"[LOG] {message}")


class TimestampMixin:
    """Mixin for timestamp tracking."""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        from datetime import datetime
        self.created_at = datetime.now()


class User(LoggerMixin, TimestampMixin):
    """User with mixins."""
    
    def __init__(self, username: str):
        super().__init__()
        self.username = username
        self.log(f"Created user: {username}")


def main():
    """Demonstrates MRO."""
    print("="*70)
    print("METHOD RESOLUTION ORDER (MRO)".center(70))
    print("="*70)
    
    print("\n[1] DIAMOND PROBLEM")
    print("-" * 70)
    
    d = D()
    d.method()  # Which method gets called?
    
    print("\n[2] MRO INSPECTION")
    print("-" * 70)
    
    print("D's MRO:")
    for i, cls in enumerate(D.__mro__, 1):
        print(f"  {i}. {cls.__name__}")
    
    print("\n[3] MIXINS")
    print("-" * 70)
    
    user = User("alice")
    print(f"User created at: {user.created_at}")
    user.log("User logged in")
    
    print("\nUser's MRO:")
    for cls in User.__mro__[:4]:  # First 4
        print(f"  - {cls.__name__}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• MRO determines method lookup order")
    print("• Uses C3 linearization algorithm")
    print("• Left-to-right, depth-first, but respecting hierarchy")
    print("• View with ClassName.__mro__")
    print("• Mixins: small classes that add functionality")
    print("="*70)


if __name__ == "__main__":
    main()