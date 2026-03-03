"""
Topic: Configuration Loading Patterns.

Robustly loading configurations involves handling missing files, 
invalid formats (parsing errors), and missing keys.
"""

import json

def load_settings(config_path):
    # Default settings
    settings = {"theme": "light", "version": "1.0"}
    
    try:
        with open(config_path, "r") as f:
            user_settings = json.load(f)
            # Update defaults with user settings
            settings.update(user_settings)
            print("✓ Settings loaded from file.")
    except FileNotFoundError:
        print("⚠ Config file missing. Using defaults.")
    except json.JSONDecodeError:
        print("✗ Config file is corrupt! Ignoring and using defaults.")
    except Exception as e:
        print(f"✗ Unknown error loading config: {e}")
        
    return settings

if __name__ == "__main__":
    # Test with non-existent file
    print(f"Final settings: {load_settings('non_existent.json')}")
