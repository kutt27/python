"""
Find Primary Contact.
"""

from typing import List, Optional, Dict

def find_primary_contact(contacts: List[Dict[str, any]]) -> Optional[Dict]:
    """
    Finds primary contact in contact list.
    
    Args:
        contacts: List of contact dictionaries
    
    Returns:
        Primary contact if found, None otherwise
    
    Real-world use case: CRM systems, notification dispatch.
    """
    print("\nSearching for primary contact")
    print("-" * 60)
    
    for contact in contacts:
        name = contact.get('name')
        is_primary = contact.get('is_primary', False)
        
        print(f"  {name}: ", end="")
        
        if is_primary:
            print("✓ PRIMARY CONTACT FOUND")
            return contact
        else:
            print("Secondary")
    
    else:
        print("\n⚠ NO PRIMARY CONTACT - Using first contact as fallback")
        return contacts[0] if contacts else None


def demonstrate_primary_contact() -> None:
    """
    Demonstrates finding primary contact.
    """
    contact_list = [
        {"name":"Alice", "email": "alice@example.com", "is_primary": False},
        {"name": "Bob", "email": "bob@example.com", "is_primary": False},
        {"name": "Charlie", "email": "charlie@example.com", "is_primary": False},
    ]
    
    primary = find_primary_contact(contact_list)
    if primary:
        print(f"\n→ Sending notification to: {primary.get('name')}")


if __name__ == "__main__":
    demonstrate_primary_contact()
