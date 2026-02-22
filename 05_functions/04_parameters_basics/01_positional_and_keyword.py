"""
Topic: Positional and Keyword Arguments.

- Positional: Arguments matched by order.
- Keyword: Arguments matched by name, allowing for clarity 
  and flexible ordering.
"""

def calculate_tax(subtotal: float, tax_rate: float):
    return subtotal * tax_rate

if __name__ == "__main__":
    # Positional usage
    print(f"Positional: {calculate_tax(100.0, 0.08)}")
    
    # Keyword usage (clearer)
    print(f"Keyword: {calculate_tax(tax_rate=0.08, subtotal=100.0)}")
