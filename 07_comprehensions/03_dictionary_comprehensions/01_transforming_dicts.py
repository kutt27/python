"""
Topic: Dictionary Comprehensions (Transforming Dictionaries).

Dictionary comprehensions `{k: v for ...}` allow you to 
create new dictionaries by processing the keys and values 
of an existing one.
"""

def demonstrate_dict_transform():
    prices_usd = {"laptop": 1000, "mouse": 25, "keyboard": 50}
    
    # 1. Update values (apply 10% tax)
    prices_with_tax = {item: price * 1.1 for item, price in prices_usd.items()}
    print(f"With Tax: {prices_with_tax}")
    
    # 2. Update keys (capitalize)
    display_prices = {item.upper(): price for item, price in prices_usd.items()}
    print(f"Display:  {display_prices}")

if __name__ == "__main__":
    demonstrate_dict_transform()
