"""
Topic: Serialization.

Convert models back into dictionaries or JSON strings. 
You can dynamically filter which fields are included or excluded.
"""

from pydantic import BaseModel, Field

class Account(BaseModel):
    id: int
    username: str
    password: str = Field(exclude=True) # Exclude by default

if __name__ == "__main__":
    acc = Account(id=1, username="admin", password="password123")
    
    # 1. Default Dump (omits 'password' due to field configuration)
    print("Default dump:")
    print(acc.model_dump())
    
    # 2. Exclude 'id' via parameter
    print("\nExclude 'id' dynamically:")
    print(acc.model_dump(exclude={'id'}))
    
    # 3. Include only 'username'
    print("\nInclude only 'username':")
    print(acc.model_dump(include={'username'}))
    
    # 4. JSON Serialization
    print("\nJSON Serialization:")
    print(acc.model_dump_json())
