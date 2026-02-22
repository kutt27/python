"""
Topic: Local and Global Scopes.

- Global: Defined at the module level. Accessible everywhere.
- Local: Defined inside a function. Only exists during execution.
"""

# GLOBAL SCOPE
APP_VERSION = "1.0.0"

def show_version():
    # Reading global from within function
    print(f"App Version: {APP_VERSION}")

def temp_calculation():
    # LOCAL SCOPE
    result = 42  # Cannot be accessed outside this function
    print(f"Local result: {result}")

if __name__ == "__main__":
    show_version()
    temp_calculation()
    
    # print(result) # This would raise NameError
