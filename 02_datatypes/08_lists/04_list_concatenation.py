"""
Demonstrates combining lists using + and repeating lists using *.
"""

def demonstrate_concatenation() -> None:
    logs_a = ["[A] Start", "[A] Work"]
    logs_b = ["[B] Done"]
    
    combined = logs_a + logs_b
    print(f"Combined logs: {combined}")
    
    # Initialization template
    template = [None] * 5
    print(f"Template list: {template}")

if __name__ == "__main__":
    demonstrate_concatenation()
