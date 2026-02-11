"""
Demonstrates how booleans are subclasses of integers (True=1, False=0).
"""

def demonstrate_type_coercion() -> None:
    # Counting successful checks using booleans
    service_a = True
    service_b = True
    service_c = False
    
    total_healthy = service_a + service_b + service_c
    print(f"Healthy services: {total_healthy}")
    print(f"Calculation: {int(service_a)} + {int(service_b)} + {int(service_c)} = {total_healthy}")
    
    print(f"\nIs True an int? {isinstance(True, int)}")
    print(f"True + 5 = {True + 5}")

if __name__ == "__main__":
    demonstrate_type_coercion()
