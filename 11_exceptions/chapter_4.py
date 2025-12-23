"""
Python Exceptions: Multiple Exceptions
=======================================

Topic: Handling multiple different exceptions specifically

Real-World Applications:
- Loading configurations (FileMissing vs InvalidJSON)
- Network requests (Timeout vs ConnectionRefused vs HTTPError)
- Data processing (KeyError vs ValueError vs IndexError)
"""

import os
from typing import Dict, Any

# Simulation for demo purposes without actual files
class ConfigLoader:
    """
    Simulates loading configuration from various sources.
    """
    
    @staticmethod
    def load_config(source_type: str) -> Dict[str, Any]:
        """
        Load config based on source type.
        Raises different exceptions based on scenarios.
        """
        print(f"\nAttempting to load from: {source_type}")
        
        if source_type == "missing_file":
            raise FileNotFoundError("/etc/app/config.json")
            
        elif source_type == "bad_permissions":
            raise PermissionError("Access denied to /secure/config.yaml")
            
        elif source_type == "corrupt_json":
            # Simulate parsing error
            raise ValueError("JSON decode error: Expecting value at line 1 column 1")
            
        elif source_type == "missing_key":
            return {"version": 1.0} # Missing 'database' key
            
        elif source_type == "valid":
            return {"version": 1.0, "database": "postgresql"}
            
        else:
            raise RuntimeError(f"Unknown source type: {source_type}")


def initialize_app(source: str):
    """
    Initialize application with robust error handling for multiple scenarios.
    """
    try:
        config = ConfigLoader.load_config(source)
        
        # Verify required keys (might raise KeyError)
        db_type = config["database"]
        print(f"✓ Config loaded. DB: {db_type}")
        
    except FileNotFoundError as e:
        print(f"⚠ Warning: Config file not found ({e}). Using defaults.")
        # Fallback logic
    
    except PermissionError:
        print("✗ Critical: Permission denied. Cannot read config.")
        # potentially exit(1)
        
    except (ValueError, TypeError) as e:
        # Grouping related exceptions
        print(f"✗ Error: Config file is corrupted or invalid format. {e}")
        
    except KeyError as e:
        print(f"✗ Error: Config missing required field: {e}")
        
    except Exception as e:
        # Catch-all for anything else
        print(f"✗ System Error: {type(e).__name__} - {e}")


def main():
    """Demonstrates handling multiple exception types."""
    print("="*70)
    print("HANDLING MULTIPLE EXCEPTIONS".center(70))
    print("="*70)
    
    scenarios = [
        "valid",
        "missing_file",
        "bad_permissions",
        "corrupt_json",
        "missing_key",
        "unknown_source"
    ]
    
    for scenario in scenarios:
        initialize_app(scenario)
    
    print("\n" + "="*70)
    print("Key Points:")
    print("• Handle specific exceptions individually for tailored responses")
    print("• Group exceptions with tuple: except (ErrorA, ErrorB)")
    print("• Order matters: Specific exceptions before general Exception")
    print("• Use hierarchy: FileNotFoundError is a subclass of OSError")
    print("="*70)


if __name__ == "__main__":
    main()