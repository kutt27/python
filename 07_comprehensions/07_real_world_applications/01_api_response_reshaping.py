"""
Topic: API Response Normalization.

Real-world APIs often return inconsistent data. Dictionary 
comprehensions can normalize types, lowercase emails, and 
reshape keys for your application.
"""

def normalize_api_data():
    raw_response = [
        {"id": "1", "email": "ALICE@EXAMPLE.COM", "NAME": "Alice Smith"},
        {"id": "2", "email": "BOB@SERVICE.NET", "NAME": "Bob Jones"},
    ]
    
    # Normalize: Convert IDs to int, emails to lowercase, simplify keys
    clean_data = {
        int(user["id"]): {
            "name": user["NAME"].title(),
            "email": user["email"].lower()
        }
        for user in raw_response
    }
    
    print("Normalized Data:")
    for uid, info in clean_data.items():
        print(f"  [{uid}] {info['name']} <{info['email']}>")

if __name__ == "__main__":
    normalize_api_data()
