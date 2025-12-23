"""
Python OOP: Attribute Shadowing
================================

Topic: Instance attributes shadowing class attributes

Real-World Applications:
- Per-instance configuration overrides
- Default vs custom values
"""


class APIClient:
    """API client with default and override capabilities."""
    
    # Class-level defaults
    base_url = "https://api.example.com"
    timeout = 30
    
    def get_url(self):
        """Get the current base URL."""
        return self.base_url


def main():
    """Demonstrates attribute shadowing."""
    print("="*70)
    print("ATTRIBUTE SHADOWING".center(70))
    print("="*70)
    
    print("\n[1] DEFAULT BEHAVIOR")
    print("-" * 70)
    
    client1 = APIClient()
    client2 = APIClient()
    
    print(f"client1.base_url: {client1.base_url}  (from class)")
    print(f"client2.base_url: {client2.base_url}  (from class)")
    
    print("\n[2] SHADOWING WITH INSTANCE ATTRIBUTE")
    print("-" * 70)
    
    # Override for specific instance
    client1.base_url = "https://api.custom.com"
    
    print(f"client1.base_url: {client1.base_url}  (instance override)")
    print(f"client2.base_url: {client2.base_url}  (still using class default)")
    print(f"APIClient.base_url: {APIClient.base_url}  (class unchanged)")
    
    print("\n[3] ACCESSING SHADOWED CLASS ATTRIBUTE")
    print("-" * 70)
    
    print(f"Via class: {APIClient.base_url}")
    print(f"Via instance with shadow: {client1.base_url}")
    print(f"Via __class__: {client1.__class__.base_url}")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Instance attributes shadow class attributes")
    print("• Useful for per-instance customization")
    print("• Class attribute still accessible via ClassName.attr")
    print("="*70)


if __name__ == "__main__":
    main()