"""
Topic: Attribute Shadowing.

If an instance is assigned an attribute with the same name as a 
class attribute, it "shadows" (hides) the class attribute for that instance.
"""

class Config:
    api_key = "DEFAULT_KEY"

if __name__ == "__main__":
    c1 = Config()
    c2 = Config()
    
    print(f"c1 key: {c1.api_key}")
    print(f"c2 key: {c2.api_key}")
    
    # Shadow the class attribute for c1 only
    c1.api_key = "SECRET_KEY_PROD"
    
    print("\nAfter shadowing c1:")
    print(f"c1 key: {c1.api_key} (Instance version)")
    print(f"c2 key: {c2.api_key} (Still class version)")
    print(f"Config default: {Config.api_key} (Unchanged)")
