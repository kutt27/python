"""
Topic: Handling Multiple Exceptions.

You can handle multiple different exceptions using multiple except 
blocks, or group them using a tuple if the handling logic is 
the same.
"""

def handle_various_errors(data, key):
    try:
        # Could raise KeyError if key missing
        # Could raise TypeError if data is not a dict
        val = data[key]
        print(f"Found: {val}")
    except KeyError:
        print(f"Key '{key}' not found.")
    except TypeError:
        print("Data is not a valid dictionary.")
    except (ValueError, ZeroDivisionError) as e:
        # Grouped exceptions
        print(f"Math/Value error: {e}")

if __name__ == "__main__":
    handle_various_errors({"a": 1}, "b")
    handle_various_errors(None, "a")
