"""
Python OOP: Namespaces
=======================

Topic: Class vs instance namespaces, attribute lookup

Real-World Applications:
- Configuration with defaults
- Shared vs instance-specific data
- Class-level constants
"""


class Config:
    """Configuration with class and instance attributes."""
    
    # Class attributes (defaults)
    debug = False
    timeout = 30
    max_retries = 3
    
    def set_debug(self, value: bool):
        """Set instance-specific debug mode."""
        self.debug = value  # Creates instance attribute


def main():
    """Demonstrates namespaces."""
    print("="*70)
    print("CLASS VS INSTANCE NAMESPACES".center(70))
    print("="*70)
    
    print("\n[1] CLASS ATTRIBUTES (Defaults)")
    print("-" * 70)
    
    print(f"Config.debug: {Config.debug}")
    print(f"Config.timeout: {Config.timeout}")
    
    print("\n[2] INSTANCE ATTRIBUTES")
    print("-" * 70)
    
    config1 = Config()
    config2 = Config()
    
    # Read class attribute through instance
    print(f"config1.debug: {config1.debug}  (from class)")
    print(f"config2.debug: {config2.debug}  (from class)")
    
    # Create instance attribute
    config1.debug = True  
    
    print(f"\nAfter config1.debug = True:")
    print(f"config1.debug: {config1.debug}  (instance attr)")
    print(f"config2.debug: {config2.debug}  (still from class)")
    print(f"Config.debug: {Config.debug}  (unchanged)")
    
    print("\n[3] NAMESPACE LOOKUP")
    print("-" * 70)
    
    print("Lookup order: instance → class → parent classes")
    print(f"config1.__dict__: {config1.__dict__}")
    print(f"Config.__dict__ keys: {list(Config.__dict__.keys())[:5]}...")
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Class attributes: shared across all instances")
    print("• Instance attributes: specific to each instance")
    print("• Lookup: instance first, then class")
    print("• Assignment creates instance attribute")
    print("="*70)


if __name__ == "__main__":
    main()